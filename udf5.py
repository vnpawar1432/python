def result(name,math,sci,mar,eng,hindi,his,sc):
    total_marks = math+sci+hindi+mar+eng+his+sc
    percentage = total_marks/7
    print(f"{name} your marks is {total_marks} and your percentage is {percentage}")

result("vaibhav",90,63,91,80,83,63,63)