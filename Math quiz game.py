import random
total_win=0
total_question=1
while total_question<=5:
    a=random.randint(1,20)
    b=random.randint(1,20)
    add=a+b
    print (total_question," the sum of",a,"+",b,"?")
    c=input(" enter the sum:").strip()
    if c =="":
        continue
    if c.isdigit():
        c=int(c)
        if add ==c:
            print (" you win👍👍")
            total_win+=1
        else:
            print ("you lose👎👎,sum:",add)
        total_question+=1
    else:
        print(" invalid entry 🚫\n try again")
print ("quiz over\n your total score:",total_win,"/5")
