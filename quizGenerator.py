import dataAdd

#QUIZ GENERATOR
def quiz_generator():
	quiz_name = input("Enter the Quiz Name :- ")
	total_ques = eval(input("Total Number of Questions in a quiz :- "))
	total_opt = eval(input("Number of Options for each Question :- "))
	time_alloted = eval(input("Time Alloted for Quiz (in minutes):- "))

	#CALL A GENERATOR FUNCTION quiz_data_add
	quiz_data = dataAdd.quiz_data_add(total_ques,total_opt)
	print(quiz_data)

	#WRITE DATA TO A FILE
	f = open("myquiz/" +quiz_name + ".txt", 'a+')
	f.write(str(quiz_data))
	f.close()

