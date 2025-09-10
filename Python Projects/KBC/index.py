questions = [
    [
    "Which language was used to create fb?",
    "Python", "Java", "French", "Javascript", "Php", "None", 1],
    [
    "Which language was used to create fb?",
    "Python", "Java", "French", "Javascript", "Php", "None", 2],
    [
    "Which language was used to create fb?",
    "Python", "Java", "French", "Javascript", "Php", "None", 3],    
    [
    "Which language was used to create fb?",
    "Python", "Java", "French", "Javascript", "Php", "None", 3],    
    [
    "Which language was used to create fb?",
    "Python", "Java", "French", "Javascript", "Php", "None", 3],    
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 25000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}   b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quet : "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have a won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
    else:
        print("Wrong Answer")
        break
print(f"You take of money home {money}")