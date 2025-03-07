#i learned that elifs statement need to be in the right order to get the right result. 
#you can not put the consequence before the action that you would have to do to actually get the consequence.

print("Secure Login")
username = input("What is your username?")
password = input("What is your password?")

if username == "bob" and password == "bob's world":
  print("Welcome, Bob! You are looking nice today!")
elif username == "bartholemew" and password == "yep":
  print("Hi Bartholemew! Love your hair today!")
elif username == "Bill" and password == "Good!":
  print("Yo! Bill! What up?!")
else:
  print("You do not have access. Go away!")
