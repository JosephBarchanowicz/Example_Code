import hashlib
import tkinter as tk
from tkinter import messagebox


def generate_password(input_code: str) -> str:
    """
    Generate a deterministic 3-digit password from a 10-digit alphanumeric input code.
    
    Args:
        input_code: A 10-digit alphanumeric code
    
    Returns:
        A 3-digit password (100-999)
    
    Raises:
        ValueError: If input_code is not exactly 10 alphanumeric characters
    """
    # Validate input
    if len(input_code) != 10 or not input_code.isalnum():
        raise ValueError("Input code must be exactly 10 alphanumeric characters")
    
    # Use SHA-256 hash for deterministic generation
    hash_obj = hashlib.sha256(input_code.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Convert first 6 hex digits to integer and map to range 100-999
    hex_value = int(hash_hex[:6], 16)
    password = (hex_value % 900) + 100  # Ensures range 100-999
    
    return str(password)


class PasswordGeneratorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Title
        title_label = tk.Label(
            root,
            text="Password Generator",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instruction_label = tk.Label(
            root,
            text="Enter a 10-digit alphanumeric code",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        instruction_label.pack(pady=5)
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#2c3e50")
        input_frame.pack(pady=20)
        
        # Input Label
        input_label = tk.Label(
            input_frame,
            text="Input Code:",
            font=("Arial", 12, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        input_label.grid(row=0, column=0, padx=10, pady=5)
        
        # Input Entry
        self.input_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=20,
            relief=tk.SOLID,
            borderwidth=2
        )
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)
        self.input_entry.focus()
        
        # Bind Enter key to generate button
        self.input_entry.bind('<Return>', lambda event: self.generate())
        
        # Generate Button
        generate_button = tk.Button(
            root,
            text="Generate Password",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            cursor="hand2",
            relief=tk.RAISED,
            borderwidth=3,
            command=self.generate
        )
        generate_button.pack(pady=15)
        
        # Result Frame
        result_frame = tk.Frame(root, bg="#34495e", relief=tk.SOLID, borderwidth=2)
        result_frame.pack(pady=20, padx=50, fill=tk.BOTH)
        
        # Result Label
        result_title = tk.Label(
            result_frame,
            text="Generated Password:",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        result_title.pack(pady=5)
        
        # Password Display
        self.password_label = tk.Label(
            result_frame,
            text="---",
            font=("Arial", 32, "bold"),
            bg="#34495e",
            fg="#f39c12"
        )
        self.password_label.pack(pady=10)
        
        # Copy Button
        self.copy_button = tk.Button(
            result_frame,
            text="Copy to Clipboard",
            font=("Arial", 10),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            cursor="hand2",
            state=tk.DISABLED,
            command=self.copy_to_clipboard
        )
        self.copy_button.pack(pady=5)
        
        # Clear Button
        clear_button = tk.Button(
            root,
            text="Clear",
            font=("Arial", 10),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            cursor="hand2",
            command=self.clear
        )
        clear_button.pack(pady=5)
    
    def generate(self):
        """Generate password from input code"""
        input_code = self.input_entry.get().strip()
        
        try:
            password = generate_password(input_code)
            self.password_label.config(text=password, fg="#f39c12")
            self.copy_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            self.password_label.config(text="---", fg="#e74c3c")
            self.copy_button.config(state=tk.DISABLED)
    
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        password = self.password_label.cget("text")
        if password != "---":
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
    
    def clear(self):
        """Clear input and output"""
        self.input_entry.delete(0, tk.END)
        self.password_label.config(text="---", fg="#f39c12")
        self.copy_button.config(state=tk.DISABLED)
        self.input_entry.focus()


def main():
    root = tk.Tk()
    app = PasswordGeneratorUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()