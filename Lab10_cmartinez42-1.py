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

                    


            
    
            







        except FileNotFoundError:
            return False

 


