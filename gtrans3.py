from translation_pack import gtrans3_mod

print("Демонстрація googletrans 3.x")
print(gtrans3_mod.TransLate("Привіт, світе!", "uk", "en"))
print(gtrans3_mod.LangDetect("Слава Україні", "all"))
print(gtrans3_mod.CodeLang("ukrainian"))
gtrans3_mod.LanguageList("screen", "Добрий день")