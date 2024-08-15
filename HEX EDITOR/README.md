# Hex Mud Hex Editor

**Hex Mud** is a graphical hex editor built using Python and Tkinter. This application allows users to view and edit binary files in hexadecimal format. It also provides functionality for disassembling binary data and highlighting selected areas in the editor.

## Features

- **Open Binary Files**: Load binary files and view their content in hexadecimal format.
- **Hexadecimal and ASCII View**: Display binary data as both hexadecimal values and their corresponding ASCII characters.
- **Disassembly**: Disassemble binary data to view assembly instructions.
- **Highlight Selection**: Highlight selected ranges of hexadecimal data in the editor.
- **Recent Files Menu**: Quickly access recently opened files from the menu.

## Installation

To run this application, you need Python and several libraries. Follow these steps to get started:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Gu/hex-mud.git
    cd hex-mud
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages:**

    Install the necessary Python libraries using pip:

    ```bash
    pip install tkinter colorama capstone
    ```

4. **Run the Application:**

    ```bash
    python hexmud.py
    ```

    The application will open with a GUI for loading and editing binary files.

## Usage

1. **Open a File:**
   - Click on `File` -> `Open` to select and open a binary file.

2. **New File:**
   - Click on `File` -> `New` to create a new untitled file tab.

3. **Recent Files:**
   - Access recently opened files via the `File` -> `Recent files` menu.

4. **Disassemble Binary Data:**
   - Click on `Decode` to view the disassembled instructions of the opened binary file.

5. **Highlight Text:**
   - Click and drag to select a range of text in the hex editor; the selected range will be highlighted.

## Code Overview

- **`Handle` Class**: Manages the GUI components, file handling, and recent files menu.
- **`Operate` Class**: Inherits from `Handle` and handles file opening, displaying hex data, and disassembling instructions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- **Tkinter**: For providing the graphical user interface components.
- **Capstone**: For disassembling binary instructions.
- **Colorama**: For colored text in the disassembly window.

---

Feel free to adjust the content and structure based on any additional features or requirements specific to your project.
