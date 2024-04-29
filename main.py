from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import FileResponse
from pdf_to_summary import process_pdf_files, generate_summary
from translate_to_arabic import translate_to_arabic
from text_pdf import create_pdf_from_json
import positive_AFI

from weasyprint import HTML


app = FastAPI()

@app.post("/pdf_to_summary")
async def pdf_to_summary(files: List[UploadFile] = File(...)):
    try:
        files_content = [await file.read() for file in files]
        extracted_texts = await process_pdf_files(files_content)
        # summaries = generate_summary(extracted_texts)
        summaries = ["summary" for text in extracted_texts]
        summaries = await positive_AFI.process_positives_AFI(files_content, extracted_texts, summaries)
        
        return summaries
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

@app.get("/pdf")
async def generate_pdf(request: Request):
    # Sample data for demonstration
    data = {
        "name": request.query_params.get("name", "World"),
        "items": ["Apple", "Banana", "Orange"],
        "show_items": True,
        "message": "Welcome!" if request.query_params.get("name") else "Please provide a name."
    }

    # Sample HTML template with dynamic content and examples
    html_content = """
    <html>
        <body>
            <h1>Hello, {name}!</h1>
            
            <!-- Example of a for loop to iterate over items -->
            <h2>Items:</h2>
            <ul>
                {% for item in items %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
            
            <!-- Example of an if-else statement to conditionally show items -->
            {% if show_items %}
            <p>Showing items:</p>
            <ul>
                {% for item in items %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
            {% else %}
            <p>Items are not shown.</p>
            {% endif %}
            
            <!-- Example of injecting a variable into a message -->
            <p>{{ message }}</p>
        </body>
    </html>
    """.format(**data)

    # Generate PDF from HTML content
    pdf = HTML(string=html_content).write_pdf()

    # Return the generated PDF as a downloadable file
    return FileResponse(pdf, filename="output.pdf", media_type="application/pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

