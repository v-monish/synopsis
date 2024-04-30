
import pdfkit
from jinja2 import Environment, FileSystemLoader
from fastapi.responses import StreamingResponse
from io import BytesIO


async def convert_html_to_pdf(html_content, pdf_path):
    try:
        # Store pdf in local disk
        options = { 'page-size': 'A4' }
        pdf_data = pdfkit.from_string(html_content, pdf_path, options=options)
        print(f"PDF generated and saved at {pdf_path}")
      
    except Exception as e:
        print(f"PDF generation failed: {e}")


def render_template(template_name, data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_name)
    return template.render(data)

async def generatePdfFromHtmlTemplateString(html_template: str, options: dict):
    # Create a PDF from the HTML template string
    
    pdf_options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in'
}
    
    pdf_data = pdfkit.from_string(html_template, False, options=pdf_options)
    
    is_downloadable = options.get("isDownloadable", True)
    filename = options.get("filename", "document.pdf")

    # Set the Content-Disposition header
    content_disposition = "attachment" if is_downloadable else "inline"
    content_disposition += f'; filename="{filename}"'
    
    headers = { "Content-Disposition": content_disposition }

    # Return the PDF as a streaming response
    return StreamingResponse(BytesIO(pdf_data), media_type="application/pdf", headers=headers)

def injectDataIntoAfiPositivesTemplate(data):

    htmlTemplateForPositivesAndAfi = '''
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Project</title>
            <style>
              body {
                box-sizing: border-box;
              }
            
              .mainclass {
                width: 99%;
                height: 100%;
              }

              table {
                font-family: Arial, Helvitica, sans-serif;
                border: 1px solid #a19061;
                border-collapse: collapse;
                width: 100%;
                height: 100vh;
                background-color: rgb(255, 255, 255);
                padding: 5px;
                margin: 5px;
              }

              table td {
                border: 1px solid #a19061;
                width: 100px;
                padding: 5px;
              }

              table tr:nth-child(3) td:nth-child(2) {
                text-align: center;
              }

              tr:nth-child(3),
              tr:nth-child(8),
              tr:nth-child(13),
              tr:nth-child(18) {
                background-color: #ffffcc;
              }

              .firstRow {
                display: flex;
                justify-content: space-between;
                font-weight: bold;
              }

              .secondRow {
                display: flex;
                justify-content: space-between;
              }
 .thirdRow > div {
   font-weight: bold;
 }

          .thirdRow > div, .firstRow > div, .secondRow > div {
                display: inline-block;
                width: 49%;
          }
          .thirdRow > div:nth-child(2), .firstRow > div:nth-child(2), .secondRow > div:nth-child(2){
          text-align: right;
          }
              .listone {
                padding-left: 50px;
              }

              *{
                padding: 0;
                margin: 0;
              }

              
              .arabic{
              direction: rtl;
              }
              .bold{
                font-weight: bold;
              }
            </style>
          </head>

          <body>
            <div class="mainclass">
              <table class="table">
                <tr>
                  <td colspan="3">
                    <div class="firstRow">
                      <div>Key Positives and Areas for Improvement</div>
                      <div class="arabic">أهم الجوانب الإيجابية والجوانب التي تحتاج إلى تطوير</div>
                    </div>
                  </td>
                </tr>
                <tr class="bold">
                  <td colspan="3">
                    <div class="secondRow">
                      <div>Aspect</div>
                      <div class="arabic">المجال</div>
                    </div>
                  </td>
                </tr>

        '''
        
    htmlTemplateForPositivesAndAfi+= f'''        <tr class="bold">
              <td>1. Students’ Academic Achievement</td>
              <td>score</td>
              <td class="arabic">1لأكاديمي</td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Positives</div>
                  <div class="arabic">الجوانب الإيجابية</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">'''

    for positive in data[0]["positives"]:
        htmlTemplateForPositivesAndAfi += f'''
        
            <li >{positive}</li>
      
        '''

    htmlTemplateForPositivesAndAfi += f'''            </ul>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Areas of Improvements</div>
                  <div class="arabic">الجوانب التي تحتاج إلى تطوير</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">'''


    for afi in data[0]["afi"]:
        htmlTemplateForPositivesAndAfi += f'''
      
            <li >{afi}</li>

        '''

    htmlTemplateForPositivesAndAfi += f'''</ul>
                </div>
              </td>
            </tr>
            <tr class="bold">
              <td>2. Students Personal Development and Well-being</td>
              <td style="text-align: center;">score</td>
              <td  class="arabic" >2التطورالشخص ي للطلبة ورعايتهم</td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Positives</div>
                  <div class="arabic">الجوانب الإيجابية</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky"> '''



    for positive in data[1]["positives"]:
        htmlTemplateForPositivesAndAfi += f'''
        
            <li >{positive}</li>
      
        '''

    htmlTemplateForPositivesAndAfi += f''' 
                </ul>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
    <div class="thirdRow">
                  <div>Areas of Improvements</div>
                  <div class="arabic">الجوانب التي تحتاج إلى تطوير</div>
                </div>
                          </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">
    '''
    for afi in data[1]["afi"]:
        htmlTemplateForPositivesAndAfi += f'''
      
            <li >{afi}</li>

        '''

    htmlTemplateForPositivesAndAfi += f''' 
        </ul>
                </div>
              </td>
            </tr>
            <tr class="bold">
              <td>3. Teaching, Learning and Assessment</td>
              <td style="text-align: center;">score</td>
              <td class="arabic">3التعليم والتعلم والتقويم</td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Positives</div>
                  <div class="arabic">الجوانب الإيجابية</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">
    '''
    for positive in data[2]["positives"]:
        htmlTemplateForPositivesAndAfi += f'''
        
            <li >{positive}</li>
      
        '''

    htmlTemplateForPositivesAndAfi += f''' 
      </ul>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Areas of Improvements</div>
                  <div class="arabic">الجوانب التي تحتاج إلى تطوير</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">
    '''
    for afi in data[2]["afi"]:
        htmlTemplateForPositivesAndAfi += f'''
      
            <li >{afi}</li>

        '''

    htmlTemplateForPositivesAndAfi += f''' 
    </ul>
                </div>
              </td>
            </tr>
            <tr class="bold">
              <td>4. Leadership, Management, and Governance</td>
              <td style="text-align: center;">score</td>
              <td class="arabic">4القيادة والإدارة والحوكمة</td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Positives</div>
                  <div class="arabic">الجوانب الإيجابية</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">
    '''
    for positive in data[3]["positives"]:
        htmlTemplateForPositivesAndAfi += f'''
            <li >{positive}</li>
      
        '''

    htmlTemplateForPositivesAndAfi += f''' 
      </ul>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="thirdRow">
                  <div>Areas of Improvements</div>
                  <div class="arabic">الجوانب التي تحتاج إلى تطوير</div>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="3">
                <div class="listone">
                  <ul class="sky">
    '''

    for afi in data[3]["afi"]:
        htmlTemplateForPositivesAndAfi += f'''
            <li >{afi}</li>

        '''
    htmlTemplateForPositivesAndAfi += f''' 
          </ul>
                </div>
              </td>
            </tr>
          </table>
        </div>
      </body>
    </html>
    '''

    return htmlTemplateForPositivesAndAfi

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


def injectDataIntoReviewTemplatePDF(data):
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

  return html_content



