# Python Quiz Game

questions = ("What is My Full name?: ", "What is My Age?: ", "Where Am I From?: ")

options = (("A. Abah O. Lucky ", "B. OChe J. Lucky", "C. Lucky Johns", "D. Abah Q. Lucky"),
           ("A. 26", "B. 23", "C. 24", "D. 25"),
           ("A. Zaria", "B. Benue", "C. Gombe", "D. Kano"))
answers =("A", "D", "B")
guesses = []
score = 0
ques_num =0

for question in questions:
    print("*****************************")
    print(question)
    for option in options[ques_num]:
        print(option)
        
    guess = input("Enter an Options(A,B,C,D): ").upper()
    
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[ques_num]} is the correct Answer ")
    
    ques_num +=1
    
print ("*********************")
print ("RESULTS")
print ("*********************")
    
print("answers: ", end="")    
for answer in answers:
    print(answer, end=" ")    
print()
print("guesses: ", end="")    
for guess in answers:
    print(guess, end=" ")    
print()
