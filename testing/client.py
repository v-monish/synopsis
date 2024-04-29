import requests



url = 'http://localhost:8080/positives-afi-pdf'
# template_data = {
#     "template_name": "template.html",
#     "data": {
#         "title": "Sample Title",
#         "content": "Sample Content"
#     }
# }

template_data = {
    "template_name": "template.html",
    "data": [
        {
            "summary": "summary",
            "positives": [
            "Students’ high achievement in Grades 10 and 12 in the 2023 external Dhaka board examinations.",
            "Students’ English language skills, arithmetic skills and their standards in science are in line with curriculum expectations"
            ],
            "afi": [
            "Students’ proficiency rates in core subjects in a few grades in the 2023 internal examinations, particularly in Grades 4,9 and 11",
            "Progress made by low achieving students in lessons due to inconsistent teaching strategies and support provided, particularly in the middle school."
            ]
        },
        {
            "summary": "summary",
            "positives": [
            "Students’ commitment to positive behavior and citizenship values",
            "The personal support provided to foster students’ positive behavior.",
            "Some suitable opportunities for participating in ECA."
            ],
            "afi": [
            "Leadership opportunities for students inside and outside the classroom.",
            "The mechanism of identifying and supporting students’ talents.",
            "Some students' commitment to attendance."
            ]
        },
        {
            "summary": "summary",
            "positives": [
            "Implementing adequate teaching and learning strategies and resources in the better lessons.",
            "Planning and delivery of lessons within curriculum expectations.",
            "Appropriate class management across the school"
            ],
            "afi": [
            "Using learning time productively, especially in Middle school.",
            "Implementing and utilizing assessment results to support students of different abilities, particularly the low achievers",
            "The effectiveness of the academic support programmes provided is to better meet students' learning needs."
            ]
        },
        {
            "summary": "summary",
            "positives": [
            "Implementing adequate teaching and learning strategies and resources in the better lessons.",
            "Planning and delivery of lessons within curriculum expectations.",
            "Appropriate class management across the school"
            ],
            "afi": [
            "Using learning time productively, especially in Middle school.",
            "Implementing and utilizing assessment results to support students of different abilities, particularly the low achievers",
            "The effectiveness of the academic support programmes provided is to better meet students' learning needs."
            ]
        }
    ]
}


response = requests.post(url, json=template_data)

if response.status_code == 200:
    with open('output.pdf', 'wb') as f:
        f.write(response.content)
    print("PDF generated successfully.")
else:
    print("Failed to generate PDF.")
