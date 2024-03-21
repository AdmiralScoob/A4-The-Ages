import datetime

fName = input("Enter your first name: ")  # input first name
lName = input("Enter your last name: ")  # input last name
birthdate_str = input(
    "Enter your date of birth: ")  # input date of birth MM/DD/YYYY format only

birthdate = datetime.datetime.strptime(
    birthdate_str, "%m/%d/%Y").date()  # converts birthdate_str to a date

today = datetime.date.today()  # gets today's date
age = today.year - birthdate.year - (
    (today.month, today.day) < (birthdate.month, birthdate.day)
)  # gets your age
newAge = age + 1
name = f"{fName} {lName}"  # your name

if (birthdate.month < today.month):  # if your birthday has passed
  print(f"Hello {name}. You are {age} years old.")
elif (birthdate.month > today.month):  # if your birthday is upcoming
  print(f"Hello {name}, You will be {newAge} years old.")
elif (birthdate.month == today.month):  # if you birthday is this month
  if (birthdate.day == today.day):  # if your birthday is today
    print(f"Happy birthday {name}! You are {age} years old.")
  elif (birthdate.day > today.day):  # if your birthday is upcoming this month
    print(f"It's your birthday soon {name}, You will be {newAge} years old.")
  else:  # if you birthday has passed this month
    print(f"Happy belated birthday {name}, You are {age} years old.")
