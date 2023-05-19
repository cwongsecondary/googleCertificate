#!/usr/bin/env python3
# emails.py: emails.generate_email() method takes header details, then composes and sends email

import email.message
import mimetypes
import os.path
import smtplib
    
def generate_email(sender, recipient, subject, body, attachment_path = None):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage() 
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path:
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=attachment_filename)

    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


Fri May 19:10:38 chriswong@jianlonpb162019~$ ls -ltr reports.py
-rwxr-xr-x  1 chriswong  staff  605 Jan 18 10:45 reports.py
Fri May 19:10:39 chriswong@jianlonpb162019~$ cat reports.py
#!/usr/bin/env python3
# reports.py: generate_report() method CREATES the PDF, taking: attachment, title, paragraph, table_data


from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, content):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(content, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])
