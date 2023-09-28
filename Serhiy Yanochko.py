while True:
 test = print("Код #1. Написати програму, яка передбачає введення в стек цілих чисел з клавіатури. Вивести стек на екран.")
 test2 = print("Код #2. Створити і роздрукувати два стеки -- з парними та непарними числами через введених.")
 choice = input("Виберіть код (1 або 2 або q для виходу.): ")

 if choice == "1":
  mystack = []

  add = int(input("Кількість: "))

  for i in range(add):
      num =int(input("Цифри: "))
      mystack.append(num)

  print("Cтек:")
  while mystack:
      num = mystack.pop()
      print(num)
   
     
 elif choice == "2":
     mystack = []

     add = int(input("Кількість: "))

     def test(numbers):
        db_stack = []
        ndb_stack = []

        for num in numbers: 
         if num % 2 == 0:
            db_stack.append(num)
         else:
            ndb_stack.append(num)
        
        return db_stack, ndb_stack

     for i in range(add):
        num =int(input("Цифри: "))
        mystack.append(num)
     def print_stack(імя_стеку, стек):
        print(f"{імя_стеку} Стек: {стек}") 

     db, ndb = test(mystack)

     print_stack("Парні", db) 
     print_stack("Непарні", ndb) 
 elif choice.lower() == 'q':
     break