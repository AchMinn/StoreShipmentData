from flask import Flask, request, render_template, redirect, url_for
import csv
from datetime import datetime
import re


app = Flask(__name__)

# File to store shipment data
CSV_FILE = "dati_carico.csv"

# CSV Headers
HEADERS = [
    "Date", "Shipment Number", "Item", "Unit", "Movement",
    "Sender", "Recipient", "Movement Type", "Expiry Date",
    "Donor", "Bill", "Notes"
]

# Ensure the CSV file exists and has the correct headers
def initialize_csv():
    try:
        with open(CSV_FILE, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
    except FileExistsError:
        pass

# Function to validate date
def validate_date(date_str):
    if not date_str:
        return datetime.now().strftime("%d/%m/%Y")  # Default to current date
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return date_str
    except ValueError:
        return None

# Function to validate numbers
def validate_number(value):
    if value.isdigit() or not value:  # Allow empty values
        return value or "///"
    return None

# Function to validate text fields
def validate_text(value):
    if re.match(r"^[A-Za-z\s]+$", value):
        return value
    return None

# Function to validate unit
def validate_unit(value):
    if value.lower() == "pz":
        return value
    return None

# Function to validate movement type
def validate_movement_type(value):
    if value.lower() in ["ingresso", "uscita"]:
        return value.lower()
    return None

# Route to display the form
@app.route("/", methods=["GET"])
def form():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    # Get data from the form
    data = request.form.get("date")
    shipment_number = request.form.get("shipmentNumber")
    item = request.form.get("item")
    unit = request.form.get("unit")
    movement = request.form.get("movement")
    sender = request.form.get("sender")
    recipient = request.form.get("recipient")
    movement_type = request.form.get("movementType")
    expiry_date = request.form.get("expiryDate")
    donor = request.form.get("donor")
    bill = request.form.get("bill")
    notes = request.form.get("notes")
    # Validate inputs
    data = validate_date(data)
    shipment_number = validate_number(shipment_number)
    item = validate_text(item)
    unit = validate_unit(unit)
    movement = validate_number(movement)
    sender = validate_text(sender)
    recipient = validate_text(recipient)
    movement_type = validate_movement_type(movement_type)
    expiry_date = validate_date(expiry_date) or "///"
    donor = donor or "///"
    bill = bill or "///"
    notes = notes or "///"

    # Check for any validation errors
    if not (data and item and unit and movement and sender and recipient and movement_type):
        return "Error: Invalid input data. Please go back and try again.", 400

    # Append the data to the CSV file
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([data, shipment_number, item, unit, movement, sender, recipient, movement_type, expiry_date, donor, bill, notes])

    return redirect(url_for("form"))

# Initialize the CSV file when the app starts
initialize_csv()

if __name__ == "__main__":
    app.run(debug=True,port=3214)
