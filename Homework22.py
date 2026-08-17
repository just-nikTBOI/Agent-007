class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}")

    def get_info(self):
        return f"Подія: {self.title}, Дата: {self.date}"


class Training(Event):
    def __init__(self, title, date, trainer):
        super().__init__(title, date)
        self.trainer = trainer

    def show(self):
        print(f"Тренування: {self.title}, Дата: {self.date}, Тренер: {self.trainer}")

    def get_info(self):
        return f"Тренування: {self.title}, Дата: {self.date}, Тренер: {self.trainer}"


class Birthday(Event):
    def __init__(self, title, date, person):
        super().__init__(title, date)
        self.person = person

    def show(self):
        print(f"День народження: {self.title}, Дата: {self.date}, Іменинник: {self.person}")

    def get_info(self):
        return f"День народження: {self.title}, Дата: {self.date}, Іменинник: {self.person}"


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link

    def show(self):
        print(f"Онлайн подія: {self.title}, Дата: {self.date}, Посилання: {self.link}")

    def get_info(self):
        return f"Онлайн подія: {self.title}, Дата: {self.date}, Посилання: {self.link}"


events = [
    Training("Футбол", "2026-08-20", "Олександр"),
    Birthday("Святкування", "2026-09-01", "Іван"),
    Event("Зустріч", "2026-08-25"),
    OnlineEvent("Вебінар Python", "2026-08-30", "https://meet.com/python")
]

print("=== show() ===")
for event in events:
    event.show()

print("\n=== get_info() ===")
for event in events:
    print(event.get_info())