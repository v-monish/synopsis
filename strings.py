        
input='''
Student’s Galactic standards
Analysis of 3027 intergalactic examinations results indicates the following: (SN01)
• Pass rates are mostly high across the school, ranging from 99.9% in Advanced Astrology to 100% in Intergalactic Cuisine . However, pass rates are lower in subjects such as Time-Traveling Mathematics and Quantum Physics , at 85.6% and 80.2% respectively.
• Tracking pass percentages indicate generally high pass rates in most subjects and grades for the past five years.
• Proficiency rates are inconsistent, with some students achieving proficiency levels of up to 99.9% in certain subjects, while others struggle to achieve a mere 10%.
Analysis of 3027 external examinations results indicates the following: (SN01)
• In the Galactic Academy's Intergalactic Olympics, 5 students out of 10 attempted 5 events, four attempted 4 events, and one student sat three events. Pass rates are 100% for all events except for the Time-Traveling Marathon , where pass rates are 70%. Proficiency rates are zero in all events.
• In both the Quasar Certification Program and the Intergalactic Culinary Competition, students in the Science stream perform better than students in the Business Studies stream.
• In the Quasar Certification Program, pass rates are generally high in both streams, ranging from 98% in Quantum Physics to 100% in Advanced Astrology . Proficiency rates are inconsistent, particularly in the Business Studies stream. Proficiency percentages range between 15% in Intergalactic Finance and Accounting and 95% in Advanced Robotics.
• In the Intergalactic Culinary Competition, pass rates are 100% in all dishes. Proficiency rates are inconsistent, with high percentages in a majority of dishes, and very low in some dishes.
• Percentages of students achieving the Galactic Academy's prestigious Golden Quasar award is 80%, and percentages of those achieved the Silver Quasar award is 95%.
'''

output='''
The 3027 intergalactic examination results show that pass rates are high across the school, with some exceptions in Time-Traveling Mathematics and Quantum Physics. Proficiency rates are inconsistent; some achieve up to 99.9% in certain subjects, while others struggle to achieve 10%. In Intergalactic Olympics, pass rates are 100% for all events except for the Time-Traveling Marathon, where the pass rate is 70%. Proficiency rates are zero in all events.

In both the Quasar Certification Program and the Intergalactic Culinary Competition, students in the Science stream outperform those in the Business Studies stream. Pass rates are generally high in both streams in the Quasar Certification Program, ranging from 98% in Quantum Physics to 100% in Advanced Astrology. Proficiency rates are inconsistent, particularly in the Business Studies stream, with proficiency percentages ranging from 15% in Intergalactic Finance and Accounting to 95% in Advanced Robotics. In the Intergalactic Culinary Competition, pass rates are 100% for all dishes, although proficiency rates are inconsistent.
'''

prompt_template = f"""<s>[INST]You will be provided a Students Academic Achievement summary delimited with backtick. Assuming yourself as an AI which extracts all the facts from reviews or assessments without mentioning the review. Tailor your response towards readers who are eager to know about the School and Student's academic achievements. Follow the simple writing style without using points and used in general communication. Also provide the response in two paragraphs.  So for instance the following:
    {input}
    would be converted to:[/INST]
    {output}
    </s>"""+"[INST]`{text}`[/INST]"