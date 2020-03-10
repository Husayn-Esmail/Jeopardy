
class Question:
    def __init__(self,QuestionID,QuestionTxt,AnswerTxt,PointVal):
        self.QuestionID=QuestionID
        self.QuestionTxt= QuestionTxt
        self.AnswerTxt= AnswerTxt
        self.PointVal= PointVal
    def __str__(self):
      return '{} {} {} {}'.format(self.QuestionID, self.QuestionTxt, self.AnswerTxt, self.PointVal)

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
        q1=Question(currentline[1], currentline[2], currentline[3], currentline[4])
        print(q1)


#Jeopardy=
