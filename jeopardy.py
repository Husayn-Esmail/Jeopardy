
class Question:
    def __init__(self,QuestionID, CatID, QuestionTxt, AnswerTxt, PointVal):
        self.QuestionID= QuestionID
        self.CatID= CatID
        self.QuestionTxt=QuestionTxt
        self.AnswerTxt=AnswerTxt
        self.PointVal=PointVal
        print("question is:" + self.QuestionTxt)



class Category:
    def __init__(self, category):
        self.category=category

