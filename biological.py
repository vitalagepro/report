import os
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib.pagesizes import A4 # type: ignore
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import logging
import sys


# Configura logging
logging.basicConfig(filename=os.path.join(os.path.expanduser('~'), 'biological_age_calculator.log'),
                    level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')


# PDF Report Generation Function
def generate_pdf_report(data):
    try:
        pdf_path = os.path.join(os.path.expanduser('~'), 'Desktop', f"{data['Name']}_{data['Surname']}_Analysis_Report.pdf")
        c = canvas.Canvas(pdf_path, pagesize=A4)
        width, height = A4

        # Folder containing JPG files
        jpg_folder_path = os.path.join(desktop_path, 'REFERTO-LONGEVITY-in-corso')
        jpg_files = ["page1.jpg", "page2.jpg", "page3.jpg", "page4.jpg", "page5.jpg", "page6.jpg", "page7.jpg"]

        if not os.path.exists(jpg_folder_path):
            raise FileNotFoundError(f"Folder not found: {jpg_folder_path}")

        if not jpg_files:
            raise FileNotFoundError(f"No JPG files found in folder: {jpg_folder_path}")

        # Font settings
        c.setFont("Helvetica", 9)

        coordinates = {
            0: {  # Page 1
                'BASO %': (270, 565),
                'EOSI %': (270, 547),
                'LYMPH %': (270, 529),
                'MONO %': (270, 511),
                'NEUT %': (270, 493),
                'WBC': (270, 475),
                'NEUT': (270, 457),
                'LYMPH': (270, 438),
                'MONO': (270, 420),
                'EOSI': (270, 401),
                'BASO': (270, 381),
                 'HCT %': (270, 324),
                'HGB': (270, 305),
                'MCH': (270, 285),
                'MCHC': (270, 265),
                'MCV': (270, 245),
                'RBC': (270, 226),
                'RDW-SD': (270, 207),
                'RDW-CV': (270, 188),
                'AZOTEMIA': (270, 132),
                'CREATININA': (270, 106),
            },
            1: {  # Page 2
                'URICEMIA': (270, 678),
                'PLT': (270, 580),
                'MPV': (270, 560),
                'P-LCR': (270, 540),
                'PCT': (270, 520),
                'PDW': (270, 500),
                 'COLESTEROLO TOTALE': (270, 445),
                'COLESTEROLO LDL': (270, 425),
                'COLESTEROLO HDL': (270, 390),


                'TRIGLICERIDI': (270, 355),
                'SODIO': (270, 282),
                'POTASSIO': (270, 262),
                'MAGNESIO': (270, 243),
                'CLORURI': (270, 225),
                'CALCIO': (270, 207),
                'FOSFORO': (270, 187),
                'SIDEREMIA': (270, 122),
                'FERRITINA': (270, 95),
                'TRANSFERRINA': (270, 70),
            },
            2: {  # Page 3
                   'GLICEMIA': (270, 740),
                'INSULINA': (270, 720),
                'HOMA TEST': (270, 700),
                'IR TEST': (270, 670),
                'ALBUMINEMIA': (270, 600),
                'PROTEINE TOTALI': (270, 583),
                 'Proteine totali': (270, 555),
                'Albumina': (270, 538),
                'Alfa 1': (270, 520),
                'Alfa 2': (270, 504),
                'Beta 1': (270, 487),
                'Beta 2': (270, 471),
                'Gamma': (270, 456),
                'Albumina*': (270, 440),
                'Alfa 1*': (270, 424),
                'Alfa 2*': (270, 408),
                'Beta 1*': (270, 392),
                'Beta 2*': (270, 376),
                'Gamma*': (270, 361),
                'Rapporto A/G': (270, 347),
                'CM %*': (270, 317),
                'CM': (270, 300),
                'Beta 2 picco M 1%': (270, 284),
                'Beta 2 picco M 1': (270, 269),
                'TRANSAMINASI (GOT)': (270, 210),
                'TRANSAMINASI (GPT)': (270, 180),
                'GAMMA GT': (270, 150),
                'FOSFATASI ALCALINA': (270, 130),
                'BILIRUBINA TOTALE': (270, 96),
                'BILIRUBINA DIRETTA': (270, 81),
                'BILIRUBINA INDIRETTA': (270, 66),
            },
            3: {  # Page 4
                'VES': (270, 720),
                'PCR': (270, 700),
            },
            4: {  # Page 5
                'OMOICISTEINA': (270, 737),
                'COLORE': (270, 680),
                'ASPETTO': (270, 660),
                'PESO SPECIFICO': (270, 640),
                'PH': (270, 623),
                'GLUCOSIO': (270, 605),
                'NITRITI': (270, 585),
                'PROTEINE': (270, 567),
                'SANGUE': (270, 550),
                'CHETONI': (270, 530),
                'UROBILINOGENO': (270, 510),
                'BILIRUBINA': (270, 490),
                'LEUCOCITI': (270, 470),
            },
            5: {  # Page 6
                'D-ROMS': (270, 670),
                'PAT': (270, 580),
                'OSI': (270, 490),
                'OBRI': (270, 400),
            }
        }

        # Loop through each page and draw the corresponding image and text
        for page_index, jpg_file in enumerate(jpg_files):
            c.drawImage(os.path.join(jpg_folder_path, jpg_file), 0, 0, width=width, height=height)
            
            # Patient Information (assuming it's on the first page)
            if page_index == (0,5):
                c.drawString(500, 800, data['Name','Surname'])
                c.drawString(150, 780, data['DATA PRELIEVO'])
                c.drawString(150, 760, data['DOB'])
                c.drawString(150, 740, data['CF'])
                c.drawString(150, 740, data['BIOLOGICAL AGE'])
                c.drawString(150, 740, data['CHRONOLOGICAL AGE'])

            if page_index in coordinates:
                for key, (x, y) in coordinates[page_index].items():
                    if key in data:
                        c.drawString(x, y, str(data[key]))

            c.showPage() 

        # Save PDF
        c.save()

        messagebox.showinfo("Result", f"PDF report generated and saved to Desktop as {data['Name']}_{data['Surname']}_Analysis_Report.pdf")
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
        messagebox.showerror("Error", f"Template JPG not found: {e}")
    except Exception as e:
        logging.error(f"Error generating PDF report: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred while generating the PDF report: {e}")

# Funzioni di calcolo dell'età biologica
def adjust_age_obri(obri_index):
    if obri_index is None:
        return 0
    if 0.8 <= obri_index <= 1.2:
        return 0  # Normal value, no change
    elif 1.3 <= obri_index <= 1.7:
        return 2  # Increase by 2 years
    elif 1.8 <= obri_index <= 2.2:
        return 5  # Increase by 5 years
    elif obri_index > 2.2:
        return 10  # Increase by 10 years
    return 0

def adjust_age_d_roms(d_roms):
    if d_roms is None:
        return 0
    if 250 <= d_roms <= 300:
        return 0  # Normal, no change
    elif 301 <= d_roms <= 320:
        return 1  # Increase by 1 year (Valore soglia)
    elif 321 <= d_roms <= 340:
        return 1  # Increase by 1 year (Lieve stress)
    elif 341 <= d_roms <= 400:
        return 3  # Increase by 3 years (Discreto stress)
    elif d_roms > 400:
        return 6  # Increase by 6 years (Fortissimo stress)
    return 0

def adjust_age_aa_epa(aa_epa):
    if aa_epa is None:
        return 0
    if 1 <= aa_epa <= 3:
        return 0  # Good condition, no change
    elif 3.1 <= aa_epa <= 15:
        return 2  # Increase by 2 years (Altered condition)
    elif aa_epa > 15:
        return 4  # Increase by 4 years (Critic condition)
    return 0

def adjust_age_aa_dha(aa_dha):
    if aa_dha is None:
        return 0
    if 1.6 <= aa_dha <= 3.6:
        return 0  # Good condition, no change
    elif 3.7 <= aa_dha <= 4.3:
        return 2  # Increase by 2 years (Altered condition)
    elif aa_dha > 4.3:
        return 4  # Increase by 4 years (Critic condition)
    return 0

def adjust_age_homa(homa_test):
    if homa_test is None:
        return 0
    if 0.23 <= homa_test <= 2.5:
        return 0  # Low risk, no change
    else:
        return 5  # Increase by 5 years (High risk)
    return 0

def adjust_age_cardio(cardiovascular_risk):
    if cardiovascular_risk is None:
        return 0
    if cardiovascular_risk < 3:
        return 0  # Low risk, no change
    elif 3 <= cardiovascular_risk <= 20:
        return 2  # Increase by 2 years (Medium risk)
    else:
        return 5  # Increase by 5 years (High risk)
    return 0

def adjust_age_osi(osi):
    if osi is None:
        return 0
    if 0 <= osi <= 40:
        return 0  # Normal, no change
    elif 41 <= osi <= 65:
        return 2  # Increase by 2 years (Borderline)
    elif 66 <= osi <= 120:
        return 5  # Increase by 5 years (Dangerous)
    else:
        return 10  # Increase by 10 years (Very dangerous)
    return 0

def adjust_age_pat(pat):
    if pat is None:
        return 0
    if pat < 1800:
        return 10  # Increase by 10 years (Very lacking)
    elif 1800 <= pat < 2700:
        return 5  # Increase by 5 years (Lacking)
    elif 2700 <= pat < 2270:
        return 2  # Increase by 2 years (Borderline)
    elif 2270 <= pat < 2800:
        return 0  # Normal, no change
    else:
        return -5  # Decrease by 5 years (Very high)
    return 0

def adjust_age_exams(exams):
    normal_values = {
        'BASO %': (0, 2.5),
        'EOSI %': (0, 7),
        'LYMPH %': (15, 45),
        'MONO %': (0, 10),
        'NEUT %': (45, 70),
        'WBC': (4.0, 10.0),
        'HCT %': (38, 48),
        'HGB': (12, 16),
        'MCH': (27, 32),
        'MCHC': (32, 37),
        'MCV': (82, 98),
        'RBC': (4.0, 5.5),
        'RDW-SD': (38.0, 48.0),
        'RDW-CV': (11.0, 15.0),
        'AZOTEMIA': (16.6, 48.5),
        'CREATININA': (0.5, 0.9),
        'PLT': (150, 450),
        'MPV': (9.1, 12.3),
        'PDW': (10, 16),
        'COLESTEROLO TOTALE': (0, 200),
        'COLESTEROLO HDL': (0, 100),
        'COLESTEROLO LDL': (45, 65),
        'TRIGLICERIDI': (0, 150),
        'SODIO': (136, 145),
        'POTASSIO': (3.5, 5.1),
        'MAGNESIO': (1.6, 2.6),
        'CLORURI': (98, 107),
        'CALCIO': (8.6, 10.0),
        'FOSFORO': (0.8, 1.5),
        'SIDEREMIA': (37, 150),
        'FERRITINA': (13, 150),
        'TRANSFERRINA': (270, 360),
        'GLICEMIA': (70, 105),
        'INSULINA': (3, 16),
        'HOMA TEST': (0.23, 2.5),
        'ALBUMINEMIA': (3.50, 5.20),
        'TRANSAMINASI (GOT)': (0, 31),
        'TRANSAMINASI (GPT)': (0, 38),
        'GAMMA GT': (8, 31),
        'FOSFATASI ALCALINA': (100, 290),
        'VES': (0, 20),
        'PCR': (0, 5),
        'OMOICISTEINA': (5, 15),
        'PESO SPECIFICO': (1000, 1030),
        'PH': (5.0, 9.0),
        'GLUCOSIO': (0, 5),
        'PROTEINE': (0, 0.15),
        'SANGUE': (0, 0),
        'CHETONI': (0, 0.5),
        'BILIRUBINA': (0, 17),
        'UROBILINOGENO': (0, 17),
        'LEUCOCITI': (0, 15),
        'IR TEST': (0,1),
         'Proteine totali': (6.6, 8.7),
        'Albumina': (52.7, 67.4),
        'Alfa 1': (3.6, 8.0),
        'Alfa 2': (6.4, 11.5),
        'Beta 1': (5.2, 8.3),
        'Beta 2': (2.2, 8.0),
        'Gamma': (8.7, 18.0),
        'Albumina*': (3.48, 5.86),
        'Alfa 1*': (0.24, 0.70),
        'Alfa 2*': (0.42, 1.0),
        'Beta 1*': (0.34, 0.72),
        'Beta 2*': (0.15, 0.70),
        'Gamma*': (0.57, 1.56),
        'Rapporto A/G': (1.20, 2.06),
    }

    age_adjustment = 0
    for exam, value in exams.items():
        if value is None:
            continue
        normal_range = normal_values.get(exam)
        if normal_range and not (normal_range[0] <= value <= normal_range[1]):
            age_adjustment += 1  # Increase age by 1 year for each abnormal exam result

    return age_adjustment

# Funzione principale per calcolare l'età biologica
def calculate_biological_age(chronological_age, obri_index, d_roms, aa_epa, aa_dha, homa_test, cardiovascular_risk, osi, pat, exams):
    biological_age = chronological_age

    biological_age += adjust_age_obri(obri_index)
    biological_age += adjust_age_d_roms(d_roms)
    biological_age += adjust_age_aa_epa(aa_epa)
    biological_age += adjust_age_aa_dha(aa_dha)
    biological_age += adjust_age_homa(homa_test)
    biological_age += adjust_age_cardio(cardiovascular_risk)
    biological_age += adjust_age_osi(osi)
    biological_age += adjust_age_pat(pat)
    biological_age += adjust_age_exams(exams)

    return biological_age

# Funzione per calcolare e salvare i dati
def calculate_and_save():
    try:
        name = entry_name.get()
        surname = entry_surname.get()
        dob = entry_dob.get()
        cf = entry_cf.get()
        chronological_age = float(entry_chronological_age.get())
        obri_index = float(entry_obri_index.get()) if entry_obri_index.get() else None
        d_roms = float(entry_d_roms.get()) if entry_d_roms.get() else None
        aa_epa = float(entry_aa_epa.get()) if entry_aa_epa.get() else None
        aa_dha = float(entry_aa_dha.get()) if entry_aa_dha.get() else None
        homa_test = float(entry_homa_test.get()) if entry_homa_test.get() else None
        cardiovascular_risk = float(entry_cardiovascular_risk.get()) if entry_cardiovascular_risk.get() else None
        osi = float(entry_osi.get()) if entry_osi.get() else None
        pat = float(entry_pat.get()) if entry_pat.get() else None
        diagnosis = entry_diagnosis.get()

        exams = {exam: float(entries[exam].get()) if entries[exam].get() else None for exam in entries}

        data = {
            "Name": name,
            "Surname": surname,
            "DOB": dob,
            "CF": cf,
            "Chronological Age": chronological_age,
            "Obri Index": obri_index,
            "d-ROMs": d_roms,
            "AA/EPA": aa_epa,
            "AA/DHA": aa_dha,
            "HOMA Test": homa_test,
            "Cardiovascular Risk": cardiovascular_risk,
            "OSI": osi,
            "PAT": pat,
            "Diagnosis": diagnosis
        }
        data.update(exams)

        biological_age = calculate_biological_age(chronological_age, obri_index, d_roms, aa_epa, aa_dha, homa_test, cardiovascular_risk, osi, pat, exams)
        data["Biological Age"] = biological_age
        data["Older Than Chronological Age"] = 1 if biological_age > chronological_age else 0

        generate_pdf_report(data)

        messagebox.showinfo("Result", f"Calculated Biological Age: {biological_age:.2f} years")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        messagebox.showerror("Error", "An unexpected error occurred.")

# Funzione per cercare esami
def search_exam():
    search_term = search_entry.get().lower()
    for exam in entries:
        if search_term in exam.lower():
            entries[exam].focus_set()
            break

# Inizializza l'applicazione GUI
app = tk.Tk()
app.title("Biological Age Calculator")

# Crea una canvas e una scrollbar
canvas_widget = tk.Canvas(app)
scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas_widget.yview)
scrollable_frame = ttk.Frame(canvas_widget)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas_widget.configure(
        scrollregion=canvas_widget.bbox("all")
    )
)

