import logging

# Налаштування логування
logging.basicConfig(
    filename='project_manager_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

tasks = []

def add_task():
    name = input("Введіть назву завдання: ")
    if not name.strip():
        logging.warning("Спроба додати завдання без назви")
        print(" Назва завдання не може бути порожньою.")
        return
    tasks.append({'name': name, 'status': 'New'})
    logging.info(f"Додано завдання: {name}")
    print(f" Завдання '{name}' додано.")

def update_status():
    name = input("Введіть назву завдання для оновлення: ")
    status = input("Введіть новий статус (New / In Progress / Done): ")

    for task in tasks:
        if task['name'] == name:
            task['status'] = status
            logging.info(f"Оновлено статус '{name}' на '{status}'")
            print(f" Статус завдання '{name}' оновлено на '{status}'.")
            return

    logging.warning(f"Спроба оновити неіснуюче завдання: {name}")
    print(" Завдання не знайдено.")

def view_tasks():
    if not tasks:
        logging.warning("Спроба переглянути порожній список завдань")
        print(" Немає завдань для перегляду.")
    else:
        print("\n Список завдань:")
        for t in tasks:
            print(f"- {t['name']} ({t['status']})")
        logging.info("Переглянуто список завдань")

def delete_task():
    name = input("Введіть назву завдання для видалення: ")
    global tasks
    if any(t['name'] == name for t in tasks):
        tasks = [t for t in tasks if t['name'] != name]
        logging.info(f"Видалено завдання: {name}")
        print(f" Завдання '{name}' видалено.")
    else:
        logging.warning(f"Спроба видалити неіснуюче завдання: {name}")
        print(" Такого завдання не існує.")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Оновити статус")
        print("3. Переглянути завдання")
        print("4. Видалити завдання")
        print("5. Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_status()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            logging.info("Програма завершена користувачем")
            print(" Вихід із програми.")
            break
        else:
            logging.error(f"Некоректний вибір у меню: {choice}")
            print(" Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
