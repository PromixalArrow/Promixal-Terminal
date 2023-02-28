import subprocess
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import random
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Promixal Terminal\nV.0.6 BETA")
when = "no"
print1 = "no"
while True:
    code = input(">>> ").lower()
    if code == 'ping':
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Your Local IPS is: ", host_ip)
        print("Your Desktop Name Is: ", host_name)
    if code == 'date':
        print("The Local Date is: ", time.strftime("%d/%m/%Y"))
    if code == 'list':
        dir_list = os.listdir(path)
        print("Files and Directorys in ", path, "' :")
        print(dir_list)
    if code == 'list -a':
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and Directorys in ", file, "' :")
        print(dir_list2)
    if code == "echo me":
        echo = input("What Do You Want Me To Echo: ")
        print(echo)
    if code == "what are you":
        print("I am a terminal with a custom command language!")
    if code == "who created you":
        print("PromixalArrow42! I love him!")
    if code == "random number":
        user_input = input("Please input a number: ")
        if user_input.isdigit():
            user_input = int(user_input)
            print(random.randint(1, user_input))
        else:
            print("Invalid Input.")
    if code == "random word":
        user_input = input("How Many Options(Up To Three): ")
        if user_input == "2":
            r = random.randint(1, 2)
            r_1 = input("Option 1: ")
            r_2 = input("Option 2: ")
            if r == 1:
                print(r_1)
            elif r == 2:
                print(r_2)
        if user_input == "3":
            r = random.randint(1, 2)
            r_1 = input("Option 1: ")
            r_2 = input("Option 2: ")
            r_3 = input("Option 3: ")
            if r == 1:
                print(r_1)
            elif r == 2:
                print(r_2)
            elif r == 3:
                print(r_3)
            else:
                print("Invalid Input.")
    if code == "rcn":
        random_range = random.randint(1, 4034679309462034926936745387)
        print(random.randint(1, random_range))
    if code == "rcw":
        # 25 words
        word_list = ["the", "okay", "an", "people", "a", "its", "it's", "word", "password", "wing", "so", "lumber", "limb", "person", "apple", "orange", "red", "blue", "what", "stove", "won't", "cat", "dog", "chicken", "command"]
        random_word = random.randint(1, 10)
        if random_word == 1:
            random_word = word_list[0]
        if random_word == 2:
            random_word = word_list[1]
        if random_word == 3:
            random_word = word_list[2]
        if random_word == 4:
            random_word = word_list[3]
        if random_word == 5:
            random_word = word_list[4]
        if random_word == 6:
            random_word = word_list[5]
        if random_word == 7:
            random_word = word_list[6]
        if random_word == 8:
            random_word = word_list[7]
        if random_word == 9:
            random_word = word_list[8]
        if random_word == 10:
            random_word = word_list[9]
        print(random_word)
    if code == "tlai":
        name = input("What's Your Name: ")
        colour = input("What's Your Favourite Colour: ")
        age = input("How Old Are You: ")
        print(f"Your name is {name}. Your Favourite Colour Is {colour}. Your Age Is {age}.")
    if code == "save":
        save = input("What Would You Like To Save: ")
        with open("save/save.txt", "a") as f:
            f.write(save)
        with open("save/save.txt", "a") as f:
            f.write("\n")
    if code == "read saves":
        with open("save/save.txt", "r") as f:
            print(f.read())
    if code == "empty saves":
        with open("save/save.txt", "w") as f:
            f.write("")
        print("Emptied Saves!")
    if code == "create command":
        command_type = input("*NOTE Will Not Save* What Type Of Command Would You Like To Create(p): ")
        if command_type == "p":
            print1 = input("What Would You Like To Print: ")
            when = input("What Is The Activation Word: ")
    if code == when:
        print(print1)
    if code == "num guess":
        range = input("Number: ")
        if range.isdigit():
            while True:
                range = int(range)
                rand_num = random.randint(1, range)
                guess = input("Make A Guess: ")
                guess = int(guess)
                if guess == rand_num:
                    print("You Got It!")
                    break
                if guess < rand_num:
                    print("You Are Smaller Than The Number!")
                    continue
                if guess > rand_num:
                    print("You Are Greater Than The Number!")
                    continue
                else:
                    continue
    if code == "operators":
        print("+ - ÷ x")
    if code == "p operators":
        print("+ = * / % = or == >= <= != or <> < > and or not")
    if code == "w_c":
        w_t = input("What Type Of Weight Mesurement: ").lower()
        if w_t == "lbs":
            lbs = input("Weight Amount: ")
            if lbs.isdigit():
                lbs = int(lbs)
                lbs = lbs / 2.205
                print(f"Your Weight In Kg Is {lbs}!")
            else:
                print("Invalid Weight Amount!")
        elif w_t == "kg":
            kg = input("Weight Amount: ")
            if kg.isdigit():
                kg = int(kg)
                kg = kg * 2.205
                print(f"Your Weight In Kg Is {kg}!")
    if code == "draw":
        draw_type = input("What Do You Want To Draw(H, S, D): ").lower()
        if draw_type == "h":
            print("""
                     ----
                     |  |
                     ----
                     --|--
                       |
                      / |""")
        elif draw_type == "d":
            print("""
                     o------
                      ||||""")
        elif draw_type == "s":
            print("(:")
        else:
            print("Invalid Type!")
    if code == "pide":
        print("Opening Pide........\nSuccessful!")
        file_path = ""

        def set_file_path(path):
            global file_path
            file_path = path
        def run():
            code = editor.get("1.0", END)
            exec(code)
        def save_as():
            if file_path == "":
                path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
            else:
                path = file_path
            with open(path, "w") as file:
                code = editor.get("1.0", END)
                file.write(code)
                set_file_path(path)
        def open_file():
            path = askopenfilename(filetypes=[("Python Files", "*.py")])
            with open(path, "r") as file:
                code = file.read()
                editor.delete("1.0", END)
                editor.insert("1.0", code)
                set_file_path(path)
        def run():
            command = f'python {file_path}'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            code_output.insert("1.0", output)

        compiler = Tk()
        compiler.title("Pide")

        menu_bar = Menu(compiler)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=open_file)
        file_menu.add_command(label="Save", command=save_as)
        file_menu.add_command(label="Save As", command=save_as)
        file_menu.add_command(label="Exit", command=exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        run_bar = Menu(menu_bar, tearoff=0)
        run_bar.add_command(label="Run", command=run)
        menu_bar.add_cascade(label="Run", menu=run_bar)
        compiler.config(menu=menu_bar)

        editor = Text(height=20)
        editor.pack()
        code_output = Text(height=10)
        code_output.pack()
        compiler.mainloop()

    if code == "help":
        print("To Use Me Make Some Code")
        print("These Are My Commands!\nping: Will Ping A Website Of Your Choice\nlocal: Will Tell You Your IPS And Device Name\ndate: Will Tell You The Date\nlist: Will List Folders In C Drive\nlist -a: Will List Files In Any Directory\necho me: Will Echo You\nwhat are you: Will Tell You What I Am\nwho created you: Will Tell You Who Created Me\nrandom number: Will Print A Random Number\nrandom word: Will Print A Random Word\nrcn: Will Make A Random Number, Doesn't need Input\nrcw: Will Make A Random Word, Doesn't need Input\ntlai: Will Make A Temporary AI\nsave: Will Create A Save\nread saves: Will Read Saves\nempty saves: Will Empty Saves\ncreate command: Will Create A Temporary Command\nnum guess: Will Run A Number Guessing Game\noperators: Will Tell You All The Operators\np operators: Will Tell You All The Programming Operators\nw_t: Will Convert Lbs To Kg, Or Kg To Lbs\ndraw: Will Draw A Human, Dog Or Smiley Face\nhelp: Will Help With Commands.")
