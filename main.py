from typing import Dict, List, Union
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import FileResponse
from pdf_to_summary import process_pdf_files, generate_summary
from translate_to_arabic import translate_to_arabic
from text_pdf import create_pdf_from_json
import positive_AFI
from html_pdf import generatePdfFromHtmlTemplateString, injectDataIntoAfiPositivesTemplate

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/pdf/summary")
async def pdf_to_summary(files: List[UploadFile] = File(...)):
    try:
        print("Files", files)
        files_content = [await file.read() for file in files]
        extracted_texts = await process_pdf_files(files_content)
        # summaries = generate_summary(extracted_texts)
        summaries = ["summary" for text in extracted_texts]
        summaries = await positive_AFI.process_positives_AFI(files_content, extracted_texts, summaries)
        
        return summaries
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summary/arabic")
async def summary_to_arabic(summary: list[str]):
    try:
        translated_summary = translate_to_arabic(summary)
        return {"arabic_summary": translated_summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/report/pdf")
async def text_to_pdf(text: list[dict]):
    try:
        output_pdf = "/home/ws/Projects/LLM/synopsis/output.pdf"
        print("Ouput path: ", output_pdf)
        pdf = create_pdf_from_json(text, output_pdf)
        return FileResponse(pdf, media_type='application/pdf', filename="output.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/positives-afi/pdf")
async def generate_pdf_from_template(template_data: List[Dict[str, Union[str, List[str]]]], isDownloadable: bool = Query(True, description="Set to false if the PDF should be displayed in the browser instead of downloaded")):
    # data = template_data.get("data")
    
    templateStringWithInjectedData = injectDataIntoAfiPositivesTemplate(template_data)
    
    # Pass the isDownloadable parameter to generatePdfFromHtmlTemplateString
    options = {"isDownloadable": isDownloadable}
    return await generatePdfFromHtmlTemplateString(templateStringWithInjectedData, options)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

