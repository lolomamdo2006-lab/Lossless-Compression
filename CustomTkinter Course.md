
# Part 1 — Basics

## 1. Installation

Install CustomTkinter:

```bash
pip install customtkinter
```

---

## 2. First Window

```python
import customtkinter as ctk

app = ctk.CTk()

app.title("Data Compression")
app.geometry("600x400")

app.mainloop()
```

### `import`

```python
import customtkinter as ctk
```

Imports the `customtkinter` library and gives it the alias `ctk`.

Instead of:

```python
customtkinter.CTk()
```

we can write:

```python
ctk.CTk()
```

### Creating the Window

```python
app = ctk.CTk()
```

Creates the main application window.

`app` is an object representing the window.

### Window Title

```python
app.title("Data Compression")
```

Sets the window title.

### Window Size

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

Keeps the application running and allows it to receive user events.

```text
User clicks button
       ↓
User types
       ↓
User selects something
       ↓
User closes window
```

---

## 3. GUI Structure

A GUI usually contains a main window and widgets inside it:

```text
Window
  │
  ├── Label
  ├── Button
  ├── Entry
  └── Textbox
```

The window and frames are **containers**.

Labels, buttons, entries, and textboxes are **widgets**.

---

# 4. CTkLabel

A Label displays text.

```python
label = ctk.CTkLabel(
    app,
    text="Hello!"
)

label.pack()
```

### `CTkLabel`

```python
ctk.CTkLabel(parent, text="...")
```

- `parent` → the window or frame containing the label.
    
- `text` → the displayed text.
    

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

### `command`

```python
command=say_hello
```

Tells the button which function to execute when clicked.

Do not write:

```python
command=say_hello()
```

because this executes the function immediately.

### Callback

A function passed to `command` is called a **callback**.

```text
User clicks button
        ↓
command
        ↓
callback function
        ↓
function executes
```

---

# Part 2 — Input and Output

# 6. CTkEntry

`CTkEntry` is used for single-line user input.

```python
entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter text..."
)

entry.pack()
```

### Reading the Input

```python
text = entry.get()
```

If the user enters:

```text
ABABABAB
```

then:

```python
text = entry.get()
```

returns:

```python
"ABABABAB"
```

### `placeholder_text`

```python
placeholder_text="Enter text..."
```

Displays placeholder text before the user enters anything.

It is not the actual input value.

---

# 7. CTkTextbox

`CTkTextbox` is used for multi-line or large text input.

```python
textbox = ctk.CTkTextbox(app)

textbox.pack()
```

### Reading the Text

```python
text = textbox.get("1.0", "end")
```

`"1.0"` means:

```text
Line 1, character 0
```

`"end"` means:

```text
Until the end of the textbox
```

### Entry vs Textbox

|Feature|Entry|Textbox|
|---|---|---|
|Single line|Yes|Yes|
|Multiple lines|No|Yes|
|Large input|No|Yes|
|Password input|Yes|No|

For a Data Compression application, `CTkTextbox` is useful for large text input.

---

# 8. Displaying Function Results

A function can return a result:

```python
def calculate():
    return "Done!"
```

The result can be displayed in a Label:

```python
def run():
    result = calculate()
    result_label.configure(text=result)
```

General flow:

```text
Button clicked
      ↓
Function runs
      ↓
Function returns result
      ↓
Result stored in variable
      ↓
Label updated
```

---

# 9. Connecting GUI to LZ77

Suppose `lz77.py` contains:

```python
def compress(text):
    result = "Compressed: " + text
    return result
```

In `main.py`:

```python
import customtkinter as ctk
from lz77 import compress as lz77_compress


def run_compression():
    text = entry.get()

    result = lz77_compress(text)

    result_label.configure(text=result)
```

The GUI does not need to know how the compression algorithm works.

```text
User Input
    ↓
entry.get()
    ↓
lz77_compress(text)
    ↓
return result
    ↓
result_label.configure()
```

---

# Part 3 — Layout

# 10. Frames

A Frame is a container used to organize widgets.

```python
frame = ctk.CTkFrame(app)

frame.pack()
```

Widgets can be placed inside it:

```python
label = ctk.CTkLabel(
    frame,
    text="Hello"
)

label.pack()
```

Structure:

```text
app
│
├── frame
│   ├── label
│   ├── button
│   └── entry
│
└── other widgets
```

---

# 11. `pack()`

`pack()` is a layout manager used to place widgets.

```python
label.pack()
```

### Padding

```python
label.pack(
    padx=20,
    pady=10
)
```

- `padx` → horizontal space.
    
- `pady` → vertical space.
    

### `side`

