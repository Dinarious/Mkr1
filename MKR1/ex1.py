import random

def generate_random_array(rows, cols, max_number):
    """Генерація випадкового масиву з заданими розмірами та максимальним значенням числа."""
    return [[random.randint(1, max_number) for _ in range(cols)] for _ in range(rows)]

def mean_of_row(row):
    """Обчислення середнього значення рядка."""
    return sum(row) / len(row) if len(row) > 0 else 0

def sort_array(array):
    """Сортування масиву за зростанням середніх значень рядків."""
    row_means = [mean_of_row(row) for row in array]

    for i in range(len(row_means)):
        for j in range(0, len(row_means) - i - 1):
            if row_means[j] > row_means[j + 1]:
                # Обмін рядків та відповідних середніх значень
                row_means[j], row_means[j + 1] = row_means[j + 1], row_means[j]
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

# Введення данних користувачем для генерації масиву
min_rows = int(input("Задайте мінімальну кількість рядків:"))
max_rows = int(input("Задайте максимальну кількість рядків:"))
min_cols = int(input("Задайте мінімальну кількість колонок:"))
max_cols = int(input("Задайте максимальну кількість колонок:"))
max_value = int(input("Задайте максимальне значення числа:"))

# Генерація та вивід початкового масиву
rows = random.randint(min_rows, max_rows)
cols = random.randint(min_cols, max_cols)
array = generate_random_array(rows, cols, max_value)

print("Початковий масив:")
for row in array:
    print(row)

# Сортування та вивід відсортованого масиву
sorted_array = sort_array(array)
print("Масив після сортування:")
for row in sorted_array:
    print(row)