# Import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle 
from tkinter.simpledialog import askstring
from tkinter import messagebox

# Create a Pandas DataFrame to store the data
df = pd.DataFrame()



# Define dictionaries and lists for sorting and managing data
sort_order = {}
columns = ['Index', 'Request Time', 'Selected', 'Payload', 'Method', 'URL',
           'Request Headers', 'Request Body', 'Response Time', 'Cycle Time MilliSeconds',
           'Response Status Code', 'Response Reason', 'Response Headers', 'Response Body', 'Web Page Before', 'Web Page After']

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
            sort_order = {}
            # Display the data in the Treeview widget
            display_data(df)
        #df2 = df
    except pd.errors.EmptyDataError:
        # Handle empty file error
        messagebox.showerror("Error", "The selected file is empty.")
    except pd.errors.ParserError:
        # Handle parsing error
        messagebox.showerror("Error", "Error parsing the CSV file.")

# Function to display data in the Treeview widget
def display_data(dataframe):
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())
    # Insert data from the DataFrame into the Treeview
    for index, row in dataframe.iterrows():
        item_id = str(index)
        values = [index] + [row[col] for col in columns[1:] if col in row.index]
        tree.insert("", "end", iid=item_id, values=values)

# Function to search for text in specific columns and display the results
def search_data(search_text):
    global df
    if not search_text:
        # If search text is empty, display all data
        display_data(df)
        return

    # Define columns to search for text
    search_columns = ['Web Page Before', 'Web Page After', 'Request Headers', 'Response Headers', 'Response Body']
    # Create a new DataFrame to store the filtered results
    filtered_df = pd.DataFrame(columns=df.columns)

    # Iterate over search columns and filter the DataFrame
    for col in search_columns:
        condition = df[col].str.contains(search_text, case=False, na=False)
        filtered_df = pd.concat([filtered_df, df[condition]])

    # Remove duplicate rows from the filtered DataFrame
    filtered_df = filtered_df.drop_duplicates()
    # Display the filtered data in the Treeview
    display_data(filtered_df)

# Function to handle the click event of the search button
def search_button_click():
    # Prompt the user to enter search text
    search_text = askstring("Search", "Enter search text:")
    if search_text is not None:
        # Perform the search and display the results
        search_data(search_text)

# Function to clear the search results and display all data
def clear_search():
    display_data(df)


# Function to sort the Treeview based on the selected column
def sort_treeview(column):
    global sort_order

    # Determine the sorting order for the column
    if column not in sort_order:
        sort_order[column] = 'asc'
    elif sort_order[column] == 'asc':
        sort_order[column] = 'desc'
    else:
        sort_order.pop(column)

    # Sort the DataFrame based on the selected column and order
    df.sort_values(by=column, inplace=True, ascending=(sort_order.get(column) == 'asc'))
    # Display the sorted data in the Treeview
    display_data(df)

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
                full_request = f"{method} {url}\n{request_headers}\n{request_body}"
                full_response = f"HTTP/1.1 {response_status} {response_reason}\n{response_headers}\n{response_body}"

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

# Create search menu
search_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Search", command=search_button_click)
search_menu.add_command(label="Clear", command=clear_search)

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

# Configure column weights for the Treeview frame
for i in range(len(columns)):
    frame_tree_notebook.columnconfigure(i, weight=1)

frame_tree_notebook.columnconfigure(0, weight=1)
frame_tree_notebook.rowconfigure(0, weight=1)

# Start the Tkinter main loop
root.mainloop()
