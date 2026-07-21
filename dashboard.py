import customtkinter
def show_dashboard(self):
        self.clear_main()

        # configure the grid so cards can be positioned
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=2)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=3)
        self.main_frame.grid_rowconfigure(2, weight=1)

        # row 0: settings, character, stats
        settings_btn = customtkinter.CTkButton(self.main_frame, text="⚙", width=40, command=None)
        settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        character_card = customtkinter.CTkFrame(self.main_frame, corner_radius=15, width=150, height=120)
        character_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        stats_card = customtkinter.CTkFrame(self.main_frame, corner_radius=15, width=150, height=120)
        stats_card.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # row 1: calendar, map
        calendar_card = customtkinter.CTkFrame(self.main_frame, corner_radius=15, width=250, height=250)
        calendar_card.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        map_card = customtkinter.CTkFrame(self.main_frame, corner_radius=15, width=250, height=250)
        map_card.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        # row 2: bottom menu bar
        menu_bar = customtkinter.CTkFrame(self.main_frame, corner_radius=15)
        menu_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

show_dashboard(self)