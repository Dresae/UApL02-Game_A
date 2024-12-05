import tkinter as tk
from tkinter import messagebox
from questions import QUESTIONS_DICT

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.current_question = 0
        self.money = 0
        self.lifeline_used = False
        self.setup_gui()
        self.load_question()

    def setup_gui(self):
        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=600, justify="center")
        self.question_label.pack(pady=20)

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 14), width=20, command=lambda i=i: self.check_answer(i + 1))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Lifeline and Quit Buttons
        self.lifeline_button = tk.Button(self.root, text="Lifeline", font=("Arial", 14), command=self.use_lifeline)
        self.lifeline_button.pack(side="left", padx=20)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 14), command=self.quit_game)
        self.quit_button.pack(side="right", padx=20)