import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

def select_files():
    files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    if files:
        file_list.extend(files)
        update_file_listbox()

def update_file_listbox():
    listbox.delete(0, tk.END)
    for i, file in enumerate(file_list):
        listbox.insert(tk.END, f"{i+1}. {os.path.basename(file)}")

def move_up():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        if idx > 0:
            file_list[idx], file_list[idx-1] = file_list[idx-1], file_list[idx]
            update_file_listbox()
            listbox.selection_set(idx-1)

def move_down():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        if idx < len(file_list) - 1:
            file_list[idx], file_list[idx+1] = file_list[idx+1], file_list[idx]
            update_file_listbox()
            listbox.selection_set(idx+1)

def merge_pdfs():
    if not file_list:
        messagebox.showwarning("No files selected", "Please select at least two PDF files to merge.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        return

    try:
        merger = PdfMerger()
        for pdf in file_list:
            merger.append(pdf)

        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged successfully and saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_list():
    file_list.clear()
    update_file_listbox()


root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")
root.resizable(False, False)


root.configure(bg="#f7f7f7")

file_list = []


title_label = tk.Label(root, text="PDF Merger Tool", font=("Helvetica", 16), bg="#f7f7f7")
title_label.pack(pady=10)


listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, padx=(10, 0))

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)


move_frame = tk.Frame(root, bg="#f7f7f7")
move_frame.pack(pady=5)

move_up_button = tk.Button(move_frame, text="Move Up", command=move_up, width=10)
move_up_button.grid(row=0, column=0, padx=5)

move_down_button = tk.Button(move_frame, text="Move Down", command=move_down, width=10)
move_down_button.grid(row=0, column=1, padx=5)


button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=10)

select_button = tk.Button(button_frame, text="Select PDFs", command=select_files, width=15, bg="#007bff", fg="white")
select_button.grid(row=0, column=0, padx=5)

merge_button = tk.Button(button_frame, text="Merge PDFs", command=merge_pdfs, width=15, bg="#28a745", fg="white")
merge_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear List", command=clear_list, width=15, bg="#dc3545", fg="white")
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()
