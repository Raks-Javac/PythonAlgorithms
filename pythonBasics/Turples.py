# Lesson 5
# Working with Turples
# Note: Turples are unique  data holding props
# and you cant use turples for data u would like to change 
# an example of a best apllication of turple is coordinates =(x,y)
#that help you to store immutable data ,they cant be changed or modified


question1 = ("question1(index0)",True)
print(question1)
# Note:You can access them with the angular bracket
print(question1[1])
# they can also be stored in alist
question_Bank = [("question1(index0)",True),("question2(index1)",False),("question3(index2)",False) ]
print(question_Bank)

# tracking with index
print(question_Bank[1][1])