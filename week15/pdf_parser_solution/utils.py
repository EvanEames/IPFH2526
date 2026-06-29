from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.psparser import PSLiteral, PSSyntaxError
from pdfminer.pdftypes import resolve1, PDFObjRef
from applicant_class import Applicant

def initializeApplicant(directory:str) -> Applicant:
    """
    Function initializes an applicant object from a directory name (str).
    Example:
    If the directory is:
    007_James_BOND
    The applicant would have id = 007, last name = Bond, first_name = James

    directory = a directory where an applicant's data is stored
    """
    id = directory.split('_')[0]
    last_name = directory.split('_')[-1]
    first_name = ' '.join(directory.split('_')[1:-1])
    applicant = Applicant(id, first_name, last_name)
    return applicant

def extractApplicantInfo(questionnaire_file, applicant):
    """
    Parse questionnaire file pdf and add data to the applicant object.
    Return 
    """
    data = {}
    with open(questionnaire_file, 'rb') as fp:
        try:
            parser = PDFParser(fp)  # This line has issues when there is a digital signature (hence the try-except)
            doc = PDFDocument(parser)

            # Check if AcroForm exists (if not document is a scan)
            if 'AcroForm' not in resolve1(doc.catalog):
                print("WARNING: Questionnaire is a scan.")
                return {}
            
            fields = resolve1(doc.catalog['AcroForm'])['Fields']
            for f in fields:
                field = resolve1(f)
                name, value = field.get('T'), field.get('V')
                if isinstance(name, PSLiteral):
                    name = name.name
                if isinstance(value, PDFObjRef):
                    value = resolve1(value)
                if isinstance(value, PSLiteral):
                    value = value.name
                if value is not None and not isinstance(value,(str,dict)):
                    value = value.decode('utf-8')
                
                data[name.decode('utf-8')] = value

        except:
            print("WARNING: Cannot handle file with digital signature.")
            return {}
        finally:
            applicant.update_data(data)

    return data