def grade(score, pass_mark=50):
    if score >= pass_mark:
        return "Pass"
    else:
        return "Fail"

# Using the default pass_mark = 50
print(grade(75))

# Using a custom pass_mark = 30
print(grade(40, 30))

# Boolean operations
print(True and False)
print(True or False)
print(not True)