```python
button.pack(side="left")
```

Places the widget toward the left side.

```python
button.pack(side="right")
```

Places the widget toward the right side.

---

# 12. `grid()`

`grid()` arranges widgets using rows and columns.

```text
        column 0     column 1
       ┌───────────┬───────────┐
row 0  │   Label   │   Entry   │
       ├───────────┼───────────┤
row 1  │  Button   │  Button   │
       └───────────┴───────────┘
```

Example:

```python
label = ctk.CTkLabel(
    app,
    text="Input:"
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

Buttons:

```python
button77.grid(
    row=1,
    column=0
)

button78.grid(
    row=1,
    column=1
)
```

### Important Rule

Do not mix `pack()` and `grid()` in the same parent.

Incorrect:

```python
label.pack()
button.grid(...)
```

if both widgets belong directly to `app`.

Correct:

```text
app
│
└── frame
    ├── label  → grid()
    ├── button → grid()
    └── entry  → grid()
```

`pack()` can be used with `app` while `grid()` is used inside `frame`.

---

# 13. `place()`

`place()` allows widgets to be positioned using coordinates.

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

The widget is positioned at a specific location.

`place()` is useful for precise positioning, but `grid()` or `pack()` is usually easier for responsive layouts.

---

# 14. `grid()` Advanced

A widget can span multiple columns:

```python
result_label.grid(
    row=3,
    column=0,
    columnspan=2
)
```

`columnspan=2` means the widget occupies two columns.

### Expandable Columns

```python
frame.grid_columnconfigure(
    0,
    weight=1
)

frame.grid_columnconfigure(
    1,
    weight=1
)
```

This allows columns to expand when the window is resized.

---

# 15. `fill` and `expand`

With `pack()`:

```python
button.pack(
    fill="x"
)
```

Expands the button horizontally.

For both directions:

```python
textbox.pack(
    fill="both",
    expand=True
)
```

### Values

```text
fill="x"     → horizontal
fill="y"     → vertical
fill="both"  → both directions
```

`expand=True` allows the widget to use additional available space.

---

# 16. Widgets vs Containers

### Widgets

Widgets are UI elements that display information or interact with the user.

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

Containers hold other widgets.

Examples:

```text
CTk
CTkFrame
CTkScrollableFrame
```

Example:

```text
Window
│
└── Frame
    │
    ├── Label
    ├── Entry
    └── Button
```

---

# Part 4 — User Interaction

# 17. CTkComboBox

A ComboBox lets the user select one item from a list.

```python
algorithm = ctk.CTkComboBox(
    app,
    values=["LZ77", "LZ78", "LZW"]
)

algorithm.pack()
```

### Getting the Selected Value

```python
selected = algorithm.get()
```

If the user selects `LZ78`:

```python
selected
```

returns:

```text
LZ78
```

---

# 18. CTkCheckBox

A CheckBox represents an on/off option.

```python
checkbox = ctk.CTkCheckBox(
    app,
    text="Show compression ratio"
)

checkbox.pack()
```

Get its value:

```python
value = checkbox.get()
```

Returns:

```text
1
```

when selected, or:

```text
0
```

when not selected.

---

# 19. CTkSwitch

A Switch is another on/off control.

```python
switch = ctk.CTkSwitch(
    app,
    text="Dark Mode"
)

switch.pack()
```

---

# 20. `configure()`

`configure()` changes widget properties after creation.

Change the text:

```python
result_label.configure(
    text="Compression Done"
)
```

Change the font:

```python
result_label.configure(
    font=("Arial", 20)
)
```

---

# 21. StringVar

`StringVar` stores a string value connected to a widget.

```python
text_var = ctk.StringVar(
    value="Result"
)
```

Use it with a Label:

```python
label = ctk.CTkLabel(
    app,
    textvariable=text_var
)
```

Change the value:

```python
text_var.set(
    "Compression completed!"
)
```

The Label updates automatically.

---

# 22. Events and Callbacks

GUI applications are **event-driven**.

Examples of events:

```text
Button clicked
Mouse moved
Key pressed
Window closed
```

A callback is a function that runs when an event occurs.

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
Event
  ↓
Callback
  ↓
Function
  ↓
Action
```

---

# Part 5 — Application Appearance

# 23. Colors

```python
button = ctk.CTkButton(
    app,
    text="Compress",
    fg_color="green",
    hover_color="darkgreen"
)
```

- `fg_color` → normal button color.
    
- `hover_color` → color when the mouse is over the button.
    

---

# 24. Fonts

