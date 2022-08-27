# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def showQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}/{len(questions)}: {question.text}")

        for i in question.choices:
            print("-", i)

        answer = input("Cevabınız: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        #       if self.questionIndex == len(questions):   list index out of range sorununu çözmek için
        #           quit()


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.showQuestion()

    def showScore(self):
        print("Your Quiz is over.")
        print("Score:",self.score)


q1 = Question("En iyi programlama dili hangisidir?", ["C#", "Python", "JavaScript", "Java"], "Python")
q2 = Question("En popüler programlama dili hangisidir?", ["Python", "JavaScript", "C#", "Java"], "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["C#", "JavaScript", "Java", "Python"], "Python")
q4 = Question("En çok kolay programlama dili hangisidir?", ["C#", "JavaScript", "Java", "Python"], "Python")
q5 = Question("En çok gereksiz programlama dili hangisidir?", ["C#", "JavaScript", "Java", "Python"], "Python")

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)
question = quiz.getQuestion()
print(question.text)

quiz.showQuestion()
