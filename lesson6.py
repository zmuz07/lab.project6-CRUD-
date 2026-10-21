#управления списком задач(CRUD)
tasks = []
def create_task():
    title = input("Введите название: ")
    description = input("Введите описание: ")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "новая"
    }
    tasks.append(task)
    print("Задача добавлена")
def read_tasks():
    if len(tasks) == 0:
        print("Список пуст")
    else:
        for task in tasks:
            print("ID:", task["id"])
            print("Название:", task["title"])
            print("Описание:", task["description"])
            print("Статус:", task["status"])
            print("------------------")
def update_task():
    id = int(input("Введите ID: "))
    for task in tasks:
        if task["id"] == id:
            task["title"] = input("Новое название: ")
            task["description"] = input("Новое описание: ")
            task["status"] = input(
                "Введите статус (новая, в процессе, выполнена): "
            )
            print("Задача изменена!")
            return
    print("Задача не найдена")
def delete_task():
    id = int(input("Введите ID: "))

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            print("Задача удалена!")
            return
    print("Задача не найдена")
while True:
    print("\n1. Создать задачу")
    print("2. Посмотреть задачи")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("0. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "0":
        break
    else:
        print("Неправильный выбор")
