import asyncio
import time
from googletrans import Translator, LANGUAGES

def _await_if_needed(obj):
    """Допоміжна функція для безпечної обробки асинхронних результатів"""
    if hasattr(obj, '__await__'):
        return asyncio.run(obj)
    return obj

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        result = translator.translate(text, src=scr, dest=dest)
        result = _await_if_needed(result)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        result = translator.detect(text)
        result = _await_if_needed(result)
        
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
    try:
        lang_lower = lang.lower()
        if lang_lower in LANGUAGES:
            return LANGUAGES[lang_lower].capitalize()
        for code, name in LANGUAGES.items():
            if name.lower() == lang_lower:
                return code
        return "Помилка: мову або код не знайдено"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        translator = Translator()
        output_lines = [f"{'N':<4} {'Language':<15} {'ISO-639 code':<15} {'Text'}"]
        output_lines.append("-" * 60)
        
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            translated_text = ""
            if text:
                try:
                    res = translator.translate(text, dest=code)
                    res = _await_if_needed(res)
                    translated_text = res.text
                    time.sleep(0.5) # ДОДАНО: пауза півсекунди між запитами
                except Exception as e:
                    translated_text = "Помилка"
            
            output_lines.append(f"{i:<4} {name.capitalize():<15} {code:<15} {translated_text}")
            
        final_output = "\n".join(output_lines)
        
        if out == "screen":
            print(final_output)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(final_output)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"