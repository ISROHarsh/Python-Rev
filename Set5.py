#Q1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
dic = {"Thanda":"Cold","Garmi":"Hot","Maal":"Item","Sanskaar":"Well Mannered"}
i = input("enter the word in Hindi: ")
print(dic.get(i))


#Q2. Write a program to input eight numbers from the user and display all the unique numbers (once).
num = set()
for i in range(1,9):
    j = input(f"Enter the no.{i}: ")
    num.add(j)
print(num)

#Q3. Can we have a set with 18 (int) and '18' (str) as a value in it?
set = set()
set.add(18)
set.add('18')
print(set) #This Result States that there could be int(18) and str'18' in a set

#Q4. What will be the length of following set s: 
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations? I THINK 3 -> THIS WAS WRONG the 20.0 was considered to be same as 20
print(s)

#Q5. s = {}, what is the type of 's'? 
s = {} #The Type is Dictionary
print(type(s)) 

#Q6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
lang = {}
for i in range(1,5):
    name = input("Enter your Name: ")
    Lang = input("Enter your Favourite language: ")
    lang.update({name:Lang})
print(lang)

#Q7. If the names of 2 friends are same; what will happen to the program in problem 6? 
#This means that the Keys will be same and in a dict there cannot be identical keys so a error would occur

#Q8. If languages of two friends are same; what will happen to the program in problem 6? 
#This possible as Keys are must to be unique but the values are not necessarily to be unique

#Q9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
# It is important to know that list is not taken in sets and so save group of some items we should use tuples and still we are not able to iterate any element in a set
