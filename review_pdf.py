
import pdfkit

def convert_html_to_pdf(html_content, pdf_path):
    try:
        options = { 
          'page-size': 'A4'
        }
        pdfkit.from_string(html_content, pdf_path, options=options)
        print(f"PDF generated and saved at {pdf_path}")
    except Exception as e:
        print(f"PDF generation failed: {e}")

def process_summary(summary):
    sentences = summary.split('.\n\n')
    
    processed_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            sentence = sentence.replace('.', '')
            processed_sentences.append(f'<li>{sentence}</li>')
        processed_summary = '\n'.join(processed_sentences)
    return processed_summary

def print_arabic(text):
    return f'''<li class="arabic">{text}</li>'''

data =[
    {
        "summary": " Based on the analysis of 2023 internal examinations results, students in the Junior school have proficiency rates ranging between 35% in G4 Mathematics and 91% in G2 maths and science, while in the Middle school, the percentages range between 27% in G5 mathematics and 90% in G6 Mathematics. In the Senior school, the proficiency rates are very low in a majority of subjects, with a range between 6% in Accounts and Finance & Banking in G11and 87% in English G9. The proficiency percentages range between 6% in Economics and 100% in physics.\n\nThe proficiency rates in core subjects in a few grades in the 2023 internal examinations, particularly in Grades 4,9, and 11, need improvement. The progress made by low-achieving students in lessons is inconsistent due to inconsistent teaching strategies and support.\n\nThe students' English language, arithmetic skills, and standards in science are in line with curriculum expectations. However, proficiency rates in core subjects in a few grades in the 2023",
        "positives": [
            "Students’ high achievement in Grades 10 and 12 in the 2023 external Dhaka board examinations.",
            "Students’ English language skills, arithmetic skills and their standards in science are in line with curriculum expectations"
        ],
        "afi": [
            "Students’ proficiency rates in core subjects in a few grades in the 2023 internal examinations, particularly in Grades 4,9 and 11",
            "Progress made by low achieving students in lessons due to inconsistent teaching strategies and support provided, particularly in the middle school."
        ],
        "arabicSummary": "يظهر ملخص التنمية الشخصية للطلاب والرفاه أن المدرسة توفر للطلاب طرقًا مناسبة لتطوير مواهبهم وخبراتهم من خلال برامج الجمعيات والأنشطة خارج المدرسة وفرص القيادة. ومع ذلك، هناك حاجة إلى آليات دعم المواهب أكثر تنظيمًا وتركيزًا. تقدم المدرسة أيضًا دعمًا مرضيًا لحالات خاصة مثل الأمراض المزمنة ، ودراسات الحالة ، والدعم الاجتماعي والمالي عند الحاجة. تعد المدرسة الطلاب للمدرسة من خلال برامج التوجه المناسبة ، وتعد طلاب المدارس الثانوية للمرحلة التالية من خلال استضافة الزوار ، وتنفيذ جلسات المهن ، وتشجيع الطلاب على المشاركة في ندوات الكلية. يظهر الطلاب ثقة غير متسقة في أنفسهم في غالبية الدروس، ولكن غالبيتهم تظهر مهارات اتصال مرضية ومهارات قيادة في شرح وتقديم الإجابات، والتعبير عن أفكارهم، واللعب بدورهم، وغيرها من الأنشطة. يظهر الطلاب المواطنة المسؤولة من خلال تبني القيم الإسلامية والمواطنية، والحفاظ على ممتلكات المدرسة، والمشاركة في الدروس حول القضايا العالمية، والوعي بالانتخابات، والمساواة بين الجنسين، وغيرها من الموضوعات الهامة. تطبق المدرسة باستمرار سياسات الانضباط في جميع أنحاء المدرسة وتستخدم ممارسات إعادة التأهيل لمعالجة سلوك الطلاب وتعزيز العلاقات الإيجابية. معدل حضور الطلاب جيد بشكل عام ، مع "},
    {
        "summary": " The students' personal development and well-being summary shows that the school provides students with suitable ways to develop their talents and experiences through assembly programs, extracurricular activities, and leadership opportunities. However, there is a need for more organized and focused talent support mechanisms. The school also provides satisfactory support for special cases such as chronic diseases, case studies, and social and financial support when needed.\n\nThe school prepares students for school through suitable orientation programs, and they prepare high school students for the next stage by hosting visitors, implementing career sessions, and encouraging students to participate in college seminars. Students show inconsistent self-confidence in the majority of the lessons, but the majority of them show satisfactory communication skills and leadership skills in explaining and presenting answers, expressing their thoughts, role play, and other activities.\n\nStudents demonstrate responsible citizenship by adopting Islamic and citizenship values, maintaining school property, participating in lessons on global issues, and being aware of election, gender equality, and other important topics. The school consistently enforces school-wide discipline policies and uses restorative practices to address students' behavior and promote positive relationships.\n\nThe students' attendance rate is generally good, with a 9",
        "positives": [
            "Students’ commitment to positive behavior and citizenship values",
            "The personal support provided to foster students’ positive behavior.",
            "Some suitable opportunities for participating in ECA."
        ],
        "afi": [
            "Leadership opportunities for students inside and outside the classroom.",
            "The mechanism of identifying and supporting students’ talents.",
            "Some students' commitment to attendance."
        ],
        "arabicSummary": "يظهر ملخص التنمية الشخصية للطلاب والرفاه أن المدرسة توفر للطلاب طرقًا مناسبة لتطوير مواهبهم وخبراتهم من خلال برامج الجمعيات والأنشطة خارج المدرسة وفرص القيادة. ومع ذلك، هناك حاجة إلى آليات دعم المواهب أكثر تنظيمًا وتركيزًا. تقدم المدرسة أيضًا دعمًا مرضيًا لحالات خاصة مثل الأمراض المزمنة ، ودراسات الحالة ، والدعم الاجتماعي والمالي عند الحاجة. تعد المدرسة الطلاب للمدرسة من خلال برامج التوجه المناسبة ، وتعد طلاب المدارس الثانوية للمرحلة التالية من خلال استضافة الزوار ، وتنفيذ جلسات المهن ، وتشجيع الطلاب على المشاركة في ندوات الكلية. يظهر الطلاب ثقة غير متسقة في أنفسهم في غالبية الدروس، ولكن غالبيتهم تظهر مهارات اتصال مرضية ومهارات قيادة في شرح وتقديم الإجابات، والتعبير عن أفكارهم، واللعب بدورهم، وغيرها من الأنشطة. يظهر الطلاب المواطنة المسؤولة من خلال تبني القيم الإسلامية والمواطنية، والحفاظ على ممتلكات المدرسة، والمشاركة في الدروس حول القضايا العالمية، والوعي بالانتخابات، والمساواة بين الجنسين، وغيرها من الموضوعات الهامة. تطبق المدرسة باستمرار سياسات الانضباط في جميع أنحاء المدرسة وتستخدم ممارسات إعادة التأهيل لمعالجة سلوك الطلاب وتعزيز العلاقات الإيجابية. معدل حضور الطلاب جيد بشكل عام ، مع 9 ⁇ "
    },
    {
        "summary": " Based on lesson observation EFs (XF) and student's work, it appears that the school is generally effective in implementing effective teaching and learning strategies, but there is room for improvement in some areas. In the majority of lessons, teachers use adequate strategies such as lecturing, questions for learning, discussion, unorganized group work, math in grade 7, peer work, storytelling, scientific experimentation, learning by examples, roleplay, and choral reading. However, some teachers rely more heavily on other strategies such as repetition, long explanation, insufficient time management, and poor planning, which can negatively impact students' achievement.\n\nFurthermore, teachers could incorporate more diverse and engaging strategies in lessons, such as interactive activities, technology integration, and real-world examples, to enhance students' motivation and engagement. Additionally, teachers could use assessment results to identify areas of difficulty for individual students and provide targeted support and interventions to meet their needs.\n\nOverall, while there are some areas for improvement, the school appears to have effective teaching, learning, and assessment strategies in place to support student success.",
        "positives": [
            "Implementing adequate teaching and learning strategies and resources in the better lessons.",
            "Planning and delivery of lessons within curriculum expectations.",
            "Appropriate class management across the school"
        ],
        "afi": [
            "Using learning time productively, especially in Middle school.",
            "Implementing and utilizing assessment results to support students of different abilities, particularly the low achievers",
            "The effectiveness of the academic support programmes provided is to better meet students' learning needs."
        ],
        "arabicSummary": "استناداً إلى إيفات مراقبة الدروس (XF) وعمل الطلاب، يبدو أن المدرسة فعالة بشكل عام في تنفيذ استراتيجيات التدريس والتعلم الفعالة، ولكن هناك مجال للتحسين في بعض المجالات ⁇  في معظم الدروس، يستخدم المعلمون استراتيجيات كافية مثل المحاضرة، الأسئلة للتعلم، المناقشة، العمل الجماعي غير المنظم، الرياضيات في الصف السابع، العمل بين الأقران، سرد القصص، التجربة العلمية، التعلم عن طريق الأمثلة، لعب الأدوار، والقراءة الجامعية. ومع ذلك، فإن بعض المعلمين يعتمدون بشكل أكبر على استراتيجيات أخرى مثل التكرار، والتفسير الطويل، وإدارة الوقت غير الكافية، وسوء التخطيط، والتي يمكن أن تؤثر سلبًا على إنجاز الطلاب. علاوة على ذلك، يمكن للمعلمين دمج استراتيجيات أكثر تنوعًا وإشراكًا في الدروس، مثل الأنشطة التفاعلية، ودمج التكنولوجيا، ومثالات العالم الحقيقي، لتعزيز تحفيز الطلاب ومشاركتهم. بالإضافة إلى ذلك، يمكن للمعلمين استخدام نتائج التقييم لتحديد مجالات الصعوبات للطلاب الفردية وتقديم الدعم المستهدف والتدخلات لتلبية احتياجاتهم. بشكل عام، على الرغم من أن هناك بعض المجالات للتحسين، يبدو أن المدرسة لديها استراتيجيات تدريس وتعلم وتقييم فعالة لدعم نجاح الطلاب."
    },
    {
        "summary": " show that the school has made significant progress in various areas, including leadership, curriculum, resources, staff development, resilience, innovation, communication with community, parents, and governance.\n\nIn terms of leadership effectiveness and continuous improvement, the school has conducted a comprehensive self-evaluation and strategic planning, but there is room for improvement in this area, particularly in terms of documentation, governance, and stakeholder involvement. The school has also made efforts to improve its curriculum, resources, staff development, and resilience, among other areas.\n\nThe school has established a culture of collaboration and encouragement among its staff, parents, and stakeholders, which has helped to foster a friendly environment that supports teachers' professional development and personal growth. The school has also shown its ability to adapt to changes in the external environment, such as the COVID-19 pandemic, by introducing new initiatives that have helped it navigate through these challenges.\n\nOverall, the school has made significant progress in various areas, but there is still room for improvement, particularly in terms of documentation, governance, stakeholder involvement, and self-evaluation and strategic planning. With continued effort and focus on these areas, the school can further enhance its performance",
        "positives": [],
        "afi": [],
        "arabicSummary": "أظهرت مصادر الأدلة أن المدرسة حققت تقدمًا كبيرًا في مختلف المجالات، بما في ذلك القيادة، المناهج الدراسية، الموارد، تطوير الموظفين، المرونة، الابتكار، التواصل مع المجتمع، والآباء، والحوكمة. من حيث فعالية القيادة والتحسين المستمر، أجرت المدرسة تقييمًا ذاتيًا شاملًا وتخطيطًا استراتيجيًا، ولكن هناك مجال للتحسين في هذا المجال، لا سيما من حيث الوثائق والحوكمة ومشاركة أصحاب المصلحة. كما بذلت المدرسة جهوداً لتحسين المناهج الدراسية، والموارد، وتطوير الموظفين، والمرونة، من بين مجالات أخرى. أنشأت المدرسة ثقافة التعاون والتشجيع بين موظفيها، والآباء، وأصحاب المصلحة، مما ساعد على تعزيز بيئة ودية تدعم التنمية المهنية للمعلمين والنمو الشخصي. وقد أظهرت المدرسة أيضًا قدرتها على التكيف مع التغيرات في البيئة الخارجية، مثل وباء COVID-19، من خلال إدخال مبادرات جديدة ساعدتها على التنقل من خلال هذه التحديات. ⁇  بشكل عام، حققت المدرسة تقدمًا كبيرًا في مختلف المجالات، ولكن لا يزال هناك مجال للتحسين، لا سيما من حيث الوثائق والحوكمة، ومشاركة أصحاب المصلحة، والتقييم الذاتي والتخطيط الاستراتيجي. ⁇  بمواصلة الجهد والتركيز على هذه المجالات، يمكن للمدرسة أن تعزز أدائها ⁇ "
    }
]






