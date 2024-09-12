import re

def extract_phone_numbers(text):
    phone_regex = r'\(\d{3}\) \d{3}-\d{4}'
    
    phone_numbers = re.findall(phone_regex, text)
    
    return phone_numbers

text = """
Call at (123) 456-7890 or reach Cdac office at (987) 654-3210. 
You can also contact (555) 123-4567 for support.
"""

phone_numbers = extract_phone_numbers(text)

print("Extracted phone numbers:")
for phone in phone_numbers:
    print(phone)