canvas_widget.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas_widget.configure(yscrollcommand=scrollbar.set)

# Posiziona la scrollbar e la canvas nella finestra
scrollbar.pack(side="right", fill="y")
canvas_widget.pack(side="left", fill="both", expand=True)

# Crea barra di ricerca
tk.Label(scrollable_frame, text="Search Exam:").grid(row=0, column=0)
search_entry = tk.Entry(scrollable_frame)
search_entry.grid(row=0, column=1)
tk.Button(scrollable_frame, text="Search", command=search_exam).grid(row=0, column=2)

# Crea e posiziona i widget nel frame scrollabile
tk.Label(scrollable_frame, text="Name:").grid(row=1, column=0)
entry_name = tk.Entry(scrollable_frame)
entry_name.grid(row=1, column=1)

tk.Label(scrollable_frame, text="Surname:").grid(row=2, column=0)
entry_surname = tk.Entry(scrollable_frame)
entry_surname.grid(row=2, column=1)

tk.Label(scrollable_frame, text="DOB:").grid(row=3, column=0)
entry_dob = tk.Entry(scrollable_frame)
entry_dob.grid(row=3, column=1)

tk.Label(scrollable_frame, text="CF:").grid(row=4, column=0)
entry_cf = tk.Entry(scrollable_frame)
entry_cf.grid(row=4, column=1)

