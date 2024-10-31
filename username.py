import subprocess
import sys
import itertools
import os
from colorama import init, Fore

# Function to check and install required packages
def install_packages():
    required_packages = ['colorama', 'requests']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Package '{package}' not found. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        else:
            print(f"Package '{package}' is already installed.")

# Call the function to ensure packages are installed
install_packages()

# Initialize colorama
init(autoreset=True)

# ASCII Art with color
ascii_art = (
    Fore.YELLOW + """
   ▄████████  ▄██████▄  ███▄▄▄▄      ▄████████     ███      ▄█   ▄████████
  ███    ███ ███    ███ ███▀▀▀██▄   ███    ███ ▀█████████▄ ███  ███    ███
  ███    █▀  ███    ███ ███   ███   ███    █▀     ▀███▀▀██ ███▌ ███    █▀ 
  ███        ███    ███ ███   ███  ▄███▄▄▄         ███   ▀ ███▌ ███       
  ███        ███    ███ ███   ███ ▀▀███▀▀▀         ███     ███▌ ███       
  ███    █▄  ███    ███ ███   ███   ███    █▄      ███     ███  ███    █▄ 
  ███    ███ ███    ███ ███   ███   ███    ███     ███     ███  ███    ███
  ████████▀   ▀██████▀   ▀█   █▀    ██████████    ▄████▀   █▀   ████████▀  
      
""" + Fore.WHITE + "  For more updates join: " + Fore.CYAN + "https://t.me/tools2larp" + Fore.RESET
)

clear = lambda: os.system("cls")

unicode_map = {
    "a": "а", "c": "с", "d": "ԁ", "e": "е", "i": "і",
    "j": "ј", "o": "ο", "p": "р", "q": "ԛ", "s": "ѕ",
    "w": "ԝ", "x": "х", "y": "у", "A": "Α", "B": "Β",
    "C": "С", "E": "Ε", "H": "Η", "I": "Ι", "J": "Ј",
    "K": "Κ", "M": "Μ", "N": "Ν", "O": "Ο", "P": "Ρ",
    "S": "Ѕ", "T": "Τ", "X": "Χ", "Y": "Υ", "Z": "Ζ"
}

C0 = "\033[38;2;255;255;255m"
C1 = "\033[38;2;214;90;66m"
C2 = "\033[38;2;192;192;192m"  # Light gray color for 'Press'

def generate_variations(word, unicode_map):
    replaceable_positions = [(i, unicode_map[char]) for i, char in enumerate(word) if char in unicode_map]
    variations = set()
    for r in range(1, len(replaceable_positions) + 1):
        for combo in itertools.combinations(replaceable_positions, r):
            new_word = list(word)
            for pos, replacement in combo:
                new_word[pos] = replacement

            variations.add("".join(new_word))

    return sorted(variations)

def print_variations(word, variations, unicode_map):
    for index, variation in enumerate(variations, start=1):
        colored_word = ""
        for original_char, new_char in zip(word, variation):
            if original_char in unicode_map and unicode_map[original_char] == new_char:
                colored_word += Fore.LIGHTYELLOW_EX + new_char + C0
            else:
                colored_word += new_char
        print(f"  {Fore.WHITE}[{Fore.YELLOW}{index}{Fore.WHITE}] {C0}{colored_word}")

def main(word):
    variations = generate_variations(word, unicode_map)
    if len(variations) > 0:
        print_variations(word, variations, unicode_map)
    else:
        print(f" No variations for this word found")

    input(f"\n  {C2}Press {Fore.YELLOW}'{Fore.WHITE}ENTER{Fore.YELLOW}'{C2} to return to menu{Fore.RESET}")

def menu():
    while True:  # Loop to keep the menu running
        clear()
        print(ascii_art)  # Print the ASCII art after clearing the screen
        print()  # Add a new line above the input prompt
        word = input(Fore.WHITE + "  [" + Fore.YELLOW + "+" + Fore.WHITE + "] Please enter a word: " + Fore.LIGHTYELLOW_EX).strip()
        print()  # Add a single line after the input
        main(word)

if __name__ == "__main__":
    os.system(f"title Support: discord.gg/conetic, Credits: @vd_vd_vd")
    menu()
