# Import necessary modules
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Function to check if two words are anagrams
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

# Function to find anagram groups and non-anagram words
def find_anagrams(word_list):
    anagram_groups = {}  # Dictionary to store anagram groups
    non_anagrams = []    # List to store non-anagram words

    # Iterate through each word in the word list
    for word in word_list:
        sorted_word = ''.join(sorted(word))  # Sort the characters in the word

        # Add word to existing anagram group or create a new group
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    anagram_groups_list = [group for group in anagram_groups.values() if len(group) > 1]
    non_anagrams = [word for word in word_list if word not in [item for group in anagram_groups_list for item in group]]
    return anagram_groups_list, non_anagrams

# Function to find and display anagram groups and non-anagram words
def find_non_anagrams():
    input_words = entry.get()  # Get input words from the Entry widget
    word_list = input_words.split()  # Split input words into a list
    anagram_groups, non_anagrams = find_anagrams(word_list)  # Find anagram groups and non-anagram words

    result_text = ""

    if anagram_groups:
        result_text += "\nAnagram groups:\n"
        for group in anagram_groups:
            result_text += ", ".join(group) + "\n"  # Display anagram groups

    if non_anagrams:
        if anagram_groups:
            result_text += "\n"  # Add spacing between sections
        result_text += "Non-anagram words:\n" + "\n".join(non_anagrams)  # Display non-anagram words

    if not (anagram_groups or non_anagrams):
        result_text = "No anagram groups or non-anagram words found."

    result_text += f"\nTotal anagram groups found: {len(anagram_groups)}"  # Display total anagram groups
    result_text += f"\nTotal non-anagram words found: {len(non_anagrams)}"  # Display total non-anagram words

    result_label.config(text=result_text)  # Update the result label with the generated text

# Function to clear input and results
def clear_input_results():
    entry.delete(0, tk.END)  # Clear input entry
    result_label.config(text="")  # Clear result label

# GUI window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Anagram Finder") 
    root.geometry("400x450")

    root.configure(bg="#2a2a2a")
    ttk.Style().configure("TButton", padding=5, relief="flat", background="#1c72b0", foreground="#2a2a2b", font=('Helvetica', 12))
    ttk.Style().configure("TLabel", padding=5, background="#2a2a2a", foreground="white", font=('Helvetica', 12))

    input_label = ttk.Label(root, text="Enter space-separated words:", background="#2a2a2a")
    input_label.pack(pady=10)

    entry = ttk.Entry(root, width=40, font=('Helvetica', 12))
    entry.pack(pady=5)

    submit_button = ttk.Button(root, text="Find Anagrams", command=find_non_anagrams)
    submit_button.pack(pady=10)

    # Clear Button
    clear_button = ttk.Button(root, text="Clear", command=clear_input_results)
    clear_button.pack(pady=5)

    result_label = ttk.Label(root, text="", wraplength=380, background="#2a2a2a", foreground="white")
    result_label.pack(pady=10)

    root.mainloop()
