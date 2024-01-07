import os
import random

def display_ascii_art(ascii_art_file):
    if os.path.isfile(ascii_art_file):
        
        os.system(f"lolcat -f {ascii_art_file}")

    else:
        print("Error: ASCII art not found.")       

if __name__ == "__main__":
    ascii_art_file = "app/yoda.txt"
    display_ascii_art(ascii_art_file)

import subprocess

def print_three_month_calendar():

    result = subprocess.run(["cal", "-3"], capture_output=True, text=True)

    # Drukuj wynik polecenia
    print(result.stdout)

if __name__ == "__main__":
    print_three_month_calendar()