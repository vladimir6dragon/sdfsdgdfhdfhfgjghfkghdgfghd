import random


points={
    "player": 0,
    "comp":0
}

def add(number:int):
    if number %2==0:
        return True
    else:
        return False

while True:
    a=random.randint(10,120)
    if add(a):
        continue
    b=random.randint(10,110)
    if add(b):
        continue
    ad=random.choice(("+","-"))
    if ad =="+":
        ans=a+b
        user=input(f"{a}+{b}=")
    else:
        ans=a-b
        user=input(f"{a}-{b}=")
    if user==str(ans):
        print("Верно")
        points["player"]+=1
    else:
        print("Попробуй еще раз")
        points["comp"]+=1