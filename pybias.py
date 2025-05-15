import sys

try: # Importing colorama for colored terminal output, if not found on system, exit with an error message.
    from colorama import Fore, Style
except ModuleNotFoundError:
    print("Error: colorama module not found. Please install it using 'pip install colorama'.")
    print("Exiting PyBIAS.")
    sys.exit(1)

import os
import webbrowser
import random


# Variables, YAY!
RED = Fore.RED
END = Style.RESET_ALL
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW

# Functions, because code readability is good. Amiright?

def pybias_ver(): # Version? Yeah, its blah blah blah
    print("PyBIAS-Rewrite 0.2.0-alpha")

def command_error(*args): # Because shelly couldn't figure out the command. Poor child.
    print(RED + "Error: PyBIAS couldn't understand the command." + END)

def list_files(): # Here's ya files, shelly.
        for f in os.listdir():
            print(f)
def quit_pybias(): # NOOO PLEASE DON'T GOO DON'T LEAVE ME :(
    print("Quiting PyBIAS...")
    sys.exit(0)

def clear_screen():  # Call up the OS module and steal his lunch money.
    os.system("cls" if os.name == "nt" else "clear")

def biasweb(): # BiasWEB when you want to search your favorite porn. We're here.
    biasweb_user_input = input("URL: ").strip().lower()
    if not biasweb_user_input.startswith(("http://", "https://")):
        biasweb_user_input = "http://" + biasweb_user_input
    print(GREEN + "Opening the URL.." + END)
    webbrowser.open(biasweb_user_input)

def change_directory(): # Changes directory, took so long to add this to BIAS.
    try:
        pybias_user_input_cd = input("DIR: ").strip()
        if os.path.isdir(pybias_user_input_cd):
            os.chdir(pybias_user_input_cd)
            print(GREEN + "Successfully found directory." + END)
        else:
            print(RED + "Error: PyBIAS couldn't find the directory." + END)
    except (FileNotFoundError, PermissionError) as er:
        print(RED + f"Error: {er}" + END)
    except Exception:
            print(RED + "Error: PyBIAS failed to change directory." + END)

def quit_clear(): # Hides the evidence of the body
    os.system("cls" if os.name == "nt" else "clear")
    sys.exit(0)

def cwd():
    print(GREEN + os.getcwd() + END)

def pybias_help(): # Somehow people can't figure the help command, even when its at the start.
    print(
    f"""
    {GREEN}List of Commands:{END}
    {BLUE}ver{END}     - PyBIAS Version
    {BLUE}f{END}       - List files
    {BLUE}q{END}       - Quit PyBIAS
    {BLUE}c{END}       - Clear screen
    {BLUE}help{END}    - Show this help message
    {BLUE}web{END}     - Go to URL
    {BLUE}qc{END}      - Quit PyBIAS and clear screen
    {BLUE}cd{END}      - Change directory
    {BLUE}cwd{END}     - Current directory
    {BLUE}calc{END}    - Calculator
    {BLUE}md{END}      - Make directory
    {BLUE}rd{END}      - Remove directory
    {BLUE}about{END}   - About PyBIAS
    {BLUE}meme{END}    - Meme library
    """)

def pybias_calculator(): # Does anyone actually use BiasCalc? Please let me know.
    print(f"{GREEN}Opening PyBiasCalc..{END}")
    try:
        pybias_calculator_user_input = input(f"Operator? {BLUE}(+, *, /){END}: ")
        match pybias_calculator_user_input:
            case "+": 
                pybias_calculator_plus_number_1 = int(input("Number?: "))
                pybias_calculator_plus_number_2 = int(input("Number?: "))
                print(f"{GREEN}Equals: {pybias_calculator_plus_number_1 + pybias_calculator_plus_number_2:,}{END}")

            case "*":
                pybias_calculator_multi_number_1 = int(input("Number?: "))
                pybias_calculator_multi_number_2 = int(input("Number?: "))
                print(f"{GREEN}Equals: {pybias_calculator_multi_number_1 * pybias_calculator_multi_number_2:,}{END}")

            case "/":
                pybias_calculator_div_number_1 = int(input("Number?: "))
                pybias_calculator_div_number_2 = int(input("Number?: "))
                print(f"{GREEN}Equals: {pybias_calculator_div_number_1 / pybias_calculator_div_number_2:,}{END}")

            case _:
                print(RED + "Error: Operator not found." + END)
    except (ValueError) as pybias_calculator_error:
        print(RED + f"Error: {pybias_calculator_error}" + " : Did you type a letter or none?" + END)

