import datetime as date_timer
import time as ti
# vm =date_timer.date.today()
# print(vm)
def greetings():
    name = input("Hello what is your name ? \n")
    greetings_text = lambda mode: print(f'Hi ! {name} ,{mode}')  
    tm = int(ti.localtime().tm_hour)
    converted_tm = int(tm) 
    if converted_tm <=12:
        greetings_text("Good morning ! have a wonderful Day.")
    elif converted_tm >=12 and tm<=17:
        greetings_text('Good Afternooon ! How is your day going?')
    elif converted_tm>= 17 and converted_tm <= 18:
        greetings_text('Good evening ! Wow you made it this far today.\n Hope you are doing fine?')
    else:
        greetings_text('Good night ! Had a wonderful time ?,\n Sleep tight')  
greetings()


