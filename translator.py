from deep_translator import GoogleTranslator

translator_ru_en = GoogleTranslator(source='ru', target='en')
translator_en_ru = GoogleTranslator(source='en', target='ru')

def main():
    while True:
        print("=" * 50)
        print("0. Выход")
        print("1. Перевод с русского на английский")
        print("2. Перевод с английского на русский")
        print("=" * 50)

        choice = input("Выберите число от 0 до 2: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            user_text = input("Введите текст на русском: ")
            result = translator_ru_en.translate(user_text)
            print(f"Перевод: {result}")
        elif choice == "2":
            user_text = input("Введите текст на английском: ")
            result = translator_en_ru.translate(user_text)
            print(f"Перевод: {result}")
        else:
            print("=" * 50)
            print("Неверный ввод!")

if __name__ == '__main__':
    main()