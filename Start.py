from typing import List
import tkinter as tk
from math import ceil

LED_ENCRYPTION_MULT_LIST = ["r", "g", "b", "y", "p", "o"]
BUTTON_GRID_COLUMNS = 8

def sort_grid_keys(grid):
    # Sort items by value in descending order, returning the keys
    sorted_keys = sorted(grid.keys(), key=lambda x: grid[x], reverse=True)
    return sorted_keys



class KTANE(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("KTANE Modules")
        self.serial_number: str = ""
        self.lit_indicators: List[str] = []
        self.unlit_indicators: List[str] = []
        self.ports: List[str] = []
        self.port_plates: int = 0
        self.batteries: int = 0
        self.battery_holders: int = 0
        self.souvenirs: List = []
        self.root.title("KTANE Modules")
        
        # List of all module names
        self.modules = [
            "3D Maze", "Adjacent Letters", "Adventure Game", "Alphabet", "Astrology",
            "Battleship", "Binary LEDs", "Bitmaps", "Bitwise Operations", "Blind Alley",
            "Boolean Venn Diagram", "Broken Buttons", "Bulb", "Button", "Caesar Cipher",
            "Cheap Checkout", "Chess", "Chord Qualities", "Clock", "ColorFlash",
            "Color Math", "Colored Squares", "Combination Lock", "Complex Wires", "Complicated Buttons",
            "Connection Check", "Coordinates", "Crazy Talk", "Creation", "Cryptography",
            "Double-Oh", "Emoji Math", "English Test", "Fast Math", "Fizz Buzz",
            "Follow the Leader", "Foreign Exchange Rates", "Forget Me Not", "Friendship", "Gamepad",
            "Hexamaze", "HTTP Response", "Ice Cream", "Keypad", "Knobs",
            "Laundry", "LED Encryption", "Letter Keys", "Light Cycle", "Listening",
            "Logic", "Maze", "Memory", "Microcontrollers", "Minesweeper",
            "Modules Against Humanity", "Monsplode Fight", "Morse Code", "Morsematics", "Mouse In The Maze",
            "Murder", "MysticSquare", "Neutralization", "Number Pad", "Only Connect",
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
        self.frame = tk.Frame(self.root, bg= '#463f3a')
        self.frame.pack(padx = 10, pady = 10)

        # Calculate rows and columns
        self.cols = BUTTON_GRID_COLUMNS
        self.rows = 1 + (len(self.modules) // BUTTON_GRID_COLUMNS)

        # Create buttons
        edgework = tk.Button(self.frame, text="Edgework", font = ("Helvetica", 12),
                        width=100, height=4, bg= "#b36a5e",
                        command = self.get_edge_work)
        edgework.grid(columnspan = self.cols, padx=2, pady=2)

        for i, module in enumerate(self.modules):
            row = i // self.cols
            col = i % self.cols
            mods = tk.Button(self.frame, text=module, font = ("Helvetica", 8), 
                        width=15, height=2,bg = '#bcb8b1',
                        wraplength=100,
                        command=lambda m=module: self.button_click(m),
                        justify= "center")
            mods.grid(row=row + 1, column=col, padx=4, pady=4)

    def button_click(self, module_name):
        # Convert module name to command name format
        command_name = module_name.lower().replace(" ", "_")
        if hasattr(self, command_name):
            # Call the corresponding module solver
            getattr(self, command_name)()
        else:
            print(f"Module {module_name} solver not implemented yet")

    def create_widgets(self):
        # Create and pack main frame
        main_frame = tk.Frame(self.window, bg='#463f3a')
        main_frame.pack(padx=20, pady=20)
    
    def get_edge_work(self):
        print("On the Subject of Edgework")
        self.window = tk.Toplevel(self.root)
        self.window.title("Edgework Input")
        self.window.configure(bg='#463f3a')
        self.window.grab_set()

        self.result = None
        self.create_widgets()

        main_frame = tk.Frame(self.window, bg='#463f3a')
        main_frame.pack(padx=20, pady=20)

        # Create input fields
        self.entries = {}
        
        # Serial Number
        tk.Label(main_frame, text="Serial Number:", bg='#463f3a', fg='white', font=("Helvetica", 10)).grid(row=0, column=0, sticky='w', pady=5)
        self.entries['serial_number'] = tk.Entry(main_frame, font=("Helvetica", 10))
        self.entries['serial_number'].grid(row=0, column=1, padx=10, pady=5)
        
        # Indicators (with helper text)
        tk.Label(main_frame, text="Lit Indicators:", bg='#463f3a', fg='white', font=("Helvetica", 10)).grid(row=1, column=0, sticky='w', pady=5)
        self.entries['lit_indicators'] = tk.Entry(main_frame, font=("Helvetica", 10))
        self.entries['lit_indicators'].grid(row=1, column=1, padx=10, pady=5)
        tk.Label(main_frame, text="(space-separated)", bg='#463f3a', fg='white', font=("Helvetica", 8)).grid(row=1, column=2, sticky='w')
        
        tk.Label(main_frame, text="Unlit Indicators:", bg='#463f3a', fg='white', font=("Helvetica", 10)).grid(row=2, column=0, sticky='w', pady=5)
        self.entries['unlit_indicators'] = tk.Entry(main_frame, font=("Helvetica", 10))
        self.entries['unlit_indicators'].grid(row=2, column=1, padx=10, pady=5)
        tk.Label(main_frame, text="(space-separated)", bg='#463f3a', fg='white', font=("Helvetica", 8)).grid(row=2, column=2, sticky='w')
        
        # Ports
        tk.Label(main_frame, text="Ports:", bg='#463f3a', fg='white', font=("Helvetica", 10)).grid(row=3, column=0, sticky='w', pady=5)
        self.entries['ports'] = tk.Entry(main_frame, font=("Helvetica", 10))
        self.entries['ports'].grid(row=3, column=1, padx=10, pady=5)
        tk.Label(main_frame, text="(space-separated)", bg='#463f3a', fg='white', font=("Helvetica", 8)).grid(row=3, column=2, sticky='w')
        
        # Numeric inputs
        numeric_fields = [
            ("Port Plates:", "port_plates"),
            ("Batteries:", "batteries"),
            ("Battery Holders:", "battery_holders")
        ]
        
        for i, (label, field) in enumerate(numeric_fields):
            tk.Label(main_frame, text=label, bg='#463f3a', fg='white', font=("Helvetica", 10)).grid(row=i+4, column=0, sticky='w', pady=5)
            self.entries[field] = tk.Entry(main_frame, font=("Helvetica", 10), width=5)
            self.entries[field].grid(row=i+4, column=1, sticky='w', padx=10, pady=5)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#463f3a')
        button_frame.grid(row=7, column=0, columnspan=3, pady=20)
        
        tk.Button(button_frame, text="Submit", command=self.submit, bg='#b36a5e', 
                 font=("Helvetica", 10), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.window.destroy, bg='#bcb8b1',
                 font=("Helvetica", 10), width=10).pack(side=tk.LEFT, padx=5)
    
    def submit(self):
        try:
            # Validate numeric fields
            for field in ['port_plates', 'batteries', 'battery_holders']:
                value = self.entries[field].get().strip()
                if not value:
                    value = '0'
                if not value.isdigit():
                    tk.messagebox.showerror("Error", f"{field.replace('_', ' ').title()} must be a number")
                    return
            
            # Collect all values
            self.result = {
                'serial_number': self.entries['serial_number'].get().strip().lower(),
                'lit_indicators': self.entries['lit_indicators'].get().strip().lower().split(),
                'unlit_indicators': self.entries['unlit_indicators'].get().strip().lower().split(),
                'ports': self.entries['ports'].get().strip().lower().split(),
                'port_plates': int(self.entries['port_plates'].get().strip() or '0'),
                'batteries': int(self.entries['batteries'].get().strip() or '0'),
                'battery_holders': int(self.entries['battery_holders'].get().strip() or '0')
            }

            self.serial_number = self.result['serial_number']
            self.lit_indicators = self.result['lit_indicators']
            self.unlit_indicators = self.result['unlit_indicators']
            self.ports = self.result['ports']
            self.port_plates = self.result['port_plates']
            self.batteries = self.result['batteries']
            self.battery_holders = self.result['battery_holders']

            self.window.destroy()
    
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

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

    def get_lit_and_unlit_count(self, unlit_indicators, lit_indicators):
        lit_count = int
        unlit_count = int
        return lit_count, unlit_count
  
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
                if (ord(c) - 97) % 2 == 0:
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

        # find all positions with the highest value and add to a list
        print(f"Click the following positions, in order: {sort_grid_keys(grid)}")
    
    #def boolean_venn_diagram():

    #def broken_buttons():

    #def bulb():

    def button(self):
        print("On the Subject of the Button\n")
        
        button_color = input("Color Abbr.: ").lower().strip()
        button_text = input("Text: ").lower().strip()
        
        if button_color == "b" and button_text == "abort":
            action = "Hold"
        elif self.batteries > 1 and button_text == "det":
            action = "Tap"
        elif button_color == "w" and "car" in self.lit_indicators:
            action = "Hold"
        elif self.batteries > 2 and "frk" in self.lit_indicators:
            action = "Tap"
        elif button_color == "y":
            action = "Hold"
        elif button_color == "r" and button_text == "hold":
            action = "Tap"
        else:
            action = "Hold"
        
        if action == "Tap":
            print("Tap the button")
            return
        
        print("Hold the button")
        strip_color = input("Strip color: ").lower().strip()
        
        release_times = {
            "b": 4,
            "y": 5
        }
        print(f"Release on {release_times.get(strip_color, 1)}")

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

        print(f"\nItem: {item_type.title()}\nMaterial: {material_type.title()}\nColor: {color_name.title()}")

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

    #def letter_keys():

    #def light_cycle():

    #def listening():

    #def logic():               ******

    #def maze():

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

    #def password():

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
    root = tk.Tk()
    ktane = KTANE(root)
    ktane.pack(expand=True, fill='both')
    root.mainloop()
    print("Goodbye!")


if __name__ == '__main__':
    main()