import numpy as np
import matplotlib.pyplot as plt

def fibonachi(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_nums = [1, 1]
        for i in range(2, n):
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        return fib_nums

n = int(input("Введите количество чисел Фибоначчи: "))
while (n <= 0):
    n = int(input("Некорректный ввод. Введите еще раз: "))
fibonacci_numbers = fibonachi(n)

fibonacci_values = np.array(fibonacci_numbers)
fibonacci_positions = np.arange(1, n+1)

plt.plot(fibonacci_positions, fibonacci_values, marker='o')
plt.xlabel("Номер числа Фибоначчи")
plt.ylabel("Значение числа Фибоначчи")
plt.title("График чисел Фибоначчи")
plt.grid(True)
plt.show()