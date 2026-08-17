class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def get_info(self):
        return f"Назва: {self.title} | Дата: {self.date}"


events = []

while True:
    print("\n--- Планувальник подій ---")
    print("1. Додати подію")
    print("2. Показати всі події")
    print("3. Видалити подію")
    print("4. Вийти")

    choice = input("Оберіть пункт: ")

    if choice == "1":
        title = input("Введіть назву події: ")
        date = input("Введіть дату: ")

        event = Event(title, date)
        events.append(event)

        print("Подію додано!")

    elif choice == "2":
        if len(events) == 0:
            print("Подій немає.")
        else:
            print("\nСписок подій:")
            for i, event in enumerate(events, start=1):
                print(f"{i}. {event.get_info()}")

    elif choice == "3":
        if len(events) == 0:
            print("Немає подій для видалення.")
        else:
            for i, event in enumerate(events, start=1):
                print(f"{i}. {event.get_info()}")

            index = int(input("Введіть номер події для видалення: ")) - 1

            if 0 <= index < len(events):
                deleted = events.pop(index)
                print(f"Подію '{deleted.title}' видалено.")
            else:
                print("Невірний номер.")

    elif choice == "4":
        print("До побачення!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