```python
label = ctk.CTkLabel(
    app,
    text="Lossless Compression",
    font=("Arial", 24, "bold")
)
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

# 25. Dark / Light Mode

### Dark

```python
ctk.set_appearance_mode("dark")
```

### Light

```python
ctk.set_appearance_mode("light")
```

### System

```python
ctk.set_appearance_mode("system")
```

`system` follows the operating system's appearance setting.

---

# 26. Themes

Set a default color theme:

```python
ctk.set_default_color_theme("blue")
```

Themes help maintain consistent colors throughout the application.

---

# 27. Professional Layout

A clean GUI can be divided into sections using Frames.

Example:

```text
Main Window
│
├── Header Frame
│   └── Title
│
├── Input Frame
│   ├── Algorithm
│   └── Textbox
│
├── Control Frame
│   ├── Compress
│   └── Decompress
│
└── Result Frame
    ├── Result
    └── Compression Ratio
```

This makes the application easier to organize and maintain.

---

# 28. CTkProgressBar

A ProgressBar displays progress.

```python
progress = ctk.CTkProgressBar(app)

progress.pack()
```

Set its value:

```python
progress.set(0.5)
```

Range:

```text
0 → 1
```

Examples:

```text
0.0 = 0%
0.5 = 50%
1.0 = 100%
```

---

# 29. CTkSlider

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

# 30. CTkScrollableFrame

Useful when the content is larger than the available window.

```python
frame = ctk.CTkScrollableFrame(app)

frame.pack(
    fill="both",
    expand=True
)
```

The user can scroll through the content.

---

# Part 6 — Data Compression Project

# 31. Message Boxes

Import:

```python
from tkinter import messagebox
```

### Information

```python
messagebox.showinfo(
    "Success",
    "Compression completed!"
)
```

### Error

```python
messagebox.showerror(
    "Error",
    "Please enter some text."
)
```

---

# 32. Input Validation

Check whether the user entered text before running compression.

```python
def run_compression():

    text = textbox.get(
        "1.0",
        "end"
    )

    if not text.strip():

        messagebox.showerror(
            "Error",
            "Please enter text."
        )

        return

    result = lz77_compress(text)

    result_label.configure(
        text=result
    )
```

### `strip()`

```python
text.strip()
```

Removes whitespace from the beginning and end of the string.

---

# 33. File Dialog — Open File

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

# 34. File Dialog — Save File

Allow the user to choose where to save the result:

```python
file_path = filedialog.asksaveasfilename()
```

General flow:

```text
Input File
    ↓
Read File
    ↓
Compression
    ↓
Compressed Data
    ↓
Save File
```

---

# 35. Compress Button

The Compress button should:

1. Get the input.
    
2. Validate the input.
    
3. Determine the selected algorithm.
    
4. Call the algorithm.
    
5. Display the result.
    

Example:

```python
def run_compression():

    text = textbox.get(
        "1.0",
        "end"
    )

    if not text.strip():
        messagebox.showerror(
            "Error",
            "Please enter text."
        )
        return

    selected = algorithm.get()

    if selected == "LZ77":
        result = lz77_compress(text)

    elif selected == "LZ78":
        result = lz78_compress(text)

    elif selected == "LZW":
        result = lzw_compress(text)

    result_label.configure(
        text=result
    )
```

---

# 36. Decompress Button

The same idea can be used for decompression.

```python
def run_decompression():

    text = textbox.get(
        "1.0",
        "end"
    )

    selected = algorithm.get()

    if selected == "LZ77":
        result = lz77_decompress(text)

    elif selected == "LZ78":
        result = lz78_decompress(text)

    elif selected == "LZW":
        result = lzw_decompress(text)

    result_label.configure(
        text=result
    )
```

The exact input/output format depends on how the compression algorithms are implemented.

---

# 37. Displaying Results

The result can be displayed using a Label:

```python
result_label.configure(
    text=result
)
```

For large results, use a Textbox:

```python
result_textbox.delete(
    "1.0",
    "end"
)

result_textbox.insert(
    "1.0",
    result
)
```

### Useful Textbox Operations

Get:

```python
text = result_textbox.get(
    "1.0",
    "end"
)
```

Delete:

```python
result_textbox.delete(
    "1.0",
    "end"
)
```

Insert:

```python
result_textbox.insert(
    "1.0",
    result
)
```

---

# 38. Compression Ratio

A common compression ratio calculation is:

```text
Compression Ratio = Compressed Size / Original Size
```

As a percentage:

```text
Compression Ratio (%) =
(Compressed Size / Original Size) × 100
```

For example:

```text
Original Size   = 1000 bytes
Compressed Size = 600 bytes

Ratio = 600 / 1000
      = 0.6
      = 60%
