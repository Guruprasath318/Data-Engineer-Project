from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=14)
pdf.cell(200, 10, txt="YouTube Trending Data Analysis",ln=True,align="C")
pdf.set_font("Arial",size=12)
pdf.multi_cell(0, 10, txt="This report presents insights from YouTube trending video data after performing ETL pipeline.")
pdf.output("YouTube_Report.pdf")

print("✅ Report generated successfully!")

