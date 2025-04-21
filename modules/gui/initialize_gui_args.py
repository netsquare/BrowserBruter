##################################################################
"""
Name  : initialize_gui_args.py 
Date  : 1/09/2024
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing python modules and libraries
##################################################################
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk
import json

##################################################################
"""
Name          -> initialize_gui_args
Functionality -> Display GUI to get and initialize arguments and options
Algorithm     ->
    1. Create and initialize GUI
    2. Load, Save, Submit options
    3. return argparser object
Parameters    -> argparser object
Return        -> argparser object
"""
##################################################################


def initialize_gui_args(args):
    try:
        # Create the main window
        #root = ThemedTk(theme="arc")
        root = ThemedTk(theme="radiance")
        root.title("The Browser Bruter")
        root.geometry("1400x900")
        # Maximize the window
        root.attributes('-zoomed', True)

        # create menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Create file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Save/Load", menu=file_menu)
        file_menu.add_command(label="Save Configs", command=lambda: save_config())
        file_menu.add_command(label="Load Configs", command=lambda: load_config())

        # Create a canvas and a scrollbar
        canvas = tk.Canvas(root, borderwidth=10)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    
        # Create a frame to contain all the frames
        container = tk.Frame(canvas, padx=20, pady=20, bg="#f0f0f0")
        canvas.create_window((0, 0), window=container, anchor="nw")

        # Place the scrollbar and canvas in the main window
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
    
        # Configure the canvas and scrollbar
        canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=h_scrollbar.set, bg="#f0f0f0")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Create a frame for each group of arguments
        frames = {
            "Basic Arguments": tk.LabelFrame(container, text="Basic Arguments", padx=15, pady=10, bg="#f7f7f7"),
            "Attack Modes": tk.LabelFrame(container, text="Attack Modes", padx=15, pady=10, bg="#f7f7f7"),
            "Sniper and Battering Ram": tk.LabelFrame(container, text="1. Sniper and 2. Battering Ram", padx=15, pady=10, bg="#f7f7f7"),
            "PitchFork and ClusterBomb": tk.LabelFrame(container, text="3. PitchFork and 4. ClusterBomb", padx=15, pady=10, bg="#f7f7f7"),
            "Fuzzing Control": tk.LabelFrame(container, text="Fuzzing Control", padx=15, pady=10, bg="#f7f7f7"),
            "Session and Cookies": tk.LabelFrame(container, text="Session and Cookies", padx=15, pady=10, bg="#f7f7f7"),
            "Python Scripting Engine": tk.LabelFrame(container, text="Python Scripting Engine", padx=15, pady=10, bg="#f7f7f7"),
            "Automatic Navigation Handler": tk.LabelFrame(container, text="Automatic Navigation Handler", padx=15, pady=10, bg="#f7f7f7"),
            "Anti Input Validation": tk.LabelFrame(container, text="Anti Input Validation", padx=15, pady=10, bg="#f7f7f7"),
            "JavaScript Code Handler": tk.LabelFrame(container, text="JavaScript Code Handler", padx=15, pady=10, bg="#f7f7f7"),
            "Browser Control": tk.LabelFrame(container, text="Browser Control", padx=15, pady=10, bg="#f7f7f7"),
            "Reporting": tk.LabelFrame(container, text="Reporting", padx=15, pady=10, bg="#f7f7f7"),
            "Debugging": tk.LabelFrame(container, text="Debugging", padx=15, pady=10, bg="#f7f7f7"),
        }

        # Layout frames in the grid
        row = 0
        col = 0
        for frame_name, frame in frames.items():
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col > 0:
                col = 0
                row += 1

        press_enter_no_click_variable = tk.BooleanVar()
        pause_variable = tk.BooleanVar()
        interactive_variable = tk.BooleanVar()
        pause_after_submit_variable = tk.BooleanVar()
        reload_page_variable = tk.BooleanVar()
        no_reload_page_variable = tk.BooleanVar()
        force_cookie_variable = tk.BooleanVar()
        remove_session_variable = tk.BooleanVar()
        record_navigation_variable = tk.BooleanVar()
        headless_variable = tk.BooleanVar()
        no_css_variable = tk.BooleanVar()
        anti_bot_variable = tk.BooleanVar()
        no_anti_bot_variable = tk.BooleanVar()
        remove_images_variable = tk.BooleanVar()
        new_instance_variable = tk.BooleanVar()
        verbose_variable = tk.BooleanVar()
        auto_remove_javascript_validation_variable = tk.BooleanVar()
        debug_variable = tk.BooleanVar()
        force_storage_variable = tk.BooleanVar()
        force_session_storage_variable = tk.BooleanVar()
        
        target = tk.Text(frames["Basic Arguments"], font=('Hacker',14), height=2, width=120, wrap="word")
        button = tk.Text(frames["Basic Arguments"], font=('Hacker',14), height=1, width=80, wrap="word")#, textvariable=args_vars["button"])
        attack = ttk.Combobox(frames["Attack Modes"], font=('Hacker',14), values=list(['1. SNIPER','2. BATTERING RAM', '3. PITCH FORK', '4. CLUSTER BOMB']), width=20)
        #attack = ttk.Combobox(frames["Attack Modes"], font=('Hacker',14), values=list(range(1, 5)), width=5)
        elements = tk.Text(frames["Sniper and Battering Ram"], font=('Hacker',14), height=1, width=120, wrap="word")
        payloads = tk.Text(frames["Sniper and Battering Ram"], font=('Hacker',14), height=1, width=120, wrap="word")
        elements_payloads = tk.Text(frames["PitchFork and ClusterBomb"], font=('Hacker',14), height=5, width=75, wrap="word")
        fill = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=120, wrap="word")
        fill_values = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=120, wrap="word")
        buttons_to_press_before_fuzz = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=80, wrap="word")
        press_enter_no_click = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=press_enter_no_click_variable)
        delay_before = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=5, wrap="word")
        delay_after = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=5, wrap="word")
        threads = ttk.Combobox(frames["Fuzzing Control"], values=list(range(1, 21)))
        pause = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=pause_variable)
        interactive = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=interactive_variable)
        pause_after_submit = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=pause_after_submit_variable)
        reload_page = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=reload_page_variable)
        no_reload_page = ttk.Checkbutton(frames["Fuzzing Control"], text="", variable=no_reload_page_variable)
        form = tk.Text(frames["Fuzzing Control"], font=('Hacker',14), height=1, width=50, wrap="word")
        headers = tk.Text(frames["Session and Cookies"], font=('Hacker',14), height=3, width=85, wrap="word")
        cookie = tk.Text(frames["Session and Cookies"], font=('Hacker',14), height=3, width=85, wrap="word")
        add_session_storage = tk.Text(frames["Session and Cookies"], font=('Hacker',14), height=3, width=85, wrap="word")
        add_storage = tk.Text(frames["Session and Cookies"], font=('Hacker',14), height=3, width=85, wrap="word")
        force_cookie = ttk.Checkbutton(frames["Session and Cookies"], text="", variable=force_cookie_variable)
        force_session_storage = ttk.Checkbutton(frames["Session and Cookies"], text="", variable=force_session_storage_variable)
        force_storage = ttk.Checkbutton(frames["Session and Cookies"], text="", variable=force_storage_variable)
        remove_session = ttk.Checkbutton(frames["Session and Cookies"], text="", variable=remove_session_variable)
        python = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=3, width=110, wrap="word")
        python_after = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=3, width=110, wrap="word")
        python_file = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=1, width=110, wrap="word")
        python_request = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=3, width=110, wrap="word")
        python_request_file = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=1, width=110, wrap="word")
        python_response = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=3, width=110, wrap="word")
        python_response_file = tk.Text(frames["Python Scripting Engine"], font=('Hacker',14), height=1, width=110, wrap="word")
        record_navigation = ttk.Checkbutton(frames["Automatic Navigation Handler"], text="", variable=record_navigation_variable)
        load_navigation_before = tk.Text(frames["Automatic Navigation Handler"], font=('Hacker',14), height=1, width=100, wrap="word")
        load_navigation_after = tk.Text(frames["Automatic Navigation Handler"], font=('Hacker',14), height=1, width=100, wrap="word")
        auto_remove_javascript_validation = ttk.Checkbutton(frames["Anti Input Validation"], text="", variable=auto_remove_javascript_validation_variable)
        disable_events = tk.Text(frames["Anti Input Validation"], font=('Hacker',14), height=1, width=100, wrap="word")
        remove_class = tk.Text(frames["Anti Input Validation"], font=('Hacker',14), height=1, width=100, wrap="word")
        javascript  = tk.Text(frames["JavaScript Code Handler"], font=('Hacker',14), height=3, width=100, wrap="word")
        javascript_after  = tk.Text(frames["JavaScript Code Handler"], font=('Hacker',14), height=3, width=100, wrap="word")
        javascript_file  = tk.Text(frames["JavaScript Code Handler"], font=('Hacker',14), height=1, width=100, wrap="word")
        replace_code = tk.Text(frames["Anti Input Validation"], font=('Hacker',14), height=3, width=100, wrap="word")
        replace_files = tk.Text(frames["Anti Input Validation"], font=('Hacker',14), height=3, width=100, wrap="word")
        chrome_binary = tk.Text(frames["Browser Control"], font=('Hacker',14), height=3, width=100, wrap="word")
        chrome_driver = tk.Text(frames["Browser Control"], font=('Hacker',14), height=3, width=100, wrap="word")
        headless = ttk.Checkbutton(frames["Browser Control"], text="", variable=headless_variable)
        no_css = ttk.Checkbutton(frames["Browser Control"], text="", variable=no_css_variable)
        proxy = tk.Text(frames["Browser Control"], font=('Hacker',14), height=1, width=50, wrap="word")
        remove_images = ttk.Checkbutton(frames["Browser Control"], text="", variable=remove_images_variable)
        chrome_options  = tk.Text(frames["Browser Control"], font=('Hacker',14), height=1, width=80, wrap="word")
        anti_bot  = ttk.Checkbutton(frames["Browser Control"], text="", variable=anti_bot_variable)
        no_anti_bot = ttk.Checkbutton(frames["Browser Control"], text="", variable=no_anti_bot_variable)
        new_instance  = ttk.Checkbutton(frames["Browser Control"], text="", variable=new_instance_variable)
        rows_limit = tk.Text(frames["Reporting"], font=('Hacker',14), height=1, width=5, wrap="word")
        scope  = tk.Text(frames["Reporting"], font=('Hacker',14), height=1, width=80, wrap="word")
        inscope_urls  = tk.Text(frames["Reporting"], font=('Hacker',14), height=5, width=80, wrap="word")
        outofscope_urls = tk.Text(frames["Reporting"], font=('Hacker',14), height=5, width=80, wrap="word")
        verbose  = ttk.Checkbutton(frames["Debugging"], text="", variable=verbose_variable)
        debug  = ttk.Checkbutton(frames["Debugging"], text="", variable=debug_variable)

        # Define variables to store the inputs
        args_vars = {
            "target": [target, tk.StringVar()],
            "button": [button, tk.StringVar()],
            "attack": [attack, tk.StringVar()],
            "elements": [elements, tk.StringVar()],
            "payloads": [payloads, tk.StringVar()],
            "elements_payloads": [elements_payloads, tk.StringVar()],
            "fill": [fill, tk.StringVar()],
            "fill_values": [fill_values, tk.StringVar()],
            "buttons_to_press_before_fuzz": [buttons_to_press_before_fuzz, tk.StringVar()],
            "press_enter_no_click": [press_enter_no_click, press_enter_no_click_variable],
            "delay_before": [delay_before, tk.DoubleVar()],
            "delay_after": [delay_after, tk.DoubleVar()],
            "threads": [threads, tk.IntVar(value=1)],
            "pause": [pause, pause_variable],
            "interactive": [interactive, interactive_variable],
            "pause_after_submit": [pause_after_submit, pause_after_submit_variable],
            "reload_page": [reload_page, reload_page_variable],
            "no_reload_page": [no_reload_page, no_reload_page_variable],
            "form": [form, tk.StringVar()],
            "headers": [headers, tk.StringVar()],
            "cookie": [cookie, tk.StringVar()],
            "force_cookie": [force_cookie, force_cookie_variable],
            "remove_session": [remove_session, remove_session_variable],
            "add_storage": [add_storage, tk.StringVar()],
            "force_storage": [force_storage, force_storage_variable],
            "add_session_storage": [add_session_storage, tk.StringVar()],
            "force_session_storage": [force_session_storage, force_session_storage_variable],
            "python": [python, tk.StringVar()],
            "python_after": [python_after, tk.StringVar()],
            "python_file": [python_file, tk.StringVar()],
            "python_request": [python_request, tk.StringVar()],
            "python_request_file": [python_request_file, tk.StringVar()],
            "python_response": [python_response, tk.StringVar()],
            "python_response_file": [python_response_file, tk.StringVar()],
            "record_navigation": [record_navigation, record_navigation_variable],
            "load_navigation_before": [load_navigation_before, tk.StringVar()],
            "load_navigation_after": [load_navigation_after, tk.StringVar()],
            "auto_remove_javascript_validation": [auto_remove_javascript_validation, auto_remove_javascript_validation_variable],
            "disable_events": [disable_events, tk.StringVar()],
            "remove_class": [remove_class, tk.StringVar()],
            "javascript": [javascript, tk.StringVar()],
            "javascript_after": [javascript_after, tk.StringVar()],
            "javascript_file": [javascript_file, tk.StringVar()],
            "replace_code": [replace_code, tk.StringVar()],
            "replace_files": [replace_files, tk.StringVar()],
            "chrome_binary": [chrome_binary, tk.StringVar()],
            "chrome_driver": [chrome_driver, tk.StringVar()],
            "headless": [headless, headless_variable],
            "no_css": [no_css, no_css_variable],
            "proxy": [proxy, tk.StringVar()],
            "remove_images": [remove_images, remove_images_variable],
            "chrome_options": [chrome_options, tk.StringVar()],
            "anti_bot": [anti_bot, anti_bot_variable],
            "no_anti_bot": [no_anti_bot, no_anti_bot_variable],
            "new_instance": [new_instance, new_instance_variable],
            "rows_limit": [rows_limit, tk.StringVar()],
            "scope": [scope, tk.StringVar()],
            "inscope_urls": [inscope_urls, tk.StringVar()],
            "outofscope_urls": [outofscope_urls, tk.StringVar()],
            "verbose": [verbose, verbose_variable],
            "debug": [debug, debug_variable]
        }

        # Function to add widgets to a frame
        def add_widgets(frame, widgets):
            # Configure the grid for the frame
            frame.grid_columnconfigure(1, weight=1)  # Column 1 (input fields) expands to fill the frame

            for row, (label_text, widget) in enumerate(widgets):
                ttk.Label(frame, font=('Hacker',14) , text=label_text).grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
                widget.grid(row=row, column=1, sticky="w", padx=5, pady=5)

        # Add widgets to each frame
        add_widgets(frames["Basic Arguments"], [
            ("Target URL (--target):", target),
            ("Button Element(id, name, class, etc) (--button):", button),
        ])  
    
        add_widgets(frames["Attack Modes"], [
            ("Attack Mode (--attack):", attack)
        ])

        add_widgets(frames["Sniper and Battering Ram"], [
            ("Elements (id, name, class, etc)(--elements):", elements),
            ("Payload File Path (--payloads):", payloads)
        ])

        add_widgets(frames["PitchFork and ClusterBomb"], [
            ("Elements and their Payloads File Path (FIELD:/PATH/TO/FILE,textarea:payloads.txt)(--elements-payloads):", elements_payloads)
        ])
    
        add_widgets(frames["Fuzzing Control"], [
            ("Elements which are required to be filled in form(--fill):", fill),
            ("Path of JSON File containing Custom values to be fill in fields specified in (--fill) option (--fill-values):", fill_values),
            ("Buttons to Press Before Fuzz (--buttons-to-press-before-fuzz):", buttons_to_press_before_fuzz),
            ("Delay Before Fuzzing the Form(--delay-before):", delay_before),
            ("Delay After Submitting the Form(--delay-after):", delay_after),
            ("Threads (--threads):", threads),
            ("Press Enter to fuzz instead of Clicking the Form Button (--press-enter-no-click):", press_enter_no_click),
            ("Pause Browser Bruter after Opening the Browser (--pause):", pause),
            ("Interactive, Run Browser Bruter in Interactive Mode (--interactive):", interactive),
            ("Puase The Browser Bruter After Submitting the Form (--pause-after-submit):", pause_after_submit),
            ("Reload Page Before Fuzzing The Form (--reload-page):", reload_page),
            ("Prevent reload of page after fuzzing the form (--no-reload-page):", no_reload_page),
            ("Fuzz Following Form (--form):", form)
        ])
    
        add_widgets(frames["Session and Cookies"], [
            ("Headers To be added in HTTP Request (--headers):", headers),
            ("Cookie to be added in HTTP Request (--cookie):", cookie),
            ("Force Cookie specified in --cookie option at each HTTP Request (--force-cookie):", force_cookie),
            ("Remove Session and cookies set by server (useful while fuzzing authentication) (--remove-session):", remove_session),
            ("Set data in Browser's local storage with key:value pair (--add-storage):", add_storage),
            ("Prevent overriding of data set using --add-storage option (--force-storage):", force_storage),
            ("Set data in Browser's session storage with key:value pair (---session-storage):", add_session_storage),
            ("Prevent overriding of data set using --add-session-storage option (--force-session-storage):", force_session_storage)
        ])
    
        add_widgets(frames["Python Scripting Engine"], [
            ("Python Code (--python):", python),
            ("Python Code to Execute After Fuzz (--python-after):", python_after),
            ("Python Code File (--python-file):", python_file),
            ("Python HTTP Request Code (--python-request):", python_request),
            ("Python HTTP Request Code File (--python-request-file):", python_request_file),
            ("Python HTTP Response Code (--python-response):", python_response),
            ("Python HTTP Response Code File (--python-response-file):", python_response_file)
        ])

        add_widgets(frames["JavaScript Code Handler"], [
            ("JavaScript Code (--javascript):", javascript),
            ("JavaScript Code to Execute After Fuzz (--javascript-after):", javascript_after),
            ("JavaScript Code File (--javascript-file):", javascript_file)
        ])
        add_widgets(frames["Automatic Navigation Handler"], [
            ("Record Navigation (--record-navigation):", record_navigation),
            ("Load Navigation To Play Before Fuzz (--load-navigation-before):", load_navigation_before),
            ("Load Navigation To Play After Fuzz (--load-navigation-after):", load_navigation_after)
        ])
        
        add_widgets(frames["Anti Input Validation"], [
            ("Try To Auto Remove Javascript Validation (--auto-remove-javascript-validation):", auto_remove_javascript_validation),
            ("Disable Following JavaScript Events (--disable-events):", disable_events),
            ("Remove Class of Following Elements (--remove-class):", remove_class),
            ("Code To Replace:Code To Be Replaced With (--replace-code):", replace_code),
            ("File To Replace:File To Replace With (--replace-files):", replace_files),
        ])
    
        add_widgets(frames["Browser Control"], [
            ("Use this switch to provide your local/custom chrome browser's path (--chrome-binary):", chrome_binary),
            ("Use this switch to use your local/custom chromedriver's path  (--chrome-driver):", chrome_driver),
            ("Run Browser in Headless Mode (--headless):", headless),
            ("Set Proxy (--proxy):", proxy),
            ("Disable CSS of Web Pages (--no-css):", no_css),
            ("Remove Images and other Static Files like Videos (--remove-images):", remove_images),
            ("Enable All Anti Bot Defenses (--anti-bot):", anti_bot),
            ("Remove All Anti Bot Defenses (--no-anti-bot):", no_anti_bot),
            ("Open New and Fresh Browser For Each Fuzz (--new-instance):", new_instance),
            ("Provide Custom Options for Chrome Browser (--chrome-options):", chrome_options)
        ])
    
        add_widgets(frames["Reporting"], [
            ("Specify limit of rows per Final Report (This will create multiple and smaller Reports) (--rows-limit):", rows_limit),
            ("Additional Scope Domains (--scope):", scope),
            ("Specific In Scope URLs to Include in Final Report (--inscope-urls):", inscope_urls),
            ("URLs to be Excluded From Final Report (--outofscope-urls):", outofscope_urls)
        ])
    
        add_widgets(frames["Debugging"], [
            ("Enable Verbosity(Print HTTP Traffic on Console) (--verbosity):", verbose),
            ("Enable Debugging(Print Stack Traces) (--print-error):", debug)
        ])    
        # Add buttons for saving and loading configurations
        def save_config():
            #config = {key: var[0].get() for key, var in args_vars.items()}
            collected_args = {}
            for key, var in args_vars.items():
                if isinstance(var[1], tk.BooleanVar):
                    collected_args[key] = var[1].get()
                elif isinstance(var[1], tk.IntVar):
                    try:
                        #print(var)
                        collected_args[key] = int(var[0].get("1.0", "end-1c"))
                    except Exception as e:
                        try: 
                            collected_args[key] = int(var[0].get())
                        except ValueError as e:
                            collected_args[key] = 1
                        #print(e)
                    #except TypeError as e:
                        #collected_args[key] = int(var[0].get())
                        #print(e)
                elif isinstance(var[1], tk.DoubleVar):
                    try:
                        collected_args[key] = float(var[0].get("1.0", "end-1c"))
                    except ValueError as e:
                        collected_args[key] = 0.0
                elif key == "attack":
                    collected_args[key] = var[0].get()
                else:
                    collected_args[key] = var[0].get("1.0", "end-1c")

            file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if file_path:
                with open(file_path, 'w') as f:
                    json.dump(collected_args, f, indent=4)

        def load_config():
            file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if file_path:
                with open(file_path, 'r') as f:
                    config = json.load(f)
                for key, value in config.items():
                    if key in args_vars:
                        var = args_vars[key]
                        #print(var)
                        if isinstance(var[1], tk.BooleanVar):
                            var[1].set(value)
                        elif isinstance(var[1], tk.IntVar) or isinstance(var[1], tk.DoubleVar):
                            #var[0].delete("1.0", "end")  # Clear the field
                            var[0].insert("end", int(value) if isinstance(var[1], tk.IntVar) else float(value))
                        else:
                            #var[0].delete("1.0", "end")  # Clear the field
                            var[0].insert("end", value)  # Insert at the start
        def submit_args():
            #print(target.get("1.0","end-1c"))
            # Collect all inputs and update the argparse object
            #collected_args = {key: var[0].get("1.0","end-1c") if isinstance(var[1], tk.StringVar) else var[1].get() if isinstance(var[1], tk.BooleanVar) else var[0].get() for key, var in args_vars.items()}
            collected_args = {}
            for key, var in args_vars.items():
                if isinstance(var[1], tk.BooleanVar):
                    collected_args[key] = var[1].get()
                elif isinstance(var[1], tk.IntVar):
                    try:
                        collected_args[key] = int(var[0].get("1.0", "end-1c"))
                    except Exception as e:
                        try: 
                            collected_args[key] = int(var[0].get())
                        except ValueError as e:
                            pass
                        #print(e)
                elif isinstance(var[1], tk.DoubleVar):
                    try:
                        collected_args[key] = float(var[0].get("1.0", "end-1c"))
                    except ValueError as e:
                        collected_args[key] = 0.0
                elif key == "attack":
                    collected_args[key] = var[0].get()
                else:
                    collected_args[key] = var[0].get("1.0", "end-1c")
                
            # debug purpose
            #print(collected_args)

            # Update the Namespace object
            for key, value in collected_args.items():
                if value not in [None, "", 0, 0.0]:  # Also checks for empty strings and zero values
                    setattr(args, key, value)
                
            attack_mode = collected_args["attack"]
            if attack_mode == "1. SNIPER":
                setattr(args, "attack", 1)
            elif attack_mode == "2. BATTERING RAM":
                setattr(args, "attack", 2)
            elif attack_mode == "3. PITCH FORK":
                setattr(args, "attack", 3)
            else:
                setattr(args, "attack", 4)
            # Close the GUI window
            root.destroy()

        # Add a submit button
        submit_button = ttk.Button(root, text="Submit", command=submit_args)
        submit_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Update the scroll region to encompass all the frames
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        root.mainloop()
    except KeyboardInterrupt as e:
        pass
    except Exception as e:
        print(e)