tk.Label(scrollable_frame, text="Chronological Age:").grid(row=5, column=0)
entry_chronological_age = tk.Entry(scrollable_frame)
entry_chronological_age.grid(row=5, column=1)

tk.Label(scrollable_frame, text="Obri Index:").grid(row=6, column=0)
entry_obri_index = tk.Entry(scrollable_frame)
entry_obri_index.grid(row=6, column=1)

tk.Label(scrollable_frame, text="d-ROMs:").grid(row=7, column=0)
entry_d_roms = tk.Entry(scrollable_frame)
entry_d_roms.grid(row=7, column=1)

tk.Label(scrollable_frame, text="AA/EPA:").grid(row=8, column=0)
entry_aa_epa = tk.Entry(scrollable_frame)
entry_aa_epa.grid(row=8, column=1)

tk.Label(scrollable_frame, text="AA/DHA:").grid(row=9, column=0)
entry_aa_dha = tk.Entry(scrollable_frame)
entry_aa_dha.grid(row=9, column=1)

tk.Label(scrollable_frame, text="HOMA Test:").grid(row=10, column=0)
entry_homa_test = tk.Entry(scrollable_frame)
entry_homa_test.grid(row=10, column=1)

tk.Label(scrollable_frame, text="Cardiovascular Risk:").grid(row=11, column=0)
entry_cardiovascular_risk = tk.Entry(scrollable_frame)
entry_cardiovascular_risk.grid(row=11, column=1)

