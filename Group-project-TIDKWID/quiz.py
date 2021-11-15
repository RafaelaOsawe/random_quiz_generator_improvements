import tabulate
import requests
import html

total_percentage = 100
user_pass = []
access_granted = False


def users(username, password):
    file = open("password_list.csv", "r")
    data = file.readlines()
    file.close()
    for line in data:
        line = line.strip()
        line = line.split(",")
        user_pass.append(line)
    for i in user_pass:
        if username == i[0] and password == i[1]:
            access_granted = True
            return access_granted


def answer(test_choice):
    score = 0
    percentage = 100
    for x in range(10):
        print(html.unescape(trivia_questions[x]["question"]))
        print("")
        if test_choice == "A":
            print(trivia_questions[x]["incorrect_answers"][0])
            print(trivia_questions[x]["incorrect_answers"][1])
            print(trivia_questions[x]["correct_answer"])
            print(trivia_questions[x]["incorrect_answers"][2])
        else:
            pass
        print("")
        guess = input("Answer: ").upper()
        if guess == trivia_questions[x]["correct_answer"].upper():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
            print(
                f'correct answer is {trivia_questions[x] ["correct_answer"]}\n'
            )
            percentage -= 10
    return score, percentage


def answer_type():
    score = 0
    percentage = 100
    for x in range(10):
        print(questions[x][:-1])
        guess = input("Answer: ").upper()
        if guess == answers[x][:-1]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
            percentage -= 10
    return score, percentage


def scores(username, score, percentage):
    file = open("scores.csv", "a")
    final = f'{username},{score}/10,{percentage}%\n'
    file.write(final)
    file.close()


def leaderboard():
    file = open("scores.csv", "r")
    data = []
    score = file.readlines()
    for lines in score:
        lines = lines.strip()
        lines = lines.split(",")
        data.append(lines)

    data = sorted(data, key=lambda x: x[1], reverse=True)
    headers = ("Name", "Score", "Percentage")
    scores = tabulate.tabulate(data, headers=headers)
    print("-- Top Scores --")
    print(scores)


def type_q():
  abcd = True
  while abcd == True:
    print("What type of quiz you want to do?\n A. Multiple choice")
    print(" B. True/False\n C. Type in\n D. Any")
    test_choice = input("").upper()
    if test_choice == "A":
        print("You have chosen the multiple choice quiz\n")
        response = requests.get(
            "https://opentdb.com/api.php?amount=10&type=multiple")
        trivia_questions = response.json()["results"]
        abcd = False
        return trivia_questions, test_choice
    elif test_choice == "B":
        response = requests.get(
            "https://opentdb.com/api.php?amount=10&type=boolean")
        trivia_questions = response.json()["results"]
        print("You have chosen the True/False quiz\n")
        abcd = False
        return trivia_questions, test_choice
    elif test_choice == "C":
        print("You have chosen the type in quiz\n")
        trivia_questions = answer_type()
        abcd = False
        return trivia_questions, test_choice
    elif test_choice == "D":
        print("You have chosen the any choice quiz\n")
        response = requests.get("https://opentdb.com/api.php?amount=10")
        trivia_questions = response.json()["results"]
        abcd = False
        return trivia_questions, test_choice
    else:
      print("Must input A,B,C,D")
      abcd = True
      


file = open("questions.csv", "r")
questions = file.readlines()
file.close()
file = open("answers.csv", "r")
answers = file.readlines()
file.close()

print("              -----------------------------")
print("              -----Welcome to the quiz-----")
print("              -----------------------------")
print("")

while access_granted is False:
    username = input("Username:  ")
    password = input("password:  ")
    print("")
    access_granted = users(username, password)
    if access_granted is True:
        print("Access Granted")
        break
    else:
        access_granted = False
        print("Access Denied")
print("")
trivia_questions, test_choice = type_q()
if test_choice == "C":
    score, percentage = answer_type()
else:
    score, percentage = answer(test_choice)
scores(username, score, percentage)
leaderboard()
