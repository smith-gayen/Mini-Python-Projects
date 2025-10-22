import pandas as pd
import customtkinter
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES

# Set the appearance mode to "dark" for a black UI
customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")  # Optional: You can choose different dark themes

# Function to process the uploaded Excel file
def process_file(file_path):
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Remove duplicates
        df_unique = df.drop_duplicates()

        # Save the processed file
        processed_file_path = 'processed_stock_data.xlsx'
        df_unique.to_excel(processed_file_path, index=False)

        messagebox.showinfo("Success", f"File processed and saved as {processed_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle drag-and-drop event
def drop(event):
    file_path = event.data.strip('{}')  # Clean up the path
    if file_path.endswith('.xlsx'):
        process_file(file_path)
    else:
        messagebox.showerror("Error", "Please drop a valid Excel file (.xlsx).")

# Function to open file dialog
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        process_file(file_path)

# Create CustomTkinter GUI with TkinterDnD
root = TkinterDnD.Tk()  # Using TkinterDnD to enable drag-and-drop
root.title("Stock Data Processor")

# Set the default window size (larger window)
root.geometry("600x400")
root.configure(bg="#262626")

# Create a label for drag-and-drop area (set background and text colors for dark theme)
drop_label = customtkinter.CTkLabel(root, text="Drop Excel File Here", width=400, height=200, fg_color="#595959", text_color="white", corner_radius=10)
drop_label.pack(pady=20)

# Enable the drag-and-drop feature
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', drop)

# Upload Button to open file dialog as an alternative
upload_btn = customtkinter.CTkButton(root, text="Upload Excel File", command=upload_file)
upload_btn.pack(pady=20)

# Start the main loop
root.mainloop()