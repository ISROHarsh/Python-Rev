#1. Write a program to print multiplication table of a given number using for loop.
i = int(input("Enter the number: "))
for n in range(1,11):
    print(f"{i} x {n} = {i*n}")

#2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if i[0] == "S":
        print(f"Good Morning {i}")

#3. Attempt problem 1 using while loop.
i = int(input("Enter the number: "))
j = 1
while True:
    print(f"{i} x {j} = {i*j}")
    j += 1
    if j == 11:
        break

#4. Write a program to find whether a given number is prime or not.
i = int(input("Enter the number: "))
j = []
a = 0
for x in range(2,i):
    j.append(i % x)
    for n in j:
        if n == 0:
            a += 1
if a >= 1:
    print("The number is not prime")
else:
    print("The number is prime")

#5. Write a program to find thes sum of first n natural numbers using while loop.
i = int(input("Enter the number: "))
j = i - 1
while True:
    k = i + j
    i = k 
    j = j - 1
    if j == 0:
        break
print(k)
#6. Write a program to calculate the factorial of a given number using for loop.
i = int(input("Enter the number: "))
j = 1
for n in range(1,i+1):
    j = n*j
print(j)

#7. Write a program to print the following star pattern.
#*
#***
#***** for n = 3
i = int(input("Enter the number of lines: "))
j = "*"
for n in range(1,2*i,2):
    print(j*n)

#8. Write a program to print the following star pattern:
#*
#**
#*** for n = 3
i = int(input("Enter the number of lines: "))
j = "*"
for n in range(1,i+1):
    print(j*n)

#9. Write a program to print the following star pattern.
#* * *
#*   * for n = 3
#* * *
i = int(input("Enter the number: "))
j = "*"
k = 1
l = " "
while True:
    if k == 1 :
        print(i * j)
    elif k < i:
        print("*" + l * (i-2) + "*")
    elif k == i:
        print(i * j)
        break
    k += 1

#10. Write a program to print multiplication table of n using for loops in reversed order.
i = int(input("Enter the number: "))
for n in range(10,0,-1):
    print(f"{i} x {n} = {i*n}")