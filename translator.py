from deep_translator import GoogleTranslator
import locale
import os

LOCALES = {
    'en': {
        'title': "Console Translator",
        'separator': "=" * 40,
        'menu_0': "0. Exit",
        'menu_1': "1. Russian -> English",
        'menu_2': "2. English -> Russian",
        'prompt': "Choice (0-2): ",
        'input_ru': "Enter text in Russian: ",
        'input_en': "Enter text in English: ",
        'error_empty': "Error: empty input!",
        'error_translate': "Translation error: ",
        'result': "Translation: ",
        'invalid_choice': "Invalid choice!",
        'goodbye': "Goodbye!",
        'lang_detected': "Interface language: English",
    },
    'ru': {
        'title': "Консольный переводчик",
        'separator': "=" * 40,
        'menu_0': "0. Выход",
        'menu_1': "1. Русский -> Английский",
        'menu_2': "2. Английский -> Русский",
        'prompt': "Выбор (0-2): ",
        'input_ru': "Введите текст на русском: ",
        'input_en': "Введите текст на английском: ",
        'error_empty': "Ошибка: пустой ввод!",
        'error_translate': "Ошибка перевода: ",
        'result': "Перевод: ",
        'invalid_choice': "Неверный выбор!",
        'goodbye': "До свидания!",
        'lang_detected': "Язык интерфейса: Русский",
    }
}

translator_ru_en = GoogleTranslator(source='ru', target='en')
translator_en_ru = GoogleTranslator(source='en', target='ru')

def get_system_language():
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
        lang = locale.getlocale()[0]
        if lang and lang[:2] in LOCALES:
            return lang[:2]
    except:
        pass
    
    try:
        lang = os.environ.get('LANG', '') or os.environ.get('LANGUAGE', '')
        if lang and lang[:2] in LOCALES:
            return lang[:2]
    except:
        pass
    
    if os.name == 'nt':
        try:
            import subprocess
            cmd = 'powershell -command "Get-WinSystemLocale | Select-Object -ExpandProperty Name"'
            result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
            lang = result.stdout.strip()[:2]
            if lang in LOCALES:
                return lang
        except:
            pass
    
    print("\n" + "=" * 40)
    print("Unable to detect system language / Не удалось определить язык системы")
    print("=" * 40)
    print("1. English")
    print("2. Русский")
    
    while True:
        choice = input("Choice / Выбор (1-2): ").strip()
        if choice == '1':
            return 'en'
        elif choice == '2':
            return 'ru'
        else:
            print("Invalid choice / Неверный выбор. Please try again / Попробуйте снова.")

def main():
    locale_code = get_system_language()
    t = LOCALES[locale_code]
    
    print(t['lang_detected'])
    print(t['title'])
    print(t['separator'])
    
    while True:
        print(f"\n{t['menu_0']}")
        print(t['menu_1'])
        print(t['menu_2'])
        
        choice = input(t['prompt']).strip()
        
        if choice == "0":
            print(t['goodbye'])
            break
            
        elif choice == "1":
            user_text = input(t['input_ru']).strip()
            if not user_text:
                print(t['error_empty'])
                continue
            try:
                result = translator_ru_en.translate(user_text)
                print(f"{t['result']}{result}")
            except Exception as e:
                print(f"{t['error_translate']}{e}")
                
        elif choice == "2":
            user_text = input(t['input_en']).strip()
            if not user_text:
                print(t['error_empty'])
                continue
            try:
                result = translator_en_ru.translate(user_text)
                print(f"{t['result']}{result}")
            except Exception as e:
                print(f"{t['error_translate']}{e}")
                
        else:
            print(t['invalid_choice'])

if __name__ == '__main__':
    main()