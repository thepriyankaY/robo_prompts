#i learened that if the else statement is in the wrong place, it wont work and that tomi is better

print ("Are you a superfan of 'Jessie' or a fake fan? ")
print()
print("Answer these questions to find out.")

Pet = input("do they have a pet ")
if Pet == "yes":
  print("Correct!")
  
  WhatPet = input("And what is the pet?")
  if WhatPet == "Lizard":
    print("good job")
  else:
    print("NOPE, you suck, you are a fake fan")
    
else:
  print("Wrong! you suck, you are a fake fan")
