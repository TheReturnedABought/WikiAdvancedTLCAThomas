import re

# Sample text
text = "My email is example@example.com and my phone is +1234567890."

# Extract email and phone number
email = re.search(r'\S+@\S+', text)
phone = re.search(r'\+\d+', text)

print("Email:", email.group())
print("Phone:", phone.group())