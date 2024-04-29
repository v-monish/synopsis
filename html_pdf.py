
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
              }

              .secondRow {
                display: flex;
                justify-content: space-between;
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
                <tr>
                  <td colspan="3">
                    <div class="secondRow">
                      <div>Aspect</div>
                      <div class="arabic">المجال</div>
                    </div>
                  </td>
                </tr>

        '''
        
    htmlTemplateForPositivesAndAfi+= f'''        <tr>
              <td>1. Students’ Academic Achievement</td>
              <td>3</td>
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
            <tr>
              <td>2. Students" Personal Development and Well-being</td>
              <td style="text-align: center;">3</td>
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
            <tr>
              <td>3. Teaching, Learning and Assessment</td>
              <td style="text-align: center;">3</td>
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
            <tr>
              <td>4. Leadership, Management, and Governance</td>
              <td style="text-align: center;">3</td>
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



# # PDF path to save
# pdf_path = 'HTML_PDF.pdf'
# # html_content = "pdf.html"
# # Generate PDF
# convert_html_to_pdf(htmlTemplateForPositivesAndAfi, pdf_path)
