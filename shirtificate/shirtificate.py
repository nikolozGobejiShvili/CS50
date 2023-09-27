from fpdf import FPDF

#create pdf and set auto page breaker
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_auto_page_break(False)

#set font for text and write it in the center of the top of the page
pdf.set_font("Times", "B", 50)
pdf.cell(200, 20, "CS50 Shirtificate", 0, 0, align="C")

#insert shirt image
pdf.image("shirtificate.png", x=1, y=60)

#create variable name which asks user for name
name = str(input("What is your name: ")).title()

#set new font and text color
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
#write text on the shirt
pdf.cell(-210, 280, f"{name} took CS50", align="C")

#output
pdf.output("shirtificate.pdf")