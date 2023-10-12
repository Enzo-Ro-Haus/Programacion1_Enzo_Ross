import pytest
from TP5F import are_multiple, valid_id, last_word, id_maker, space, maxmin, area, perimeter, login, total_price, times_ten,  multiples_of_ten, words_size, module, prime_numbers, number_frequency, sum_of_digit, number_frequency_on_group

@pytest.mark.parametrize("document", [1_000_000, 99_999_999])
def test_valid_idn(document):
    assert valid_id(document) == True

@pytest.mark.parametrize("document", [999_999, 100_000_000, [], {}, (), "", "a", None])
def test_valid_idn(document):
    assert valid_id(document) == False

@pytest.mark.parametrize("quote", ["frase".split(), "This is a frase".split(), " frase ".split()])
def test_last_word(quote):
    assert last_word(quote) == 'frase'

@pytest.mark.parametrize("quote", ["", {}, (), 1, None])
def test_last_word(quote):
    assert last_word(quote) == ''

@pytest.mark.parametrize("f_name, id_number", [
    ("Name Surname".split(), 10_000_000),
    ("Name Surname".split(), 1_000_000),
    ("Name SecondName Surname".split(), 10_000_000),
    ("Name SecondName Surname".split(), 1_000_000)
])
def test_id_maker(f_name, id_number):
    assert  id_maker(f_name, id_number) == "Name7100"

@pytest.mark.parametrize("f_name, id_number", [
    ((), 10_000_000),
    ({}, 1_000_000),
    (None, 1_000_000),
    ("Name Surname".split(), 3),
    ("Name Surname".split(), 100000000),
    ("Name Surname".split(), []),
    ("Name Surname".split(), {}),
    ("Name SecondName Surname".split(), ()),
    ("Name SecondName Surname".split(), None)
])
def test_id_maker(f_name, id_number):
    assert  id_maker(f_name, id_number) == ""

@pytest.mark.parametrize("number, a_number", [(4, 2), (2,2), (0,2)])
def test_are_multiple(number, a_number):
    assert are_multiple(number, a_number) == True

@pytest.mark.parametrize("number, a_number", [(2, 4)])
def test_are_multiple(number, a_number):
    assert are_multiple(number, a_number) == False

@pytest.mark.parametrize("number, a_number", [
    (None, 4),
    (4, None),
    ({} , 4),
    (4,{})
    ])
def test_are_multiple(number, a_number):
    assert are_multiple(number, a_number) == None

@pytest.mark.parametrize("f", ["Hola, tú"])
def test_space(f):
    assert space(f) == "H o l a , t ú"

@pytest.mark.parametrize("f", [(), {}, [], 0, None])
def test_space(f):
    assert space(f) == None

@pytest.mark.parametrize("l_num", [[10, 1], [1, 10]])
def test_maxmin(l_num):
    assert maxmin(l_num) == (10, 1)

@pytest.mark.parametrize("l_num", [[10, 1], [1, 10]])
def test_maxmin(l_num):
    assert maxmin(l_num) == (10, 1)

@pytest.mark.parametrize("r", [3])
def test_area(r):
    assert area(r) == 28.3

@pytest.mark.parametrize("r", [3])
def test_perimeter(r):
    assert perimeter(r) == 18.8

@pytest.mark.parametrize("name, pass_w, trys", [
    ("usuario1", "asdasd", 1)
])
def test_login(name, pass_w, trys):
    assert login(name, pass_w, trys) == True

@pytest.mark.parametrize("name, pass_w, trys", [
    (" ", "asdasd", 1),
    ("usuario1", " ", 1),
    (" ", " ", 1)
])
def test_login(name, pass_w, trys):
    assert login(name, pass_w, trys) == False

@pytest.mark.parametrize("purchase_information", [
    {
        "Milk"      :   {"price" : 100, "discount": 0.5},
        "Bread"     :   {"price" : 100, "discount": 0.5},
        "Eggs"      :   {"price" : 100, "discount": 0.5},
        "Apples"    :   {"price" : 100, "discount": 0.5}
    },
    {
        "Milk"      :   {"price" : 100, "discount": 1},
        "Bread"     :   {"price" : 100, "discount": 1},
    }
])
def test_total_price(purchase_information):
    assert total_price(purchase_information) == 200

@pytest.mark.parametrize("number", [2])
def test_times_ten(number):
    assert times_ten(number) == 20

@pytest.mark.parametrize("numbers, function", [
    ([1,2,3,4,5], times_ten)
])
def test_multiples_of_ten(numbers, function):
    assert  multiples_of_ten(numbers, function) == [10, 20, 30, 40, 50]

@pytest.mark.parametrize("f", ["This is a quote"])
def test_words_size(f):
    assert words_size(f) == {'This': 4, 'is': 2, 'a': 1, 'quote': 5}

@pytest.mark.parametrize("vx, vy, vz", [(2, 2, 2)])
def test_module(vx, vy, vz):
    assert module(vx, vy, vz) == 3.5

@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
def test_prime_numbers(num):
    assert prime_numbers(num) == True

@pytest.mark.parametrize("num", [4, 6, 8, 12, 14, 18, 20, 24, 20, 32, 38, 42, 44, 48, 54, 60, 62, 68, 72, 74, 80, 84, 90, 98])
def test_prime_numbers(num):
    assert prime_numbers(num) == False

@pytest.mark.parametrize("num, dig", [("11", "1"), ("252", "2")])
def test_number_frequency(num, dig):
    assert number_frequency(num, dig) == 2

@pytest.mark.parametrize("a_of_num", [[11, 13, 17, 19], [2, 4, 8, 91], [11, 31,  71, 91]])
def test_sum_of_digit(a_of_num):
    assert sum_of_digit(a_of_num) == [2, 4, 8, 10]

@pytest.mark.parametrize("a_of_num, number", [
    ([13,17,11], 1),
    ([1,1,1,1], 1),
    ([1111], 1)
    ])
def test_number_frequency_on_group(a_of_num, number):
    assert number_frequency_on_group(a_of_num, number) == 4

#! Algunos imprimen pero no retornan nada, ¿deberían restornar algo testeable? Ej: fac

