import json
import os
import re
from translation_pack import gtrans4_mod, gtrans3_mod, deeptr_mod

modules = {
    "gtrans4_mod": gtrans4_mod,
    "gtrans3_mod": gtrans3_mod,
    "deeptr_mod": deeptr_mod
}

def analyze_text(text):
    chars = len(text)
    words = len(text.split())
    sentences = len(re.split(r'[.!?]+', text)) - 1
    return chars, words, sentences

def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        file_name = config["file_name"]
        if not os.path.exists(file_name):
            print(f"Помилка: Файл {file_name} не знайдено.")
            return

        with open(file_name, "r", encoding="utf-8") as f:
            full_text = f.read()

        chars, words, sentences = analyze_text(full_text)
        file_size = os.path.getsize(file_name)
        lang = modules[config["module"]].LangDetect(full_text, "lang")

        print(f"Файл: {file_name}\nРозмір: {file_size} байт\nСимволів: {chars}\nСлів: {words}\nРечень: {sentences}\nМова: {lang}")

        sentences_list = re.split(r'(?<=[.!?]) +', full_text)
        text_to_translate = ""
        current_chars, current_words, current_sents = 0, 0, 0

        for sentence in sentences_list:
            if (current_chars + len(sentence) > config["max_chars"] or
                current_words + len(sentence.split()) > config["max_words"] or
                current_sents + 1 > config["max_sentences"]):
                break
            text_to_translate += sentence + " "
            current_chars += len(sentence)
            current_words += len(sentence.split())
            current_sents += 1

        mod = modules[config["module"]]
        translated = mod.TransLate(text_to_translate.strip(), lang, config["target_lang"])

        if config["output"] == "screen":
            print(f"\nМова перекладу: {config['target_lang']}\nМодуль: {config['module']}\nПереклад:\n{translated}")
        elif config["output"] == "file":
            new_file_name = f"{os.path.splitext(file_name)[0]}_{config['target_lang']}.txt"
            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write(translated)
            print("Ok")

    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()