def make_directory(): # Don't forget this basic file operation. MAKE THE DIR!
    try:
        pybias_user_input_md = input("Enter directory to make: ").strip()
        if os.path.isdir(pybias_user_input_md):
            print(RED + "Error: Already a directory." + END)
        else:
            os.mkdir(pybias_user_input_md)
            print(f"{GREEN}Successfully made directory: {pybias_user_input_md}{END}")
    except (FileNotFoundError, PermissionError, OSError):
        print(RED + "Error: Unable to make directory." + END)

def remove_directory(): # This removes the directory, ran out of ideas.
    try:
        pybias_user_input_rd = input("Enter directory to remove: ")
        os.rmdir(pybias_user_input_rd)
        print(f"{GREEN}Successfully removed directory: {pybias_user_input_rd}{END}")
    except (FileNotFoundError, PermissionError) as remove_directory_error:
        print(f"{RED}Error: {remove_directory_error}{END}")
    except OSError:
        print(RED + "Error: Directory is not empty." + END)

def about_pybias(): # About PyBIAS, because everyone loves a good backstory.
    print("PyBIAS is licensed under the GNU General Public License v3.0.")
    print("It is free software: you can redistribute it and/or modify it under the terms of the License.\n")
    print("PyBIAS is a simple command-line tool for making basic CLI operations easy.")
    print("It includes basic file operations, a calculator, and web browsing capabilities.")
    print(f"{GREEN}Made with passion by Landon <3{END}")

def meme_library(): # This is a meme library. 
    memes = [
        "Why did the chicken cross the road? To get to the other side! Please laugh.",
        "No jokes today, you know what you did.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Error: Memes not found.",
        "Please don't look at the code comments.",
        "Coded in Visual Studio Code, because this shitty HP Stream 11 can't run anything else.",
        "Made by a single developer :(",
        "I really need to get a life.",
        "NO COPILOT, I DON'T WANT YOUR HELP!",
        "Hannah Montana Linux is the best Linux distro.",
        "CS Students, please take showers.",
        "Hacking the mainframe..",
        "I know what im doing, I swear.",
        "Landon is Terry Davis in the flesh.",
        "We <3 CTRL-Z",
        "SWE is better than web dev.",
    ]
    pick_meme = random.choice(memes)
    print(f"{YELLOW}Meme: {pick_meme}{END}")
        

pybias_command = { # Every single command is stored here, CTRL-Z if needed.
    "ver": pybias_ver,
    "f": list_files,
    "q": quit_pybias,
    "c": clear_screen,
    "help": pybias_help,
    "web": biasweb,
    "qc": quit_clear,
    "cd": change_directory,
    "cwd": cwd,
    "calc": pybias_calculator,
    "md": make_directory,
    "rd": remove_directory,
    "about": about_pybias,
    "meme": meme_library,
}

# Here's the actual program. IT'S COMING WITH THE HORRIBLE SPEED OF PYTHON! RAAAH!

os.system("cls" if os.name == "nt" else "clear")

print(r""".______   ____    ____ .______    __       ___           _______.
|   _  \  \   \  /   / |   _  \  |  |     /   \         /       |
|  |_)  |  \   \/   /  |  |_)  | |  |    /  ^  \       |   (----`
|   ___/    \_    _/   |   _  <  |  |   /  /_\  \       \   \    
|  |          |  |     |  |_)  | |  |  /  _____  \  .----)   |   
| _|          |__|     |______/  |__| /__/     \__\ |_______/   """)

pybias_ver()
print(GREEN + "Type 'help' for a list of commands.\n" + END)

# Main loop, this is where the commands happen. Hip hip!

while True:
    try:
        pybias_user_input_main = input("pb: ").strip().lower()
        pybias_command.get(pybias_user_input_main, command_error)()
    except KeyboardInterrupt:
        print("\nKeyboard Exception: Quiting..")
        sys.exit(0)