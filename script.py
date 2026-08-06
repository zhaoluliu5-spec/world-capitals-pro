import os
import random
import webbrowser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Requires Pillow for image processing

# Dataset: Cleaned 197 UN member/observer states and entities (Alphabetized)
CAPITALS_DATA = {
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Antigua and Barbuda": "Saint John's",
    "Argentina": "Buenos Aires",
    "Armenia": "Yerevan",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bhutan": "Thimphu",
    "Bolivia": "Sucre",
    "Bosnia and Herzegovina": "Sarajevo",
    "Botswana": "Gaborone",
    "Brazil": "Brasília",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cabo Verde": "Praia",
    "Cambodia": "Phnom Penh",
    "Cameroon": "Yaoundé",
    "Canada": "Ottawa",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Chile": "Santiago",
    "China": "Beijing",
    "Colombia": "Bogota",
    "Comoros": "Moroni",
    "Costa Rica": "San Jose",
    "Croatia": "Zagreb",
    "Cuba": "Havana",
    "Cyprus": "Nicosia",
    "Czechia": "Prague",
    "Democratic Republic of the Congo": "Kinshasa",
    "Denmark": "Copenhagen",
    "Djibouti": "Djibouti",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "East Timor": "Dili",
    "Ecuador": "Quito",
    "Egypt": "Cairo",
    "El Salvador": "San Salvador",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Estonia": "Tallinn",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Fiji": "Suva",
    "Finland": "Helsinki",
    "France": "Paris",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Greece": "Athens",
    "Grenada": "Saint George's",
    "Guatemala": "Guatemala City",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Guyana": "Georgetown",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Ivory Coast": "Yamoussoukro",
    "Jamaica": "Kingston",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Astana",
    "Kenya": "Nairobi",
    "Kiribati": "Tarawa",
    "Kosovo": "Pristina",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Latvia": "Riga",
    "Lebanon": "Beirut",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Malé",
    "Mali": "Bamako",
    "Malta": "Valletta",
    "Marshall Islands": "Majuro",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Mexico": "Mexico City",
    "Micronesia": "Palikir",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Mongolia": "Ulaanbaatar",
    "Montenegro": "Podgorica",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Namibia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Nicaragua": "Managua",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "North Korea": "Pyongyang",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palau": "Ngerulmud",
    "Palestine": "Jerusalem",
    "Panama": "Panama City",
    "Papua New Guinea": "Port Moresby",
    "Paraguay": "Asunción",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Qatar": "Doha",
    "Republic of the Congo": "Brazzaville",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "Rwanda": "Kigali",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Samoa": "Apia",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "São Tomé",
    "Saudi Arabia": "Riyadh",
    "Senegal": "Dakar",
    "Serbia": "Belgrade",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Solomon Islands": "Honiara",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "South Sudan": "Juba",
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sudan": "Khartoum",
    "Suriname": "Paramaribo",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Tanzania": "Dodoma",
    "Thailand": "Bangkok",
    "Togo": "Lomé",
    "Tonga": "Nukuʻalofa",
    "Trinidad and Tobago": "Port of Spain",
    "Tunisia": "Tunis",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "Tuvalu": "Funafuti",
    "Uganda": "Kampala",
    "Ukraine": "Kyiv",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent",
    "Vanuatu": "Port Vila",
    "Vatican City": "Vatican City",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare",
}

