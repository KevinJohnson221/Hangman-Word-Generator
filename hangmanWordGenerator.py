import random
import nltk
from nltk.corpus import words
import tkinter as tk

ENGLISH_WORDS = words.words()

def checkInRange(word, min_length, max_length):
    return max_length >= len(word) >= min_length

def getRandomWord(words, min_length, max_length):
    while True:
        randomWord = random.choice(words)
        if checkInRange(randomWord, min_length, max_length):
            return randomWord

def generateWord():
    min_length = int(min_length_entry.get())
    max_length = int(max_length_entry.get())
    generated_word = getRandomWord(ENGLISH_WORDS, min_length, max_length)
    output_label.config(text=generated_word)

def updateDictionary():
    nltk.download('words')
    ENGLISH_WORDS = words.words()
    update_label.config(text="Dictionary Updated!")

# Create the main window
root = tk.Tk()
root.title("Random Word Generator")
root.configure(background='navy')  # Set background color
bold_font = ("Arial", 10, "bold")  # Bold font style

# Padding values
padding_x = 10
padding_y = 5

min_length_label = tk.Label(root, text="Min Word Length:", bg='red', fg='black', font=bold_font)
min_length_label.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)
min_length_entry = tk.Entry(root, bg='orange')
min_length_entry.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

max_length_label = tk.Label(root, text="Max Word Length:", bg='yellow', fg='black', font=bold_font)
max_length_label.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)
max_length_entry = tk.Entry(root, bg='#4CAF50')
max_length_entry.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generateWord, bg='#008CBA', fg='white', font=bold_font)
generate_button.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

# Update Dictionary button
update_button = tk.Button(root, text="Update Dictionary", command=updateDictionary, bg='purple', fg='white', font=bold_font)
update_button.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

# Output label for generated word
output_label = tk.Label(root, text="WORD WILL BE GENERATED HERE", bg='pink', fg='black', font=bold_font)
output_label.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

# Label for dictionary update status
update_label = tk.Label(root, text="Click \"Update Dictionary\"", bg='black', fg='white')
update_label.pack(fill='both', expand=True, padx=padding_x, pady=padding_y)

root.mainloop()
