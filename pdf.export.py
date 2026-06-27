from reportlab.pdfgen import canvas

def create_pdf(minutes):
    pdf = canvas.Canvas("MeetingMinutes.pdf")

    pdf.drawString(100, 800, "SHG Meeting Minutes")
    pdf.drawString(100, 760, minutes[:1000])

    pdf.save()
