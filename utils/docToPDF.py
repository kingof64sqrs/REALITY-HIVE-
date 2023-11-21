from docx import Document

doc_path = 'path/to/your/document.docx'
doc = Document(doc_path)

document_text = ""
for para in doc.paragraphs:
    document_text += para.text + "\n"

print(document_text)