# HTML content
html_content = '''
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Review Report</title>
<!-- <link rel="stylesheet" href="index.css"> -->
<style>
  *{
box-sizing: border-box;

}
body{
    # font-family: Arial, Helvitica, sans-serif;
    background: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem 1.2rem;
}

footer {
    font-size: small;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    background-color: #ffffff;
    padding: 10px;
    border-top: 1px solid #ebebeb;
    margin-bottom: 1.5cm;
  }

  .main {
    padding: 60px;
    # border: 2px solid rgb(0, 0, 0);
    width: 100%;
    height: 100%;
    background: #ffffff;    
  }

  .page-number {
    float: left;
  }

  .date {
    float: right;
  }

  .heading { 
    text-align: center;
  }

  .points {
    font-size: large;
    text-align: justify;
  }
  # .arabic{
  #   direction: rtl;
    
    
  # }

  .seperator{
    margin-top: 1in;
  }
</style>
</head>
<body>
  <div class="main">
    <header>
        <h1 style="font-size: 200%; color: rgb(6, 14, 109); border-bottom:10px solid #ebebeb; padding-bottom: 25px;">Review Report</h1>
    </header>
    <main>
        <h2 class="heading">Students’ Academic Achievement</h2>
        <ul class="points">
        '''


# formatted_list_items = split_and_format_list(english_summary1)
# for items in formatted_list_items:
#     for item in items:
#         html_content+=item

