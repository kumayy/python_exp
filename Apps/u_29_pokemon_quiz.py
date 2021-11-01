
import random

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choises = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choises:
            raise ValueError("Şıklardaki dillerden birini giriniz.")
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex +1}: {question.text}")

        for q in question.choises:
            print("-" + q )

        answer = input("Cevabınız: ")
        if (question.checkAnswer(answer)):
            self.score +=1
            print(f"********************************\n=^.^= Tebrikler {self.questionIndex + 1}. soruyu bildiniz")

        self.questionIndex +=1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()    

    def displayScore(self):
        print("################################################################################")
        print("  TEST SONUCUNUZ  ".center(80,'#'))
        puan = 100/len(self.questions)
        totalScore = round(self.score * puan)
        print(f"TEBRİKLER!!!... \n{len(self.questions)} sorudan {self.score} tanesin doğru cevapladınız")
        print("Toplam Puanınız: ",totalScore)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1 

        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız.".center(100,'*'))

q1 = Question("En iyi başlangıç pokemonu nedir?",["charmender","bulbasaur","squirtle"],"charmender")
q2 = Question("En janti efsanevi pokemon hangisidir?",["dialga","ho-oh","entei","mewtwo"],"mewtwo")
q3 = Question("En iyi efsanevi olmayan pokemon hangisidir?",["charizard","gengar","pigeot","raichu"],"gengar")

sorular = [q1,q2,q3]

quiz = Quiz(sorular)

quiz.loadQuestion()



#######################################################################
