#!/usr/bin/python
print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='/Jeopardy/styles.css'>")
print("</head>")
print("<body>")
print("<div class = "center" >")
#This is the Jeopardy font. It's an image, if you ever have to change it, go to this website to use the same font https://fontmeme.com/jeopardy-font/-->
print("<a href="https://fontmeme.com/jeopardy-font/">")
print("<img src="https://fontmeme.com/permalink/200220/6b98c047956a0573caad64c61c62769d.png" alt="jeopardy-font" border="0" id="jeop">")
print("</a>")
print("</div>")

#defining a class and creating constructors
class Question:
    def __init__(self,QuestionID,QuestionTxt,AnswerTxt,PointVal):
        self.QuestionID=QuestionID
        self.QuestionTxt= QuestionTxt
        self.AnswerTxt= AnswerTxt
        self.PointVal= PointVal
        #converts values to string
    def __str__(self):
      return '{} {} {} {}'.format(self.QuestionID, self.QuestionTxt, self.AnswerTxt, self.PointVal)

class Category:
    def __init__(self, category):
        self.category=category
        self.Questions=[]
    #def __str__(self):
    #   return '{} {}'.format(self.category, self.Questions)

class Game:
    def __init__(self):
        self.Categories = []
#creating game
Jeopardy=Game()

#Python index starts at 0!
#Opens and reads the file Book1.csv creates a list out split by commas and then creates an object q1 and prints various indexes
oldcat = ""
nbrCat = -2

print ("<table>")

with open("Book1.csv", "r") as filestream:
    for line in filestream:
        if nbrCat == -2:
            nbrCat += 1
        else:
            currentline= line.split(",")
            cat = currentline[0]
            if cat != oldcat:
                Jeopardy.Categories.append(Category(cat))
                oldcat = cat
                nbrCat = nbrCat + 1
            qid = currentline[1]
            qtxt = currentline[2]
            atxt = currentline[3]
            pval = currentline[4]

            Jeopardy.Categories[nbrCat].Questions.append(Question(qid,qtxt,atxt,pval))
#adds a table row and prints a header per each category
print("<tr>")
for c in Jeopardy.Categories:
    print("<th>")
    print(c.category)
    print("</th>")
print("</tr>")
#CHANGE TO QUESTIONS and increment
print("<tr>")
for c in Jeopardy.Categories:
    print("<th>")
    print(c.category)
    print("</th>")
print("</tr>")

print ("</table>")

print("</body>")
print("</html>")
#Jeopardy=
