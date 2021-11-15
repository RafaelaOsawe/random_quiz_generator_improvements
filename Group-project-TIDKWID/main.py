from quiz import *
from guizero import App, Text, PushButton


def answer_button(on_click):
    print(on_click)


def total_button(scores):
    total_score.value = "Your total score is: " + scores


def last_score():
    file = open("scores.csv", "r")
    data = file.readlines()
    latest_score = data[-1]
    values = latest_score.split(",")
    values = latest_score.strip()
    file.close()
    return values


app = App(title="Quiz Challenge", width=500, height=300)

total_score = Text(app, text="....waiting for your score")

user_score = PushButton(app,
                        text="Display score",
                        command=total_button,
                        args=[str(last_score())])

questions = Text(app, text="Did you enjoy the quiz?")
button1 = PushButton(app,
                     text="YES",
                     command=answer_button,
                     args=["Cool! Hope to see you soon!"])

button2 = PushButton(app,
                     text="NO",
                     command=answer_button,
                     args=["Oh well... maybe next time!"])
app.display()
