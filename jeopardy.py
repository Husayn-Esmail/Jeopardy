#!/usr/bin/python
import cgi
from http import cookies

form = cgi.FieldStorage()

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='/Jeopardy/styles.css'>")
print("</head>")
print("<body>")
print("<div class=center>")
#This is the Jeopardy font. It's an image, if you ever have to change it, go to this website to use the same font https://fontmeme.com/jeopardy-font/-->
print("<img src=https://fontmeme.com/permalink/200220/6b98c047956a0573caad64c61c62769d.png alt=jeopardy-font border=0 id=jeop>")
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
    def __str__(self):
       return '{} {}'.format(self.category, self.Questions)
       
class Game:
    def __init__(self):
        self.Categories = []
    def __str__(self):
        return '{}'.format(self.Categories)
#creating game
Jeopardy=Game()

#Python index starts at 0!
#Opens and reads the file Book1.csv creates a list out split by commas and then creates an object q1 and prints various indexes
oldcat = ""
nbrCat = -1
maxcol = 5
maxrow = 5
irow = 1
icol = 1
firstline = True

# load objects with data from csv file
with open("Book1.txt", "r") as filestream:
        questionsDict = {}
        for line in filestream:
            if firstline:
                firstline = False
            else:
                # Note that IF THE CSV CONTAINS COMMAS ANYWHERE IN THE FILE IT WILL BREAK THE PROGRAM
                currentline=line.split('\t')
                print(line + "<br>")
                # currentQuestion=[currentLine[1],currentLine[2],currentLine[3],currentLine[4].rstrip()]
                # questionsDict.update({currentLine[0] : currentQuestion })
                # print(questionsDict)
                #cat is the category name taken from the csv
                cat = currentline[0]
                if cat != oldcat:
                    #connects game(property:categories) appending to list categories using Category object constructor
                    Jeopardy.Categories.append(Category(cat))
                    oldcat = cat
                    nbrCat = nbrCat + 1
                
                qid = currentline[1]
                qtxt = currentline[2]
                atxt = currentline[3]
                pval = currentline[4]

                Jeopardy.Categories[nbrCat].Questions.append(Question(qid,qtxt,atxt,pval))
filestream.close()
#clicked=open("Game_status.txt", "w+")
#clicked.close()
print ("<form action=# method='post'>")

print("<div class='center'>")
print ("<table>")            

#adds a table row and prints a header per each category
print("<tr>")
for c in Jeopardy.Categories:
    print("<th>")
    print(c.category)
    print("</th>")
print("</tr>")
        
print ("</table>")
print("</div>")


btn = form.getvalue("btn")
print(btn)
if btn != None:
    yx = btn.split(",")
    col = int(yx[0])
    row = int(yx[1])
    qa = yx[2]
    if qa == "Q":
        print ("<div class='questions'><h1><button value='%s,%s,A' name='btn'>%s</button></h1></div>" % (row,col,Jeopardy.Categories[col].Questions[row].QuestionTxt))
        print("<div> %s,%s </div>" % (row,col))
    else:
        print ("<div class='questions'><h1><button value='%s,%s' name='return'>%s</button></h1></div>" % (row,col,Jeopardy.Categories[col].Questions[row].AnswerTxt))
        print("<div> %s,%s </div>" % (row,col))
print ("</form>")

print("</body>")
print("</html>")