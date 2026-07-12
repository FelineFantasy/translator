from deep_translator import GoogleTranslator

# Тексты интерфейса на разных языках
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
    }
}

translator_ru_en = GoogleTranslator(source='ru', target='en')
translator_en_ru = GoogleTranslator(source='en', target='ru')

def get_locale():
    """Запрашивает у пользователя язык интерфейса"""
    print("Select language / Выберите язык:")
    print("1. English")
    print("2. Русский")
    choice = input("Choice / Выбор (1-2): ").strip()
    return 'en' if choice == '1' else 'ru'

def main():
    locale = get_locale()
    t = LOCALES[locale]
    
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
