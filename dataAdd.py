def quiz_data_add(q_total,o_total):
	quiz_paper = []
	print("Kindly Add your Questions : ")
	for ques in range(0,q_total):
		ques_obj = {"question":'',"options":[]}
		ques_obj['question'] = input("Enter the %d question : "%(ques+1))
		for opt in range(0,o_total):
			ques_obj["options"].append(input("Option %d : " %(opt+1)))
		print("Your options are : -")
		for index,opt in enumerate(ques_obj["options"]):
			print("%d. %s"%(index+1,opt))
		ques_obj["answer"] = eval(input("Answer Number out of these options : "))
		quiz_paper.append(ques_obj)
	return quiz_paper