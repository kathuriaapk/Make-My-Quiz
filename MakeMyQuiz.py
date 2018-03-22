import quizGenerator
import playQuiz

#MAKE MY QUIZ
print("\nApp is designed ito create and play quizes .\n")
sel = True
while(sel is True):
	selection = input("Select the operation you want to perform ?\n \
	(type 1 to create quiz & \ntype 2 to attemp quizes)\n \
	or type 'quit' to exit.\nYour choice :- ")
	if selection == '1':
		quizGenerator.quiz_generator()
		print("Your quiz has been sucessfully created in dir 'myquiz' at current path of this app.")
	elif selection == '2':
		playQuiz.play_quiz()
	else:
		print("Thankyou for using MakeMyQuiz.Closing App.....")
		sel = False