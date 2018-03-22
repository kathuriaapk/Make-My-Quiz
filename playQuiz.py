import os
def start_quiz(q_data):
	count = 0
	print("\n## QUIZ ##\n")
	for n in range(len(q_data)):
		print("Q%d. %s\nYour Options are : -"%(n+1,q_data[n]['question']))
		for index,opt in enumerate(q_data[n]['options']):
			print("%d. %s"%(index+1,opt))
		ans = eval(input("Select the Ans Number : "))
		if  ans is q_data[n]['answer']:
			count += 1
	print("You scored %d out of %d questions."%(count,len(q_data)))

def play_quiz():	
	#DISPLAY QUIZ LIST
	quiz_files = os.listdir("myquiz")
	print("Select the quiz you want to attempt.")
	for index,quiz in enumerate(quiz_files):
		print("%d. %s"%(index+1,quiz))

	#STUDENTS DATA AS INPUT
	current_quiz = eval(input("Selec the quiz number ( Ex- 1,2,3... ) :: "))
	stu_name = input("Enter your name :-")
	while stu_name == '':
		print("Your havn't entered your name.")
		stu_name = input("Enter your name :- ")
	with open("myquiz/" + quiz_files[current_quiz-1]) as file:
		data = file.read()
		quiz_data = eval(data)
	#Start Quiz
	start_quiz(quiz_data)




