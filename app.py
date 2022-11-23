from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


class Message:
    Id: int
    UserName: str
    Message: str

    def __init__(self, Id, UserName, Message):
        self.Id = Id
        self.UserName = UserName
        self.Message = Message


snowballs = [Message(Id=1, UserName='Danil', Message='Спасибо!'),
             Message(Id=2, UserName='Denis', Message='Спасибо Олегу!'),
             Message(Id=3, UserName='Oleg', Message='Спасибо Олегу из!'),
             Message(Id=4, UserName='Petr', Message='Спасибо Олегу из отдела!'),
             Message(Id=5, UserName='Zenya', Message='Спасибо Олегу из отдела обучения!'),
             Message(Id=6, UserName='Lera', Message='Ю-ху'),
             Message(Id=7, UserName='Petya', Message='Текстик')]


@app.route('/')
def index():
    return render_template("index.html", len=len(snowballs), snowballs=snowballs)


@app.route('/add-congratulation')
def add_congratulation():
    return render_template("add_congratulations.html")


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
