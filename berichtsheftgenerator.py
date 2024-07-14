import random
import datetime
import subprocess

tasks = [
    "ASP.NET Programmierung",
    "HTML Programmierung",
    "ASP.NET Schnittstellenprogrammierung",
    "PHP Backend-Programmierung",
    "Code-Reviews durchführen",
    "Fehlerbehebung und Debugging",
    "Dokumentation schreiben",
    "Datenbankverwaltung",
    "Netzwerkadministration",
    "Benutzersupport",
    "Systemwartung",
    "Tests und Qualitätssicherung",
    "Entwicklung von Scripts",
    "Automatisierung von Prozessen",
    "SQL-Prozedur erstellt",
    "SQL-Abfragen erstellt",
    "PowerShell Skript erstellt"
]

def generate_random_entry(date):
    task = random.choice(tasks)
    hours = round(random.uniform(7.0, 8.0), 1)  
    return f"{date}: {task}", hours

# Liste der Berufsschultage
school_days = [
    datetime.date(2022, 9, 26), datetime.date(2022, 9, 27), datetime.date(2022, 9, 28),
    datetime.date(2022, 9, 29), datetime.date(2022, 9, 30), datetime.date(2022, 10, 2), 
    datetime.date(2022, 10, 3),
    datetime.date(2022, 10, 4), datetime.date(2022, 10, 5), datetime.date(2022, 10, 6),
    datetime.date(2022, 10, 7), datetime.date(2022, 11, 14), datetime.date(2022, 11, 15),
    datetime.date(2022, 11, 16), datetime.date(2022, 11, 17), datetime.date(2022, 11, 18),
    datetime.date(2022, 11, 20),
    datetime.date(2022, 11, 21), datetime.date(2022, 11, 22), datetime.date(2022, 11, 23),
    datetime.date(2022, 11, 24), datetime.date(2022, 11, 25),  datetime.date(2023, 1, 16),
    datetime.date(2023, 1, 17), datetime.date(2023, 1, 18), datetime.date(2023, 1, 19),
    datetime.date(2023, 1, 20),
    datetime.date(2023, 1, 22), datetime.date(2023, 1, 23), datetime.date(2023, 1, 24),
    datetime.date(2023, 1, 25), datetime.date(2023, 1, 26), datetime.date(2023, 1, 27), 
    datetime.date(2023, 1, 29),
    datetime.date(2023, 1, 30), datetime.date(2023, 1, 31), datetime.date(2023, 2, 1),
    datetime.date(2023, 2, 2), datetime.date(2023, 2, 3), datetime.date(2023, 3, 20),
    datetime.date(2023, 3, 21), datetime.date(2023, 3, 22), datetime.date(2023, 3, 23),
    datetime.date(2023, 3, 24), datetime.date(2023, 3, 27), datetime.date(2023, 3, 28),
    datetime.date(2023, 3, 29), datetime.date(2023, 3, 30), datetime.date(2023, 3, 31),
    datetime.date(2023, 5, 15), datetime.date(2023, 5, 16), datetime.date(2023, 5, 17),
    datetime.date(2023, 5, 18), datetime.date(2023, 5, 19), datetime.date(2023, 5, 22),
    datetime.date(2023, 5, 23), datetime.date(2023, 5, 24), datetime.date(2023, 5, 25),
    datetime.date(2023, 5, 26), datetime.date(2023, 6, 12), datetime.date(2023, 6, 13),
    datetime.date(2023, 6, 14), datetime.date(2023, 6, 15), datetime.date(2023, 6, 16),
    datetime.date(2023, 6, 19), datetime.date(2023, 6, 20), datetime.date(2023, 6, 21),
    datetime.date(2023, 6, 22), datetime.date(2023, 6, 23), datetime.date(2023, 6, 26),
    datetime.date(2023, 6, 27), datetime.date(2023, 6, 28), datetime.date(2023, 6, 29),
    datetime.date(2023, 6, 30), datetime.date(2023, 9, 18), datetime.date(2023, 9, 19),
    datetime.date(2023, 9, 20), datetime.date(2023, 9, 21), datetime.date(2023, 9, 22),
    datetime.date(2023, 9, 25), datetime.date(2023, 9, 26), datetime.date(2023, 9, 27),
    datetime.date(2023, 9, 28), datetime.date(2023, 9, 29), datetime.date(2023, 11, 6),
    datetime.date(2023, 11, 7), datetime.date(2023, 11, 8), datetime.date(2023, 11, 9),
    datetime.date(2023, 11, 10), datetime.date(2023, 11, 13), datetime.date(2023, 11, 14),
    datetime.date(2023, 11, 15), datetime.date(2023, 11, 16), datetime.date(2023, 11, 17)
]