html_content += process_summary(data[0]["summary"])


html_content+=f'''
        </ul>
      
        <h2 class="heading seperator">Students' Personal Development and Wellbeing</h2>
        <ul class="points">
          '''


# formatted_list_items = split_and_format_list(english_summary2)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item

html_content += process_summary(data[1]["summary"])

html_content+=f'''
        </ul> 
        <h2 class="heading seperator">Teaching, Learning and Assessment</h2>
        <ul class="points"> 
          '''

# formatted_list_items = split_and_format_list(english_summary3)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item

html_content += process_summary(data[2]["summary"])


html_content+=f'''
        </ul>
        <h2 class="heading seperator">Leadership, Management and Governance</h2>
        <ul class="points">
'''


# formatted_list_items = split_and_format_list(english_summary4)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item

html_content += process_summary(data[3]["summary"])


html_content+=f'''
        </ul>

        <h2 class="heading seperator">
        التحصيل الأكاديمي للطلاب
        </h2>
        <ul class="points"> 
'''


# formatted_list_items = split_and_format_list(arabic_summary1)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item


html_content += print_arabic(data[0]["arabicSummary"])


html_content+=f'''
        </ul>
        <h2 class="heading seperator">
      التنمية الشخصية والرفاهية للطلاب
        </h2>
        <ul class="points"> 
'''
# formatted_list_items = split_and_format_list(arabic_summary2)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item

html_content += print_arabic(data[1]["arabicSummary"])


html_content+=f'''
        </ul>
        <h2 class="heading seperator">
        التدريس والتعلم والتقييم
        </h2>
        <ul class="points"> 
'''

# formatted_list_items = split_and_format_list(arabic_summary3)
# for items in formatted_list_items:
#     for item in items:
#        html_content+=item

html_content += print_arabic(data[2]["arabicSummary"])



html_content+=f'''
        </ul>
        <h2 class="heading seperator">
        القيادة والإدارة والحوكمة
        </h2>
        <ul class="points"> 
'''

# formatted_list_items = split_and_format_list(arabic_summary3)
# for items in formatted_list_items:
#     for item in items:
#         html_content+=item

html_content += print_arabic(data[3]["arabicSummary"])


html_content+=f'''
    </ul>
    </main>
    <footer>
        <span class="page-number">1</span>
        <span class="date">27-28 April 2024</span>
    </footer>
  </div>
</body>
</html>
'''


pdf_path = 'HTML_PDF______.pdf'
convert_html_to_pdf(html_content, pdf_path)