CHOICE_COLORS = ["#ff9aa2", "#fff5ba", "#baffc9", "#bae1ff"]


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("World Capitals Pro")
        self.geometry("450x680")
        self.configure(bg="#000000")

        # 1. Create Splash / Loading Screen Frame
        self.splash_frame = tk.Frame(self, bg="#000000")
        self.splash_frame.pack(fill="both", expand=True)

        tk.Label(
            self.splash_frame,
            text="🌍 WORLD CAPITALS PRO",
            font=("Helvetica", 18, "bold"),
            bg="#000000",
            fg="#deff9a"
        ).pack(pady=(220, 10))

        self.status_label = tk.Label(
            self.splash_frame,
            text="Loading assets...",
            font=("Helvetica", 10),
            bg="#000000",
            fg="#888888"
        )
        self.status_label.pack(pady=5)

        # Style Progressbar
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "Green.Horizontal.TProgressbar",
            troughcolor='#111111',
            background='#deff9a',
            thickness=6
        )

        self.progress = ttk.Progressbar(
            self.splash_frame,
            style="Green.Horizontal.TProgressbar",
            orient="horizontal",
            length=250,
            mode="determinate"
        )
        self.progress.pack(pady=15)

        # Container for main app pages (Hidden initially)
        self.container = tk.Frame(self, bg="#000000")
        self.nav_bar = tk.Frame(self, bg="#000000")

        # Start loading animation
        self.loading_step(0)

    def loading_step(self, step):
        messages = [
            "Initializing app...",
            "Loading capital database...",
            "Preparing study guide...",
            "Building interface...",
            "Ready!"
        ]

        if step <= 100:
            self.progress['value'] = step
            msg_idx = min(step // 25, len(messages) - 1)
            self.status_label.config(text=messages[msg_idx])
            # Advance progress every 25ms (~2.5 second total loading duration)
            self.after(25, self.loading_step, step + 1)
        else:
            # Loading finished: destroy splash and display main application
            self.splash_frame.destroy()
            self.launch_main_app()

    def launch_main_app(self):
        self.container.pack(side="top", fill="both", expand=True)
        self.nav_bar.pack(side="bottom", fill="x")

        for text, page in [("LEARN", LearnPage), ("QUIZ", QuizSetupPage), ("VIDEO", VideoPage)]:
            btn = tk.Label(
                self.nav_bar,
                text=text,
                font=("Helvetica", 10, "bold"),
                fg="#FFFFFF",
                bg="#000000",
                pady=15,
                cursor="hand2"
            )
            btn.pack(side="left", expand=True, fill="both")
            btn.bind("<Button-1>", lambda event, p=page: self.show_page(p))
            btn.bind("<Enter>", lambda event, b=btn: b.config(bg="#222222"))
            btn.bind("<Leave>", lambda event, b=btn: b.config(bg="#000000"))

        self.current_frame = None
        self.show_page(LearnPage)

    def show_page(self, page_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = page_class(self.container, self, *args)
        self.current_frame.pack(fill="both", expand=True)


# --- SLIDESHOW LEARN PAGE ---
class LearnPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#000000")
        self.countries = sorted(list(CAPITALS_DATA.keys()))
        self.current_index = 0

        tk.Label(self, text="Geography Study Guide", font=("Helvetica", 18, "bold"),
                 bg="#000000", fg="#FFFFFF").pack(pady=(15, 5))

        self.counter_label = tk.Label(self, text="", font=("Helvetica", 10), bg="#000000", fg="#888888")
        self.counter_label.pack(pady=(0, 10))

        self.card_frame = tk.Frame(self, bg="#111111", padx=15, pady=15)
        self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.image_label = tk.Label(self.card_frame, bg="#111111")
        self.image_label.pack(pady=10)

        self.country_label = tk.Label(self.card_frame, text="", font=("Helvetica", 18, "bold"), bg="#111111",
                                      fg="#FFFFFF")
        self.country_label.pack(pady=(10, 2))

        self.capital_label = tk.Label(self.card_frame, text="", font=("Helvetica", 14), bg="#111111", fg="#bae1ff")
        self.capital_label.pack(pady=(0, 10))

        nav_frame = tk.Frame(self, bg="#000000")
        nav_frame.pack(fill="x", padx=20, pady=15)

        prev_btn = tk.Label(nav_frame, text="◀ PREV", font=("Helvetica", 11, "bold"), bg="#222222", fg="#FFFFFF",
                            padx=20, pady=10, cursor="hand2")
        prev_btn.pack(side="left")
        prev_btn.bind("<Button-1>", lambda e: self.navigate(-1))

        next_btn = tk.Label(nav_frame, text="NEXT ▶", font=("Helvetica", 11, "bold"), bg="#222222", fg="#FFFFFF",
                            padx=20, pady=10, cursor="hand2")
        next_btn.pack(side="right")
        next_btn.bind("<Button-1>", lambda e: self.navigate(1))

        self.update_card()

    def navigate(self, direction):
        self.current_index = (self.current_index + direction) % len(self.countries)
        self.update_card()

    def update_card(self):
        country = self.countries[self.current_index]
        capital = CAPITALS_DATA[country]

        self.counter_label.config(text=f"{self.current_index + 1} / {len(self.countries)}")
        self.country_label.config(text=country)
        self.capital_label.config(text=f"Capital: {capital}")

        img_filename = f"{country}.jpg"
        if os.path.exists(img_filename):
            try:
                img = Image.open(img_filename)
                img.thumbnail((320, 220))
                self.photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.photo, text="")
            except Exception:
                self.image_label.config(image="", text="[Error Loading Image]", fg="#ff9aa2", font=("Helvetica", 11))
        else:
            self.image_label.config(image="", text=f"[{img_filename}\nNot Found]", fg="#555555",
                                    font=("Helvetica", 10, "italic"))


# --- QUIZ SETUP PAGE ---
class QuizSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#000000")
        self.controller = controller

        tk.Label(self, text="FILTER QUIZ COUNTRIES", font=("Helvetica", 16, "bold"), bg="#000000", fg="#deff9a").pack(
            pady=(15, 5))
        tk.Label(self, text="Checked countries = Already Known (Excluded)", font=("Helvetica", 10), bg="#000000",
                 fg="#888888").pack(pady=(0, 10))

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Dark.TCheckbutton", background="#000000", foreground="#FFFFFF", font=("Helvetica", 10))
        style.map("Dark.TCheckbutton", background=[('active', '#000000')], foreground=[('active', '#deff9a')])

        action_frame = tk.Frame(self, bg="#000000")
        action_frame.pack(pady=5)

        btn_all = tk.Label(action_frame, text="Check All (Exclude All)", font=("Helvetica", 9, "bold"), bg="#222222",
                           fg="#FFFFFF", padx=8, pady=4, cursor="hand2")
        btn_all.pack(side="left", padx=5)
        btn_all.bind("<Button-1>", lambda e: self.toggle_all(True))

        btn_none = tk.Label(action_frame, text="Uncheck All (Include All)", font=("Helvetica", 9, "bold"), bg="#222222",
                            fg="#FFFFFF", padx=8, pady=4, cursor="hand2")
        btn_none.pack(side="left", padx=5)
        btn_none.bind("<Button-1>", lambda e: self.toggle_all(False))

        frame = tk.Frame(self, bg="#000000")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(frame, bg="#000000", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_content = tk.Frame(canvas, bg="#000000")

        scroll_content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.checkbox_vars = {}
        for country in sorted(CAPITALS_DATA.keys()):
            var = tk.BooleanVar(value=True)
            self.checkbox_vars[country] = var
            chk = ttk.Checkbutton(scroll_content, text=country, variable=var, style="Dark.TCheckbutton")
            chk.pack(anchor="w", pady=2)

        start_btn = tk.Label(
            self,
            text="START QUIZ",
            font=("Helvetica", 12, "bold"),
            bg="#baffc9",
            fg="#000000",
            pady=12,
            cursor="hand2"
        )
        start_btn.pack(fill="x", padx=20, pady=12)
        start_btn.bind("<Button-1>", lambda e: self.start_filtered_quiz())

    def toggle_all(self, select_state):
        for var in self.checkbox_vars.values():
            var.set(select_state)

    def start_filtered_quiz(self):
        quiz_pool = [country for country, var in self.checkbox_vars.items() if not var.get()]
        if not quiz_pool:
            error_lbl = tk.Label(self, text="Please uncheck at least one country to test!",
                                 font=("Helvetica", 10, "bold"), bg="#000000", fg="#ff9aa2")
            error_lbl.pack(pady=2)
            self.after(2000, error_lbl.destroy)
            return
        self.controller.show_page(QuizPage, quiz_pool)


# --- QUIZ PAGE ---
class QuizPage(tk.Frame):
    def __init__(self, parent, controller, selected_countries=None):
        super().__init__(parent, bg="#000000")
        if selected_countries:
            self.questions_list = [(c, CAPITALS_DATA[c]) for c in selected_countries]
        else:
            self.questions_list = list(CAPITALS_DATA.items())

        random.shuffle(self.questions_list)

        self.current_index = 0
        self.score = 0
        self.wrong_answers = []
        self.is_answering = False

        tk.Label(self, text="WORLD CAPITALS QUIZ", font=("Helvetica", 16, "bold"), bg="#000000", fg="#deff9a").pack(
            pady=20)
        self.progress_label = tk.Label(self, text="", font=("Helvetica", 10), bg="#000000", fg="#888888")
        self.progress_label.pack()

        self.question_label = tk.Label(self, text="", font=("Helvetica", 16, "bold"), bg="#000000", fg="#FFFFFF",
                                       wraplength=400)
        self.question_label.pack(pady=35)

        self.feedback_label = tk.Label(self, text="", font=("Helvetica", 11, "italic"), bg="#000000")
        self.feedback_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Label(
                self,
                text="",
                font=("Helvetica", 12, "bold"),
                fg="#000000",
                bg=CHOICE_COLORS[i],
                width=24,
                pady=12,
                cursor="hand2",
                relief="flat"
            )
            btn.pack(pady=8)
            btn.bind("<Button-1>", lambda event, idx=i: self.check_answer(idx))
            self.option_buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.current_index >= len(self.questions_list):
            self.show_results()
            return

        self.is_answering = False
        self.feedback_label.config(text="")
        self.progress_label.config(text=f"PROGRESS: {self.current_index + 1} / {len(self.questions_list)}")

        self.current_country, self.correct_capital = self.questions_list[self.current_index]
        self.question_label.config(text=f"What is the capital of\n{self.current_country}?")

        all_capitals = list(CAPITALS_DATA.values())
        wrong_capitals = [cap for cap in all_capitals if cap != self.correct_capital]
        self.options = random.sample(wrong_capitals, 3) + [self.correct_capital]
        random.shuffle(self.options)

        for i in range(4):
            self.option_buttons[i].config(text=self.options[i], bg=CHOICE_COLORS[i])

    def check_answer(self, button_index):
        if self.is_answering:
            return

        self.is_answering = True
        selected = self.options[button_index]

        if selected == self.correct_capital:
            self.score += 1
            self.feedback_label.config(text="✔ CORRECT!", fg="#baffc9")
        else:
            self.wrong_answers.append({
                "country": self.current_country,
                "user_answer": selected,
                "correct": self.correct_capital
            })
            self.feedback_label.config(
                text=f"✘ INCORRECT!\nCorrect Answer: {self.correct_capital}",
                fg="#ff9aa2"
            )

        self.current_index += 1
        self.after(1200, self.load_question)

    def show_results(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="TEST COMPLETE", font=("Helvetica", 22, "bold"), bg="#000000", fg="#FFFFFF").pack(pady=20)
        tk.Label(self, text=f"FINAL SCORE: {self.score} / {len(self.questions_list)}",
                 font=("Helvetica", 14, "bold"), bg="#000000", fg="#deff9a").pack(pady=5)

        if self.wrong_answers:
            tk.Label(self, text=f"Review Missed ({len(self.wrong_answers)} Total):", font=("Helvetica", 11, "bold"),
                     bg="#000000", fg="#ff9aa2").pack(pady=10)

            frame = tk.Frame(self, bg="#000000")
            frame.pack(fill="both", expand=True, padx=20, pady=5)

            canvas = tk.Canvas(frame, bg="#000000", highlightthickness=0)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scroll_content = tk.Frame(canvas, bg="#000000")

            scroll_content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scroll_content, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for item in self.wrong_answers:
                item_frame = tk.Frame(scroll_content, bg="#111111", padx=10, pady=6)
                item_frame.pack(fill="x", pady=4)

                tk.Label(item_frame, text=f"• {item['country']}", font=("Helvetica", 11, "bold"), bg="#111111",
                         fg="#FFFFFF", anchor="w").pack(fill="x")
                tk.Label(item_frame, text=f"   Your Answer: {item['user_answer']}", font=("Helvetica", 10),
                         bg="#111111", fg="#ff9aa2", anchor="w").pack(fill="x")
                tk.Label(item_frame, text=f"   Correct Answer: {item['correct']}", font=("Helvetica", 10), bg="#111111",
                         fg="#baffc9", anchor="w").pack(fill="x")


# --- VIDEO PAGE ---
class VideoPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#000000")
        self.youtube_url = "https://www.youtube.com/watch?v=LUMDx4embmg"

        tk.Label(self, text="Multimedia Learning", font=("Helvetica", 20, "bold"), bg="#000000", fg="#FFFFFF").pack(
            pady=50)
        tk.Label(self, text="Watch the official mnemonic guide to memorize\nall 197 world capitals efficiently.",
                 font=("Helvetica", 11), bg="#000000", fg="#888888", justify="center").pack(pady=10)

        watch_btn = tk.Label(
            self,
            text="▶ WATCH LESSON",
            font=("Helvetica", 13, "bold"),
            bg="#000000",
            fg="#FFFFFF",
            padx=25,
            pady=15,
            relief="solid",
            bd=1,
            cursor="hand2"
        )
        watch_btn.pack(pady=50)

        watch_btn.bind("<Button-1>", lambda e: webbrowser.open(self.youtube_url))
        watch_btn.bind("<Enter>", lambda e: watch_btn.config(bg="#222222"))
        watch_btn.bind("<Leave>", lambda e: watch_btn.config(bg="#000000"))


if __name__ == "__main__":
    MainApp().mainloop()