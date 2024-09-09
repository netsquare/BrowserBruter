##################################################################
"""
Name  : show_context_menu.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.copy.copy_payload import copy_payload
from modules.report_explorer.copy.copy_row import copy_row

##################################################################
"""
Name          -> show_context_menu
Functionality -> Shows context menu for handling right click on row
Algorithm     ->
    1. Get the selected item
    2. Create context menu
    3. Add to commands in context menus -> 1. Copy Payload, 2. Copy Row and add respective functions
    4. Display the context menu
    5. Quick hide method to hide the this menu when user clicks somewhere else
    6. Bind the mouse button with root
Parameters    -> event, tree, tk, root
Return        -> 
"""
##################################################################

# Function to show context menu when user right clicks on selected row
def show_context_menu(event, tree, tk, root):
    # Get the selected item from the Treeview
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)

        # Define a context menu
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Copy Payload", command=lambda: copy_payload(tree, root))
        context_menu.add_command(label="Copy Row", command=lambda: copy_row(tree, root))

        # Display the context menu at the current mouse position
        context_menu.post(event.x_root, event.y_root)

        # Hide the context menu when an option is selected or the user clicks somewhere else
        def hide_menu(event):
            context_menu.unpost()
            try:
                root.unbind("<Button-1>", hide_menu)
            except TypeError:
                pass

        root.bind("<Button-1>", hide_menu)