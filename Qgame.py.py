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