tk.Label(scrollable_frame, text="OSI:").grid(row=12, column=0)
entry_osi = tk.Entry(scrollable_frame)
entry_osi.grid(row=12, column=1)

tk.Label(scrollable_frame, text="PAT:").grid(row=13, column=0)
entry_pat = tk.Entry(scrollable_frame)
entry_pat.grid(row=13, column=1)

tk.Label(scrollable_frame, text="Diagnosis:").grid(row=14, column=0)
entry_diagnosis = tk.Entry(scrollable_frame)
entry_diagnosis.grid(row=14, column=1)

# Divide gli esami in colonne per una migliore visualizzazione
exams = [
    'BASO %', 'EOSI %', 'LYMPH %', 'MONO %', 'NEUT %', 'WBC', 'NEUT', 'LYMPH', 'MONO', 'EOSI', 'BASO',
    'HCT %', 'HGB', 'MCH', 'MCHC', 'MCV', 'RBC', 'RDW-SD', 'RDW-CV', 'AZOTEMIA', 'CREATININA', 'URICEMIA',
    'PLT', 'MPV', 'P-LCR', 'PCT', 'PDW', 'COLESTEROLO TOTALE', 'COLESTEROLO HDL', 'COLESTEROLO LDL',
    'TRIGLICERIDI', 'SODIO', 'POTASSIO', 'MAGNESIO', 'CLORURI', 'CALCIO', 'FOSFORO', 'SIDEREMIA', 'FERRITINA', 'TRANSFERRINA',
    'GLICEMIA', 'INSULINA', 'HOMA TEST', 'ALBUMINEMIA', 'PROTEINE TOTALI', 'TRANSAMINASI (GOT)',
    'TRANSAMINASI (GPT)', 'GAMMA GT', 'FOSFATASI ALCALINA', 'BILIRUBINA TOTALE', 'BILIRUBINA DIRETTA', 'BILIRUBINA INDIRETTA',
    'VES', 'PCR', 'OMOICISTEINA', 'COLORE', 'ASPETTO', 'PESO SPECIFICO', 'PH', 'GLUCOSIO', 'NITRITI',
    'PROTEINE', 'SANGUE', 'CHETONI', 'UROBILINOGENO', 'BILIRUBINA', 'LEUCOCITI','Proteine totali', 'Albumina', 'Alfa 1', 'Alfa 2', 'Beta 1', 'Beta 2', 'Gamma', 'Albumina*', 'Alfa 1*',
    'Alfa 2*', 'Beta 1*', 'Beta 2*', 'Gamma*', 'Rapporto A/G', 'CM %*', 'CM', 'Beta 2 picco M 1%', 'Beta 2 picco M 1','IR TEST'
]

