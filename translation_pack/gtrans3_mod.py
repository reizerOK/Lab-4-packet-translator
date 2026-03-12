import sys
from googletrans import Translator, LANGUAGES

if sys.version_info >= (3, 13):
    print("Попередження: Версія Python 3.13 або вище. Пакет googletrans==3.1.0a0 може працювати нестабільно або не підтримуватися.")

def TransLate(text: str, scr: str, dest: str) -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        translator = Translator()
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту."""
    try:
        translator = Translator()
        result = translator.detect(text)

        confidence = result.confidence
        if isinstance(confidence, list):
            confidence = confidence[0]
            
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"Мова: {result.lang}, Довіра: {confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови або її назву."""
    try:
        lang_lower = lang.lower()
        if lang_lower in LANGUAGES:
            return LANGUAGES[lang_lower].capitalize()
        for code, name in LANGUAGES.items():
            if name.lower() == lang_lower:
                return code
        return "Помилка: мову або код не знайдено в таблиці"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить таблицю всіх мов, що підтримуються, та їх кодів."""
    try:
        translator = Translator()
        output_lines = [f"{'N':<4} {'Language':<15} {'ISO-639 code':<15} {'Text'}"]
        output_lines.append("-" * 60)
        
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            translated_text = ""
            if text:
                try:
                    translated_text = translator.translate(text, dest=code).text
                except:
                    translated_text = "Помилка"

            output_lines.append(f"{i:<4} {name.capitalize():<15} {code:<15} {translated_text}")
            
        final_output = "\n".join(output_lines)
        
        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("language_list_v3.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        return "Ok"
    except Exception as e:
        return f"Помилка виводу списку мов: {e}"