```

The exact size calculation depends on the representation used by the project.

---

# 39. Connecting LZ77, LZ78, and LZW

Import the algorithms:

```python
from lz77 import compress as lz77_compress
from lz78 import compress as lz78_compress
from lzw import compress as lzw_compress
```

Create the ComboBox:

```python
algorithm = ctk.CTkComboBox(
    app,
    values=["LZ77", "LZ78", "LZW"]
)

algorithm.pack()
```

Then select the algorithm:

```python
selected = algorithm.get()
```

Use conditions:

```python
if selected == "LZ77":
    result = lz77_compress(text)

elif selected == "LZ78":
    result = lz78_compress(text)

elif selected == "LZW":
    result = lzw_compress(text)
```

---

# 40. Project Organization

Recommended structure:

```text
CompressionProject/
│
├── main.py
│
├── lz77.py
├── lz78.py
├── lzw.py
│
├── README.md
└── requirements.txt
```

### `main.py`

Contains:

- GUI
    
- Input
    
- Buttons
    
- Algorithm selection
    
- Output
    
- Application flow
    

### `lz77.py`

Contains:

- LZ77 compression
    
- LZ77 decompression
    

### `lz78.py`

Contains:

- LZ78 compression
    
- LZ78 decompression
    

### `lzw.py`

Contains:

- LZW compression
    
- LZW decompression
    

### `README.md`

Contains:

- Project description
    
- Algorithms
    
- Installation
    
- Usage
    
- Team information
    

### `requirements.txt`

Contains project dependencies.

---

# 41. requirements.txt

For this project:

```text
customtkinter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 42. `main()`

Organize the application using a `main()` function:

```python
import customtkinter as ctk


def main():

    app = ctk.CTk()

    app.title("Data Compression")
    app.geometry("600x400")

    # Create GUI widgets here

    app.mainloop()


if __name__ == "__main__":
    main()
```

### `if __name__ == "__main__":`

Runs `main()` when the file is executed directly.

If another file imports this module:

```python
import main
```

the GUI will not automatically start.

---

# 43. Final GUI

A possible final interface:

```text
┌────────────────────────────────────────┐
│          LOSSLESS COMPRESSION          │
│                                        │
│ Algorithm: [ LZ77 ▼ ]                  │
│                                        │
│ Input:                                 │
│ ┌────────────────────────────────────┐ │
│ │ Enter your text here...            │ │
│ │                                    │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
│                                        │
│ [ Compress ]      [ Decompress ]       │
│                                        │
│ Result:                                │
│ ┌────────────────────────────────────┐ │
│ │                                    │ │
│ │ Compressed data                    │ │
│ └────────────────────────────────────┘ │
│                                        │
│ Compression Ratio: 60%                 │
│                                        │
│ [ Save Result ]                        │
└────────────────────────────────────────┘
```

---

# 44. Final Application Architecture

```text
                    main.py
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
         GUI       Algorithms     File I/O
          │            │
          │      ┌─────┼─────┐
          │      ↓     ↓     ↓
          │     LZ77  LZ78  LZW
          │
          ↓
      Display Result
```

Application flow:

```text
User
 ↓
Input
 ↓
Select Algorithm
 ↓
Compress / Decompress
 ↓
Algorithm Function
 ↓
Return Result
 ↓
Display Result
 ↓
Save Result
```

---

# 45. Must Know

## Widgets

- `CTk`
    
- `CTkLabel`
    
- `CTkButton`
    
- `CTkEntry`
    
- `CTkTextbox`
    
- `CTkFrame`
    
- `CTkComboBox`
    

## Layout

- `pack()`
    
- `grid()`
    
- `place()`
    

## Interaction

- `command`
    
- `.get()`
    
- `.configure()`
    
- callbacks
    
- events
    

## Application Features

- `filedialog`
    
- `messagebox`
    
- input validation
    
- `main()`
    

## Project Structure

Keep the GUI code separate from the compression algorithms.

---

# 46. Nice to Have

- `CTkCheckBox`
    
- `CTkSwitch`
    
- `CTkProgressBar`
    
- `CTkSlider`
    
- `CTkScrollableFrame`
    
- `StringVar`
    
- Dark/Light mode
    
- Themes
    
- Custom colors
    
- Custom fonts
    

---

# 47. Key Concept

The GUI and compression algorithms should have separate responsibilities.

```text
GUI
 │
 ├── Get input
 ├── Get user choices
 ├── Call functions
 └── Display results

Algorithms
 │
 ├── LZ77
 ├── LZ78
 └── LZW
```

The GUI should not contain the compression logic.

The compression modules should not depend on CustomTkinter.