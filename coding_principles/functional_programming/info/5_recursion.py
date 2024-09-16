# Рекурсивная функция (recursive function)
# — функция, которая в своем теле вызывает саму себя.

# Плюсы рекурсии:

# может сокращать время выполнения
# рекурсию легко отлаживать
# использует меньший объём кода и позволяет избежать сложных циклических конструкций




# Минусы рекурсии:

# может быть ресурсоёмкой
# может привести к переполнению стека при слишком глубокой рекурсии
# требует анализа влияния на производительность

# Пример: факторил

# Без рекурсии
def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        product = 1
        for i in range(1, n+1):
            product *= i
        return product

print(factorial(5))

# С рекурсией
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_rec(n - 1)

print(factorial_rec(5))



