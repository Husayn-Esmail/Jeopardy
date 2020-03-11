#!/usr/bin/python
import cgi
form = cgi.FieldStorage()

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='/Jeopardy/styles.css'>")
print("</head>")
print("<body>")
print("<div class=center>")
#This is the Jeopardy font. It's an image, if you ever have to change it, go to this website to use the same font https://fontmeme.com/jeopardy-font/-->
#print("<a href=https://fontmeme.com/jeopardy-font/>")
print("<img src=https://fontmeme.com/permalink/200220/6b98c047956a0573caad64c61c62769d.png alt=jeopardy-font border=0 id=jeop>")
#print("</a>")
print("</div>")
#test
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
Jeopardy.Categories.index("Sports")
#Python index starts at 0!
#Opens and reads the file Book1.csv creates a list out split by commas and then creates an object q1 and prints various indexes
oldcat = ""
nbrCat = -1
maxcol = 5
maxrow = 5
irow = 1
icol = 1
firstline = True

print ("<form action=# method='post'>")
print ("<table>")

with open("Book1.csv", "r") as filestream:
    questionsDict = {}
    for line in filestream:
        if firstline:
            firstline = False
        else:
            currentline=line.split(",")
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

            #for x in range(len(Jeopardy.Categories)):
            #    for y in range(len(Jeopardy.Categories[x].Questions)):
            #        print(Jeopardy.Categories[x].Questions[y])
            
                
            #print(str(Jeopardy.Categories[0].Questions))
            

#adds a table row and prints a header per each category
print("<tr>")
for c in Jeopardy.Categories:
    print("<th>")
    print(c.category)
    print("</th>")
print("</tr>")


#if cat != oldcat:
#    ind=-1
#    for x in Jeopardy.Categories:        
#        ind += 1
#        print("<button class=but>")
#        print(cat.Questions[ind])

#CHANGE TO QUESTIONS and increment
for row in range(len(Jeopardy.Categories[0].Questions)):
    print("<tr>")
    for c in Jeopardy.Categories:
        if len(c.Questions)>row:
            print("<td><button class='but' value='%s' name='btn'>%s</button></td>" % (c.Questions[row].QuestionID, c.Questions[row].PointVal)) 
        else:
            print("<td></td>")
    print("</tr>")
    

print ("</table>")
print ("</form>")

print ("<div>Button pressed: %s</div>" % form.getvalue("btn"))

print("</body>")
print("</html>")

