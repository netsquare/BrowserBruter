import sys
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
from tkinter.simpledialog import askstring
from tkinter import messagebox

# Get Greppable values from user
greppables = []
if len(sys.argv) > 1:
    greppables = sys.argv[1].split(',')

# Create a Pandas DataFrame to store the data
df = pd.DataFrame()

# Define dictionaries and lists for sorting and managing data
sort_order = {}
columns = ['Index', 'Request Time', 'Fuzzing', 'Payload', 'Method', 'URL',
           'Request Headers', 'Request Body', 'Response Time', 'Cycle Time MilliSeconds',
           'Response Status Code', 'Response Reason', 'Response Headers', 'Response Body', 'Response Length', 'Web Page Before', 'Web Page After']

# Append greppable columns
for greppable in greppables:
    columns.append(greppable)

# Function to load a CSV file and display its data
def load_csv():
    global df, sort_order
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    try:
        # If a file is selected, read it into a Pandas DataFrame
        if file_path:
            df = pd.read_csv(file_path)
            # Set the 'Index' column as the DataFrame index
            df.set_index('Index', inplace=True)

            # Check if 'Index' column is empty
            if df.index.isnull().all():
                # Fill 'Index' column with sequential numbers starting from 0
                df['Index'] = range(len(df))

            # Replace incorrect or null values with "N/A"
            df.fillna("N/A", inplace=True)

            sort_order = {}
            if greppables:
                grep_strings(greppables)
            else:
                # Display the data in the Treeview widget
                display_data(df)

    except pd.errors.EmptyDataError:
        # Handle empty file error
        messagebox.showerror("Error", "The selected file is empty.")
    except pd.errors.ParserError:
        # Handle parsing error
        messagebox.showerror("Error", "Error parsing the CSV file.")

# Function to display data in the Treeview widget
def display_data(dataframe):
    # Check if 'Index' column is present in the DataFrame
    if 'Index' not in dataframe.columns:
        # If 'Index' column is missing, reset the index
        dataframe.reset_index(drop=False, inplace=True)
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())
    # Get the sorted index of the DataFrame
    sorted_index = dataframe.index.tolist()
    # Insert data from the DataFrame into the Treeview using the sorted index
    for index in sorted_index:
        item_id = str(index)
        values = [dataframe.at[index, col] for col in columns]
        tree.insert("", "end", iid=item_id, values=values)

# If user has entered the greppable values, count the occurences of those strings in data and display the occurrence coun
def grep_strings(greppables):
    global df

    if not greppables:
        return

    # Define columns to filter for text
    filter_columns = ['Web Page Before', 'Web Page After', 'Request Body', 'Request Headers', 'Response Headers', 'Response Body']

    # Add greppable columns at the last position in the DataFrame and UI
    for greppable in greppables:
        df = df.assign(col_name=greppable)
        df[greppable] = 0

    # Iterate over each greppable string
    for greppable in greppables:
        greppable_lower = greppable.lower()  # Convert greppable string to lowercase
        # Iterate over each row
        for index, row in df.iterrows():
            # Convert content to lowercase before counting
            count = sum([str(row[col]).lower().count(greppable_lower) for col in filter_columns])
            # Update the value in the greppable column for the current row
            df.at[index, greppable] = count

    # Update the display after processing all greppable strings
    display_data(df)

# Function to filter for text in specific columns and display the results
def filter_data(filter_text):
    global df
    if not filter_text:
        # If filter text is empty, display all data
        display_data(df)
        return

    # Define columns to filter for text
    filter_columns = ['URL','Web Page Before', 'Web Page After', 'Request Body', 'Request Headers', 'Response Headers', 'Response Body']
    # Create a new DataFrame to store the filtered results
    filtered_df = pd.DataFrame(columns=df.columns)

    # Iterate over filter columns and filter the DataFrame
    for col in filter_columns:
        condition = df[col].str.contains(filter_text, case=False, na=False)
        filtered_df = pd.concat([filtered_df, df[condition]])

    # Remove duplicate rows from the filtered DataFrame
    filtered_df = filtered_df.drop_duplicates()
    # Display the filtered data in the Treeview
    display_data(filtered_df)

# Function to handle the click event of the filter button
def filter_button_click():
    # Prompt the user to enter filter text
    filter_text = askstring("filter", "Enter filter text:")
    if filter_text is not None:
        # Perform the filter and display the results
        filter_data(filter_text)

# Function to clear the filter results and display all data
def clear_filter():
    display_data(df)

# Function to sort the Treeview based on the selected column
def sort_treeview(column):
    try:
        global sort_order, df

        # Determine the sorting order for the column
        if column not in sort_order:
            sort_order[column] = 'asc'
        elif sort_order[column] == 'asc':
            sort_order[column] = 'desc'
        else:
            sort_order.pop(column)

        # Sort the DataFrame based on the selected column and order
        df = df.sort_values(by=column, ascending=(sort_order[column] == 'asc')).reset_index(drop=True)
        # Display the sorted data in the Treeview
        display_data(df)
    except KeyError:
        pass

