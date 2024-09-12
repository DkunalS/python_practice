import re

def find_urls(text):
    regex = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    
    urls = re.findall(regex, text)
    
    return urls

text = """
Visit our website at http://www.cad.com for more details about the courses.
Check out https://iacsd.cdac.co.in/exam/dac/resource and http://nic-cert.org/page.
Don't forget https://cdacpune.com and http://localhost:8000!
"""

urls = find_urls(text)

print("Extracted URLs:")
for url in urls:
    print(url)
