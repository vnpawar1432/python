'''
we can give default value to the arguments in function like name = "vaibhav"
but always rember default value argumnet write after the non default arguments
'''



def result(math,sci,mar,eng,hindi,his,sc,name = "vaibhav"):
    total_marks = math+sci+hindi+mar+eng+his+sc
    percentage = total_marks/7
    print(f"{name} your marks is {total_marks} and your percentage is {percentage}")

result(90,63,91,80,83,63,63)