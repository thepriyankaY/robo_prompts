# we all, including Mr.P, Ms.Terkper and me, collectivly struggled to get my code working, so we found that the 3 quotations in the begining and end of line 8 made it believe it was one big chunk and not like their were variables to input

print("""welcome to the beginning of a wonderful expeirence. Before we begin, I would just like you to answer a few questions""")
print()
name = input("what is your name?: ")
superpowerofchoice = input("what superpower would you like?: ")
archnemesis = input("who is your archnemesis in the story?: " )
island = input("what island would you be trying to escape?: ")
print()
print("Hello " + name + "! Your ability to " + superpowerofchoice + " has aided you in defeating " + archnemesis + ". You have now escaped " + island + " and are now on your way to safety. Good luck!")
