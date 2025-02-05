from typing import List
import customtkinter as ctk
from math import ceil

LED_ENCRYPTION_MULT_LIST = ["r", "g", "b", "y", "p", "o"]

PASSWORDS = ["about", "after", "again", "below", "could",
"every", "first", "found", "great", "house",
"large", "learn", "never", "other", "place",
"plant", "point", "right", "small", "sound",
"spell", "still", "study", "their", "there",
"these", "thing", "think", "three", "water",
"where", "which", "world", "would", "write"]

BUTTON_GRID_COLUMNS = 8
FONT="FangSong"

# Define color scheme
BACKGROUND_COLOR = "#56554e"
BUTTON_COLOR = "#bcb8b1"
RED_COLOR = "#bf534c"
BLUE_COLOR = "#455773"
WHITE_COLOR = "#fff5e3"
YELLOW_COLOR = "#f8c42c"
BLACK_COLOR = "#16171b"
MODULE_COLOR = "#bbbdbd"
ORANGE_COLOR = "#bb421e"

# Configure customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")




def sort_grid_keys(grid):
    # Sort items by value in descending order, returning the keys
    sorted_keys = sorted(grid.keys(), key=lambda x: grid[x], reverse=True)
    return sorted_keys

class KTANE(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("KTANE Solver")
        self.serial_number: str = ""
        self.last_digit_even: bool = False
        self.last_digit_odd: bool = False
        self.serial_number_vowel: bool = False
        self.lit_indicators: List[str] = []
        self.lit_indicators_count: int = 0
        self.unlit_indicators: List[str] = []
        self.unlit_indicators_count: int = 0
        self.ports: List[str] = []
        self.port_plates: int = 0
        self.batteries: int = 0
        self.battery_holders: int = 0
        self.souvenirs: List = []

        # List of all module names
        self.modules = [
            "3D Maze", "Adjacent Letters", "Adventure Game", "Alphabet", "Astrology",
            "Battleship", "Binary LEDs", "Bitmaps", "Bitwise Operations", "Blind Alley",
            "Boolean Venn Diagram", "Broken Buttons", "Bulb", "Button", "Caesar Cipher",
            "Cheap Checkout", "Chess", "Chord Qualities", "Clock", "Color Flash",
            "Color Math", "Colored Squares", "Combination Lock", "Complicated Wires", "Complicated Buttons",
            "Connection Check", "Coordinates", "Crazy Talk", "Creation", "Cryptography",
            "Double-Oh", "Emoji Math", "English Test", "Fast Math", "Fizz Buzz",
            "Follow the Leader", "Foreign Exchange Rates", "Forget Me Not", "Friendship", "Gamepad",
            "Hexamaze", "HTTP Response", "Ice Cream", "Keypad", "Knobs",
            "Laundry", "LED Encryption", "Letter Keys", "Light Cycle", "Listening",
            "Logic", "Maze", "Memory", "Microcontrollers", "Minesweeper",
            "Modules Against Humanity", "Monsplode Fight", "Morse Code", "Morsematics", "Mouse In The Maze",
            "Murder", "Mystic Square", "Neutralization", "Number Pad", "Only Connect",
            "Orientation Cube", "Password", "Perspective Pegs", "Piano Keys", "Plumbing",
            "Point of Order", "Probing", "Resistors", "Rhythms", "Rock",
            "Round Keypad", "Rubik's Cube", "Safety Safe", "Screw", "Sea Shells",
            "Semaphore", "Shape Shift", "Silly Slots", "Simon Says", "Simon Screams",
            "Simon States", "Simple Wires", "Skewed Slots", "Souvenir", "Square Button",
            "Switches", "Symbolic Password", "Text Field", "Tic Tac Toe", "Turn the Keys",
            "Two Bits", "Vent Gas", "Web Design", "Who's on First", "Wire Placement",
            "Wire Sequences", "Word Search", "Yahtzee", "Zoo"
        ]

        # Create main frame
        self.create_gui()

    def create_gui(self):
        # Create edgework button
        edgework_btn = ctk.CTkButton(
            self,
            text="Edgework",
            font=(FONT, 20),
            height=40,
            command=self.get_edge_work
        )
        edgework_btn.grid(row=0, column=0, columnspan=BUTTON_GRID_COLUMNS, 
                         padx=10, pady=10, sticky="ew")

        # Create scrollable frame for module buttons
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=1600,
            height=600
        )
        self.scroll_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Calculate grid layout
        cols = BUTTON_GRID_COLUMNS
        rows = ceil(len(self.modules) / cols)

        # Create module buttons
        for i, module in enumerate(self.modules):
            row = i // cols
            col = i % cols
            btn = ctk.CTkButton(
                self.scroll_frame,
                text=module,
                font=(FONT, 14),
                width=190,
                height=40,
                command=lambda m=module: self.button_click(m)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def button_click(self, module_name):
        # Convert module name to command name format
        command_name = module_name.lower().replace(" ", "_")
        if hasattr(self, command_name):
            # Call the corresponding module solver
            getattr(self, command_name)()
        else:
            print(f"Module {module_name} solver not implemented yet")

    def get_edge_work(self):
        window = ctk.CTkToplevel(self)
        window.title("On the Subject of Edgework")
        window.grab_set()

        main_frame = ctk.CTkFrame(window)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create input fields
        self.entries = {}
        self.labels = {}
        self.result = {}

        def on_serial_change(*args):
            value = self.entries["serial_number"].get().strip().lower()
            self.serial_number = value
            self.result['serial_number'] = value
            
            if value:
                has_vowel = any(vowel in value.lower() for vowel in 'aeiou')
                self.serial_number_vowel = has_vowel
                self.labels["vowel"].configure(text=f"Vowel = {has_vowel}")
                
                try:
                    last_digit = int(value[-1])
                    is_even = last_digit % 2 == 0
                    self.last_digit_even = is_even
                    self.last_digit_odd = not is_even
                    self.labels["digit"].configure(text=f"Last Digit {'Even' if is_even else 'ODD'}")
                except (IndexError, ValueError):
                    self.labels["digit"].configure(text="")
            else:
                self.labels["vowel"].configure(text="")
                self.labels["digit"].configure(text="")

        def on_count_change(*args, field):
            value = self.entries[field].get().strip().lower()
            value_list = value.split()
            setattr(self, field, value_list)
            self.result[field] = value_list
            count = len(value_list)
            setattr(self, f"{field}_count", count)
            self.labels[f"{field}_count"].configure(text=f"Count = {count}")

        def on_numeric_change(*args, field):
            value = self.entries[field].get().strip()
            try:
                if not value:
                    value = '0'
                
                if not value.isdigit():
                    self.labels[f"{field}_error"].configure(text="Must be a number")
                    return
                else:
                    self.labels[f"{field}_error"].configure(text="")
                
                int_value = int(value)
                setattr(self, field, int_value)
                self.result[field] = int_value
                
            except ValueError:
                self.labels[f"{field}_error"].configure(text="Invalid number")

        # Create fields
        # Serial Number
        serial_frame = ctk.CTkFrame(main_frame)
        serial_frame.pack(fill="x", pady=5)
        
        ctk.CTkLabel(serial_frame, text="Serial:").pack(side="left", padx=5)
        self.entries["serial_number"] = ctk.CTkEntry(serial_frame)
        self.entries["serial_number"].pack(side="left", padx=5)
        self.entries["serial_number"].bind('<KeyRelease>', lambda e: on_serial_change())
        
        self.labels["vowel"] = ctk.CTkLabel(serial_frame, text="")
        self.labels["vowel"].pack(side="left", padx=5)
        
        self.labels["digit"] = ctk.CTkLabel(serial_frame, text="")
        self.labels["digit"].pack(side="left", padx=5)

        # List fields
        list_fields = [
            ("Lit Indicators:", "lit_indicators"),
            ("Unlit Indicators:", "unlit_indicators"),
            ("Ports:", "ports")
        ]

        for label_text, field in list_fields:
            frame = ctk.CTkFrame(main_frame)
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=label_text).pack(side="left", padx=5)
            self.entries[field] = ctk.CTkEntry(frame)
            self.entries[field].pack(side="left", padx=5)
            self.entries[field].bind('<KeyRelease>', lambda e, f=field: on_count_change(field=f))
            
            self.labels[f"{field}_count"] = ctk.CTkLabel(frame, text="Count = 0")
            self.labels[f"{field}_count"].pack(side="left", padx=5)

        # Numeric fields
        numeric_fields = [
            ("Port Plates:", "port_plates"),
            ("Batteries:", "batteries"),
            ("Battery Holders:", "battery_holders")
        ]

        for label_text, field in numeric_fields:
            frame = ctk.CTkFrame(main_frame)
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=label_text).pack(side="left", padx=5)
            self.entries[field] = ctk.CTkEntry(frame)
            self.entries[field].pack(side="left", padx=5)
            self.entries[field].bind('<KeyRelease>', lambda e, f=field: on_numeric_change(field=f))
            
            self.labels[f"{field}_error"] = ctk.CTkLabel(frame, text="")
            self.labels[f"{field}_error"].pack(side="left", padx=5)

        # Set initial values if they exist
        for field in self.entries:
            if hasattr(self, field):
                value = getattr(self, field)
                if value is not None:
                    if isinstance(value, (int, float)):
                        self.entries[field].insert(0, str(value))
                    elif isinstance(value, list):
                        self.entries[field].insert(0, ' '.join(map(str, value)))
                    else:
                        self.entries[field].insert(0, str(value))

        # Close button
        ctk.CTkButton(
            window,
            text="Close",
            command=window.destroy
        ).pack(pady=10)

    def get_serial_first_and_last_digit(self):
        for c in self.serial_number:
            if c.isdigit():
                first = int(c)
                break
        for c in reversed(self.serial_number):
            if c.isdigit():
                last = int(c)
                break
                
        return first, last

    def get_serial_letters(self):
        return [c for c in self.serial_number if c.isalpha()]
  
    '''
    #def three_d_maze():

    #def adjacent_letters():

    #def adventure_game():

    #def alphabet():

    #def astrology():

    #def battleship():

    #def binary_leds():

    #def bitmaps():

    #def bitwise_operations():
    '''

    def blind_alley(self):    
        # Create new window
        window = ctk.CTkToplevel(self.root)  # Fixed: CTktoplevel -> CTkToplevel
        window.title("Blind Alley Grid")
        
        # Create main frame
        frame = ctk.CTkFrame(window)
        frame.pack(padx=20, pady=20)

        # Calculate grid values
        grid = {
            "top_left": 0,
            "top_middle": 0,
            "middle_left": 0,
            "center": 0,
            "middle_right": 0,
            "bottom_left": 0,
            "bottom_middle": 0,
            "bottom_right": 0
        }

        if "bob" in self.unlit_indicators:
            grid["top_left"] += 1
        if "car" in self.lit_indicators:
            grid["top_left"] += 1
        if "ind" in self.lit_indicators:
            grid["top_left"] += 1
        if self.battery_holders % 2 == 0:
            grid["top_left"] += 1

        if "car" in self.unlit_indicators:
            grid["top_middle"] += 1
        if "nsa" in self.unlit_indicators:
            grid["top_middle"] += 1
        if "frk" in self.lit_indicators:
            grid["top_middle"] += 1
        if "rj" in self.ports:
            grid["top_middle"] += 1

        if "frq" in self.unlit_indicators:
            grid["middle_left"] += 1
        if "ind" in self.unlit_indicators:
            grid["middle_left"] += 1
        if "trn" in self.unlit_indicators:
            grid["middle_left"] += 1
        if "dvi" in self.ports:
            grid["middle_left"] += 1

        if "sig" in self.unlit_indicators:
            grid["center"] += 1
        if "snd" in self.unlit_indicators:
            grid["center"] += 1
        if "nsa" in self.lit_indicators:
            grid["center"] += 1
        if self.batteries % 2 == 0:
            grid["center"] += 1

        if "bob" in self.lit_indicators:
            grid["middle_right"] += 1
        if "clr" in self.lit_indicators:
            grid["middle_right"] += 1
        if "ps" in self.ports:
            grid["middle_right"] += 1
        if "serial" in self.ports:
            grid["middle_right"] += 1

        if "frq" in self.lit_indicators:
            grid["bottom_left"] += 1
        if "sig" in self.lit_indicators:
            grid["bottom_left"] += 1
        if "trn" in self.lit_indicators:
            grid["bottom_left"] += 1
        for c in self.serial_number:
            if c.isdigit():
                if (ord(c) - ord('0')) % 2 == 0:  # Fixed: ord(c) - 97 -> ord(c) - ord('0')
                    grid["bottom_left"] += 1
                    break

        if "frk" in self.unlit_indicators:
            grid["bottom_middle"] += 1
        if "msa" in self.lit_indicators:
            grid["bottom_middle"] += 1
        if "parallel" in self.ports:
            grid["bottom_middle"] += 1
        if any(vowel in self.serial_number.lower() for vowel in 'aeiou'):
            grid["bottom_middle"] += 1
        
        if "clr" in self.unlit_indicators:
            grid["bottom_right"] += 1
        if "msa" in self.unlit_indicators:
            grid["bottom_right"] += 1
        if "snd" in self.lit_indicators:
            grid["bottom_right"] += 1
        if "rca" in self.ports:
            grid["bottom_right"] += 1
        
        # Find maximum value for highlighting
        max_value = max(grid.values())
        
        # Create 3x3 grid of labels
        positions = [
            ["top_left", "top_middle", ""],
            ["middle_left", "center", "middle_right"],
            ["bottom_left", "bottom_middle", "bottom_right"]
        ]
        
        for row_idx, row in enumerate(positions):
            for col_idx, pos in enumerate(row):
                if pos:  # Skip empty position
                    value = grid[pos]
                    # Create frame for border
                    cell_frame = ctk.CTkFrame(
                        frame,
                        width=60,
                        height=60,
                        border_width=2
                    )
                    cell_frame.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                    cell_frame.grid_propagate(False)  # Maintain size
                    
                    # Create label for value
                    label = ctk.CTkLabel(
                        cell_frame,
                        text=str(value),
                        font=(FONT, 20, "bold"),
                        corner_radius=2,
                        fg_color=RED_COLOR if value == max_value and value > 0 else BACKGROUND_COLOR,  
                        text_color=WHITE_COLOR,
                        width=60,
                        height=60
                    )
                    label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Add close button
        ctk.CTkButton(
            window,
            text="Close",
            command=window.destroy,
            font=(FONT, 10)
        ).pack(pady=10)
        
    
    '''
    #def boolean_venn_diagram():

    #def broken_buttons():

    #def bulb():
    '''

    def button(self):
        window = ctk.CTkToplevel(self.root)
        window.title("On the Subject of The Button")

        main_frame = ctk.CTkFrame(window)
        main_frame.pack(padx=20, pady=20)

        # Button Color Selection
        color_frame = ctk.CTkFrame(main_frame)
        ctk.CTkLabel(color_frame, text="Button Color", text_color=WHITE_COLOR, font=(FONT, 12)).pack()
        color_frame.pack(fill="x", pady=10)

        button_color = ctk.StringVar(value="b")
        colors = [
            ("Blue", "b", BLUE_COLOR, "white"),
            ("Yellow", "y", YELLOW_COLOR, "black"),
            ("Red", "r", RED_COLOR, "white"),
            ("White", "w", WHITE_COLOR, "black"),
        ]

        # Action Display
        action_label = ctk.CTkLabel(
            main_frame,
            text="",
            text_color=WHITE_COLOR,
            font=(FONT, 14, "bold")
        )
        action_label.pack(pady=10)

       
        strip_frame = ctk.CTkFrame(main_frame)
        ctk.CTkLabel(strip_frame, text="Strip Color and Release Time", text_color=WHITE_COLOR, font=(FONT, 12)).pack()
        strip_frame.pack(fill="x", pady=10)
        strip_frame.pack_forget()

        strip_colors = [
            ("4", "b", BLUE_COLOR, "white", 4),
            ("5", "y", YELLOW_COLOR, "black", 5),
            ("1", "r", RED_COLOR, "white", 1),
            ("1", "w", WHITE_COLOR, "black", 1)
        ]

        for text, value, bg_color, text_color, _ in strip_colors:
            ctk.CTkLabel(
                strip_frame,
                text=text,
                corner_radius=15,
                fg_color=bg_color,
                text_color=text_color,
                font=(FONT, 10),
                width=40
            ).pack(side="left", padx=10, pady=10)

        def check_button():
            color = button_color.get()
            text = button_text.get()

            if color == "b" and text == "abort":
                action = "Hold"
            elif self.batteries > 1 and text == "detonate":
                action = "Tap"
            elif color == "w" and "car" in self.lit_indicators:
                action = "Hold"
            elif self.batteries > 2 and "frk" in self.lit_indicators:
                action = "Tap"
            elif color == "y":
                action = "Hold"
            elif color == "r" and text == "hold":
                action = "Tap"
            else:
                action = "Hold"

            if action == "Tap":
                action_label.configure(text="Tap the button")
                strip_frame.pack_forget()
            else:
                action_label.configure(text="Hold the button")
                strip_frame.pack()

        # First set of color buttons in color_frame
        for text, value, fg_color, text_color in colors:
            ctk.CTkRadioButton(
                color_frame,
                radiobutton_width=100,
                text="",
                variable=button_color,
                value=value,
                corner_radius=15,
                fg_color=fg_color,
                border_color=fg_color,
                command=check_button,
                font=(FONT, 10)
            ).pack(side="left", padx=10, pady=10)

        # Pack the color_frame
        color_frame.pack(fill="both", pady=10)

        # Create and pack the text frame
        text_frame = ctk.CTkFrame(main_frame)
        text_frame.pack(fill="both", pady=10)  # Make sure text_frame is packed

        # Add the "Button Text" label
        ctk.CTkLabel(text_frame, text="Button Text", text_color=WHITE_COLOR, font=(FONT, 12)).pack()

        button_text = ctk.StringVar(value="abort")
        texts = [("Abort", "abort"), ("Detonate", "detonate"), ("Hold", "hold"), ("Press", "press")]

        # Create a frame for the grid layout
        grid_frame = ctk.CTkFrame(text_frame)
        grid_frame.pack(pady=5)

        # Create labels and buttons using grid in the grid_frame
        for column, (text, value) in enumerate(texts):
            # Create and place label
            ctk.CTkLabel(
                grid_frame, 
                text=text, 
                corner_radius=15, 
                text_color=WHITE_COLOR, 
                font=(FONT, 10)
            ).grid(row=0, column=column, padx=10, pady=5)
            
            # Create and place radio button
            ctk.CTkRadioButton(
                grid_frame,
                radiobutton_width=100,
                variable=button_text,
                value=value,
                command=check_button,
                text="",
                corner_radius=15,
                fg_color='#b36a5e',
                font=(FONT, 10)
            ).grid(row=1, column=column, padx=10, pady=5)

        # Call check_button initially to set the initial state
        check_button()

    '''
    #def caesar_cipher(): ******

    #def cheap_checkout():

    #def chess():

    #def chord_qualities():

    #def clock():

    #def color_flash():

    #def color_math():

    #def colored_squares():

    #def combination_lock():   *******
    '''

    def complicated_wire_solver(self, color, light, star):
        last_digit_even = self.get_serial_first_and_last_digit()[1] % 2 == 0
        has_parallel = "parallel" in self.ports
        
        # Define rules as (light_off_nostar, light_off_star, light_on_nostar, light_on_star)
        rules = {
            "w": ("cut", "cut", "dont cut", "cut" if self.batteries > 1 else "dont cut"),
            "r": (("cut" if last_digit_even else "dont cut"), "cut", 
                "cut" if self.batteries > 1 else "dont cut", "cut" if self.batteries > 1 else "dont cut"),
            "b": (("cut" if last_digit_even else "dont cut"), "dont cut",
                    "cut" if has_parallel else "dont cut", "cut" if has_parallel else "dont cut"),
            "rb": (("cut" if last_digit_even else "dont cut"), "cut" if has_parallel else "dont cut",
                ("cut" if last_digit_even else "dont cut"), "dont cut")
        }
        
        rule_index = (0 if light == "0" else 2) + (0 if star == "1" else 1)
        print(rules[color][rule_index])

    def complicated_wires(self):
        print("On the Subject of Complicated Wires\nList the wire colors in order.")
        prompt = "Wire {} as\nColor: W, R, B, RB\nLight: 1, 0\nStar: 1, 0\n"
        
        for i in range(1, 7):
            wire = input(prompt.format(i)).split()
            self.complicated_wire_solver(wire[0].lower(), wire[1].lower(), wire[2].lower())

    '''
    #def complicated_buttons():

    #def connection_check():

    #def coordinates():

    #def crazy_talk():

    #def creation():

    #def cryptography():

    #def double_oh():

    #def emoji_math():

    #def english_test():

    #def fast_math():

    #def fizzbuzz():

    #def follow_the_leader():

    #def foreign_exchange_rates():

    #def forget_me_not():

    #def friendship():

    #def gamepad():

    #def hexamaze():

    #def http_response():

    #def ice_cream():

    #def keypad():
    '''

    def knobs(self):
        print("On the Subject of Knobs\nList the lights on the left as a string of six 1s and 0s with 1:on or 0:off")
        lights = input()
        if lights == "001111" or "101011":
            print("UP")
        if lights == "011111" or "101010":
            print("DOWN")
        if lights == "000100" or "000000":
            print("LEFT")
        if lights == "101111":
            print("RIGHT")

    def laundry(self):
        print("On the Subject of Laundry")
        print(self.batteries)
        print(self.battery_holders)
        unsolved = int(input("unsolved: "))
        solved = int(input("solved: "))
        item = (unsolved + len(self.lit_indicators) + len(self.unlit_indicators)) % 6
        material = (len(self.ports) + solved - self.battery_holders) % 6
        
        last = self.get_serial_first_and_last_digit()[1]
        try:
            color = (last + self.batteries) % 6
        except NameError:
            color = self.batteries % 6

        wash_index: int = 1
        dry_index: int = 2
        iron_index: int = 3
        special_index: int = 4 
        wash_instruction = ""
        dry_instruction = ""
        iron_instruction = ""
        special_instruction = None

        match item:
            case 0:
                item = ["Corset", "140F", "Dry Flat", "150C, 300F", "Bleach"]
            case 1:
                item = ["Shirt", "105°F", "High Heat","No steam", "No Tetrachlorethylene"]
            case 2:
                item = ["Skirt", "30°C", "Hang To Dry", "Iron", "Reduced Moisture"]
            case 3:
                item = ["Skort", "Machine Wash Gentle or Delicate", "Tumble Dry", "3 Dots", "Circle Top Left"]
            case 4:
                item = ["Shorts", "Do Not Wring", "Shade", "150°C 300°F", "Do Not Bleach"]
            case 5:
                item = ["Scarf", "95°C", "Dry", "110°C 230°F", "Do not Dry Clean"]

        match material:
            case 0:
                material = ["Polyester", "50°C", "No Heat", "150°C 300°F", "Petroleum Solvent Only"]
            case 1:
                material = ["Cotton", "95°C 200°F", "Medium Heat", "Iron", "Do Not Dry Clean"]
            case 2:
                material = ["Wool", "Dry In The Shade",	"Handwash", "200°C or 390°F", "Reduced Moisture"]
            case 3:
                material = ["Nylon", "30°C", "Drip Dry", "No Steam", "Low Heat"]
            case 4:
                material = ["Corduroy", "105°F", "Drip Dry", "110°C", "Wet Cleaning"]
            case 5:
                material = ["Leather", "Do Not Wash", "Do Not Dry", "Do Not Iron", "Any Solvent Except Tetrachlorethylene"]

        match color:
            case 0:
                color = ["Ruby Fountain", "140°F", "High Heat", "Do Not Iron", "Any Solvent"]
            case 1:
                color = ["Star Lemon Quart", "95°C or 200°F", "Dry Flat", "Iron", "Low Heat"]
            case 2:
                color = ["Sapphire Springs", "80°F", "Tumble Dry", "200°C or 390°F", "Short Cycle"]
            case 3:
                color = ["Jade Cluster", "30°C", "Do Not Tumble Dry", "300°F", "No Steam Finishing"]
            case 4:
                color = ["Clouded Pearl", "Machine Wash Permanent Press", "Low Heat", "No steam", "Low Heat"]
            case 5:
                color = ["Malinite", "60°C", "Medium Heat", "200°C or 390°F", "Non-Chlorine Bleach"]

        if self.batteries == 4 and self.battery_holders == 2 and "BOB" in self.lit_indicators:
            print("You're done!")
            return
        
        color_name: str = color[0].lower()
        material_type: str = material[0].lower()
        item_type: str = item[0].lower()

        if color_name == "clouded pearl":
            special_instruction = "Always Use non-chlorine bleach"
        if material_type == "leather" or color_name == "jade cluster":
            wash_instruction = "Wash Always 80°F"
        if item_type == "corset" or material_type == "corduroy":
            special_instruction = f"Special Always {material[special_index]}"
        if material_type == "wool" or color_name == "star lemon quart":
            dry_instruction = "Always Dry With High Heat"
        if bool(set(self.serial_number) & set(color_name)):
            special_instruction = color[special_index]

        #print(f"\nItem: {item_type.title()}\nMaterial: {material_type.title()}\nColor: {color_name.title()}")

        if "always" not in str(wash_instruction).lower():
            wash_instruction = material[wash_index]
        if "always" not in str(dry_instruction).lower():
            dry_instruction = color[dry_index]
        if "always" not in str(iron_instruction).lower():
            iron_instruction = item[iron_index]
        if "always" not in str(special_instruction).lower() and special_instruction is None:
            special_instruction = item[special_index]

        print(f"\nWash: {wash_instruction.title()}\nDry: {dry_instruction.title()}\nIron: {iron_instruction.title()}\nSpecial: {special_instruction.title()}")

    @staticmethod 
    def led_encryption():
        print("On the Subject of LED Encryption")
        leds = input("LEDs (abbrev.): ").split()
        
        for stage in range(len(leds) - 1):
            multiplier = LED_ENCRYPTION_MULT_LIST.index(leds[stage]) + 2

            letters = input("Letters (in English reading order): ").split()
            tl, tr, bl, br = map(lambda x: ord(x) - 97, letters)
            
            pairs = [
                (tl, br),
                (tr, bl),
                (bl, tr),
                (br, tl)
            ]
            
            for first, second in pairs:
                if first == (second * multiplier) % 26:
                    result = chr(second + 97)
                    break
                else:
                    print("No solution was found, try again.")
            
            print(f"Answer: {result.upper()}")

    '''
    #def letter_keys():

    #def light_cycle():

    #def listening():

    #def logic():               ******

    #def maze():

    '''

    def memory(self):
        print("On the Subject of Memory\n")
        
        # Initialize storage for positions and numbers for each stage
        stage_pos = [""] * 5
        stage_num = [""] * 5
        
        # Process each stage
        for stage in range(5):
            print(f"\nStage {stage + 1}:")
            
            while True:
                try:
                    display = int(input("Display: "))
                    if 1 <= display <= 4:
                        break
                    print("Please enter a number between 1 and 4")
                except RuntimeError:
                    return
                except ValueError:
                    print("Please enter a valid number")
            
            if stage == 0:  # Stage 1
                match display:
                    case 1: print("Press position 2")
                    case 2: print("Press position 2")
                    case 3: print("Press position 3")
                    case 4: print("Press position 4")
            
            elif stage == 1:  # Stage 2
                match display:
                    case 1: print("Press button labeled 4")
                    case 2: print(f"Press position {stage_pos[0]}")
                    case 3: print("Press position 1")
                    case 4: print(f"Press position {stage_pos[0]}")
            
            elif stage == 2:  # Stage 3
                match display:
                    case 1: print(f"Press button labeled {stage_num[1]}")
                    case 2: print(f"Press button labeled {stage_num[0]}")
                    case 3: print("Press position 3")
                    case 4: print("Press button labeled 4")
            
            elif stage == 3:  # Stage 4
                match display:
                    case 1: print(f"Press position {stage_pos[0]}")
                    case 2: print("Press position 1")
                    case 3: print(f"Press position {stage_pos[1]}")
                    case 4: print(f"Press position {stage_pos[1]}")
            
            elif stage == 4:  # Stage 5
                match display:
                    case 1: print(f"Press button labeled {stage_num[0]}")
                    case 2: print(f"Press button labeled {stage_num[1]}")
                    case 3: print(f"Press button labeled {stage_num[3]}")
                    case 4: print(f"Press button labeled {stage_num[2]}")

            while True:
                try:
                    pos = int(input("Position pressed (1-4): "))
                    num = int(input("Number in that position (1-4): "))
                    if 1 <= pos <= 4 and 1 <= num <= 4:
                        stage_pos[stage] = pos
                        stage_num[stage] = num
                        break
                    print("Position and number must be between 1 and 4")
                except ValueError:
                    print("Please enter valid numbers")

        print("\nStages summary:")
        for i in range(5):
            print(f"Stage {i + 1}: Position {stage_pos[i]}, Number {stage_num[i]}")

    '''
    #def microcontrollers():

    #def minesweeper():

    #def modules_against_humanity():

    #def monsplode_fight():

    #def morse_code():

    #def morsematics():

    #def mouse_in_the_maze():

    #def murder():              *******

    #def mystic_square():

    #def neutralization():

    #def number_pad():

    #def only_connect():

    #def orientation_cube():
    '''


    def password(self):
        window = ctk.CTkToplevel(self.root)
        window.title("On the Subject of Passwords")

        main_frame = ctk.CTkFrame(window)
        main_frame.pack(padx=20, pady=20)

        # Initialize slot lists
        self.slot_1 = []
        self.slot_2 = []
        self.slot_3 = []
        self.slot_4 = []
        self.slot_5 = []
        
        # Dictionary to store StringVar for each slot's letters
        self.slot_vars = {}

        # Create result label
        self.result_label = ctk.CTkLabel(main_frame, text="Possible words will appear here",
                                    fg="white", 
                                    wraplength=300, justify=ctk.CTkLEFT,
                                    font=(FONT, 10))
        self.result_label.grid(row=6, column=0, pady=10)
        
        def validate_letter(value):
            """Validate that input is a single letter"""
            return len(value) <= 1 and (value.isalpha() or value == "")

        def update_slot_list(slot_num):
            """Update the corresponding slot list with current values"""
            slot_letters = []
            for var in self.slot_vars[f"slot_{slot_num}"]:
                letter = var.get().upper()
                if letter:
                    slot_letters.append(letter)
            
            # Update the corresponding slot list
            slot_list = getattr(self, f"slot_{slot_num}")
            slot_list.clear()
            slot_list.extend(slot_letters)
            
            # Update possible words whenever any slot changes
            update_possible_words()

        def update_possible_words():
            """Update the display of possible words"""
            possible_words = self.solve_password()
            if possible_words:
                words_text = "Possible words:\n" + "\n".join(possible_words)
            else:
                if all(len(getattr(self, f'slot_{i}')) > 0 for i in range(1, 6)):
                    words_text = "No valid words possible with current letters"
                else:
                    words_text = "Keep entering letters..."
            self.result_label.config(text=words_text)

        def create_letter_entries(slot_num, row):
            """Create 6 entry widgets for letters in a slot"""
            frame = ctk.CTkFrame(main_frame)
            frame.grid(row=row, column=0, pady=5)
            
            # Label for the slot
            ctk.CTklabel(frame, text=f"Slot {slot_num}", fg="white").pack(side=ctk.CTkLEFT, padx=5)
            
            # Create list to store StringVars for this slot
            self.slot_vars[f"slot_{slot_num}"] = []
            
            # Create 6 entry widgets for letters
            for i in range(6):
                validate_cmd = (window.register(validate_letter), '%P')
                var = ctk.StringVar()
                # Add trace to update slot list whenever value changes
                var.trace('w', lambda *args, s=slot_num: update_slot_list(s))
                self.slot_vars[f"slot_{slot_num}"].append(var)
                
                entry = ctk.CTkEntry(frame, 
                            textvariable=var,
                            width=2,
                            validate='key',
                            validatecommand=validate_cmd,
                            justify='center')
                entry.pack(side=ctk.LEFT, padx=2)
                
                # Store entry widget in a dictionary for easy access
                entry_key = f"slot_{slot_num}_entry_{i}"
                setattr(self, entry_key, entry)
                
                # Auto-focus next entry when a letter is entered
                if i < 5:  # Within same slot
                    var.trace('w', lambda *args, curr_entry=entry, 
                            next_idx=i+1: self.auto_advance(curr_entry, frame, next_idx))
                elif slot_num < 5:  # Last entry in slot, move to next slot
                    var.trace('w', lambda *args, curr_slot=slot_num: self.advance_to_next_slot(curr_slot))

        # Create entry fields for each slot
        for i in range(5):
            create_letter_entries(i + 1, i)

        # Add a clear button
        clear_btn = ctk.CTkButton(main_frame, text="Clear", 
                            command=lambda: [var.set('') for vars in self.slot_vars.values() for var in vars],
                            fg=WHITE_COLOR, font=(FONT, 12))
        clear_btn.grid(row=5, column=0, pady=10)

    def auto_advance(self, current_entry, parent, next_idx):
        """Automatically advance to next entry when a letter is entered"""
        value = current_entry.get()
        if value and len(value) == 1:
            next_entry = parent.winfo_children()[next_idx + 1]  # +2 to skip label
            next_entry.focus()

    def advance_to_next_slot(self, current_slot):
        """Advance to the first entry of the next slot"""
        value = self.slot_vars[f"slot_{current_slot}"][-1].get()  # Get value of last entry in current slot
        if value and len(value) == 1:
            next_slot_first_entry = getattr(self, f"slot_{current_slot + 1}_entry_0")
            next_slot_first_entry.focus()

            
    def solve_password(self):
        """Find all possible valid words from the slot combinations"""
        # Use a set to automatically eliminate duplicates
        possible_words = set()
        for letter1 in self.slot_1:
            for letter2 in self.slot_2:
                for letter3 in self.slot_3:
                    for letter4 in self.slot_4:
                        for letter5 in self.slot_5:
                            word = (letter1 + letter2 + letter3 + letter4 + letter5).lower()
                            if word in PASSWORDS:
                                possible_words.add(word)
        
        # Convert back to sorted list for display
        return sorted(list(possible_words))
        


        
        

        




    '''
    #def perspective_pegs():

    #def piano_keys():

    #def plumbing():

    #def point_of_order():

    #def probing():

    #def resistors():

    #def rhythms():

    #def rock_paper_scissors_lizard_spock():

    #def round_keypad():

    #def rubiks_cube():

    #def safety_safe():

    #def screw():

    #def sea_shells():

    #def semaphore():

    #def shape_shift():
    
    #def silly_slots():
    '''

    def simon_says(self):
        print("On the Subject of Simon Says\n")
        if any(vowel in self.serial_number.lower() for vowel in 'aeiou'):
            print("RED->BLUE\nBLUE->RED\nGREEN->YELLOW\nYELLOW->GREEN")
        else:
            print("RED->BLUE\nBLUE->YELLOW\nGREEN->GREEN\nYELLOW->RED")
        
    #def simon_screams():

    #def simon_states():

    def simple_wires(self):
        print("On the Subject of Wires\nList the wire colors in order.")
        
        wires = input("Wires: ").lower().split()
        wire_count = len(wires)
        
        # Get counts and last digit only when needed
        if wire_count in (4, 5, 6):
            last = self.get_serial_first_and_last_digit()[1]
        
        # Pre-calculate common counts once
        counts = {
            'red': wires.count('red'),
            'blue': wires.count('blue'),
            'yellow': wires.count('yellow'),
            'black': wires.count('black'),
            'white': wires.count('white')
        } if wire_count > 3 else {}

        def get_last_index(color):
            """Get the position of the last occurrence of a color (1-based)"""
            return len(wires) - wires[::-1].index(color)

        match wire_count:
            case 3:
                if 'red' not in wires:
                    result = 2
                elif wires[-1] == 'white':
                    result = 3
                elif wires.count('blue') > 1:
                    result = get_last_index('blue')
                else:
                    result = 3
                    
            case 4:
                if counts['red'] > 1 and last % 2:
                    result = get_last_index('red')
                elif wires[-1] == 'yellow' and not counts['red']:
                    result = 1
                elif counts['blue'] == 1:
                    result = 1
                elif counts['yellow'] > 1:
                    result = 4
                else:
                    result = 2
                    
            case 5:
                if wires[-1] == 'black' and last % 2:
                    result = 4
                elif counts['red'] == 1 and counts['yellow'] > 1:
                    result = 1
                elif not counts['black']:
                    result = 2
                else:
                    result = 1
                    
            case 6:
                if not counts['yellow'] and last % 2:
                    result = 3
                elif counts['yellow'] == 1 and counts['white'] > 1:
                    result = 4
                elif not counts['red']:
                    result = 6
                else:
                    result = 4
            
            case _:
                result = "\nInvalid wire count"
        
        print(f"Cut wire {result}")

    #def skewed_slots():

    '''
    #def souvenir():
    #def square_button():
    #def switches():
    #def symbolic_password():
    #def text_field():
    #def tic_tac_toe():
    #def turn_the_keys():
    #def two_bits():
    #def vent_gas():
    #def web_design():
    #def whos_on_first():
    #def wire_placement():
    '''

    def wire_sequences(self):
        WIRE_ACTIONS = {
            'r': {  # red
                1: "C", 2: "B", 3: "A", 4: "A OR C", 5: "B",
                6: "A OR C", 7: "CUT", 8: "A OR B", 9: "B"
            },
            'b': {  # blue
                1: "B", 2: "A OR C", 3: "B", 4: "A", 5: "B",
                6: "B OR C", 7: "C", 8: "A OR C", 9: "A"
            },
            'k': {  # black
                1: "CUT", 2: "A OR C", 3: "B", 4: "A OR C", 5: "B",
                6: "B OR C", 7: "A OR B", 8: "C", 9: "C"
            }
        }
        
        print("On the Subject of Wire Sequences.")
        print("List the wire colors Abbr. in order.")
        print("r:red b:blue k:black 0:empty positions")
        
        # Track count of each wire color
        wire_counts = {'r': 0, 'b': 0, 'k': 0}
        
        while True:
            # Get input and break if empty
            wire_input = input().strip()
            if not wire_input:
                break
                
            # Process each wire in the sequence
            for wire in wire_input.lower().split():
                if wire in wire_counts:
                    wire_counts[wire] += 1
                    count = wire_counts[wire]
                    action = WIRE_ACTIONS[wire][count]
                    print(f"Wire {count} ({wire}): {action}")

    #def word_search():

    #def yahtzee(): 

    #def zoo():



def main():
    root = ctk.CTk()
    root.title("Keep Talking and Nobody Explodes - Module Solver")
    app = KTANE(root)
    app.pack(expand=True, fill="both", padx=10, pady=10)
    root.mainloop()

if __name__ == '__main__':
    main()