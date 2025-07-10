#1. Write a program using functions to find greatest of three numbers.
def great(a,b,c):
    if a > b and a > c :
        print(f"{a} is the greatest number.")
    elif a < b and b > c :
        print(f"{b} is the greatest number.")
    elif a < b and b < c :
        print(f"{c} is the largest number.")

#2. Write a python program using function to convert Celsius to Fahrenheit.
def celfar(temp):
    print(f"{round(temp * 1.8 + 32)} degree Fahrenheit.")

#3. How do you prevent a python print() function to print a new line at the end.
print("Hello",end="") #the end parameter would not let the default new line at the end
print("Vau")

#4. Write a recursive function to calculate the sum of first n natural numbers.
def sumn(num):
    if num == 1 or 0:
        return num
    return num + sumn(num - 1)

#5. Write a python function to print first n lines of the following pattern:
#***
#** - for n = 3
#*
def patt(n):
    for j in range(n, 0, -1):
        print("*" * j)

#6. Write a python function which converts inches to cms.
def intocm(inc):
    return f"{inc} inches are {2.5 * inc} cms."

#7. Write a python function to remove a given word from a list ad strip it at the same time.
def remnstrip(lis,word):
    l = []
    for i in lis:
        l.append(i.strip())
    for i in l:
        if i == word:
            l.remove(word)
    return l 
#8. Write a python function to print multiplication table of a given number.
def multable(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")