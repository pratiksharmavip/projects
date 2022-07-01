# #string concatination (put string together)
# #suppose we want to create a string that says "subscribe to ______"
# youtuber = " abc " #some string variable

# # A few ways to create a concatinated string
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

from re import I


adj = input("adjective:")
verb1=input("verb: ")
verb2= input("verb: ")
fam=input("fam: ")
madlib = f"computer programmig is so {adj}! it makes me so excited all the time beacuse\
    i love to {verb1}. stay hydrated and {verb2} like you are {fam}!"
print(madlib)