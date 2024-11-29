def personal_sum(numbers):
    result = 0  # переменная для хранения суммы чисел.
    incorrect_data = 0  # счетчик некорректных данных.
    for item in numbers:  # перебираем каждый элемент в коллекции numbers.
        try:  # try: блок кода, где мы пытаемся выполнить операции, которые могут вызвать исключения.
            result += item  # добавляем текущий элемент к result.
        except TypeError:  # если возникает ошибка при попытке сложения (например,если item не число),выполняется  код
            print(f' Некорректный тип данных для подсчета суммы-{item}')
            incorrect_data += 1  # увеличиваем счетчик некорректных данных.
    return result, incorrect_data  # возвращает кортеж, содержащий сумму всех корректных чисел и
    # количество некорректных данных.


def calculate_average(numbers):
    try:
        total_sam, incorrect_data = personal_sum(
            numbers)  # вызываем personal_sum, сумма и количество некорректных данных.
        average = total_sam / (len(numbers) - incorrect_data)  # вычисляем среднее арифметическое. Вычитаем количество
        # некорректных данных из общего количества элементов numbers
        return average
    except ZeroDivisionError:  # Обработка исключения деления на ноль.
        return 0  # если в numbers все элементы оказались некорректными и делить нечего, возвращаем 0.
    except TypeError:  # если numbers не является итерируемым объектом, выводим сообщение об ошибке
        print(f'В numbers записан некорректный тип данных')
        return None  # возвращаем None.

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать