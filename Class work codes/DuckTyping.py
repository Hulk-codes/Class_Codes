# DuckTyping : It is a concept where the type of an object is determined 
# by its behaviour, not by it's class

class InkjetPrinter:
    def PrintDocument(self,document):
        print("InkjetPrinter printing : ", document)

class LaserPrinter:
    def PrintDocument(self,document):
        print("LasePrinter  printing : ", document)

class PDFWriter:
    def PrintDocument(self,document):
        print(f"Saving {document} as a PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())
main()