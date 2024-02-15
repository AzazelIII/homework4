def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file: # відкрити файл 
            for line in file:                               # для ліній в файлі 
                parts = line.strip().split(',')         # розділ по комі в  рядку 
                if len(parts) == 2:                     # перевірка на формат запису 
                    salary = int(parts[1])                 # Прирівнюємо зарплату до змінної 
                    total += salary
                    count += 1
                else:
                    print(f"Неправильний формат рядка: {line}")
                    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0,0
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0,0
    
    if count == 0:
        print("Файл пустий.")
        return 0,0

total, average = total_salary("C:\learning\Homework\goit-algo-hw-04\salary.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
