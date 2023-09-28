class ATBQueue:
    def __init__(self):
        self.queue = []
    def join(self, name):
        self.queue.append(name)
    def obs(self):
        if self.queue:
            print(f"Обслужено: {self.queue.pop(0)}")
        else:
            print("Черга пуста")
    def pokaz(self):
        if self.queue:
            print("Черга:")
            for i, name in enumerate(self.queue, start=1):
                print(f"{i}. {name}")
        else:
            print("Черга пуста")
queue = ATBQueue()
while True:
    print("===___===___===")
    print("Оберіть функцію:")
    print("1. Приєднатися до черги")
    print("2. Обслужити клієнта")
    print("3. Показати чергу")
    print("4. Вийти")
    print("===___===___===")
    choice = input("Введіть номер функції: ")
    if choice == "1":
        name = input("Введіть ім'я клієнта: ")
        queue.join(name)
        print(f"{name} приєднався до черги.")
    elif choice == "2":
        queue.obs()
    elif choice == "3":
        queue.pokaz()
    elif choice == "4":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")