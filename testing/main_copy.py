from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pdf_to_summary import process_pdf_files, generate_summary
from translate_to_arabic import translate_to_arabic
from text_pdf import create_pdf_from_json
from positive_AFI import process_summary_files

app = FastAPI()

@app.post("/pdf_to_summary")
async def pdf_to_summary(files: List[UploadFile] = File(...)):
    try:
        extracted_texts = await process_pdf_files(files)
        summaries = generate_summary(extracted_texts)
        positive_AFI = process_summary_files(files)
        return summaries,positive_AFI
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summary-to-arabic")
async def summary_to_arabic(summary: list[str]):
    try:
        translated_summary = translate_to_arabic(summary)
        return {"arabic_summary": translated_summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/text-to-pdf")
async def text_to_pdf(text: list[dict]):
    try:
        output_pdf = "/home/ws/Projects/LLM/synopsis/output.pdf"
        print("Ouput path: ", output_pdf)
        pdf = create_pdf_from_json(text, output_pdf)
        return FileResponse(pdf, media_type='application/pdf', filename="output.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
