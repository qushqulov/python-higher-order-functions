emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

gmail_emails = []

for email in emails:
    if email.endswith("@gmail.com"):
        gmail_emails.append(email)

print(gmail_emails)
 