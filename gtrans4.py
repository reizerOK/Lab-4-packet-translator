from translation_pack import gtrans4_mod

print("Демонстрація googletrans 4.x")
print(gtrans4_mod.TransLate("Привіт, світе!", "uk", "en"))
print(gtrans4_mod.LangDetect("Слава Україні", "all"))
print(gtrans4_mod.CodeLang("ukrainian"))
gtrans4_mod.LanguageList("screen", "Добрий день")