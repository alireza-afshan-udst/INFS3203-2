# quiz_app.py

import tkinter as tk
from tkinter import ttk 
from tkinter import *

root = tk.Tk()

root.title("Quiz App")
root.geometry('730x480')


# questions generated using chatGPT
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 3 # Position in the options array 
    },
    {
        "topic": "Lists",
        "question": "What will be the result of the following code?",
        "code": "my_list = [10, 20, 30]\nmy_list.append(40)\nprint(my_list)",
        "options": ["[10, 20, 30, 40]", "[10, 20, 40, 30]", "[40, 10, 20, 30]", "[10, 40, 20, 30]"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Strings",
        "question": "What will be the output of this code?",
        "code": "text = 'Python'\nprint(text[1:4])",
        "options": ["'Pyt'", "'yth'", "'hon'", "'Py'"],
        "answer": 1  # Position in the options array
    },
    {
        "topic": "Dictionaries",
        "question": "What will be the result of this code?",
        "code": "my_dict = {'a': 1, 'b': 2}\nmy_dict['c'] = 3\nprint(my_dict)",
        "options": ["{'a': 1, 'b': 2, 'c': 3}", "{'a': 1, 'b': 2, 'c': '3'}", "{'a': 1, 'b': 2, 'c': [3]}", "{'a': 1, 'b': 2}"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Functions",
        "question": "What will be the result of calling this function with argument 5?\n\n def multiply(x):\n    return x * 2",
        "options": ["10", "5", "2", "20"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Conditionals",
        "question": "What will be printed by the following code?\n\n if 3 > 2:\n    print('Yes')\nelse:\n    print('No')",
        "options": ["Yes", "No", "Error", "Nothing"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Loops",
        "question": "What will be the output of the following code?\n\n for i in range(2, 5):\n    print(i)",
        "options": ["2 3 4", "1 2 3 4", "2 3", "3 4"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Strings",
        "question": "What does the method .upper() do to a string?",
        "options": ["Makes all characters lowercase", "Makes all characters uppercase", "Reverses the string", "Makes the first letter uppercase"],
        "answer": 1  # Position in the options array
    }
    
]


root.mainloop()
