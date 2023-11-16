def fibonachi(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]  # если n равно 1, то нужно вернуть список с одним числом 1
    elif n == 2:
        return [1, 1]  # если n равно 2, то нужно вернуть список с двумя числами 1
    elif n > 2:
        fib_nums = [1, 1]  # создаем начальный список fib_nums с двумя числами 1
        for i in range(2, n):
            fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])  # добавляем в массив число, равное сумме двух предыдущих чисел из списка fib_nums
        return fib_nums

def bubble_sort(arr):
    n = len(arr)  # количество элементов исходного массива
    for i in range(n):  # цикл от 0 до n-1, отвечает за проходы по массиву
        for j in range(0, n - i - 1):  # цикл от 0 до n-i-1, отвечает за сравнение и обмен элементов
            if arr[j] > arr[j + 1]:  # сравнение элементов arr[j] и arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # меняем местами
    return arr

def calculator(number1, number2, operation):
    if operation == "+":
        return number1 + number2  # если знак операции "+", выполняем сложение
    elif operation == "-":
        return number1 - number2  # если знак операции "-", выполняем вычитание
    elif operation == "*":
        return number1 * number2  # если знак операции "*", выполняем умножение
    elif operation == "/":
        return number1 / number2  # если знаменатель не равен нулю, выполняем деление

