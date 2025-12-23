#словник, автор Кондратенко Р. ППМР1-104
students = {
    "Andrii Andrienko": {
        'Навчальна група': "КН-42",
        'Предмети': ["Чисельні методи", "Алгоритми та структури даних",
                     "Програмування мовою Пайтон", "Математичні методи дослідження операцій"],
        'Бали за семестр': [90, 95, 98, 85]
    },
    "Igor Igorovych": {
        'Навчальна група': "КН-41",
        'Предмети': ["Чисельні методи", "Алгоритми та структури даних",
                     "Програмування мовою Пайтон", "Математичні методи дослідження операцій"],
        'Бали за семестр': [80, 90, 85, 97]
    },
    "Anna Anenko": {
        'Навчальна група': "КН-42",
        'Предмети': ["Чисельні методи", "Алгоритми та структури даних",
                     "Програмування мовою Пайтон", "Математичні методи дослідження операцій"],
        'Бали за семестр': [79, 91, 83, 97]
    },
    "Egor Egorovych": {
        'Навчальна група': "КН-43",
        'Предмети': ["Чисельні методи", "Алгоритми та структури даних",
                     "Програмування мовою Пайтон", "Математичні методи дослідження операцій"],
        'Бали за семестр': [82, 87, 81, 100]
    }
}

groups_list = ["КН-41", "КН-42", "КН-43", "КН-44", "КН-45"]
disciplines_list = ["Чисельні методи", "Алгоритми та структури даних",
                    "Програмування мовою Пайтон", "Математичні методи дослідження операцій"]


#функція додання студентів, автор Кондратенко Р. ППМР1-104
def add_students():
    print("\nВведіть дані студентів, яких дописуватимете.")
    print("Щоб завершити, напишіть 'стоп' при введенні імені студента.")

    while True:
        student_id = input("\nВведіть ім’я та прізвище студента: ")
        if student_id.lower() == "стоп":
            break

        group_input = input("Введіть свою навчальну групу (КН-41, КН-42, КН-43, КН-44, КН-45): ")
        if group_input not in groups_list:
            print("Такої навчальної групи не існує.")
            continue

        disciplines_input = input("Введіть дисципліни через кому: ").split(", ")

        marks_input = input("Введіть оцінки через кому: ").split(", ")
        try:
            marks = list(map(int, marks_input))
        except ValueError:
            print("Оцінки мають бути цілими числами.")
            continue

        if len(marks) != len(disciplines_input):
            print("Кількість оцінок не співпадає з кількістю предметів.")
            continue

        students[student_id] = {
            'Навчальна група': group_input,
            'Предмети': disciplines_input,
            'Бали за семестр': marks
        }

        print(f"Студента {student_id} додано до словника.")


#Функція сортування за групою, автор Гуменюк Андрій ППМР1-104
def sort_students_by_group(students_dict):
    items = students_dict.items()
    sorted_items = sorted(items, key=lambda x: x[1]['Навчальна група'])
    sorted_students_dict = dict(sorted_items)
    print("\nСловник студентів відсортовано за навчальною групою.")
    return sorted_students_dict


#функція середнього арифметичного, автор Шевченко О. ППМР1-105
def calculate_group_average(data, target_group):
    if target_group not in groups_list:
        return f"Помилка: Група '{target_group}' не існує у системі."

    total_marks_sum = 0
    total_marks_count = 0

    for student_name, info in data.items():
        if info['Навчальна група'] == target_group:
            total_marks_sum += sum(info['Бали за семестр'])
            total_marks_count += len(info['Бали за семестр'])

    if total_marks_count > 0:
        average = total_marks_sum / total_marks_count
        return f"Середній бал для групи {target_group}: {average:.2f}"
    else:
        return f"Студентів у групі {target_group} не знайдено."


#робота з файлами, автор Діана Пасішніченко ППМР1-105
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не відкрився!")
        return None
    else:
        print("Файл", file_name, "відкрився успішно")
        return file


file1_name = "laboratorna8.txt"
file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    lines = [
        "Кондратенко Роман",
        "напиши, що тобі подобається у цій програмі,",
        "а також напиши те, що тобі не подобається.",
        "можеш коротко, 1-2 реченнями про кожен пункт",
        "і не забудь вписати потім своє прізвище та ім'я",
        "та не забудь написати питання наступній людині з команди.",
        "і якщо будуть проблеми з кодуванням текстового файлу, обирай віндовс-1251."
    ]

    for line in lines:
        file_1_w.write(line + "\n")

    print("Текст був успішно доданий до laboratorna8.txt!")
    file_1_w.close()
    print("Файл laboratorna8.txt закрився")


#демонстрація видалення зі словника, автор Діана Пасішніченко ППМР1-105
students_demo = {
    "Іван": 18,
    "Марія": 19,
    "Олег": 20,
    "Аліна": 18
}

print("\nПочатковий словник:", students_demo)

del students_demo["Олег"]
removed_age = students_demo.pop("Марія")

print("Марія була видалена, її вік був:", removed_age)
print("Словник після видалень:", students_demo)


#перемикач, автор Кондратенко Р. ППМР1-104
choice = input(
    "Введіть 1, щоб дописати студентів, 0 — щоб вивести дані, "
    "2 — щоб завершити, 3 — щоб сортувати за групою, "
    "4 — щоб обчислити середній бал групи: "
)

if choice == "1":
    add_students()

elif choice == "0":
    for name, info in students.items():
        print(f"\n {name}")
        print(f"   Група: {info['Навчальна група']}")
        print(f"   Предмети: {', '.join(info['Предмети'])}")
        print(f"   Оцінки: {', '.join(map(str, info['Бали за семестр']))}")

elif choice == "2":
    print("Завершення програми.")

elif choice == "3":
    students = sort_students_by_group(students)

elif choice == "4":
    group_to_check = input("Введіть назву групи: ")
    print(calculate_group_average(students, group_to_check))

else:
    print("Введено неіснуюче число.")
