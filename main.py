# we imported a package called random which enables the user type any number and still get it wrong basically. 

# range returns a series of values within a sequence in this case.

# I removed the "print" statement and replaced it with a "return" just to simplify it and then asked the def ask_user_check_number to print the answer to the user. 


import random

magic_numbers = [random.randint(0,9),random.randint(0,9)]

def ask_user_check_number():
  user_number = int(input("Enter a number between 0 and 9: "))
  if user_number in magic_numbers:
    return "yes baby"
  if user_number not in magic_numbers:
    return "sadly your wrong"


def run_program_x_times(chances):
  for attempt in range(chances): # range(chances) is [0,1,2]
    print("this is attempt {}". format(attempt))
    print(ask_user_check_number())

# doing this calls the method: I added "(user_decides)" in order for the user to decide how many chances they want. I placed in defining statement and deleted the variable "chances"

user_decides = int(input("how many attempts do you want: "))
run_program_x_times(user_decides)

  