# Function to copy payload from selected row
def copy_payload():
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)
        payload = df.at[index, 'Payload']
        root.clipboard_clear()
        root.clipboard_append(payload)

# Function to copy whole selected row
def copy_row():
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)
        # Exclude 'Index' column when copying the row
        row_data = [f"\n\n[+]-------------------------------------------[+]\n{col}\n[+]-------------------------------------------[+]\n\n{df.at[index, col]}" for col in columns[1:]]
        row_string = "\n".join(row_data)
        root.clipboard_clear()
        root.clipboard_append(row_string)

# Function to show context menu when user right clicks on selected row
def show_context_menu(event):
    # Get the selected item from the Treeview
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)

        # Define a context menu
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Copy Payload", command=copy_payload)
        context_menu.add_command(label="Copy Row", command=copy_row)

        # Display the context menu at the current mouse position
        context_menu.post(event.x_root, event.y_root)

        # Hide the context menu when an option is selected or the user clicks somewhere else
        def hide_menu(event):
            context_menu.unpost()
            root.unbind("<Button-1>", hide_menu)

        root.bind("<Button-1>", hide_menu)

# Function to show request/response details when a Treeview item is selected
def show_request_response(event):
    # Get the selected item from the Treeview
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)

        # Define required columns for request/response details
        required_columns = ['Method', 'URL', 'Request Headers', 'Response Status Code', 'Web Page Before', 'Web Page After', 'Response Body', 'Request Body']

        # Check if required columns are present in the DataFrame
        if all(col in df.columns for col in required_columns):
            if index in df.index:
                # Extract details from the DataFrame based on the selected index
                method = df.at[index, 'Method']
                url = df.at[index, 'URL']
                request_headers = df.at[index, 'Request Headers']
                request_body = df.at[index, 'Request Body']

                response_status = df.at[index, 'Response Status Code']
                response_reason = df.at[index, 'Response Reason']
                response_headers = df.at[index, 'Response Headers']
                response_body = df.at[index, 'Response Body']

                web_page_before = df.at[index, 'Web Page Before']
                web_page_after = df.at[index, 'Web Page After']

                # Build full request and response strings
                full_request = f"{method} {url}\n{request_headers}{request_body}"
                full_response = f"HTTP/1.1 {response_status} {response_reason}\n{response_headers}{response_body}"

                # Display request and response details in the respective Text widgets
                request_text.delete(1.0, tk.END)
                response_text.delete(1.0, tk.END)
                request_text.insert(tk.END, full_request)
                response_text.insert(tk.END, full_response)

                # Display web page before and after details in the respective Text widgets
                web_page_before_text.delete(1.0, tk.END)
                web_page_after_text.delete(1.0, tk.END)
                web_page_before_text.insert(tk.END, web_page_before)
                web_page_after_text.insert(tk.END, web_page_after)
        else:
            # Handle missing columns error
            messagebox.showerror("Error", "Required columns are missing in the DataFrame.")

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
file_menu.add_command(label="Load Report", command=load_csv)

# Create filter menu
filter_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="filter", menu=filter_menu)
filter_menu.add_command(label="filter", command=filter_button_click)
filter_menu.add_command(label="Clear", command=clear_filter)

# Create Panedwindow for Treeview and Notebook
paned_window = ttk.Panedwindow(root, orient=tk.VERTICAL)
paned_window.pack(expand=True, fill='both')

# Create frame for Treeview and Notebook
frame_tree_notebook = ttk.Frame(paned_window)
paned_window.add(frame_tree_notebook, weight=1)

# Create Treeview widget
tree = ttk.Treeview(frame_tree_notebook, columns=columns, show='headings')

# Configure Treeview columns
for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_treeview(c))
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

# Function to ignore keyboard events (used for copying text)
def ignore_keyboard(event):
    if event.keysym == 'c' and event.state == 4:
        return
    else:
        return 'break'

# Bind keyboard events to the ignore_keyboard function
request_text.bind("<KeyPress>", ignore_keyboard)
response_text.bind("<KeyPress>", ignore_keyboard)
web_page_before_text.bind("<KeyPress>", ignore_keyboard)
web_page_after_text.bind("<KeyPress>", ignore_keyboard)

# Bind Treeview click event to show_request_response function
tree.bind('<ButtonRelease-1>', show_request_response)

# Bind Treeview up and down arrow keys to show_request_response function
tree.bind('<Up>', show_request_response)
tree.bind('<Down>', show_request_response)

# Bind the right-click event to the show_request_response function
tree.bind("<Button-3>", show_context_menu)

# Configure column weights for the Treeview frame
for i in range(len(columns)):
    frame_tree_notebook.columnconfigure(i, weight=1)

frame_tree_notebook.columnconfigure(0, weight=1)
frame_tree_notebook.rowconfigure(0, weight=1)

# Start the Tkinter main loop
root.mainloop()
