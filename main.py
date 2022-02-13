print("Welcome To My Quiz Game")

playing=input("Do you really want to play this game (yes/no)?\n")
playing=playing.lower()


if playing!="yes":
    print("Ok Bye")
    quit()

print("Ok then let's continue with quiz \n")
print("Rules \n1)For each right answers you will be awarded 2 points\n2)For each wrong answers you will get -1 point. \n")
your_score=0

ques=input("121 Divided by 11 is : ")
if ques=="11":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("60 Times of 8 Equals to : ")
if ques=="480":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("What is the Next Prime Number after 7 ? ")
if ques=="11":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("The Product of 131 × 0 × 300 × 4 : ")
if ques=="0":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("Solve 3 + 6 × ( 5 + 4) ÷ 3 - 7  ")
if ques=="14":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("How Many Years are there in a Decade? ")
if ques=="10":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("How Many Months Make a Century? ")
if ques=="1200":
    print("Correct!\n")
    your_score+=2
else:
    print("Incorrect!\n")  
    your_score-=1  

ques=input("How Many Months Have 120 Days? ")
if ques=="4":
    print("Correct!\n")
    your_score+=2
else:
    print("Correct!\n")  
    your_score-=1  

print("Your Score is",your_score,"\n")
if your_score==16:
    print("Excellent Work!")
elif your_score>4 and your_score<16:
    print("Good Work!")    
else:
    print("You need to work on your maths :)")    