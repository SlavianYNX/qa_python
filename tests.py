import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_not_genre(self):
        collector = BooksCollector()
        book_one = 'Война и мир'
        collector.add_new_book(book_one)
        assert book_one in collector.books_genre
        assert collector.books_genre[book_one] == ''


    def test_set_book_genre_new_genre_book(self):
        collector = BooksCollector()
        book_one = 'Гордость и предубеждение и зомби'
        genre = 'Комедии'
        collector.add_new_book(book_one)
        collector.set_book_genre(book_one, genre)
        assert book_one in collector.books_genre
        assert collector.get_book_genre(book_one) == 'Комедии'

