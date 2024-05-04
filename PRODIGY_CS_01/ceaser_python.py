import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            # Shift uppercase letters
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Shift lowercase letters
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            shifted_char = char
        
        # Apply encryption or decryption based on the mode
        if mode == 'encrypt':
            result += shifted_char
        elif mode == 'decrypt':
            if char.isalpha():
                result += chr((ord(shifted_char) - shift - ord('A')) % 26 + ord('A')) if shifted_char.isupper() else chr((ord(shifted_char) - shift - ord('a')) % 26 + ord('a'))
            else:
                result += char
    return result

def process():
    text = entry_text.get()
    shift = int(entry_shift.get())
    mode = mode_var.get()
    
    if mode == 'encrypt':
        result_text = caesar_cipher(text, shift, 'encrypt')
    elif mode == 'decrypt':
        result_text = caesar_cipher(text, shift, 'decrypt')
    
    output_text.delete(1.0, tk.END)  # Clear previous text
    output_text.insert(tk.END, result_text)

def clear_fields():
    entry_text.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    output_text.delete(1.0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.resizable(False, False)  # Disable window resizing

# Create widgets
label_instructions = ttk.Label(window, text="Enter text to encrypt or decrypt, and specify the shift amount.")
label_text = ttk.Label(window, text="Text:")
entry_text = ttk.Entry(window)
label_shift = ttk.Label(window, text="Shift amount:")
entry_shift = ttk.Entry(window)
label_mode = ttk.Label(window, text="Mode:")
mode_var = tk.StringVar()
mode_var.set('encrypt')
encrypt_radio = ttk.Radiobutton(window, text="Encrypt", variable=mode_var, value='encrypt')
decrypt_radio = ttk.Radiobutton(window, text="Decrypt", variable=mode_var, value='decrypt')
process_button = ttk.Button(window, text="Process", command=process)
clear_button = ttk.Button(window, text="Clear", command=clear_fields)
output_label = ttk.Label(window, text="Output:")
output_text = tk.Text(window, height=2, width=40, wrap=tk.WORD)

# Arrange widgets using grid layout
label_instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label_text.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_text.grid(row=1, column=1, padx=10, pady=5)
label_shift.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_shift.grid(row=2, column=1, padx=10, pady=5)
label_mode.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
encrypt_radio.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
decrypt_radio.grid(row=3, column=1, padx=10, pady=5, sticky=tk.E)
process_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
output_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()