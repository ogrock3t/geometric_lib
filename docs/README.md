# Математические формулы

## [Круг (circle.py)](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/circle.py)
### Нахождение площади круга с заданным радиусом
`def area(r)`
### Нахождение длины окружности с заданным радиусом
`def perimeter(r)`

## [Прямоугольник (rectangle.py)](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/rectangle.py)
### Нахождение площади прямоугольника с заданными сторонами
def area(a, b)
### Нахождение периметра прямоугольника с заданными сторонами
`def perimeter(a, b)`

## [Квадрат (square.py)](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/square.py)
### Нахождение площади квадрата с заданной стороной
`def area(a)`
### Нахождение периметра квадрата с заданной стороной
`def perimeter(a)`

## [Треугольник (triangle.py)](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/triangle.py)
### Нахождение площади треугольника с заданным основанием и высотой, проведенной к нему
`def area(a, h)`
### Нахождение периметра треугольника с заданным основанием и высотой, проведенной к нему
`def perimeter(a, b, c)`


# [Тесты (/test)](https://github.com/ogrock3t/geometric_lib/tree/new_features_464914/tests)
### Чтобы проверить корректность работы функций нужно запустить тесты

### В папке [`tests`](https://github.com/ogrock3t/geometric_lib/tree/new_features_464914/tests) находится 4 файла:
#### 1. [`test_circle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_circle.py) - файл для проверки корректности функций из [`circle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/circle.py)
#### 2. [`test_rectangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_rectangle.py) - файл для проверки корректности функций из [`rectangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/rectangle.py)
#### 3. [`test_square.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_square.py) - файл для проверки корректности функций из [`square.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/square.py)
#### 4. [`test_triangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_triangle.py) - файл для проверки корректности функций из [`triangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/triangle.py)


### Для запуска тестов введите в терминал:
`python3 -m unittest discover -s tests`

# [История изменений](https://github.com/ogrock3t/geometric_lib/commits/new_features_464914/)
1. [`8ba9aeb`](https://github.com/ogrock3t/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) - Добавлены [`circle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/circle.py) и [`square.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/square.py)
2. [`d078c8d`](https://github.com/ogrock3t/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) - Добавлены документы
3. [`3ee901d`](https://github.com/ogrock3t/geometric_lib/commit/3ee901d8a519f9a0322bf9b78acd437efe6e0f29) - Исправлена ошибка в файле [`rectangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/rectangle.py)
4. [`6882bdd`](https://github.com/ogrock3t/geometric_lib/commit/6882bdd72d11567eccb2be2b668bed10721acfda) - Добавлен файл [`triangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/triangle.py)
5. [`6788eac`](https://github.com/ogrock3t/geometric_lib/commit/6788eacc8ac97780226f085e5e6e6ef17165c3eb) - Добавлена документация в [`circle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/circle.py), [`rectangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/rectangle.py), [`square.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/square.py)
6. [`3868bb9`](https://github.com/ogrock3t/geometric_lib/commit/3868bb91a1f51ec5d2b5e6010dba2c6da93e7308) - Добавление документации в [`README.md`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/docs/README.md)
7. [`58c58cc`](https://github.com/ogrock3t/geometric_lib/commit/58c58cc059ef3916a9d48738f1febece117eb605) - Добавление файлов [`test_circle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_circle.py), [`test_rectangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_rectangle.py), [`test_square.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_square.py), [`test_triangle.py`](https://github.com/ogrock3t/geometric_lib/blob/new_features_464914/tests/test_triangle.py)
8. [`e859d06`](https://github.com/ogrock3t/geometric_lib/commit/e859d06b52a68b276122ddf7b30026c1e65f30fe) - Исправлены все ошибки
