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
            
            with self._filepath.open(self._filepath) as file:
                for line in file:

                    no_punctuation = str.maketrans("", "", string.punctuation)

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
        sorted_words = sorted(self._frequencies.keys())

        for word in sorted_words:
            count = self._frequencies[word]
            print(f"{word}: {count}")

 

def main():
    files_menu = {
        "1": pathlib.Path("princess_mars.txt"),
        "2": pathlib.Path("treasure_island.txt"),
        "3": pathlib.Path("monte_cristo.txt"),
        "4": pathlib.Path("Tarzan.txt")
    }
