# импорт библиотек
# для работы установить пакеты bs4, requests и пакет googletrans (версии 3.1.0а0)
from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words(): # парсим слово и описание с сайта
    url = "http://randomword.com" # адрес сайта
    try: # пытаемся сделать запрос и обработка исключения, если не получиться
        response = requests.get(url) # получаем все данные с сайта
        soup = BeautifulSoup(response.content, 'html.parser') # парсим полученные данные как html
        english_words = soup.find("div", id="random_word").text.strip() # берем из результа само слово
        word_definition = soup.find("div", id="random_word_definition").text.strip() # берем из результа описание слова
        translator = Translator() # создаем объект для перевода на русский
        rus_words = translator.translate(english_words, src="en", dest="ru").text # переводим слово на русский
        rus_definition = translator.translate(word_definition, src="en", dest="ru").text # переводим описание на русский
        # print(f"rus_woerd = {rus_words}")
        # print(f"rus_definition = {rus_definition}")
        # print(f"english_words = {english_words}")
        # print(f"word_definition = {word_definition}")

        return{
            "english_words": english_words,
            "word_definition": word_definition,
            "rus_words": rus_words,
            "rus_definition": rus_definition
        } # возвращаем словарь с полученными данными английскими и русскими
    except:
        print("произошла ошибка") # если произошла ошибка

def word_game(): # запуск игры
    print("добро пожаловать в игру")
    while True:
        word_dict = get_english_words() # получаем словарь
        word = word_dict.get("english_words") # берем из словаря значение слова на английском
        word_definition = word_dict.get("word_definition") # берем из словаря значение описания
        word_rus = word_dict.get("rus_words") # берем из словаря значение слова на русском
        word_definition_rus = word_dict.get("rus_definition") # берем из словаря значение описания

        print(f"Значение слова en - {word_definition}") # выводим на экран описание на английском
        print(f"Значение слова rus- {word_definition_rus}") # выводим на экран описание на русском
        user = input("что это за слово? ") # игрок вводит ответ
        translator = Translator() # создаем объект для перевода на английский
        user_en = translator.translate(user, src="ru", dest="en").text # переводим слово на английский
        if user == word or user_en == word or user == word_rus: # сравниваем ответ и правильный ответ
            print("Все верно!")
        else:
            print(f"Неверно, правильный ответ - {word} / {word_rus}")

        play_again = input("Хотите сыграть еще раз? y/n д/н ")
        print("")
        if play_again != "y" and play_again != "д":
            print("Спасибо за игру!")
            break

word_game() # запускаем игру
