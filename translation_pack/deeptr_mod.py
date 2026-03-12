from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

try:
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
except Exception as e:
    langs_dict = {}
    print(f"Помилка завантаження словника мов: {e}")

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        # deep_translator також розуміє 'auto' як джерело (source)
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту."""
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            # detect_langs повертає список ймовірностей, беремо першу (найбільшу)
            langs = detect_langs(text)
            return str(langs[0].prob)
        else:
            langs = detect_langs(text)
            return f"Мова: {langs[0].lang}, Довіра: {langs[0].prob}"
    except LangDetectException as e:
        return f"Помилка визначення мови: {e}"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови або її назву."""
    try:
        lang_lower = lang.lower()
        
        # Перевіряємо, чи передано назву мови (ключ у langs_dict)
        if lang_lower in langs_dict:
            return langs_dict[lang_lower]
            
        # Перевіряємо, чи передано код мови (значення у langs_dict)
        for name, code in langs_dict.items():
            if code.lower() == lang_lower:
                return name.capitalize()
                
        return "Помилка: мову або код не знайдено"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить таблицю всіх мов, що підтримуються, та їх кодів."""
    try:
        output_lines = [f"{'N':<4} {'Language':<15} {'ISO-639 code':<15} {'Text'}"]
        output_lines.append("-" * 60)
        
        for i, (name, code) in enumerate(langs_dict.items(), 1):
            translated_text = ""
            if text:
                try:
                    translator = GoogleTranslator(source='auto', target=code)
                    translated_text = translator.translate(text)
                except Exception:
                    translated_text = "Помилка"
                    
            output_lines.append(f"{i:<4} {name.capitalize():<15} {code:<15} {translated_text}")
            
        final_output = "\n".join(output_lines)
        
        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("language_list_deeptr.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        return "Ok"
    except Exception as e:
        return f"Помилка виводу списку мов: {e}"