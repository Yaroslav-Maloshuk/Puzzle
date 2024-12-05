def find_longest_sequence(numbers):
    print("Початок пошуку найдовшої послідовності...")
    
    # Створимо словники для швидкого пошуку
    start_ends = {}
    
    # Підготуємо словник: кожне число як ключ, де воно може бути наступним
    for num in numbers:
        start_two = num[:2]
        if start_two not in start_ends:
            start_ends[start_two] = []
        start_ends[start_two].append(num)
    
    print(f"Підготовлено словник можливих переходів. Унікальних початків: {len(start_ends)}")
    
    # Функція для знаходження найдовшого ланцюжка
    def find_longest_chain(current, used):
        best_chain = [current]
        
        # Шукаємо наступне число, що починається з кінця поточного
        next_start = current[-2:]
        
        # Перебираємо всі можливі наступні числа
        for candidate in start_ends.get(next_start, []):
            if candidate not in used:
                new_used = used.copy()
                new_used.add(candidate)
                
                # Рекурсивно шукаємо подальший ланцюжок
                chain = [current] + find_longest_chain(candidate, new_used)
                
                # Обираємо найдовший ланцюжок
                if len(chain) > len(best_chain):
                    best_chain = chain
        
        return best_chain

    # Знайдемо найдовший ланцюжок
    longest_sequence = []
    print("Пошук найдовшого ланцюжка...")
    
    for start_num in numbers:
        sequence = find_longest_chain(start_num, {start_num})
        print(f"Поточний ланцюжок з {start_num}: {len(sequence)} чисел")
        
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence

    return longest_sequence

# Зчитування чисел з файлу
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # Читаємо рядки та перетворюємо їх на рядки фіксованої довжини
        return [line.strip().zfill(6) for line in file]

# Зчитування чисел
print("Зчитування чисел з файлу...")
numbers = read_numbers_from_file('text.txt')

print("Запуск алгоритму пошуку найдовшої послідовності...")
result = find_longest_sequence(numbers)

print(f"\nНайдовша послідовність ({len(result)} чисел):")
print(result)

print("\nПеревірка послідовності:")
for i in range(len(result)-1):
    current = result[i]
    next_num = result[i+1]
    is_valid = current[-2:] == next_num[:2]
    print(f"{current} -> {next_num} (Правильний перехід: {is_valid})")
    
