100 DAYS OF PYTHON - DAY 9
#in this lesson, i learned that int() is used when inserting whole numbers, and float() is used when adding decimal numbers.

print("Hello. Answer this quick qestion to find out what generation you are from!.")
print()
birthYear = int(input("What year were you born? "))
if birthYear <= 1946:
  print("You're an oldie")
elif birthYear >= 1947 and birthYear <= 1964:
  print("You're a baby boomer!")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! That's you!")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! You're the tech addicts!")
elif birthYear >= 1996:
  print("Hey, Gen Z! You're the best!")
else: 
  print("Try again!")
