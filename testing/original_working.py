from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from PyPDF2 import PdfReader, PdfReader
from googletrans import Translator
import pdfkit
import io

from text_pdf import create_pdf_from_json

import ctranslate2
import sentencepiece as spm

import os
from PyPDF2 import PdfReader

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

app = FastAPI()

translator = Translator()

@app.post("/pdf_to_summary")
async def pdf_to_summary(files: List[UploadFile] = File(...)):
    try:
        extracted_texts = await process_pdf_files(files)
        summaries = generate_summary(extracted_texts)
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



def generate_pdf(text):
    pdf_bytes = pdfkit.from_string(text, False)
    pdf_io = io.BytesIO(pdf_bytes)
    return pdf_io


model_path = "/home/ws/.cache/lm-studio/models/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q8_0.gguf"

def llm_response(prompt):
    llm = setup_llamacpp()
    response = llm.invoke({"text": prompt})
    del llm
    return response


def setup_llamacpp():
    template = f"""<s>[INST]You will be provided a Students Academic Achievement summary delimited with backtick. Assuming yourself as an AI which extracts all the facts from reviews or assessments without mentioning the review. Tailor your response towards readers who are eager to know about the School and Student's academic achievements. Follow the simple writing style without using points and used in general communication. Also provide the response in two paragraphs.  So for instance the following:
    {input}
    would be converted to:[/INST]
    {output}
    </s>"""+"[INST]`{text}` Also provide few Positives and Areas of Improvement(AFI) at the end.[/INST]"
    prompt = PromptTemplate.from_template(template)
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        temperature=0.7,
        model_path=model_path,
        n_gpu_layers=-1,
        n_batch=512,
        n_ctx=4000,
        max_tokens=2500,
        callback_manager=callback_manager,
        verbose=True
    )
    return prompt | llm

def extract_text_from_pdf(pdf_data):
    reader = PdfReader(io.BytesIO(pdf_data))
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    print("Extracted text: ", text)
    return text

def remove_consecutive_short_lines(input_text: str, length: int) -> str:
    lines = input_text.split('\n') 
    result_lines = []               
    short_count = 0                 
    for line in lines:
        if len(line) < 3:
            continue
        elif len(line) < length:
            short_count += 1
        else:
            if short_count >= 3:
                del result_lines[-short_count:]
            short_count = 0
        result_lines.append(line)
    if short_count >= 3:
        del result_lines[-short_count:]
        short_count = 0
    return '\n'.join(result_lines)

async def process_pdf_files(pdf_files: List[UploadFile]):
    
    extracted_text_list = []
    shortened_text_list = []
    file_name_list = []
    
    for pdf_file in pdf_files:
        pdf_data = await pdf_file.read()
        
        file_name_list.append(pdf_file.filename)
        
        extracted_text = extract_text_from_pdf(pdf_data)
        extracted_text_list.append(extracted_text)
        
        shortened_text = remove_consecutive_short_lines(extracted_text, length=50)
        print("Shortened text: ", shortened_text)
        shortened_text_list.append(shortened_text)

    return shortened_text_list

def translate_to_arabic(summary):
    ct_model_path = "/home/ws/Desktop/opennmt/ct2_model"
    sp_model_path = "/home/ws/Desktop/opennmt/flores200_sacrebleu_tokenizer_spm.model"
    device = "cuda" 
    sp = spm.SentencePieceProcessor()
    
    sp.load(sp_model_path)

    translator = ctranslate2.Translator(ct_model_path, device)
    src_lang = "</s> eng_Latn"
    tgt_lang = "arb_Arab"

    beam_size = 4

    for i in range(len(summary)):
        summary = summary[i].split(".")

        summary = [sent.strip() for sent in summary]
        target_prefix = [[tgt_lang]] * len(summary)

        summary_subworded = sp.encode_as_pieces(summary)
        summary_subworded = [[src_lang] + sent + ["</s>"] for sent in summary_subworded]

        translator = ctranslate2.Translator(ct_model_path, device=device)
        translations = translator.translate_batch(summary_subworded, batch_type="tokens", max_batch_size=2024, beam_size=beam_size, target_prefix=target_prefix)
        translations = [translation.hypotheses[0] for translation in translations]

        translated_summary = sp.decode(translations)
        translated_summary = [sent[len(tgt_lang):].strip() for sent in translated_summary]

        return translated_summary


def generate_summary(extracted_text_list):
    summaries = []
    for text in extracted_text_list:
        summary = llm_response(text)
        summaries.append(summary)
    
    return summaries
        
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
The 3027 intergalactic examination results show that pass rates are generally high across the school, with some exceptions in certain subjects such as Time-Traveling Mathematics and Quantum Physics. Proficiency rates are inconsistent; some students achieve proficiency levels of up to 99.9% in certain subjects, while others struggle to achieve a mere 10%.

In the Galactic Academy's Intergalactic Olympics, pass rates are 100% for all events except for the Time-Traveling Marathon, where the pass rate is 70%. Proficiency rates are zero in all events.

In both the Quasar Certification Program and the Intergalactic Culinary Competition, students in the Science stream outperform those in the Business Studies stream.

Pass rates are generally high in both streams in the Quasar Certification Program, ranging from 98% in Quantum Physics to 100% in Advanced Astrology. Proficiency rates are inconsistent, particularly in the Business Studies stream, with proficiency percentages ranging from 15% in Intergalactic Finance and Accounting to 95% in Advanced Robotics.

In the Intergalactic Culinary Competition, pass rates are 100% for all dishes, although proficiency rates are inconsistent, with high percentages in the majority of dishes and very low in some.
'''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
