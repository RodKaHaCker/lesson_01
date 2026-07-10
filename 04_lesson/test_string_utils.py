import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ========== Тесты для capitalize ==========

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),          # цифры в начале — capitalize не меняет
    ("", ""),                      # пустая строка
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", " "),                    # строка с пробелом
    ("123", "123"),                # только цифры
    ("   skypro", "   skypro"),    # пробелы в начале
    ("skypro   ", "Skypro   "),    # пробелы в конце
    (None, None),                  # None — ожидаем ошибку
])
def test_capitalize_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected


# ========== Тесты для trim ==========

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),   # удаляет только пробелы в начале
    ("skypro", "skypro"),                   # без пробелов
    ("", ""),                               # пустая строка
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),                     # только пробел
    ("   ", ""),                   # несколько пробелов
    ("123", "123"),                # цифры без пробелов
    (None, None),                  # None — ожидаем ошибку
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# ========== Тесты для contains ==========

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "U", False),
    ("hello", "h", True),
    ("", "", False),               # пустая строка и пустой символ
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", False),        # символа нет
    ("123", "1", True),            # цифра как символ
    ("", "a", False),              # пустая строка
    (None, "a", False),            # None — метод вернёт False
    ("abc", None, False),          # символ None — ожидаем ошибку
])
def test_contains_negative(string, symbol, expected):
    if symbol is None:
        with pytest.raises(TypeError):
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected


# ========== Тесты для delete_symbol ==========

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello", "l", "heo"),
    ("", "", ""),                  # пустая строка, пустой символ
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),     # символа нет — строка не меняется
    ("123", "4", "123"),           # символа нет
    ("", "a", ""),                 # пустая строка
    ("abc", "", "abc"),            # пустой символ — строка не меняется
    (None, "a", None),             # None — ожидаем ошибку
])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(string, symbol)
    else:
        assert string_utils.delete_symbol(string, symbol) == expected
