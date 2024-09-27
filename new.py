import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import logging

# Paths for resources
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
BG_IMAGE_PATH = os.path.join(desktop_path, 'vital.jpg')

def create_biological_age_app():
    root = tk.Tk()
    root.title("Biological Age Calculator")
    root.geometry("1280x768")

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
    

    # Create a frame for the background image
    bg_frame = tk.Frame(main_frame)
    bg_frame.pack(fill="both", expand=True)
    bg_label = tk.Label(bg_frame, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the scrollable sections
    section_frame = tk.Frame(bg_frame, bg="#ffffff", width=1000, padx=0, pady=0)
    section_frame.pack(side="left", fill="y")

    # Create a Canvas for the scrollable sections
    canvas_widget = tk.Canvas(section_frame, bg="white")
    canvas_widget.pack(side="left", fill="both", expand=True)

    # Create a vertical scrollbar
    scrollbar = tk.Scrollbar(section_frame, orient="vertical", command=canvas_widget.yview)
    scrollbar.pack(side="right", fill="y")
    canvas_widget.configure(yscrollcommand=scrollbar.set)

    # Create a scrollable frame for input fields
    scrollable_frame = tk.Frame(canvas_widget, bg="#ffffff", padx=40, pady=40, width=2000)
    canvas_widget.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Function to adjust scrolling region
    def on_configure(event):
        canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))

    scrollable_frame.bind("<Configure>", on_configure)

    # Create header labels for user input
    tk.Label(scrollable_frame, text="Biological Age Calculator", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)
    tk.Label(scrollable_frame, text="Please enter the values for the following biomarkers:", font=("Helvetica", 14), bg="white").pack(pady=5)

    # Function to dynamically create input sections
    def create_section(frame, section_name, biomarkers):
        section_frame = tk.LabelFrame(frame, text=section_name, padx=10, pady=10, bg="#e0f7fa", font=("Helvetica", 18, "bold"))
        section_frame.pack(fill="x", pady=10)

        entries = {}
        for biomarker, unit in biomarkers.items():
            frame = tk.Frame(section_frame, bg="white")
            frame.pack(fill="x", pady=5)

            label = tk.Label(frame, text=f"{biomarker} ({unit})", anchor="w", width=30, bg="white")
            label.pack(side="left")

            entry = tk.Entry(frame, width=10)
            entry.pack(side="left", padx=10)

            entries[biomarker] = entry

        return entries

    # Define the sections and biomarker fields
    sections = {
        # Adding Personal Information section
        "Personal Information": {
            "Name": "",
            "Surname": "",
            "Date of Birth": "DD/MM/YYYY",
            "Chronological Age": "years",
            "CF": ""
        },
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
        },
    }

    # Create sections and their fields dynamically
    all_entries = {}
    for section_name, biomarkers in sections.items():
        all_entries[section_name] = create_section(scrollable_frame, section_name, biomarkers)

    # Add a "Submit" button at the bottom
    submit_button = tk.Button(bg_frame, text="Generate Report", font=("Helvetica", 14), bg="#00796b", fg="white", command=lambda: submit_data())
    submit_button.place(relx=0.5, rely=0.95, anchor="center")

    def submit_data():
        data = {}
        
        for section, entries in all_entries.items():
            for key, entry in entries.items():
                data[key] = entry.get()

        print(data)  # To see the collected data in the console

        try:
            chronological_age = float(data.get("Chronological Age", 0) or 0)  # Ensure to get the chronological age
            
            # Collect necessary biomarker values and handle empty strings
            def safe_float(value):
                try:
                    return float(value)
                except ValueError:
                    return 0  # Or handle it as needed

            obri_index = safe_float(data.get("OBRI", ''))
            d_roms = safe_float(data.get("D-ROMS", ''))
            aa_epa = safe_float(data.get("AA/EPA", ''))
            aa_dha = safe_float(data.get("AA/DHA", ''))
            homa_test = safe_float(data.get("HOMA Test", ''))
            cardiovascular_risk = safe_float(data.get("Cardiovascular Risk", ''))
            osi = safe_float(data.get("OSI Index", ''))
            pat = safe_float(data.get("PAT Test", ''))

            biological_age = calculate_biological_age(
                chronological_age,
                obri_index,
                d_roms,
                aa_epa,
                aa_dha,
                homa_test,
                cardiovascular_risk,
                osi,
                pat
            )
            data["Biological Age"] = biological_age

            # Generate the report PDF
            generate_pdf_report(data)

            messagebox.showinfo("Result", f"Calculated Biological Age: {biological_age:.2f} years")

        except ValueError as e:
            logging.error(f"ValueError: {e}")
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            messagebox.showerror("Error", "An unexpected error occurred.")

    root.mainloop()

# Placeholder for biological age calculation
def calculate_biological_age(chronological_age, obri_index, d_roms, aa_epa, aa_dha, homa_test, cardiovascular_risk, osi, pat):
    # Dummy calculation for demonstration purposes
    return chronological_age + 5  # Replace with actual logic

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

if __name__ == "__main__":
    create_biological_age_app()
