import random
import string
import sys
import time
upper_case=string.ascii_uppercase
lower_case=string.ascii_lowercase
numbers=string.digits
puntuations=string.punctuation
attempt=0
max_attempts=3
while attempt<max_attempts:
  user_password=input("enter the password:")
  has_upper=any(char.isupper() for char in user_password),
  has_lower=any(char.islower() for char in user_password),
  has_numbers=any(char.isdigit() for char in user_password),
  has_punctuation=any(char in string.punctuation for char in user_password)
  if has_upper and has_lower and has_numbers and has_punctuation:
    print("Password generated Sucessfully!")
    sys.exit()
  else:
   attempt+=1
   print(f"WEAK Password")
  if attempt < max_attempts:
    print("Please try again...\n")
    time.sleep(1)

print("Too many attempts suggesting a password")
password=[
    random.choice(upper_case),
    random.choice(lower_case),
    random.choice(numbers),
    random.choice(puntuations)
    ]
all_char=upper_case+lower_case+numbers+puntuations
password+=random.choices(all_char,k=4)
random.shuffle(password)
print("SUGGESTED PASSWORD⬇️")
print(''.join(password))
sys.exit()


"""elif (user_password!=has_upper) or (user_password!=has_lower) or (user_password!=has_numbers) or (user_password!=has_punctuation):
    print("Password should contain any one upper and lower_case and #$%^@ or 1245")
    print("Retry!")"""

