##################################################################
"""
Name  : ReportExplorer.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Algorithm ->
    1. Import necessary libraries:
        a. sys, argparse: For handling command-line arguments.
        b. pandas: For working with CSV files.
        c. tkinter, ttk, filedialog, ThemedStyle, askstring, messagebox: For creating the GUI.
        d. os: For file operations.
    2. Define an argument parser (argParser) using argparse to handle command-line arguments for the script. Add command-line arguments for:
        a. --report: Path of the final report to explore.
        b. --grep: Comma-separated list of words or strings to be grepped and displayed from the HTTP traffic and web page source code.
        c. --split-report: Split the large final report into smaller reports by specifying the maximum limit of rows in a single file.
    3. Parse the command-line arguments using argParser.parse_args() and store the values in the args variable.
    4. Split the report if the split_report argument is provided:
        a. Read the CSV file into a pandas DataFrame.
        b. Split the DataFrame into chunks of rows.
        c. Write each chunk to a new CSV file.
    5. Extract greppable values if the grep argument is provided and update the DataFrame with occurrence counts of these values in specific columns.
    6. Create a Tkinter main window (root) and configure its size, title, and theme.
    7. Define functions:
        a. load_csv(): Open a file dialog to select a CSV file, read it into a pandas DataFrame, and display the data in the Treeview widget.
        b. display_data(dataframe): Display data in the Treeview widget.
        c. grep_strings(greppables): Count the occurrences of greppable strings in data and display the occurrence count.
        d. filter_data(filter_text): Filter data based on user input and display the filtered results.
        e. clear_filter(): Clear the filter results and display all data.
        f. sort_treeview(column): Sort the Treeview based on the selected column.
        g. copy_text(event, text_widget): Copy selected text from a text widget.
        h. create_context_menu(text_widget): Create a context menu for copying text from a text widget.
        i. show_context_menu_notebook(event, text_widget): Show a context menu for copying selected text from a notebook.
        j. copy_payload(), copy_row(): Functions to copy payload from a selected row and copy the whole selected row, respectively.
        k. show_context_menu(event): Show a context menu when the user right-clicks on a selected row in the Treeview.
        l. show_request_response(event): Show request/response details when a Treeview item is selected.
    8. Create the main GUI components:
        a. Treeview widget for displaying data.
        b. Notebook widget for displaying request/response details and web page before/after details.
        c. Text widgets for displaying detailed information.
    9. Bind keyboard and mouse events to the appropriate functions for copying text and displaying context menus.
   10. Start the Tkinter main loop to run the GUI application.

This is the main file of the Report Explorer tool.
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
import sys
import pandas as pd
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.split_report.split_report import split_report
from modules.report_explorer.show_data.sort_treeview import sort_treeview
from modules.report_explorer.context_menu.show_context_menu_notebook import show_context_menu_notebook
from modules.report_explorer.context_menu.show_context_menu import show_context_menu
from modules.report_explorer.show_data.show_request_response import show_request_response
from modules.report_explorer.show_data.load_csv import load_csv
from modules.report_explorer.filter.filter_button_click import filter_button_click
from modules.report_explorer.filter.clear_filter import clear_filter
from modules.report_explorer.show_data.display_data import display_data
from modules.report_explorer.grep.grep_strings import grep_strings
from modules.report_explorer.show_data.ignore_keyboard import ignore_keyboard

##################################################################
"""
The block of code for Creating UI Components and
Assigning and implementing the functional logic of UI starts here
"""
##################################################################

##################################################################
"""
Name          -> update_font_size
Functionality -> Increase and decrease font size of all elements
Algorithm     ->
    1. get global font_size
    2. add/remove delta from font_size
    3. update size and font of UI elements
