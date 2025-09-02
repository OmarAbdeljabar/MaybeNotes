from pyperclip import copy
from datetime import date
import tkinter
from docx import Document
from tkinter import filedialog


def main():
    gui = tkinter.Tk()
    gui.title("MaybeNotes")
    textwindow = tkinter.Text(gui)
    textwindow.pack()
    gui.configure(bg="black")
    textwindow.configure(
        bg="black",
        fg="lime",
        insertbackground="lime",
        font=("Calibri", 12),
        wrap="word",
    )
    button = tkinter.Button(
        gui,
        text="Save to clipboard and Exit",
        command=lambda: save_exit(textwindow, gui),
    )
    button.pack()

    doc_button = tkinter.Button(
        gui, text="Save as Word Document", command=lambda: save_docx(textwindow, gui)
    )
    doc_button.pack()
    gui.mainloop()


def save_exit(x, y):
    notes = x.get("1.0", "end")
    bullet_notes = add_bullet_points(notes)
    savednotes = add_date(bullet_notes)
    save_to_clipboard(savednotes)
    y.destroy()


def save_docx(x, y):
    notes = x.get("1.0", "end")
    bullet_notes = add_bullet_points(notes)
    savednotes = add_date(bullet_notes)
    path = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Word document", "*.docx")],
        title="Save notes as",
    )
    if path:
        doc = Document()
        for line in savednotes.split("\n"):
            doc.add_paragraph(line)
        doc.save(path)
        y.destroy()


def add_bullet_points(x):
    lines = x.split("\n")
    bullet_lines = []
    for line in lines:
        if line.strip():
            bullet_lines.append(f"- {line}")
        else:
            bullet_lines.append("")
    return "\n".join(bullet_lines)


def add_date(x):
    today_date = date.today()
    today_date = str(today_date)
    today_date = today_date + "\n" + x
    return today_date


def save_to_clipboard(x):
    copy(x)


if __name__ == "__main__":
    main()