entries = {}
columns = 3
rows_per_column = len(exams) // columns + 1
for i, exam in enumerate(exams):
    col = i // rows_per_column
    row = i % rows_per_column + 15  # Inizia dalla riga 15
    tk.Label(scrollable_frame, text=f"{exam}:").grid(row=row, column=col*2)
    entry = tk.Entry(scrollable_frame)
    entry.grid(row=row, column=col*2+1)
    entries[exam] = entry

# Aggiungi pulsante per calcolare e salvare i dati
tk.Button(scrollable_frame, text="Calculate and Save Data", command=calculate_and_save).grid(row=rows_per_column+16, columnspan=columns*2)

# Get the user's desktop path and set the background image path
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
BG_IMAGE_PATH = os.path.join(desktop_path, 'vital.jpg')

# Function to create labeled entry fields dynamically
def create_section(frame, section_name, biomarkers):
    """Helper function to create sections of biomarker entries"""
    section_frame = tk.Frame(frame, bg="#e0f7fa", padx=10, pady=10)
    section_frame.grid(sticky="ew", padx=20, pady=10)

    tk.Label(section_frame, text=section_name, font=("Helvetica", 12, "bold"), bg="#e0f7fa").grid(row=0, column=0, columnspan=2, sticky="w")
    
    entries = {}
    for i, (biomarker, unit) in enumerate(biomarkers.items()):
        label = f"{biomarker} ({unit}):"
        tk.Label(section_frame, text=label, anchor="w", bg="#e0f7fa", fg="#004d40", width=25).grid(row=i+1, column=0, sticky="w")
        entry = tk.Entry(section_frame, width=10, bg="#f0f0f0")
        entry.grid(row=i+1, column=1, padx=10, pady=2)
        entries[biomarker] = entry
    
    return entries

