
class Question:
    def __init__(self,QuestionID, QuestionTxt, AnswerTxt, PointVal):
        self.QuestionID= QuestionID
        self.QuestionTxt=QuestionTxt
        self.AnswerTxt=AnswerTxt
        self.PointVal=PointVal
    def prnt_all(self):
        print(self.QuestionID)
        print(self.QuestionTxt)
        print(self.AnswerTxt)
        print(self.PointVal)



class Category:
    def __init__(self, category):
        self.category=category
        self.Questions=[]

class Game:
    def __init__(self):
        self.Categories=[]

Jeopardy=Game()

with open("Book1.csv", "r") as filestream:
    for line in filestream:
        currentline= line.split(",")
        q1=Question(Category, QuestionID, Question, Answer, Points)


#Jeopardy=
