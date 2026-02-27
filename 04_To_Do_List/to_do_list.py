tasks = []
while True:
      print("What do u want to do?")
      print("1. Add a task")
      print("2. View tasks")
      print("3. Remove tasks")
      print("4. Exit") 

      options = input('Enter your choice: (1, 2, 3, or 4) ')

      if options == '1':
          task = input("Enter the task you want to add: ")
          tasks.append(task)
          print("Task added successfully!")

      elif options == '2':
          if not tasks:
              print("No tasks to show.")
          else:
              print("Your tasks:")
              for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

      elif options == '3':
          if not tasks:
              print("No tasks to remove.")
          else:
              print("Which task do you want to remove?, pick the number")
              for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
              task_number = int(input("Enter the task number to remove: "))
              tasks.pop(task_number - 1)
              print("Task removed successfully!")

      elif options == '4':
        print("Goodbye!")
        break
      else:
        print("Invalid choice, please try again.")