import os
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib.pagesizes import A4 # type: ignore
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import logging

# Paths for resources
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
BG_IMAGE_PATH = os.path.join(desktop_path, 'vital.jpg')
jpg_folder_path = r'C:\Users\Manuel Mersini\Desktop\REFERTO-LONGEVITY-in-corso'
jpg_files = [f"page{i}.jpg" for i in range(1, 8)]  


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

# Function to create sections for biomarker entries dynamically
def create_section(frame, section_name, biomarkers):
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

# Main function to create the app
def create_biological_age_app():
    root = tk.Tk()
    root.title("Biological Age Calculator")
    root.geometry("1280x768")  # Larger window size

    # Load and set the background image
    try:
        background_image = Image.open(BG_IMAGE_PATH)
        bg_photo = ImageTk.PhotoImage(background_image.resize((1280, 768), Image.LANCZOS))
    except FileNotFoundError:
        messagebox.showerror("Error", f"Background image not found at {BG_IMAGE_PATH}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image: {str(e)}")
        return

    # Create a main frame for the layout
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Create a frame for the scrollable sections, aligned to the left
    section_frame = tk.Frame(main_frame, bg="#ffffff", width=600)  # Fixed width for the sections
    section_frame.pack(side="left", fill="y", expand=False)  # Align to the left, make non-expandable

    # Create a Canvas for the scrollable sections
    canvas_widget = tk.Canvas(section_frame)
    canvas_widget.pack(side="left", fill="both", expand=True)

    # Create a vertical scrollbar that scrolls only the sections
    scrollbar = tk.Scrollbar(section_frame, orient="vertical", command=canvas_widget.yview)
    scrollbar.pack(side="right", fill="y")

    canvas_widget.configure(yscrollcommand=scrollbar.set)

    # Create a scrollable frame for input fields (attach this frame to the canvas)
    scrollable_frame = tk.Frame(canvas_widget, bg="white", padx=20, pady=20)
    canvas_widget.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Function to adjust scrolling region
    def on_configure(event):
        canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))

    scrollable_frame.bind("<Configure>", on_configure)

    # Set background image to cover the remaining right part of the screen
    bg_label = tk.Label(main_frame, image=bg_photo)
    bg_label.place(x=400, y=0, relwidth=1, relheight=1)  # Place background to the right of the sections

    # Create input fields for patient details
    patient_details_frame = tk.Frame(scrollable_frame, bg="#e0f7fa", padx=10, pady=10)
    patient_details_frame.grid(sticky="ew", padx=20, pady=10)

    tk.Label(patient_details_frame, text="Patient Details", font=("Helvetica", 12, "bold"), bg="#e0f7fa").grid(row=0, column=0, columnspan=2, sticky="w")
    
    tk.Label(patient_details_frame, text="Name:", bg="#e0f7fa", fg="#004d40", width=25).grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(patient_details_frame, width=25, bg="#f0f0f0")
    name_entry.grid(row=1, column=1, padx=10, pady=2)

    tk.Label(patient_details_frame, text="Surname:", bg="#e0f7fa", fg="#004d40", width=25).grid(row=2, column=0, sticky="w")
    surname_entry = tk.Entry(patient_details_frame, width=25, bg="#f0f0f0")
    surname_entry.grid(row=2, column=1, padx=10, pady=2)

    tk.Label(patient_details_frame, text="Date of Birth (DOB):", bg="#e0f7fa", fg="#004d40", width=25).grid(row=3, column=0, sticky="w")
    dob_entry = tk.Entry(patient_details_frame, width=25, bg="#f0f0f0")
    dob_entry.grid(row=3, column=1, padx=10, pady=2)

    tk.Label(patient_details_frame, text="Chronological Age:", bg="#e0f7fa", fg="#004d40", width=25).grid(row=4, column=0, sticky="w")
    chronological_age_entry = tk.Entry(patient_details_frame, width=25, bg="#f0f0f0")
    chronological_age_entry.grid(row=4, column=1, padx=10, pady=2)

    # Define the biomarker sections
    sections = {
        "Stress Ossidativo": {
            "D-ROMS": "Radicali Liberi", 
            "PAT Test": "Potential Antioxidant Test", 
            "OSI Index": "Oxidative Stress Index", 
            "OBRI": "Oxidative Balance Risk Index"
        },
        "Stadi della Malattia Renale Cronica": {
            "GFR Stage I": ">90", 
            "GFR Stage II": "60-89", 
            "GFR Stage III": "30-59", 
            "GFR Stage IV": "15-29", 
            "GFR Stage V": "<15"
        },
        "Stato della Coagulazione": {
            "PLT": "10^3/uL", 
            "MPV": "fL", 
            "P-LCR": "%", 
            "PCT": "%", 
            "PDW": "fL"
        },
        "Assetto Lipidico": {
            "Colesterolo Totale": "mg/dL", 
            "Colesterolo LDL": "mg/dL", 
            "Colesterolo HDL": "mg/dL", 
            "Trigliceridi": "mg/dL"
        },
        "Minerali": {
            "Sodio": "mEq/L", 
            "Potassio": "mEq/L", 
            "Magnesio": "mg/dL", 
            "Cloruri": "mEq/L", 
            "Calcio": "mg/dL", 
            "Fosforo": "mg/dL"
        },
        "Assetto Marziale": {
            "Sideremia": "μg/dL", 
            "Ferritina": "ng/mL", 
            "Transferrina": "mg/dL"
        },
        "Assetto Diabetologico": {
            "Glicemia": "mg/dL", 
            "Insulina": "μU/mL", 
            "HOMA Test": ""
        },
        "Proteine": {
            "Albuminemia": "g/dL", 
            "Proteine Totali": "g/dL"
        },
        "Funzionalità Epatica": {
            "Transaminasi GOT": "U/L", 
            "Transaminasi GPT": "U/L", 
            "Gamma GT": "U/L", 
            "Fosfatasi Alcalina": "U/L"
        },
        "Bilirubina": {
            "Bilirubina Totale": "mg/dL", 
            "Bilirubina Diretta": "mg/dL", 
            "Bilirubina Indiretta": "mg/dL"
        },
        "Indici di Flogosi": {
            "VES": "mm/h", 
            "PCR": "mg/L"
        },
        "Esame delle Urine": {
            "Colore": "", 
            "Aspetto": "", 
            "Peso Specifico": "", 
            "pH": "", 
            "Glucosio": "mmol/L", 
            "Nitriti": "", 
            "Proteine": "mg/dL", 
            "Sangue": "ery/μL", 
            "Chetoni": "mg/dL", 
            "Urobilinogeno": "umol/L", 
            "Bilirubina": "mg/dL", 
            "Leucociti": "Leu/μL"
        }
    }

    # Create input sections for each biomarker
    section_entries = {}
    for section_name, biomarkers in sections.items():
        section_entries[section_name] = create_section(scrollable_frame, section_name, biomarkers)


    data = {}

    data['Name'] = "John"
    data['Surname'] = "Doe"
    data['Chronological Age'] = 45
    data['Biological Age'] = 48  

    data = [name_entry, surname_entry, dob_entry, chronological_age_entry, section_entries]

    # Add the "Calcolo Età Biologica" button
    calculate_button = tk.Button(scrollable_frame, text="Calcolo Età Biologica",
                                 command=lambda: generate_pdf_report(data))
    calculate_button.grid(pady=20)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    create_biological_age_app()
