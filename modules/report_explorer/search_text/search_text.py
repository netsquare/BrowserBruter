

# Function to search text in the request_text widget
def search_text(search_entry, text_element, tk):
    # Get the text from the entry field
    search_query = search_entry.get()

    # Remove any previous tag and search for the new text
    text_element.tag_remove('highlight', '1.0', tk.END)

    if search_query:
        start_pos = '1.0'
        while True:
            # Search for the text in the Text widget
            start_pos = text_element.search(search_query, start_pos, stopindex=tk.END, nocase=True)
            if not start_pos:
                break

            # Get the end position of the matched text
            end_pos = f"{start_pos}+{len(search_query)}c"

            # Highlight the found text
            text_element.tag_add('highlight', start_pos, end_pos)

            # Move the start position forward to avoid infinite loop
            start_pos = end_pos

        # Add a tag config to highlight the found text
        text_element.tag_config('highlight', background='yellow')
