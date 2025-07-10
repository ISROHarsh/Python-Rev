import random

print("""Welcome to the Snake-Water-Gun game. let's begin to play!!""")

print("""Choose your item and enter the int from the below
    [1] Snake
    [2] Water
    [3] Gun
    """)
outcomes = {
    (1, 1): "draw",     
    (1, 2): "won",      
    (1, 3): "lose",     
    (2, 1): "lose",     
    (2, 2): "draw",     
    (2, 3): "won",      
    (3, 1): "won",      
    (3, 2): "lose",     
    (3, 3): "draw", 
    }

while True:
    i = int(input("Your Choice: "))
    j = random.randrange(1,4)
    k = ["Snake", "Water", "Gun"]
    print(f"You Chose {k[i - 1]} and the Computer Chose {k[j - 1]}")
    print(f"You {outcomes.get((i,j))} the game !!")
    print("If you want to play more click Enter \nIf you want to Quit click Q")
    r = input("Enter or Quit ??:")
    if r.lower() == "q":
        print("Thanks for playing the game :)")
        break
    elif r == "":
        continue