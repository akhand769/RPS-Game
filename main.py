import random
rock='''
        -----------
--------|    _______)
            (________)
            (________)
            (________)
--------___(_____)
'''

paper = '''
        -----------
--------|    _______)
            (________________)
            (________________)
            (________________)
--------___(______________)
'''
scissor = '''
        -----------
--------|    _______)
            (________________)
            (________________)
            (_______)
--------___(________)
'''
win = 0
while not(win):
    user = input("Enter 0 for rock | 1 for paper | 2 for scissor\n")
    print("You entered - "+ user)
    comp = random.randint(0,2)
    comp=str(comp)
    win=1
    if user=='0' and comp=='1':
        print(rock)
        print(paper)
        print("comp entered - "+ comp +" comp won.")
    elif user=='1' and comp=='0':
        print(paper)
        print(rock)
        print("comp entered - "+comp+" you won.")
    elif user=='1' and comp=='2':
        print(paper)
        print(scissor)
        print("comp entered - "+comp+" comp won.")
    elif user=='2' and comp=='1':
        print(scissor)
        print(paper)
        print("comp entered - "+comp+" you won.")
    elif user=='0' and comp=='2':
        print(rock)
        print(scissor)
        print("comp entered - "+comp+" you won.")
    elif user=='2' and comp=='0':
        print(scissor)
        print(rock)
        print("comp entered - "+comp+" comp won.")
    else:
        print("comp entered - "+comp+" match draw.")
        win=0
    
