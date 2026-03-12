from translation_pack import deeptr_mod

print("Демонстрація googletrans 4.x")
print(deeptr_mod.TransLate("Привіт, світе!", "uk", "en"))
print(deeptr_mod.LangDetect("Слава Україні", "all"))
print(deeptr_mod.CodeLang("ukrainian"))
deeptr_mod.LanguageList("screen", "Добрий день")