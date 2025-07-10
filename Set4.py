#Q1. Write a program to store seven fruits in a list entered by the user. 
fruit = []
for i in range(1,8):
    j = input(f"enter the name of fruit no.{i} :")
    fruit.append(j)
print(fruit)

#Q2. Write a program to accept marks of 6 students and display them in a sorted 
Marks = []
for i in range(1,8):
    j = input(f"enter the Marks of Student no.{i} :")
    Marks.append(j)
Marks.sort()
print(Marks)

#Q3. Check that a tuple type cannot be changed in python. 
i = (2,)
j = list(i)
print(j) #This result tells that Tuple Type could be changed to other Types

#Q4. Write a program to sum a list with 4 numbers. 
i = [23,23,23,0]
print(sum(i[:]))

#Q5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))