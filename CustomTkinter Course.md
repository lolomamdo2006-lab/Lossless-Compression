# CustomTkinter Course

A practical guide to building modern desktop GUI applications with Python using CustomTkinter.

---

# Part 1 — Getting Started

## 1. Installation

Install CustomTkinter:

```bash
pip install customtkinter
```

Check that it is installed:

```bash
pip show customtkinter
```

---

# 2. Your First Window

```python
import customtkinter as ctk

app = ctk.CTk()

app.title("My Application")
app.geometry("600x400")

app.mainloop()
```

### `import`

```python
import customtkinter as ctk
```

Imports the library and gives it the alias `ctk`.

### `CTk()`

```python
app = ctk.CTk()
```

Creates the main application window.

### `title()`

```python
app.title("My Application")
```

Sets the window title.

### `geometry()`

```python
app.geometry("600x400")
```

Sets:

```text
width  = 600
height = 400
```

### `mainloop()`

```python
app.mainloop()
```

Starts the GUI event loop.

The application stays running and waits for user events such as clicks, typing, and window actions.

---

# 3. GUI Structure

A typical GUI has a hierarchy:

```text
Application Window
│
├── Frame
│   ├── Label
│   ├── Entry
│   └── Button
│
└── Frame
    ├── Textbox
    └── Button
```

The main window and frames are **containers**.

Labels, buttons, entries, and textboxes are **widgets**.

---

# Part 2 — Basic Widgets

# 4. CTkLabel

A Label displays text.

```python
label = ctk.CTkLabel(
    app,
    text="Hello!"
)

label.pack()
```

### Important Parameters

```python
ctk.CTkLabel(
    parent,
    text="..."
)
```

* `parent` → the window or frame containing the widget.
* `text` → the displayed text.

---

# 5. CTkButton

A Button is a clickable widget.

```python
button = ctk.CTkButton(
    app,
    text="Click Me"
)

button.pack()
```

---

## Button + Function

```python
def say_hello():
    print("Hello!")


button = ctk.CTkButton(
    app,
    text="Click Me",
    command=say_hello
)

button.pack()
```

When the user clicks the button:

```text
Button Click
      ↓
say_hello()
      ↓
print("Hello!")
```

### Important

Use:

```python
command=say_hello
```

Not:

```python
command=say_hello()
```

The first passes the function to be called later.

The second calls the function immediately while creating the button.

---

# 6. Callbacks

A **callback** is a function passed to another function or widget to be executed later when an event occurs.

Example:

```python
def button_clicked():
    print("Button clicked!")


button = ctk.CTkButton(
    app,
    text="Click",
    command=button_clicked
)
```

Flow:

```text
User Event
    ↓
Callback
    ↓
Function
    ↓
Action
```

---

# 7. CTkEntry

`CTkEntry` is used for single-line input.

```python
entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter your name..."
)

entry.pack()
```

### Reading the Input

```python
name = entry.get()
```

If the user enters:

```text
Alaa
```

then:

```python
name = entry.get()
```

returns:

```python
"Alaa"
```

### Placeholder Text

```python
placeholder_text="Enter your name..."
```

Displays temporary text before the user enters a value.

The placeholder is not the actual input.

---

# 8. CTkTextbox

`CTkTextbox` is used for multi-line text.

```python
textbox = ctk.CTkTextbox(app)

textbox.pack()
```

### Reading Text

```python
text = textbox.get("1.0", "end")
```

`"1.0"` means:

```text
Line 1, character 0
```

`"end"` means:

```text
The end of the textbox
```

### Inserting Text

```python
textbox.insert(
    "1.0",
    "Hello!"
)
```

### Deleting Text

```python
textbox.delete(
    "1.0",
    "end"
)
```

---

# 9. Entry vs Textbox

| Feature        | CTkEntry  | CTkTextbox |
| -------------- | --------- | ---------- |
| Single line    | Yes       | Yes        |
| Multiple lines | No        | Yes        |
| Large text     | Not ideal | Yes        |
| Simple input   | Yes       | Yes        |

Use `CTkEntry` for things such as:

```text
Name
Email
Username
Search
Number
```

Use `CTkTextbox` for:

```text
Notes
Descriptions
Documents
Large text
Logs
```

---

# 10. Updating a Widget

