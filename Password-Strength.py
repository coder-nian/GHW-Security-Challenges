def password_strength(password):
  strength = 0

  #Checks password length
  if len(password) >= 8:
    strength += 1

  #Checks if password contains any uppercase and lowercase characters
  if any(char.isupper() for char in password) and any(char.islower() for char in password):
    strength += 1

  #Check if password any contains digits
  if any(char.isdigit() for char in password):
    strength += 1

  #Check if password contains any special characters
  if any(char in "!@#$%^&*()-_+=[]{};':\",.<>/?`~" for char in password):
    strength += 1

  score_evaluation(strength)
  return strength


def score_evaluation(score):
  if score == 0:
    print("Weak password")
  elif score == 1:
    print("Moderate password")
  elif score == 2:
    print("Strong password")
  elif score == 3:
    print("Very strong password")
  elif score == 4:
    print("Extremely strong password")


#Taking user input
user_password = input("Enter a password: ")
evaluation = password_strength(user_password)
print(f"Your Score was {evaluation + 1} out of 5.")