# Function to toggle visibility of a frame
def toggle_section(section_frame):
    if section_frame.winfo_ismapped():
        section_frame.grid_remove()
    else:
        section_frame.grid()







# Main application function
def create_biological_age_app():
    root = tk.Tk()
    root.title("Biological Age Calculator")
    root.geometry("1024x768")

    # Load the background image
    try:
        background_image = Image.open(BG_IMAGE_PATH)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Background image not found at {BG_IMAGE_PATH}")
        return

    background_image = background_image.resize((1792, 1024), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(background_image)

    # Canvas for the background image
    canvas_widget = tk.Canvas(root, width=1024, height=768)
    canvas_widget.pack(fill="both", expand=True)
    canvas_widget.create_image(0, 0, image=bg_photo, anchor="nw")

    # Scrollable Frame for input sections
    scrollable_frame = tk.Frame(canvas_widget, bg="white")
    canvas_widget.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas_widget.yview)
    canvas_widget.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Coagulation State Section
    coagulation_biomarkers = {
        "PLT": "10^3/uL", 
        "MPV": "fL", 
        "P-LCR": "%", 
        "PCT": "%", 
        "PDW": "fL"
    }
    coagulation_entries = create_section(scrollable_frame, "Coagulation State", coagulation_biomarkers)

    # Lipid Metabolism Section
    lipid_biomarkers = {
        "Total Cholesterol": "mg/dL", 
        "LDL": "mg/dL", 
        "HDL": "mg/dL", 
        "Triglycerides": "mg/dL"
    }
    lipid_entries = create_section(scrollable_frame, "Lipid Metabolism", lipid_biomarkers)

    # Button to calculate and save
    calculate_button = tk.Button(scrollable_frame, text="Generate Report", command=lambda: calculate_and_save(coagulation_entries, lipid_entries))
    calculate_button.grid(pady=20)

    # Update scroll region
    scrollable_frame.update_idletasks()
    canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))

    root.mainloop()

