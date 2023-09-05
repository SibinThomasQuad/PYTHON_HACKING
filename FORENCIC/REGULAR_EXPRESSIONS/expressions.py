import re

# Regular expressions
credit_card_pattern = r'^\d{16}$'
debit_card_pattern = r'^\d{13,19}$'
phone_number_pattern = r'^\d{10}$'
aadhar_number_pattern = r'^\d{12}$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
currency_pattern = r'^\d+(\.\d{2})?$'
address_pattern = r'^[A-Za-z0-9\s\.,#-]+$'
date_pattern = r'^\d{4}-\d{2}-\d{2}$'
time_pattern = r'^\d{2}:\d{2}$'
url_pattern = r'^https?://\S+$'

# Function to validate data using a regular expression
def validate_data(data, pattern, data_name):
    if re.match(pattern, data):
        print(f"{data_name} is valid: {data}")
    else:
        print(f"{data_name} is not valid: {data}")

# Input data
credit_card_number = "1234567890123456"
debit_card_number = "1234567890123456789"
phone_number = "1234567890"
aadhar_number = "123456789012"
email = "example@email.com"
currency = "100.00"
address = "1234 Elm Street, Apt #5"
date = "2023-09-15"
time = "14:30"
url = "https://www.example.com"

# Validate data
validate_data(credit_card_number, credit_card_pattern, "Credit Card Number")
validate_data(debit_card_number, debit_card_pattern, "Debit Card Number")
validate_data(phone_number, phone_number_pattern, "Phone Number")
validate_data(aadhar_number, aadhar_number_pattern, "Aadhar Number")
validate_data(email, email_pattern, "Email")
validate_data(currency, currency_pattern, "Currency")
validate_data(address, address_pattern, "Address")
validate_data(date, date_pattern, "Date")
validate_data(time, time_pattern, "Time")
validate_data(url, url_pattern, "URL")
