# Математические формулы

## [Круг (circle.py)](../circle.py)
### Нахождение площади круга с заданным радиусом
`def area(r)`
### Нахождение длины окружности с заданным радиусом
`def perimeter(r)`

### Пример вызова

```
r = int(input("Введите радиус круга: "))
a = area(r) # Вызываем функцию area с аргументом r
p = perimetr(r) # Вызываем функцию perimetr с аргументом r
print("Area:", a)
print("Perimetr", p) 
```  
```
Введите радиус круга: 5
Area: 78.53981633974483
Perimetr: 31.41592653589793
```  
</details>  

## [Прямоугольник (rectangle.py)](../rectangle.py)
### Нахождение площади прямоугольника с заданными сторонами
def area(a, b)
### Нахождение периметра прямоугольника с заданными сторонами
`def perimeter(a, b)`

### Пример вызова

``` python
x = int(input("Введите первую сторону прямоугольника: "))
y = int(input("Введите вторую сторону: "))
a = area(x, y) # Вызываем функцию area с аргументами x и y
p = perimetr(x, y) # Вызываем функцию perimetr с аргументами x и y
print("Area:", a)
print("Perimetr", p) 
```  
```
Введите первую сторону прямоугольника: 5
Введите вторую сторону: 6
Area: 30
Perimetr: 22
```  

## [Квадрат (square.py)](../square.py)
### Нахождение площади квадрата с заданной стороной
`def area(a)`
### Нахождение периметра квадрата с заданной стороной
`def perimeter(a)`

### Пример вызова

``` python
x = int(input("Введите длину квадрата: "))
a = area(x) # Вызываем функцию area с аргументом x
p = perimetr(x) # Вызываем функцию perimetr с аргументом x
print("Area:", a)
print("Perimetr", p) 
```  
```
Введите длину квадрата: 5
Area: 25
Perimetr: 20
```  

## [Треугольник (triangle.py)](../triangle.py)
### Нахождение площади треугольника с заданным основанием и высотой, проведенной к нему
`def area(a, h)`
### Нахождение периметра треугольника с заданным основанием и высотой, проведенной к нему
`def perimeter(a, b, c)`


### Пример вызова
``` python
h = int(input("Введите высоту треугольника: ")) # Задаём высоту треугольнику и длины его сторон
x = int(input("Введите первую сторону треугольника (на которую опирается высота): "))
y = int(input("Введите вторую сторону треугольника: "))
z = int(input("Введите третью сторону треугольника: "))
a = area(x, h) # Вызываем функцию area с аргументами x и h
p = perimetr(x, y, z) # Вызываем функцию perimetr с аргументами x, y, z
print("Area:", a)
print("Perimetr", p) 
```  
```
Введите высоту треугольника: 5
Введите первую сторону треугольника (на которую опирается высота): 6
Введите вторую сторону треугольника: 8
Введите третью сторону треугольника: 10
Area: 15
Perimetr: 24
```  

# [Тесты (/test)](../tests)
### Чтобы проверить корректность работы функций нужно запустить тесты

### В папке [`tests`](../tests) находится 4 файла:
#### 1. [`test_circle.py`](../tests/test_circle.py) - файл для проверки корректности функций из [`circle.py`](../circle.py)
#### 2. [`test_rectangle.py`](../tests/test_rectangle.py) - файл для проверки корректности функций из [`rectangle.py`](../rectangle.py)
#### 3. [`test_square.py`](../tests/test_square.py) - файл для проверки корректности функций из [`square.py`](../square.py)
#### 4. [`test_triangle.py`](../tests/test_triangle.py) - файл для проверки корректности функций из [`triangle.py`](../triangle.py)


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
9. [`eda87d5`](https://github.com/ogrock3t/geometric_lib/commit/eda87d55284e8fc21315a0a4ea68af030a592daa) - Добавлены CI/CD
10. [`7339730`](https://github.com/ogrock3t/geometric_lib/commit/7339730d546ec76ec112e0c0e665937887d2f021) - Проверка работы CI/CD
11. [`c3381fe`](https://github.com/ogrock3t/geometric_lib/commit/c3381fe221a9d352e294b85abf7f2ac331c81a45) - Исправлено документирование в [`README.md`](./README.md)