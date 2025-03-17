from flask import Flask, render_template, request, send_file
import os
import subprocess

app = Flask(__name__)

INVOICE_DIR = "invoices"
os.makedirs(INVOICE_DIR, exist_ok=True)

TEMPLATE_PATH = "templates/invoice_template.tex"

def generate_invoice(data):
    """Creates a LaTeX invoice with multiple items and compiles it into a PDF."""
    with open(TEMPLATE_PATH, "r") as template_file:
        latex_content = template_file.read()

    # Format item rows for the LaTeX table
    item_rows = "\n".join([
        f"{desc} & {qty} & \\${price} & \\${float(qty) * float(price)} \\\\ \\hline"
        for desc, qty, price in zip(data["description"], data["quantity"], data["unit_price"])
    ])
    
    total_amount = sum(float(qty) * float(price) for qty, price in zip(data["quantity"], data["unit_price"]))

    # Replace placeholders
    replacements = {
        "invoice_number": data["invoice_number"],
        "date": data["date"],
        "customer_name": data["customer_name"],
        "items": item_rows,
        "total_amount": f"{total_amount:.2f}"
    }

    for key, value in replacements.items():
        latex_content = latex_content.replace(f"{{{{{key}}}}}", str(value))

    tex_filename = f"{INVOICE_DIR}/invoice_{data['invoice_number']}.tex"
    pdf_filename = tex_filename.replace(".tex", ".pdf")

    with open(tex_filename, "w") as tex_file:
        tex_file.write(latex_content)

    subprocess.run(["pdflatex", "-output-directory", INVOICE_DIR, tex_filename])

    return pdf_filename

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "invoice_number": request.form["invoice_number"],
            "date": request.form["date"],
            "customer_name": request.form["customer_name"],
            "description": request.form.getlist("description[]"),
            "quantity": request.form.getlist("quantity[]"),
            "unit_price": request.form.getlist("unit_price[]")
        }
        pdf_path = generate_invoice(data)
        return send_file(pdf_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
