# Útěk ze Střední průmyslové Shawshank

## Projekt studentů oboru elektronické počítačové systémy, jaro 2022

Top-down bludišťovka s minihrami. Unikněte ze školy, než zazvoní na hodinu!

### Struktura repozitáře
- `bin` binární verze hry
- `data` assety hry
- `doc` dokumentace, návody
- `src` zdrojové soubory v Pythonu

### Použitý software
- [Thonny](https://thonny.org/)
- [Tiled](https://www.mapeditor.org/)
- [Pixel Studio](https://com-pixelstudio.en.uptodown.com/android)
- [Aseprite](https://www.aseprite.org/)
- [Ardour](https://ardour.org/)

### Build distribuční verze s jedním .exe souborem
0. Je třeba mít nainstalovaný nástroj [`pyinstaller`](https://pyinstaller.org/en/stable/index.html)
1. Ve složce `bin/` spusťte dávkový soubor `build_onefile.bat`
2. Vygeneruje se složka `bin/dist/` s binární verzí aplikace
3. Hra se spouští souborem `shawshank.exe` ve složce `bin/dist/`

### Build distribuční verze s pomocnými soubory
0. Je třeba mít nainstalovaný nástroj [`pyinstaller`](https://pyinstaller.org/en/stable/index.html)
1. Ve složce `bin/` spusťte dávkový soubor `build.bat`
2. Vygeneruje se složka `bin/dist/` s binární verzí aplikace
3. Hra se spouští souborem `shawshank.exe` ve složce `bin/dist/shawshank/`

