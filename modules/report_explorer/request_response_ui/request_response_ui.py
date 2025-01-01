##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.context_menu.show_context_menu_notebook import show_context_menu_notebook
from modules.report_explorer.show_data.ignore_keyboard import ignore_keyboard
from modules.report_explorer.search_text.search_text import search_text

def on_entry_click(event, search_entry, tk):
    if search_entry.get() == 'Enter text to search':
        search_entry.delete(0, tk.END)  # Clear the entry field
        search_entry.config(fg='black')  # Change text color to black

# Function to restore placeholder text if empty
def on_focus_out(event,search_entry):
    if search_entry.get() == '':
        search_entry.insert(0, 'Enter text to search')  # Insert placeholder text
        search_entry.config(fg='grey')  # Change text color to grey



def request_response_ui(root, tk, ttk, paned_window, ):
    # Create frame for Request tab
    tab = ttk.Frame(paned_window)
    tab.pack(fill='both', expand=True)
    paned_window.add(tab, weight=1)

    # Create Text widget for displaying request details
    text = tk.Text(tab, wrap='word', width=80, height=20)
    text.grid(row=0, column=0, sticky='nsew')

    # Create a Scrollbar
    scrollbar = ttk.Scrollbar(tab, command=text.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # Configure the Text widget to work with the Scrollbar
    text['yscrollcommand'] = scrollbar.set

    # Configure grid weights
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    # Add a Text field for user input in the second row
    search_entry = tk.Entry(tab, width=60)
    search_entry.grid(row=1, column=0, sticky='nsew')

    # Add placeholder text to the entry field
    search_entry.insert(0, 'Enter text to search')

    # Bind focus events to handle placeholder text behavior
    search_entry.bind('<FocusIn>', lambda event: on_entry_click(event, search_entry, tk))
    search_entry.bind('<FocusOut>', lambda event: on_focus_out(event, search_entry))

    # Create a Search button
    search_button = ttk.Button(tab, width=3, text='Go', command=lambda: search_text(search_entry, text, tk))
    search_button.grid(row=1, column=1)

    # Configure grid weights for the second row
    tab.grid_rowconfigure(1, weight=0)  # Allow the first row to expand
    tab.grid_columnconfigure(0, weight=1)  # Allow the text entry to expand

    # Bind keyboard events to notebook
    text.bind("<KeyPress>", lambda event: ignore_keyboard(event, text, root, tk))
    text.bind("<Button-3>", lambda event: show_context_menu_notebook(event, text, root, tk))

    return text, search_entry
