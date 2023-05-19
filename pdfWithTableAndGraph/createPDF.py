#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet				# Import style to use
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

styles = getSampleStyleSheet()
report = SimpleDocTemplate("/Users/chriswong/Desktop/report.pdf")
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])      # report_title


# Fruit Dictionary
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}


report.build([report_title])

# Create a table from the Fruit Dict
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# Add the Table to the report
report_table = Table(data=table_data)                                           # report_table

# Add a Style
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Add a Graph
report_pie = Pie(width=3*inch, height=3*inch)

# Add Data to the Pie Chart Graph above.  You'll need to create 'Data' and 'Labels'
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# Add the above Pie Chart Graph inside a Flowable Drawing
report_chart = Drawing()
report_chart.add(report_pie)                                                    # report_chart


# Add everyhing together: report_title, report_table, report_chart, and Generate the PDF
report.build([report_title, report_table, report_chart])
