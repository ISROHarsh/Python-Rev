#1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
i = input("Enter your name: ")
print(i + " Good Afternoon")

#2. Write a program to fill in a letter template given below with name and date. 
Name = input("Enter your name: ")
Date = input("Enter date in the format of dd/mm/yyyy: ")
letter = '''  
Dear ''' + Name +''', 
You are selected! 
'''+ Date
print(letter)

#Q3.Write a program to detect double space in a string.
i = input("enter:")
print(i.count("  ") > 0)

#Q4.Replace the double space from problem 3 with single spaces. 
i = input("enter:")
print(i.replace("  "," "))

#Q5. Write a program to format the following letter using escape sequence characters. 
letter = "Dear Harry, this python course is nice. Thanks!"
i = letter.find(",")
j = letter.find(".")
letter_new = letter[:i+1] +"\n"+ letter[i+2:j+1] +"\n" + letter[j+2:]
print(letter_new)