holidays = [
    datetime.date(2022, 1, 1),    # Neujahrstag
    datetime.date(2022, 4, 15),   # Karfreitag
    datetime.date(2022, 4, 18),   # Ostermontag
    datetime.date(2022, 5, 1),    # Tag der Arbeit
    datetime.date(2022, 5, 26),   # Christi Himmelfahrt
    datetime.date(2022, 6, 6),    # Pfingstmontag
    datetime.date(2022, 10, 3),   # Tag der Deutschen Einheit
    datetime.date(2022, 10, 31),
    datetime.date(2022, 12, 26),
    datetime.date(2022, 12, 25),
  
    datetime.date(2023, 10, 3),   # Tag der Deutschen Einheit
    datetime.date(2023, 12, 25),  # 1. Weihnachtstag
    datetime.date(2023, 12, 26),  # 2. Weihnachtstag
    datetime.date(2024, 1, 1),    # Neujahrstag
    datetime.date(2024, 4, 19),   # Karfreitag
    datetime.date(2024, 4, 22),   # Ostermontag
    datetime.date(2024, 5, 1),    # Tag der Arbeit
    datetime.date(2024, 5, 30),   # Christi Himmelfahrt
    datetime.date(2024, 6, 10),   # Pfingstmontag
    datetime.date(2024, 10, 3)    # Tag der Deutschen Einheit
]

# Generiere Einträge für ein Jahr
def generate_yearly_report():
    start_date = datetime.date(2022, 9, 1)  
    end_date = datetime.date(2023, 9, 1)   
    delta = datetime.timedelta(days=1)
    
    report = []
    current_date = start_date
    month_entries = []  
    
    while current_date <= end_date:
        if current_date.weekday() < 5:  
            if current_date in holidays:
                month_entries.append((f"{current_date}: Feiertag", None))
            elif current_date in school_days:
                month_entries.append((f"{current_date}: Berufsschule", None))
            else:
                entry, hours = generate_random_entry(current_date)
                month_entries.append((entry, hours))
        

        if current_date.weekday() == 4 and current_date.day >= 24:

            if current_date.month != (current_date + datetime.timedelta(days=7)).month:
                month_entries.append(("SIGNATURE", None))
                report.append(month_entries)
                month_entries = []
        
        current_date += delta
    
    if month_entries:
        report.append(month_entries)
    
    return report

yearly_report = generate_yearly_report()

latex_template = r"""
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{longtable}
\usepackage{array}
\usepackage{fancyhdr}
\usepackage{lastpage}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Berichtsheft 1. Lehrjahr FiAe}
\fancyhead[R]{NAME \quad \quad Seite \thepage\ von \pageref{LastPage}}

\begin{document}
"""

latex_end = r"""
\end{document}
"""

latex_content = ""
for month_entries in yearly_report:
    month_start_date = datetime.datetime.strptime(month_entries[0][0].split(": ")[0], "%Y-%m-%d").date()
    month_end_date = month_start_date + datetime.timedelta(days=29)  
    
    period = f"{month_start_date.strftime('%d.%m.%Y')} - {month_end_date.strftime('%d.%m.%Y')}"
    
    latex_content += fr"""
\newpage
\section*{{{period}}}

\begin{{longtable}}{{|p{{0.15\textwidth}}|p{{0.55\textwidth}}|p{{0.15\textwidth}}|}}
\hline
\textbf{{Datum}} & \textbf{{Aufgabe}} & \textbf{{Arbeitszeit (Stunden)}} \\
\hline
\endfirsthead
\hline
\textbf{{Datum}} & \textbf{{Aufgabe}} & \textbf{{Arbeitszeit (Stunden)}} \\
\hline
\endhead
\hline
"""

    for entry, hours in month_entries:
        if entry == "SIGNATURE":
            latex_content += r"\multicolumn{3}{|p{0.95\textwidth}|}{\textbf{Unterschrift Azubi:} \hfill \textbf{Unterschrift Arbeitgeber:} \vspace{2cm}} \\ \hline" + "\n"
        elif "Berufsschule" in entry:
            latex_content += fr"\textbf{{{entry.split(': ')[0]}}} & \textbf{{Berufsschule}} & \\ \hline" + "\n"
        else:
            date, task = entry.split(": ")
            latex_content += fr"{date} & {task} & {hours} \\ \hline" + "\n"
    
    latex_content += r"""
\end{longtable}
"""

latex_full = latex_template + latex_content + latex_end

with open("berichtsheft_gesamt.tex", "w", encoding="utf-8") as file:
    file.write(latex_full)

subprocess.run(["pdflatex", "berichtsheft_gesamt.tex"])
subprocess.run(["pdflatex", "berichtsheft_gesamt.tex"])

print("Gesamtes Berichtsheft wurde generiert und in 'berichtsheft_gesamt.pdf' gespeichert.")