# Function to calculate and save
def calculate_and_save(coagulation_entries, lipid_entries):
    data = {}

    # Collect Coagulation Data
    for key, entry in coagulation_entries.items():
        data[key] = entry.get()

    # Collect Lipid Data
    for key, entry in lipid_entries.items():
        data[key] = entry.get()

    # Additional Data
    data['Name'] = "John"
    data['Surname'] = "Doe"
    data['Chronological Age'] = 45
    data['Biological Age'] = 48  

    generate_pdf_report(data)

app.mainloop()

















""" # Function to generate the PDF report
def generate_pdf_report(data):

    pdf_path = os.path.join(os.path.expanduser('~'), 'Desktop', f"{data['Name']}_{data['Surname']}_Analysis_Report.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Biological Age Report")
    
    # Personal Information
    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Name: {data['Name']}")
    c.drawString(100, 750, f"Surname: {data['Surname']}")
    c.drawString(100, 730, f"Chronological Age: {data['Chronological Age']}")
    c.drawString(100, 710, f"Biological Age: {data['Biological Age']}")
    
    # Coagulation State
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 680, "Coagulation State:")
    c.setFont("Helvetica", 12)
    c.drawString(120, 660, f"PLT: {data.get('PLT', 'N/A')}")
    c.drawString(120, 640, f"MPV: {data.get('MPV', 'N/A')}")
    
    # Add Lipid Metabolism
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 610, "Lipid Metabolism:")
    c.setFont("Helvetica", 12)
    c.drawString(120, 590, f"Total Cholesterol: {data.get('Total Cholesterol', 'N/A')}")
    c.drawString(120, 570, f"LDL: {data.get('LDL', 'N/A')}")
    
    # Diabetic Profile
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 540, "Diabetic Profile:")
    c.setFont("Helvetica", 12)
    c.drawString(120, 520, f"Glycemia: {data.get('Glycemia', 'N/A')}")
    c.drawString(120, 500, f"Insulin: {data.get('Insulin', 'N/A')}")
    
    # Liver Function
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 470, "Liver Function:")
    c.setFont("Helvetica", 12)
    c.drawString(120, 450, f"GOT: {data.get('GOT', 'N/A')}")
    
    c.save()
    messagebox.showinfo("Report Generated", f"PDF report saved at {pdf_path}")
 """
