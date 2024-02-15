
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:  # відкрити файл 
            count = 0  # ініціалізуємо лічильник
            for line in file:  # для кожного рядка в файлі 
                parts = line.strip().split(',')  # розділити рядок за комами
                if len(parts) == 3:  # перевірити формат запису
                    Id = parts[0].strip()  # отримати ідентифікатор
                    name = parts[1].strip()  # отримати ім'я
                    age = parts[2].strip()  # отримати вік
                    cats_info = {'id': Id, 'name': name, 'age': age}  # створити словник з інформацією про кота
                    print(cats_info)  # вивести інформацію про кота
                    count += 1  # збільшити лічильник
                else:
                    print(f"Неправильний формат рядка: {line}")  # вивести повідомлення про неправильний формат рядка
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None  # повернути None у випадку відсутності файлу
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None  # повернути None у випадку будь-якої іншої помилки

    if count == 0:
        print("Файл пустий.")
        return None, None  # повернути None, якщо файл пустий

# Приклад використання:
get_cats_info(r"C:\learning\Homework\goit-algo-hw-04\cats.txt")