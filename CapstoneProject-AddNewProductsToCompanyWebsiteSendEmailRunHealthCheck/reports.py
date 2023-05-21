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

