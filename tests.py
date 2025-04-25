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

    @pytest.mark.parametrize('book_name, genre', {('Чужой', 'Ужасы'),
    ('Преступление и наказание', 'Детективы'),
    ('Гарри Поттер и философский камень', 'Фантастика')})
    def test_get_book_genre_by_name(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_list_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']
        assert collector.get_books_with_specific_genre('Приключения') == []

    def test_get_books_genre_get_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        books_genre = {'Колобок': 'Мультфильмы', 'Шрек': 'Мультфильмы'}
        assert collector.get_books_genre() == books_genre

    def test_get_books_for_children_return_books_children(self):
        collector = BooksCollector()
        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.genre_age_rating = ['Ужасы', 'Детективы']
        collector.books_genre = {
            'Колобок': 'Мультфильмы',
            'Чужой': 'Ужасы',
            'Гарри Потер': 'Фантастика',
            'Агата Кристи': 'Детективы'
        }
        result = ['Колобок', 'Гарри Потер']
        result_new = ['Чужой', 'Агата Кристи']
        assert collector.get_books_for_children() == result
        assert collector.get_books_for_children() != result_new

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        books_genre = 'Чужой'
        collector.add_new_book(books_genre)
        collector.add_book_in_favorites(books_genre)
        assert books_genre in collector.favorites
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        book_new = 'Чужой'
        collector.add_book_in_favorites(book_new)
        collector.delete_book_from_favorites(book_new)
        assert book_new not in collector.favorites

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.favorites = ['Чужой', 'Колобок', 'Шерлок Холмс']
        assert collector.get_list_of_favorites_books() == ['Чужой', 'Колобок', 'Шерлок Холмс']