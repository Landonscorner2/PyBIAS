from colorama import Fore, Style
import os
import webbrowser
import sys

# Variables, YAY!
RED = Fore.RED
END = Style.RESET_ALL
GREEN = Fore.GREEN

# Functions, because code readability is good. Amiright?

def pybias_ver(): # Version? Yeah, its blah blah blah
    print("PyBIAS-Rewrite 0.1.0-alpha")

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
        print(f"Error: {er}")
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
    {GREEN}List of Commands: {END}
    ver     - PyBIAS Version
    f       - List files
    q       - Quit PyBIAS
    c       - Clear screen
    help    - Show this help message
    web     - Go to URL
    qc      - Quit PyBIAS and clear screen
    cd      - Change directory
    cwd     - Current directory
    """)


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
        pybias_user_input_main = input("pb>: ").strip().lower()
        pybias_command.get(pybias_user_input_main, command_error)()
    except KeyboardInterrupt:
        print("\nKeyboard Exception: Quiting..")
        sys.exit(0)