Widgets can be changed after creation using `configure()`.

```python
label.configure(
    text="New Text"
)
```

You can also change other properties:

```python
label.configure(
    font=("Arial", 20)
)
```

Example:

```python
def change_text():
    label.configure(
        text="Text Changed!"
    )
```

---

# Part 3 — Layout Managers

# 11. `pack()`

`pack()` places widgets automatically.

```python
label.pack()
button.pack()
entry.pack()
```

Widgets are arranged according to the available space.

---

## Padding

```python
label.pack(
    padx=20,
    pady=10
)
```

* `padx` → horizontal padding.
* `pady` → vertical padding.

Example:

```python
button.pack(
    padx=20,
    pady=20
)
```

---

## `side`

```python
button.pack(side="left")
```

or:

```python
button.pack(side="right")
```

Possible values include:

```text
left
right
top
bottom
```

---

## `fill`

```python
button.pack(
    fill="x"
)
```

Makes the widget expand horizontally.

```python
textbox.pack(
    fill="both"
)
```

Allows expansion in both directions.

---

## `expand`

```python
textbox.pack(
    fill="both",
    expand=True
)
```

Allows the widget to use additional available space.

---

# 12. `grid()`

`grid()` arranges widgets using rows and columns.

```text
        Column 0       Column 1
       ┌───────────┬───────────┐
Row 0  │   Label   │   Entry   │
       ├───────────┼───────────┤
Row 1  │  Button   │  Button   │
       └───────────┴───────────┘
```

Example:

```python
label = ctk.CTkLabel(
    app,
    text="Name:"
)

label.grid(
    row=0,
    column=0
)

entry = ctk.CTkEntry(app)

entry.grid(
    row=0,
    column=1
)
```

Another example:

```python
button1.grid(
    row=1,
    column=0
)

button2.grid(
    row=1,
    column=1
)
```

---

# 13. `columnspan`

A widget can occupy multiple columns.

```python
label.grid(
    row=0,
    column=0,
    columnspan=2
)
```

```text
       Column 0       Column 1
       ┌───────────────────────┐
Row 0  │         Label         │
       └───────────────────────┘
```

---

# 14. `grid_columnconfigure()`

Controls how columns expand when the window is resized.

```python
app.grid_columnconfigure(
    0,
    weight=1
)

app.grid_columnconfigure(
    1,
    weight=1
)
```

A larger `weight` gives a column more of the available space.

---

# 15. `place()`

`place()` positions widgets using coordinates.

```python
button = ctk.CTkButton(
    app,
    text="Click"
)

button.place(
    x=100,
    y=50
)
```

The coordinates represent the widget position inside its parent.

`place()` is useful for precise positioning, but `pack()` and `grid()` are usually better for flexible layouts.

---

# 16. Important Layout Rule

Do not mix `pack()` and `grid()` inside the same parent.

Incorrect:

```python
label.pack()
button.grid(row=0, column=0)
```

if both widgets belong directly to `app`.

You can, however, use different layout managers in different containers:

```text
app
│
├── Frame       → pack()
│   ├── Label   → grid()
│   └── Entry   → grid()
│
└── Button      → pack()
```

---

# Part 4 — Containers

# 17. CTkFrame

A Frame is a container for organizing widgets.

```python
frame = ctk.CTkFrame(app)

frame.pack()
```

Add widgets to the Frame:

```python
label = ctk.CTkLabel(
    frame,
    text="Hello"
)

label.pack()
```

The important part is:

```python
frame
```

instead of:

```python
app
```

The Label belongs to the Frame.

---

# 18. Nested Frames

Frames can contain other Frames.

```text
Application
│
├── Header Frame
│   └── Title
│
├── Input Frame
│   ├── Label
│   └── Entry
│
└── Control Frame
    ├── Button
    └── Button
```

Example:

```python
header = ctk.CTkFrame(app)
header.pack()

input_frame = ctk.CTkFrame(app)
input_frame.pack()

control_frame = ctk.CTkFrame(app)
control_frame.pack()
```

This is one of the main ways to build organized interfaces.

---

# 19. Widgets vs Containers

### Widgets

UI components that display information or interact with the user.

Examples:

```text
CTkLabel
CTkButton
CTkEntry
CTkTextbox
CTkComboBox
CTkCheckBox
CTkSwitch
```

