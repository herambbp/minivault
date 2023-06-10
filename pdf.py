from fpdf import FPDF
import time
import datetime
import os
import webbrowser

def generate_transaction_pdf(username, transactions, name):
    pdf = FPDF()

    pdf.set_title('PassBook MYBANK')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Passbook", ln=True, align="C")
    pdf.set_font("Courier", "B", 12)
    pdf.cell(0, 10, f'Name: {name}\n Username: {username}\n', ln=True, align="C")
    pdf.cell(0, 10, f'Printing time: {datetime.datetime.now()}', ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(40, 10, "Transaction Type", 1)
    pdf.cell(40, 10, "Amount", 1)
    pdf.cell(40, 10, "Balance", 1)
    pdf.cell(75, 10, "Date", 1)
    pdf.ln()

    pdf.set_font("Arial", "B", 12)

    pdf.set_font("Courier", "B", 12)

    for transaction in transactions:
        pdf.cell(40, 10, transaction["type"], 1)
        pdf.cell(40, 10, f'Rs {str(transaction["amount"])}/-', 1)
        pdf.cell(40, 10, f'Rs {str(transaction["balance"])}/-', 1)
        pdf.cell(75, 10, transaction["date"], 1)
        pdf.ln()

    pdf.set_font("Arial", "B", 12)
    output_file = f"{username} Passbook.pdf" 
    output_dir = os.path.dirname(os.path.abspath(__file__))  

    output_path = os.path.join(output_dir, output_file)

    pdf.output(output_path, "F")

    print("Passbook generated successfully!")
    print("Output file path:", output_path) 
    webbrowser.open(output_path)