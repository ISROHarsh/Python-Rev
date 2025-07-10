#Q1. Write a program to find the greatest of four numbers entered by the user.
i = int(input("enter 1st number: "))
j = int(input("enter 2nd number: "))
k = int(input("enter 3rd number: "))
l = int(input("enter 4th number: "))
if i > j:
    if i > k:
        if i > l:
            print(f"{i} is the greatest number")
elif j > k:
    if j > l:
        print(f"{j} is the greatest number")
elif k > l:
    print(f"{k} is the greatest number")
else:
    print(f"{l} is the greatest number")

#Q2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
i = int(input("Enter the Marks of Sub1: "))
j = int(input("Enter the Marks of Sub2: "))
k = int(input("Enter the Marks of Sub3: "))
if i >= 33 and j >= 33 and k>= 33 and (i + j + k)/3 >= 40:
    print("The Student passed!")
else:
    print("The Student failed!")

#Q3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
i = input("Enter the statement: ")
flaw = ["make a lot of money", "buy now", "subscribe this", "click this"]
for x in flaw:
    if x in i:
        print("It's a Scam")

#Q4. Write a program to find whether a given username contains less than 10 characters or not.
i = input("enter username: ")
if len(i) < 10:
    print("username is less than 10 char")
elif len(i) == 10:
    print("username is 10 char")
else:
    print("username is more than 10 char")
#Q5. Write a program which finds out whether a given name is present in a list or not.
i = input("Enter the Name: ")
naam = ["Saksham", "Harsh", "Nishant", "Neil"]
for n in naam:
    if n in i:
        print("The name is present")
else:  
    print("The name is not present")

#Q6. Write a program to calculate the grade of a student from his marks from the
#following scheme:
#90 – 100 => Ex
#80 – 90 => A
#70 – 80 => B
#60 – 70 =>C
#50 – 60 => D
#<50 => F
mark = []
for n in range(50,101):
    mark.append(n)
i = int(input("Enter the Marks: "))
mark.reverse()
if i in mark[0:9]:
    print("Student is graded Excellent")
elif i in mark[10:19]:
    print("Student is graded A")
elif i in mark[20:29]:
    print("Student is graded B")
elif i in mark[30:39]:
    print("Student is graded C")
elif i in mark[40:49]:
    print("Student is graded D")
else:
    print("Student is graded F")


#Q7. Write a program to find out whether a given post is talking about “Harry” or not.
i = input("Enter the post:")
if "harry" in i.lower():
    print("The post is talking about Harry")
else:
    print("The post is not talking about Harry")