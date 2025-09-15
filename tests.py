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

@pytest.fixture
def collector():
    return BooksCollector()


def test_add_new_book_not_genre(collector):
    book_one = 'Война и мир'
    collector.add_new_book(book_one)
    assert book_one in collector.books_genre
    assert collector.books_genre[book_one] == ''


def test_set_book_genre_new_genre_book(collector):
    book_one = 'Гордость и предубеждение и зомби'
    genre = 'Комедии'
    collector.add_new_book(book_one)
    collector.set_book_genre(book_one, genre)
    assert book_one in collector.books_genre
    assert collector.get_book_genre(book_one) == 'Комедии'


@pytest.mark.parametrize('book_name, genre', {('Чужой', 'Ужасы'),
    ('Преступление и наказание', 'Детективы'),
    ('Гарри Поттер и философский камень', 'Фантастика')})
def test_get_book_genre_by_name(collector, book_name, genre):
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.books_genre[book_name] == genre


def test_get_books_with_specific_genre_list_book(collector):
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Детективы')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', '1984']
    assert collector.get_books_with_specific_genre('Приключения') == []


def test_get_books_genre_get_dictionary(collector):
    collector.add_new_book('Колобок')
    collector.set_book_genre('Колобок', 'Мультфильмы')
    collector.add_new_book('Шрек')
    collector.set_book_genre('Шрек', 'Мультфильмы')
    books_genre = {'Колобок': 'Мультфильмы', 'Шрек': 'Мультфильмы'}
    assert collector.get_books_genre() == books_genre


def test_get_books_for_children_return_books_children(collector):
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


def test_add_book_in_favorites_add_book(collector):
    books_genre = 'Чужой'
    collector.add_new_book(books_genre)
    collector.add_book_in_favorites(books_genre)
    assert books_genre in collector.favorites
    assert len(collector.favorites) == 1


def test_delete_book_from_favorites_delete_book(collector):
    book_new = 'Чужой'
    collector.add_book_in_favorites(book_new)
    collector.delete_book_from_favorites(book_new)
    assert book_new not in collector.favorites


def test_get_list_of_favorites_books_get_list(collector):
    collector.favorites = ['Чужой', 'Колобок', 'Шерлок Холмс']
    assert collector.get_list_of_favorites_books() == ['Чужой', 'Колобок', 'Шерлок Холмс']


# Дополнительные тесты

# Тест: не добавлять книгу с пустым именем
def test_add_new_book_empty_name(collector):
    collector.add_new_book('')
    assert '' not in collector.books_genre
    assert len(collector.get_books_genre()) == 0


# Тест: граничные значения длины имени (40 допустимо, 41 — нет)
def test_add_new_book_name_length_boundary(collector):
    name_40 = 'x' * 40
    name_41 = 'y' * 41
    collector.add_new_book(name_40)
    collector.add_new_book(name_41)
    assert name_40 in collector.books_genre
    assert name_41 not in collector.books_genre


# Тест: добавление дубликата книги не создаёт второй записи
def test_add_duplicate_book(collector):
    name = 'Дублированная книга'
    collector.add_new_book(name)
    collector.add_new_book(name)
    # словарь должен содержать только одну запись
    assert list(collector.get_books_genre().keys()).count(name) == 1


# Тест: установка жанра для несуществующей книги — ничего не меняется
def test_set_genre_for_nonexistent_book(collector):
    collector.set_book_genre('Несуществующая', 'Фантастика')
    assert collector.get_book_genre('Несуществующая') is None


# Тест: попытка установить недопустимый жанр — жанр не устанавливается
def test_set_invalid_genre_not_in_list(collector):
    book = 'Книга с неверным жанром'
    collector.add_new_book(book)
    collector.set_book_genre(book, 'НеЖанр')
    assert collector.get_book_genre(book) == ''


# Тест: добавить в избранное книгу, которой нет в коллекции — не добавлять
def test_add_book_in_favorites_without_adding_book(collector):
    collector.add_book_in_favorites('НеДобавленнаяКнига')
    assert 'НеДобавленнаяКнига' not in collector.favorites


# Тест: повторное добавление в избранное не дублирует элемент
def test_add_book_in_favorites_duplicate_favorite(collector):
    book = 'Любимая книга'
    collector.add_new_book(book)
    collector.add_book_in_favorites(book)
    collector.add_book_in_favorites(book)
    assert collector.favorites.count(book) == 1
    assert len(collector.favorites) == 1


# Тест: удаление несуществующей книги из избранного — не вызывает ошибок и не меняет список
def test_delete_nonexistent_favorite(collector):
    # Начинаем с пустого favorites
    collector.delete_book_from_favorites('Нету')
    assert collector.favorites == []


# Тест: get_books_with_specific_genre на пустой коллекции возвращает []
def test_get_books_with_specific_genre_empty_collection(collector):
    assert collector.get_books_with_specific_genre('Фантастика') == []


# Тест: книги с жанром вне списка genre игнорируются в get_books_for_children
def test_get_books_for_children_ignores_invalid_genre(collector):
    collector.books_genre = {'СтраннаяКнига': 'НеИзвестныйЖанр'}
    assert collector.get_books_for_children() == []


# Тест: полный 
def test_workflow_state_consistency(collector144):
    a = 'Книга A'
    b = 'Книга B'
    collector.add_new_book(a)
    collector.add_new_book(b)
    collector.set_book_genre(a, 'Фантастика')
    collector.set_book_genre(b, 'Ужасы')
    collector.add_book_in_favorites(a)
    collector.add_book_in_favorites(b)
    collector.delete_book_from_favorites(b)

    assert collector.get_book_genre(a) == 'Фантастика'
    assert collector.get_book_genre(b) == 'Ужасы'
    assert a in collector.favorites and b not in collector.favorites
    assert collector.get_books_with_specific_genre('Фантастика') == [a]