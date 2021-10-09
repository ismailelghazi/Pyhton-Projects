import random
guesse = random.randint(1, 100)
logo="""" /$$$$$$$$                                   /$$$$$$                                      /$$     /$$       /$$                          
|__  $$__/                                  /$$__  $$                                    | $$    | $$      |__/                          
   | $$ /$$   /$$  /$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$  | $$$$$$$  /$$ /$$$$$$$   /$$$$$$       
   | $$| $$  | $$ /$$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$| $$_  $$_  $$ /$$__  $$|_  $$_/  | $$__  $$| $$| $$__  $$ /$$__  $$      
   | $$| $$  | $$| $$  \ $$| $$$$$$$$       \____  $$| $$  \ $$| $$ \ $$ \ $$| $$$$$$$$  | $$    | $$  \ $$| $$| $$  \ $$| $$  \ $$      
   | $$| $$  | $$| $$  | $$| $$_____/       /$$  \ $$| $$  | $$| $$ | $$ | $$| $$_____/  | $$ /$$| $$  | $$| $$| $$  | $$| $$  | $$      
   | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$  |  $$$$/| $$  | $$| $$| $$  | $$|  $$$$$$$      
   |__/ \____  $$| $$____/  \_______/       \______/  \______/ |__/ |__/ |__/ \_______/   \___/  |__/  |__/|__/|__/  |__/ \____  $$      
        /$$  | $$| $$                                                                                                     /$$  \ $$      
       |  $$$$$$/| $$                                                                                                    |  $$$$$$/      
        \______/ |__/                                                                                                     \______/        """
print(logo)
print("the number is between 1 and 100")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
def easy():
 cort = 10
 while cort:
     the_number=int(input("give me you the number "))
     if guesse == the_number:
      print("win")
      cort=0
     elif guesse<the_number:
      print("low")
      cort-=1
     elif guesse > the_number:
      print("high")
      cort-=1
     else:
      print(f"the number is {guesse}")
def hard():
 cort=5
 while  cort:
     the_number=int(input("give me you the number "))
     if guesse == the_number:
      print("win")
      cort=0
     elif guesse<the_number:
      cort-=1
      print("low")
     elif guesse > the_number:
      cort-=1
      print("high")
if choose_difficulty=='hard':
 hard()
else:
 easy()
print(f"the number is {guesse}")