### Containers

Components used to hold other widgets.

Examples:

```text
CTk
CTkFrame
CTkScrollableFrame
```

---

# Part 5 — Selection and Controls

# 20. CTkComboBox

A ComboBox allows the user to select one option.

```python
options = ctk.CTkComboBox(
    app,
    values=[
        "Option 1",
        "Option 2",
        "Option 3"
    ]
)

options.pack()
```

### Get Selected Value

```python
selected = options.get()
```

---

# 21. CTkCheckBox

A CheckBox represents an on/off option.

```python
checkbox = ctk.CTkCheckBox(
    app,
    text="Enable option"
)

checkbox.pack()
```

Get its value:

```python
value = checkbox.get()
```

Returns:

```text
1 → selected
0 → not selected
```

---

# 22. CTkSwitch

A Switch is another on/off control.

```python
switch = ctk.CTkSwitch(
    app,
    text="Enable feature"
)

switch.pack()
```

Get its value:

```python
value = switch.get()
```

---

# 23. CTkSlider

A Slider allows the user to select a numeric value.

```python
slider = ctk.CTkSlider(
    app,
    from_=0,
    to=100
)

slider.pack()
```

Get the value:

```python
value = slider.get()
```

---

# 24. CTkProgressBar

A ProgressBar displays progress.

```python
progress = ctk.CTkProgressBar(app)

progress.pack()
```

Set the progress:

```python
progress.set(0.5)
```

Range:

```text
0.0 → 0%
0.5 → 50%
1.0 → 100%
```

---

# 25. CTkScrollableFrame

Useful when a Frame contains more content than can fit in the window.

```python
frame = ctk.CTkScrollableFrame(app)

frame.pack(
    fill="both",
    expand=True
)
```

The user can scroll through its contents.

---

# Part 6 — Variables and Dynamic Data

# 26. StringVar

`StringVar` stores a string value that can be connected to widgets.

```python
text_var = ctk.StringVar(
    value="Initial Text"
)
```

Use it with a Label:

```python
label = ctk.CTkLabel(
    app,
    textvariable=text_var
)

label.pack()
```

Change the value:

```python
text_var.set(
    "Updated Text"
)
```

The Label updates automatically.

Get the value:

```python
value = text_var.get()
```

---

# 27. Dynamic Output

Instead of creating a new Label every time, update an existing widget.

```python
result_label = ctk.CTkLabel(
    app,
    text="Result"
)

result_label.pack()


def process():
    result = "Operation completed"
    
    result_label.configure(
        text=result
    )
```

General pattern:

```text
Input
 ↓
Function
 ↓
Result
 ↓
configure()
 ↓
Updated GUI
```

---

# Part 7 — Appearance

# 28. Colors

Example:

```python
button = ctk.CTkButton(
    app,
    text="Submit",
    fg_color="green",
    hover_color="darkgreen"
)

button.pack()
```

Common properties:

```text
fg_color
hover_color
text_color
border_color
border_width
```

---

# 29. Fonts

```python
label = ctk.CTkLabel(
    app,
    text="Application",
    font=("Arial", 24, "bold")
)

label.pack()
```

Format:

```text
(font name, size, style)
```

Examples:

```python
font=("Arial", 18)
```

```python
font=("Arial", 18, "bold")
```

---

# 30. Appearance Mode

### Dark Mode

```python
ctk.set_appearance_mode("dark")
```

### Light Mode

```python
ctk.set_appearance_mode("light")
```

### System Mode

```python
ctk.set_appearance_mode("system")
```

`system` follows the operating system's appearance setting.

---

# 31. Themes

Set a default color theme:

```python
ctk.set_default_color_theme("blue")
```

Themes provide consistent colors across widgets.

---

# Part 8 — User Input and Errors

# 32. Message Boxes

Import:

```python
from tkinter import messagebox
```

### Information

```python
messagebox.showinfo(
    "Success",
    "Operation completed!"
)
```

### Error

```python
messagebox.showerror(
    "Error",
    "Something went wrong."
)
```

### Warning

```python
messagebox.showwarning(
    "Warning",
    "Please check your input."
)
```

---

# 33. Input Validation

Always validate user input before processing it.

Example:

