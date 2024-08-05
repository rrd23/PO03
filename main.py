import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_russian_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        english_definition = soup.find("div", id="random_word_definition").text.strip()

        russian_word = translator.translate(english_word, src='en', dest='ru').text
        russian_definition = translator.translate(english_definition, src='en', dest='ru').text

        return {
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру угадывания слов!")
    while True:
        word_dict = get_russian_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте еще раз.")
            continue

        word = word_dict["russian_word"]
        word_definition = word_dict["russian_definition"]

        print(f"\nОпределение слова: {word_definition}")
        user_guess = input("Какое это слово? ")

        if user_guess.lower() == word.lower():
            print("Верно! Вы угадали слово!")
        else:
            print(f"К сожалению, это неверно. Правильное слово: {word}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру! До свидания!")
            break


word_game()
