import random
words=["ананас",
       "стол",
       "город",
       "репозиторий",
       "плед",
       "одеяла",
       "скатерть",
       "покрывало",
       "покрывало",
       "пол"]

while True:
    a=random.choice(words)
    b=random.choice(words)
    ab =a+b
    user=input(f"{a}+{b}=")
    if user==ab:
        print("ты молодец")
    else:
        print("иди учись неуч!!!!")