```python
def process():

    text = textbox.get(
        "1.0",
        "end"
    )

    if not text.strip():

        messagebox.showerror(
            "Error",
            "Please enter some text."
        )

        return

    result = process_data(text)

    result_label.configure(
        text=result
    )
```

### `strip()`

```python
text.strip()
```

Removes whitespace from the beginning and end of a string.

For example:

```python
"   Hello   ".strip()
```

returns:

```python
"Hello"
```

---

# Part 9 — Files

# 34. File Dialog

Import:

```python
from tkinter import filedialog
```

Open a file-selection dialog:

```python
file_path = filedialog.askopenfilename()
```

The function returns the selected file path.

Example:

```text
C:/Users/User/Desktop/file.txt
```

---

# 35. Selecting File Types

You can restrict the displayed file types:

```python
file_path = filedialog.askopenfilename(
    filetypes=[
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    ]
)
```

---

# 36. Save File Dialog

```python
file_path = filedialog.asksaveasfilename()
```

You can specify a default extension:

```python
file_path = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    ]
)
```

---

# 37. Reading a Selected File

```python
def open_file():

    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    textbox.delete(
        "1.0",
        "end"
    )

    textbox.insert(
        "1.0",
        content
    )
```

If the user cancels the dialog:

```python
if not file_path:
    return
```

prevents the program from trying to open an empty path.

---

# 38. Saving Data

```python
def save_file():

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt"
    )

    if not file_path:
        return

    text = textbox.get(
        "1.0",
        "end"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)
```

General flow:

```text
Select File
    ↓
Read File
    ↓
Process Data
    ↓
Display Result
    ↓
Save Result
```

---

# Part 10 — Connecting GUI to Python Logic

# 39. Separate GUI from Logic

A good project structure separates the interface from the application logic.

Example:

```text
project/
│
├── main.py
├── logic.py
└── requirements.txt
```

`logic.py`:

```python
def process_data(text):
    return text.upper()
```

`main.py`:

```python
import customtkinter as ctk

from logic import process_data
```

The GUI calls the function:

```python
def process():

    text = entry.get()

    result = process_data(text)

    result_label.configure(
        text=result
    )
```

---

# 40. GUI → Function → Result

The general architecture is:

```text
User
 ↓
GUI
 ↓
Input
 ↓
Python Function
 ↓
Processing
 ↓
Return Value
 ↓
GUI
 ↓
Display Result
```

The GUI should handle user interaction.

The logic module should handle the actual processing.

---

# 41. Example Project

`logic.py`:

```python
def calculate(a, b):
    return a + b
```

`main.py`:

```python
import customtkinter as ctk

from logic import calculate


def calculate_result():

    a = int(entry1.get())
    b = int(entry2.get())

    result = calculate(a, b)

    result_label.configure(
        text=f"Result: {result}"
    )


app = ctk.CTk()

app.geometry("400x300")

entry1 = ctk.CTkEntry(app)
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(app)
entry2.pack(pady=10)

button = ctk.CTkButton(
    app,
    text="Calculate",
    command=calculate_result
)

button.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="Result:"
)

result_label.pack(pady=10)

app.mainloop()
```

Architecture:

```text
entry1 ──┐
         │
entry2 ──┼──→ calculate()
         │        ↓
         │      result
         │        ↓
         └──→ result_label
```

---

# Part 11 — Organizing the Application

# 42. Using `main()`

Instead of creating everything globally:

```python
def main():

    app = ctk.CTk()

    app.title("My Application")
    app.geometry("600x400")

    # Create widgets here

    app.mainloop()


if __name__ == "__main__":
    main()
```

### `if __name__ == "__main__":`

Runs `main()` when the file is executed directly.

If the file is imported:

```python
import main
```

the `main()` function will not automatically run.

This prevents the GUI from starting unexpectedly when the module is imported.

---

# 43. Recommended Project Structure

For a larger application:

```text
project/
│
├── main.py
├── gui.py
├── logic.py
├── utils.py
│
├── requirements.txt
└── README.md
```

Possible responsibilities:

### `main.py`

Starts the application.

### `gui.py`

Contains GUI-related code.

### `logic.py`

Contains the main application logic.

### `utils.py`

Contains reusable helper functions.

### `requirements.txt`

Contains external dependencies.

---

# Part 12 — Building a Clean GUI

# 44. Use Frames to Divide the Interface

Example:

