from fpdf import FPDF

def add_chapter_title(pdf, title, language):
    pdf.set_font('Arial', 'B', 12)
    if language == 'arabic':
        pdf.add_font('AmiriB', '', "Fonts/Amiri-Bold.ttf", uni=True)
        pdf.set_font('AmiriB', '', 12)
        title_width = pdf.get_string_width(title)
        pdf.cell(190 - title_width, 10, '', 0, 0) 
        pdf.cell(title_width, 10, title, 0, 1, 'R') 
    else:
        pdf.cell(0, 10, title, 0, 1, 'L')

def add_chapter_body(pdf, body, language):
    pdf.set_font('Arial', '', 12)
    if language == 'arabic':
        pdf.add_font('Amiri', '', "Fonts/Amiri-Regular.ttf", uni=True)
        pdf.set_font('Amiri', '', 12)
        pdf.set_right_margin(10)
        pdf.multi_cell(0, 10, body, 0, 'R')
    else:
        pdf.set_right_margin(0)
        pdf.multi_cell(0, 10, body)
    pdf.ln()

def create_pdf_from_json(json_data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'My PDF', 0, 1, 'C')

    for item in json_data:
        add_chapter_title(pdf, item['heading'], item['language'])
        add_chapter_body(pdf, item['text'], item['language'])
        pdf.ln(10)  # Add 10 units of space between sections

    pdf.output(output_file)
    print("PDF created successfully.")

json_array = [
    {"language": "english", "heading": "Heading 1", "text": "content1"},
    {"language": "english", "heading": "Heading 2", "text": "content2"},
    {"language": "arabic", "heading": "عنوان 1", "text": "دروس غير كافية (13.5٪): تكرار الدروس (Eng gr3 ، gr8) ، عدم وجود أنشطة صعبة لتعزيز التفكير النقدي. دعم الطلاب (LA sts ، sts مع ضعف اللغة الإنجليزية): أنشطة إضافية وداعمة أثناء الدروس ، دروس علاجية أثناء الاستراحة ، دعم خلال الامتحانات السابقة ، تتبع تقدم الطالب من خلال التقييم التشخيصي والاختبارات الشهرية. تقييم التشخيص الأكاديمي: يتم تقديمه لجميع الطلاب في بداية العام الدراسي لتحديد المعايير الخضراء"},
    {"language": "arabic", "heading": "عنوان 2", "text": "المحتوى 2"}
]
