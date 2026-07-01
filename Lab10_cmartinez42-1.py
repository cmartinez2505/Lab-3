"""
Program Name: Word Analyzer
Author: Chris Martinez
Purpose: This is a OOP Program that is used to count word frequencies in the text files.
Starter Code: No starter code used
Date: June 30, 2026
"""

import pathlib
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self._filepath = pathlib.Path(filepath)
        self._frequencies = {}

    def process_file(self):
        try:
            if not self._filepath.exists():
                return False
         
            no_punctuation = str.maketrans("", "", string.punctuation)
            
            with self._filepath.open("r", encoding="utf-8") as file:
                for line in file:

                    no_line = line.translate(no_punctuation)

                    lowercase_line = no_line.lower()

                    words = lowercase_line.split()


                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] = self._frequencies[word] +1

                        else:
                            self._frequencies[word] = 1

            return True                

        except FileNotFoundError:
            return False
        
    def print_report(self):
        """
        This method takes all the words found, sorts them in alphabetical order, and prints them.
        """
        sorted_words = sorted(self._frequencies.keys())

        for word in sorted_words:
            count = self._frequencies[word]
            print(f"{word} :: {count}")

 

def main():
    """
    The main starting point and driver of the program. It displays the front end of the program.
    
    """
    files_menu = {
        "1": pathlib.Path("princess_mars.txt"),
        "2": pathlib.Path("treasure_island.txt"),
        "3": pathlib.Path("monte_cristo.txt"),
        "4": pathlib.Path("Tarzan.txt")
    }

    while True:

        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Princess Mars")
        print("2. Treasure Island")
        print("3. Monte Cristo")
        print("4. Tarzan")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice in files_menu:
            selected_choice = files_menu[choice]

        
            print(f"\nProcessing '{selected_choice.name}'...\n")
            analyzer = WordAnalyzer(selected_choice)

            if analyzer.process_file():
                analyzer.print_report()
            else:
                 print(f"Error: The file {selected_choice.name} could not be found.")    

            input("\nPress return to return to the menu... ")
        
        else:
             print("\nInvalid choice. Please select from 1-5.")     
             input("\nPress enter to return to the menu... ")   

if __name__ == "__main__":
    main()