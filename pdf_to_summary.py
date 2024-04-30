from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from strings import prompt_template
from PyPDF2 import PdfReader
import io

async def process_pdf_files(pdfs_data):
    
    extracted_text_list = []
    shortened_text_list = []
    # file_name_list = []
    
    for pdf_data in pdfs_data:
        # pdf_data = await pdf_file.read()
        
        # file_name_list.append(pdf_file.filename)
        
        extracted_text = extract_text_from_pdf(pdf_data)
        extracted_text_list.append(extracted_text)
        
        shortened_text = remove_consecutive_short_lines(extracted_text, length=50)
        # print("Shortened text: ", shortened_text)
        shortened_text_list.append(shortened_text)

    return shortened_text_list

def extract_text_from_pdf(pdf_data):
    reader = PdfReader(io.BytesIO(pdf_data))
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    # print("Extracted text: ", text)
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

def generate_summary(extracted_text_list):
    summaries = []
    llm = setup_llamacpp()
    for text in extracted_text_list:
        # summary = llm_response(text)
        response = llm.invoke({"text": text})
        summaries.append(response)

    del llm
    return summaries

model_path = "Models/mistral-7b-instruct-v0.1.Q8_0.gguf"

# def llm_response(prompt):
#     llm = setup_llamacpp()
#     response = llm.invoke({"text": prompt})
#     del llm
#     return response

def setup_llamacpp():
    template = prompt_template
    prompt = PromptTemplate.from_template(template)
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        temperature=0.7,
        model_path=model_path,
        n_gpu_layers=-1,
        n_batch=512,
        n_ctx=9000,
        # max_tokens=2500,
        callback_manager=callback_manager,
        verbose=True
    )
    return prompt | llm