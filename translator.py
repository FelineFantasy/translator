from deep_translator import GoogleTranslator

translator_ru_en = GoogleTranslator(source='ru', target='en')
translator_en_ru = GoogleTranslator(source='en', target='ru')

def main():
    print("Console Translator")
    print("=" * 40)

    while True:
        print("\n0. Exit")
        print("1. Russian -> English")
        print("2. English -> Russian")

        choice = input("Choice (0-2): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            user_text = input("Enter text in Russian: ").strip()
            if not user_text:
                print("Error: empty input!")
                continue
            try:
                result = translator_ru_en.translate(user_text)
                print(f"Translation: {result}")
            except Exception as e:
                print(f"Translation error: {e}")
        elif choice == "2":
            user_text = input("Enter text in English: ").strip()
            if not user_text:
                print("Error: empty input!")
                continue
            try:
                result = translator_en_ru.translate(user_text)
                print(f"Translation: {result}")
            except Exception as e:
                print(f"Translation error: {e}")
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