```python
header_frame = ctk.CTkFrame(app)
header_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

content_frame = ctk.CTkFrame(app)
content_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

footer_frame = ctk.CTkFrame(app)
footer_frame.pack(
    fill="x",
    padx=20,
    pady=10
)
```

Structure:

```text
Application
│
├── Header
│
├── Content
│
└── Footer
```

---

# 45. Example Clean Layout

```text
┌─────────────────────────────────────┐
│              TITLE                  │
├─────────────────────────────────────┤
│                                     │
│  Input:                             │
│  ┌───────────────────────────────┐  │
│  │                               │  │
│  │           Textbox             │  │
│  │                               │  │
│  └───────────────────────────────┘  │
│                                     │
│      [ Process ]    [ Clear ]       │
│                                     │
│  Result:                            │
│  ┌───────────────────────────────┐  │
│  │                               │  │
│  │           Result              │  │
│  │                               │  │
│  └───────────────────────────────┘  │
│                                     │
└─────────────────────────────────────┘
```

---

# 46. Clear Button

A Clear button can remove user input.

```python
def clear_text():

    textbox.delete(
        "1.0",
        "end"
    )

    result_label.configure(
        text="Result:"
    )
```

Create the button:

```python
clear_button = ctk.CTkButton(
    app,
    text="Clear",
    command=clear_text
)

clear_button.pack()
```

---

# 47. Complete Basic Application

```python
import customtkinter as ctk
from tkinter import messagebox


def process_data(text):
    return text.upper()


def process():

    text = textbox.get(
        "1.0",
        "end"
    )

    if not text.strip():

        messagebox.showerror(
            "Error",
            "Please enter some text."
        )

        return

    result = process_data(text)

    result_textbox.delete(
        "1.0",
        "end"
    )

    result_textbox.insert(
        "1.0",
        result
    )


def clear():

    textbox.delete(
        "1.0",
        "end"
    )

    result_textbox.delete(
        "1.0",
        "end"
    )


def main():

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("My Application")
    app.geometry("700x500")

    title = ctk.CTkLabel(
        app,
        text="My Application",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=20)

    textbox = ctk.CTkTextbox(
        app,
        height=150
    )

    textbox.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    process_button = ctk.CTkButton(
        app,
        text="Process",
        command=process
    )

    process_button.pack(pady=10)

    clear_button = ctk.CTkButton(
        app,
        text="Clear",
        command=clear
    )

    clear_button.pack(pady=10)

    result_textbox = ctk.CTkTextbox(
        app,
        height=150
    )

    result_textbox.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    app.mainloop()


if __name__ == "__main__":
    main()
```

---

# Part 13 — Important Concepts

## Widgets

Know how to use:

```text
CTkLabel
CTkButton
CTkEntry
CTkTextbox
CTkComboBox
CTkCheckBox
CTkSwitch
CTkSlider
CTkProgressBar
CTkFrame
CTkScrollableFrame
```

## Layout

Know:

```text
pack()
grid()
place()
```

and:

```text
padx
pady
fill
expand
row
column
columnspan
weight
```

## Interaction

Know:

```text
command
callback
get()
configure()
insert()
delete()
StringVar
```

## User Input

Know:

```text
Entry input
Textbox input
ComboBox selection
CheckBox state
Switch state
Slider value
```

## Files

Know:

```text
filedialog.askopenfilename()
filedialog.asksaveasfilename()
open()
read()
write()
```

## Errors

Know:

```text
messagebox.showinfo()
messagebox.showwarning()
messagebox.showerror()
```

---

# 14. Final Mental Model

When building a CustomTkinter application, think in this order:

```text
1. Create Window
        ↓
2. Create Frames
        ↓
3. Create Widgets
        ↓
4. Arrange Widgets
        ↓
5. Get User Input
        ↓
6. Run Python Logic
        ↓
7. Get Result
        ↓
8. Update GUI
        ↓
9. Save / Display Result
```

The most important architecture is:

```text
              GUI
               │
        ┌──────┴──────┐
        ↓             ↓
      Input         Events
        │             │
        └──────┬──────┘
               ↓
          Python Logic
               │
               ↓
            Result
               │
               ↓
              GUI
```

Keep the GUI responsible for **interaction and presentation**, and keep the actual application logic in separate Python functions or modules.
