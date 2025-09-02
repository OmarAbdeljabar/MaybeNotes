# MaybeNotes (maybe its important, maybe its useless, we got you covered regardless, "SPEED I AM SPEED")

## Video Demo:  https://youtu.be/XFb54XtPxk8


## Description

*MaybeNotes* the lightest weight note taking app on the planet, with no fancy features by design, inspiration is from my ever long search for basic local note taking apps, that are fast, private, simple, and no frills. 

*Save to clipboard & Exit* – prefixes your notes with today’s date (YYYY-MM-DD), adds bullet points to each line, copies the whole block to the clipboard, and closes the window. This was the original idea and why the application is called MaybeNotes, because sometimes you might watch a YouTube lesson or be on a phone call, and are not sure if the notes your taking need to be saved, or just written for quick use, then deleted, so this app allows you to take notes on a platform capable of both. If you actually needed the notes, it saves to clipboard and you can save at location and file of your choice, but if not needed, the app exits with no bloat or annoying save messages.

*Save as Word Document* – does the same date-stamp, and bullet points but then lets you pick a filename and path for a docx file. Originally this was not part of the plan, but after creating the first version, I instantly recognized that many users would probably paste important notes from clipboard into a Word doc file, so I made it a built in feature instead, to save time for users.

That’s it—no menus, no distractions, just friction-free capture of thoughts, meeting minutes, or grocery lists, with the ability to keep data local, safe, private, and MOVE FAST.

## Files

*project.py* Main application. Contains main() plus three helper functions— `add_bullet_points`, `add_date`, and `save_to_clipboard` —all at top level for easy testing. Uses `tkinter` for GUI, `pyperclip` for clipboard, and `python-docx` for Word export.

main(): Builds and launches the Tkinter gui window, styles the text box and text, adds the "Save to clipboard" and "Save as Word" buttons, and initiates the event loop
save_exit(): Converts the text box's content to bullet-point form, adds today's date to the top, copies to clipboard, and closes the application gui
save_docx(): Formats the text with bullet and date, similar to above, prompts the user for a file name and save location, writes each line to a word document, and then exits the application gui
add_bullet_points(): Returns the input string with every non-empty line prefixed by "-", to represent "bullet points"
add_date(): Adds the current day's date (YYYY-MM-DD) to top of the note, and adds empty line between the date and the notes
save_to_clipboard(): Copies the provided string to the system's clipboard 


*test_project.py* Pytest file with one test for each helper function, ensuring bullet logic, date-stamp format, and clipboard copy all behave as expected.

*requirements.txt* Lists third-party dependencies: `pyperclip`, `python-docx`, and `pytest` 

*README.md* This document—overview, project description, installation, usage, and future ideas. 


## Installation & Usage

1) Clone the repository into local workspace
2) cd project
3) python -m venv venv (start a new virtual environment to test this project, optional but recomended)        
4) source .venv/bin/activate (activate the virtual environment)    
5) pip install -r requirements.txt (install needed libraries into current venv)
6) python project.py (start the application, and gui interface)           
*** Linux users need to install xclip for clipboard functionality

## Future Improvements

1) Improve GUI with customization options for users for fonts, colors, themes, and formatting
2) Design to become a full fledged application, with installer and security signatures for Linux, Windows and Mac, so that I can use across all my devices, and for others as well. Then it would really become one of the world's lightest weight note taking applications, completely open sourced, local, and private.
3) Add option for local offline LLM integration, to bring the power of AI into notes, for voice to text, summarization, and other features. 
