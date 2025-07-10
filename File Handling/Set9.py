#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poem.txt") as f:
    for i in f.readlines():
        for j in i.split():
            if j == "twinkle":
                print("twinkle is present")

#2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
#contains the previous Hi-score. You need to write a program to update the Hi
#score whenever the game() function breaks the Hi-score. 
import random
i = random.randrange(1,1000000000)
with open("High-Score.txt",) as f:
    if int(f.read()) < i:
        with open("High-Score.txt", "w") as f:
            f.write(str(i))

#3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
#different files. Place these files in a folder for a 13 – year old. 
import os
if os.path.exists("C:\\Users\\gamoa\\Documents\\Python\\Expert_Python.py\\File Handling\\Tables"):
    print("File exists")
else:
    os.mkdir("C:\\Users\\gamoa\\Documents\\Python\\Expert_Python.py\\File Handling\\Tables")
os.chdir("C:\\Users\\gamoa\\Documents\\Python\\Expert_Python.py\\File Handling\\Tables")
for i in range(2,21):
    with open(f"table of {i}.txt", "a") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i * j}\n")

#4. A file contains a word “Donkey” multiple times. You need to write a program 
#which replace this word with ##### by updating the same file.  
with open("file.txt") as f:
    txt = f.read()
up_txt = txt.replace("Donkey","#####")
with open("file.txt","w") as f:
    f.write(up_txt)

#5. Repeat program 4 for a list of such words to be censored. 
with open("file.txt") as f:
    txt = f.read().lower()
censor = ["shit","donkey"]
for i in censor:
    txt = txt.replace(i,"#####")
with open("file.txt","w") as f:
    f.write(txt)

#6. Write a program to mine a log file and find out whether it contains ‘python’. 
with open("log.txt") as f:
    for i in f.read().split():
        if i.lower() == "python":
            print("It contains python")
            break

#7. Write a program to find out the line number where python is present from ques 6. 
with open("log.txt") as f:
    lis = f.readlines()
    for i in lis:
        for j in i.lower().split():
            if j == "python":
                print(f"python is present on line {lis.index(i) + 1}")

#8. Write a program to make a copy of a text file “this. txt” 
with open("this.txt") as f:
    content = f.read()
with open("copy_this.txt","w") as f:
    f.write(content)

#9. Write a program to find out whether a file is identical & matches the content of 
#another file. 
with open("this.txt") as f:
    with open("copy_this.txt") as g:
        if f.read() == g.read():
            print("both files are identical")

#10. Write a program to wipe out the content of a file using python. 
with open("poem.txt","w") as f:
    pass

#11. Write a python program to rename a file to “renamed_by_ python.txt".
import os
os.rename("python.txt","renamed_by_ python.txt")