import re

def extract_unique_emails(filename):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    unique_emails = set()

    with open(filename, 'r') as file:
        for line in file:
            emails_in_line = re.findall(email_regex, line)
            unique_emails.update(emails_in_line)
    
    return unique_emails, len(unique_emails)

filename = 'email_text_file.txt'
emails, count = extract_unique_emails(filename)

print(f"Found {count} unique email addresses:")
for email in emails:
    print(email)