Parameters    -> font size
Return        ->
"""
##################################################################

# Global font size variable
font_size = 14 

def update_font_size(delta):
    # Update font size of all elements in the application and adjust widget sizes
    global font_size
    font_size += delta
    new_font = (None, font_size)

    # Update font size for all text widgets
    request_text.configure(font=new_font)
    response_text.configure(font=new_font)
    web_page_before_text.configure(font=new_font)
    web_page_after_text.configure(font=new_font)
    request_text_base64.configure(font=new_font)
    response_text_base64.configure(font=new_font)

    # Adjust Text widget height and width
    request_text.config(height=int(font_size * 1.5), width=int(font_size * 8))
    response_text.config(height=int(font_size * 1.5), width=int(font_size * 8))
    web_page_before_text.config(height=int(font_size * 1.5), width=int(font_size * 4))
    web_page_after_text.config(height=int(font_size * 1.5), width=int(font_size * 4))
    request_text_base64.config(height=int(font_size * 1.5), width=int(font_size * 8))
    response_text_base64.config(height=int(font_size * 1.5), width=int(font_size * 8))
    
    # Update font size for Treeview
    style.configure('Treeview', font=new_font)

    # Adjust the row height for the Treeview based on font size
    row_height = int(font_size * 2)
    style.configure('Treeview', rowheight=row_height)

    # Update font size for menu items and other labels if needed
    style.configure('TLabel', font=new_font)
    style.configure('TMenu', font=new_font)

if __name__ == "__main__":
    if re_global_variable.args.split_report:
        split_report(re_global_variable.args)

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("BrowserBruter Report Explorer")
    root.geometry("1200x600")

    # Maximize the window
    root.attributes('-zoomed', True)

    # Setting theme
    style = ThemedStyle(root)
    style.set_theme("radiance")

    # Create menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Create file menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Load Report", command=lambda: load_csv(pd, tree))

    # Create filter menu
    filter_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="filter", menu=filter_menu)
    filter_menu.add_command(label="filter", command=lambda: filter_button_click(pd,tree))
    filter_menu.add_command(label="Clear", command=lambda: clear_filter(tree))

    # Create view menu for font size
    view_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Increase Font Size", command=lambda: update_font_size(1))
    view_menu.add_command(label="Decrease Font Size", command=lambda: update_font_size(-1))


    # Create Panedwindow for Treeview and Notebook
    paned_window = ttk.Panedwindow(root, orient=tk.VERTICAL)
    paned_window.pack(expand=True, fill='both')

    # Create frame for Treeview and Notebook
    frame_tree_notebook = ttk.Frame(paned_window)
    paned_window.add(frame_tree_notebook, weight=1)

    # Create Treeview widget
    tree = ttk.Treeview(frame_tree_notebook, columns=re_global_variable.columns, show='headings')

    # Configure Treeview columns
    for col in re_global_variable.columns:
        tree.heading(col, text=col, command=lambda c=col: sort_treeview(c, tree))
        tree.column(col, stretch=True)

    # Create vertical and horizontal scrollbars for Treeview
    tree_scroll = ttk.Scrollbar(frame_tree_notebook, orient='vertical', command=tree.yview)
    tree_hscroll = ttk.Scrollbar(frame_tree_notebook, orient='horizontal', command=tree.xview)
    tree_scroll.pack(side='right', fill='y')
    tree_hscroll.pack(side='bottom', fill='x')

    # Configure Treeview to use scrollbars
    tree.configure(yscrollcommand=tree_scroll.set, xscrollcommand=tree_hscroll.set)

    # Pack Treeview widget
    tree.pack(expand=True, fill='both')

    # Create Notebook widget
    notebook = ttk.Notebook(paned_window)
    paned_window.add(notebook, weight=1)

    # Create tab for Request/Response details
    request_response_tab = ttk.Frame(notebook)
    notebook.add(request_response_tab, text='Request/Response')

    # Create Panedwindow for Request/Response tabs
    request_response_paned_window = ttk.Panedwindow(request_response_tab, orient=tk.HORIZONTAL)
    request_response_paned_window.pack(expand=True, fill='both')

    # Create frame for Request tab
    request_tab = ttk.Frame(request_response_paned_window)
    request_response_paned_window.add(request_tab, weight=1)

    # Create Text widget for displaying request details
    request_text = tk.Text(request_tab, wrap='word', width=80, height=20)
    request_text.pack(fill='both', expand=True)

    # Create frame for Response tab
    response_tab = ttk.Frame(request_response_paned_window)
    request_response_paned_window.add(response_tab, weight=1)

    # Create Text widget for displaying response details
    response_text = tk.Text(response_tab, wrap='word', width=80, height=20)
    response_text.pack(fill='both', expand=True)

    # Create tab for Web Page Before/After details
    web_page_tab = ttk.Frame(notebook)
    notebook.add(web_page_tab, text='Web Page Before/After')

    # Create Panedwindow for Web Page Before/After tabs
    web_page_paned_window = ttk.Panedwindow(web_page_tab, orient=tk.HORIZONTAL)
    web_page_paned_window.pack(expand=True, fill='both')

    # Create frame for Web Page Before tab
    web_page_before_tab = ttk.Frame(web_page_paned_window)
    web_page_paned_window.add(web_page_before_tab, weight=1)

    # Create Text widget for displaying web page before details
    web_page_before_text = tk.Text(web_page_before_tab, wrap='word', width=40, height=20)
    web_page_before_text.pack(fill='both', expand=True)

    # Create frame for Web Page After tab
    web_page_after_tab = ttk.Frame(web_page_paned_window)
    web_page_paned_window.add(web_page_after_tab, weight=1)

    # Create Text widget for displaying web page after details
    web_page_after_text = tk.Text(web_page_after_tab, wrap='word', width=40, height=20)
    web_page_after_text.pack(fill='both', expand=True)

    # Create label for displaying response body length
    response_body_length_label = ttk.Label(web_page_after_tab, text="")
    response_body_length_label.pack()

    # Create tab for Request/Response details base64
    request_response_tab_base64 = ttk.Frame(notebook)
    notebook.add(request_response_tab_base64, text='Base64')

    # Create Panedwindow for Request/Response tabs base64
    request_response_paned_window_base64 = ttk.Panedwindow(request_response_tab_base64, orient=tk.HORIZONTAL)
    request_response_paned_window_base64.pack(expand=True, fill='both')

    # Create frame for Request tab base64
    request_tab_base64 = ttk.Frame(request_response_paned_window_base64)
    request_response_paned_window_base64.add(request_tab_base64, weight=1)

    # Create Text widget for displaying request details base64
    request_text_base64 = tk.Text(request_tab_base64, wrap='word', width=80, height=20)
    request_text_base64.pack(fill='both', expand=True)

    # Create frame for Response tab base64
    response_tab_base64 = ttk.Frame(request_response_paned_window_base64)
    request_response_paned_window_base64.add(response_tab_base64, weight=1)

    # Create Text widget for displaying response details base64
    response_text_base64 = tk.Text(response_tab_base64, wrap='word', width=80, height=20)
    response_text_base64.pack(fill='both', expand=True)

    # Bind keyboard events to notebook
    request_text.bind("<KeyPress>", lambda event: ignore_keyboard(event, request_text, root, tk))
    response_text.bind("<KeyPress>", lambda event: ignore_keyboard(event, response_text, root, tk))
    web_page_before_text.bind("<KeyPress>", lambda event: ignore_keyboard(event, web_page_before_text, root, tk))
    web_page_after_text.bind("<KeyPress>", lambda event: ignore_keyboard(event, web_page_after_text, root, tk))
    response_text_base64.bind("<KeyPress>", lambda event: ignore_keyboard(event, response_text_base64, root, tk))
    request_text_base64.bind("<KeyPress>", lambda event: ignore_keyboard(event, request_text_base64, root, tk))

    # Bind Right mouse click to copy selection
    request_text.bind("<Button-3>", lambda event: show_context_menu_notebook(event, request_text, root, tk))
    response_text.bind("<Button-3>", lambda event: show_context_menu_notebook(event, response_text, root, tk))
    web_page_before_text.bind("<Button-3>", lambda event: show_context_menu_notebook(event, web_page_before_text, root, tk))
    web_page_after_text.bind("<Button-3>", lambda event: show_context_menu_notebook(event, web_page_after_text, root, tk))
    response_text_base64.bind("<Button-3>", lambda event: show_context_menu_notebook(event, response_text_base64, root, tk))
    request_text_base64.bind("<Button-3>", lambda event: show_context_menu_notebook(event, request_text_base64, root, tk))
    

    # Bind Treeview click event to show_request_response function
    tree.bind('<ButtonRelease-1>', lambda event: show_request_response(event, tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox))

    # Bind Treeview up and down arrow keys to show_request_response function
    tree.bind('<Up>', lambda event: show_request_response(event, tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox))
    tree.bind('<Down>', lambda event: show_request_response(event, tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox))

    # Bind the right-click event to the show_request_response function
    tree.bind("<Button-3>", lambda event: show_context_menu(event, tree, tk, root))

    # Configure column weights for the Treeview frame
    for i in range(len(re_global_variable.columns)):
        frame_tree_notebook.columnconfigure(i, weight=1)

    frame_tree_notebook.columnconfigure(0, weight=1)
    frame_tree_notebook.rowconfigure(0, weight=1)

    if re_global_variable.args.report:
        # Open a file dialog to select a CSV file
        file_path = re_global_variable.args.report
        try:
            # If a file is selected, read it into a Pandas DataFrame
            if file_path:
                re_global_variable.df = pd.read_csv(file_path)
                # Set the 'Index' column as the DataFrame index
                re_global_variable.df.set_index('Index', inplace=True)

                # Check if 'Index' column is empty
                if re_global_variable.df.index.isnull().all():
                    # Fill 'Index' column with sequential numbers starting from 0
                    re_global_variable.df['Index'] = range(len(re_global_variable.df))

                re_global_variable.sort_order = {}
                if re_global_variable.greppables:
                    grep_strings(re_global_variable.greppables, tree)
                else:
                    # Display the data in the Treeview widget
                    display_data(re_global_variable.df, tree)

        except pd.errors.EmptyDataError:
            # Handle empty file error
            messagebox.showerror("Error", "The selected file is empty.")
        except pd.errors.ParserError:
            # Handle parsing error
            messagebox.showerror("Error", "Error parsing the CSV file.")

    # Start the Tkinter main loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)

##################################################################
"""
The block of code for Creating UI Components and
Assigning and implementing the functional logic of UI ends here
"""
##################################################################