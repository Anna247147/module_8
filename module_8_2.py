def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    len_numbers = 0

    for num in numbers:
        try:
            if isinstance(num, (int, float)):
                result += num
                len_numbers +=1
            else:
                raise TypeError(f'Некорректный тип данных для подсчёта суммы - {num}')
        except TypeError as e:
            print(e)
        incorrect_data += 1

    return result, incorrect_data, len_numbers


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple,str)):
            raise TypeError('В numbers записан некорректный тип данных')

        total_sum, incorrect_count,len_numbers = personal_sum(numbers)

        if len(numbers) == 0:
            return 0  # Обработка пустой коллекции

        average = total_sum / len_numbers
        return average
    except TypeError as e:
        print(e)
        return None  # В случае некорректного типа данных возвращаем None
    except ZeroDivisionError:
        return 0  # Обработка деления на ноль, если коллекция пустая
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция



