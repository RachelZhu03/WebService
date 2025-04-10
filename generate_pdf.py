
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Unit Test Results", border=False, ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)

    def add_test_results(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)


if __name__ == "__main__":
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    with open("test_results.txt", "r") as file:
        test_results = file.read()

    pdf.add_test_results("Test Results", test_results)
    pdf.output("test_results.pdf")
