import camelot
import numpy as np
import PyPDF2
import tempfile
import re
import os

def split_clean(string: str):
    val = [item.strip() for item in string.split("•")]
    val = [item for item in val if item != ""]
    val = [s.replace("\n", " ") for s in val]
    val = [s.replace("  ", " ") for s in val]
    return val

def get_full_text(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def find_positives_inner(df):
    try:
        loc1 = np.where(df.isin(["Positive Areas", "Main Positives", "Main positives"]))
        loc1 = [loc1[0][0], loc1[1][0]]
        val = df[loc1[1]][loc1[0]+1]
        return split_clean(val)
    except:
        return

def find_AFI_inner(df):
    try:
        loc2 = np.where(df.isin(["Areas for Improvements", "Main Areas for Improvement", "Main AFI"]))
        loc2 = [loc2[0][0], loc2[1][0]]
        val = df[loc2[1]][loc2[0]+1].strip()
        return split_clean(val)
    except:
        return

def extract_AFI(text):
    lines = text.split("\n")
    start_index = None
    end_index = None
    sections = []

    for i, line in enumerate(lines):
        if "Areas on improvement:" in line:
            start_index = i + 1
        elif start_index is not None and re.match(r"^\s*\d", line):
            end_index = i
            section = "\n".join(lines[start_index:end_index])
            sections.append(section)
            start_index = None
            end_index = None
            break

    return split_clean("" if len(sections) <= 0 else sections[0])

def extract_positives(text):
    lines = text.split("\n")
    start_index = None
    end_index = None
    sections = []

    for i, line in enumerate(lines):
        if "Positives:" in line:
            start_index = i + 1
        elif "Areas on improvement:" in line:
            end_index = i
            if start_index is not None and end_index is not None:
                section = "\n".join(lines[start_index:end_index])
                sections.append(section)
                start_index = None
                end_index = None
            break
        
    # print("Im  before split clean", sections, { "helllo": "replaced" if len(sections) <= 0 else sections[0] })

    return split_clean("" if len(sections) <= 0 else sections[0])

def foreach_df(t, func):
    for t1 in t:
        result = func(t1.df)
        if result is not None:
            return result
    return None

def find_AFI(t1, text):
    areas = foreach_df(t1, find_AFI_inner)
    if areas is None:
        return extract_AFI(text)
    return areas

def find_positives(t1, text):
    areas = foreach_df(t1, find_positives_inner)
    # print("areas", areas)
    if areas is None:
        print("text", len(text))
        return extract_positives(text)
    return areas

def create_temp_file(byte_list):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(byte_list)
            return temp_file.name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


async def process_positives_AFI(files_content, full_text, summaries):
    for idx, file_content in enumerate(files_content):
        try:
            # print("Index in postivies", idx)
            # file_content = await file.read()
            temp_file = create_temp_file(file_content)
            pdf = camelot.read_pdf(temp_file, pages="all")
            os.remove(temp_file)
            # full_text = get_full_text(file)
            
            print("Full text length", len(full_text))
            
            positives = find_positives(pdf, full_text[idx])
            print("A", idx, positives)
            afi = find_AFI(pdf, full_text[idx])
            print("B", idx, afi)

            # results[file] = {'positives': positives, 'areas_for_improvement': afi}
            summaries[idx] = {"summary": summaries[idx], "positives":positives, "afi":afi}
            print("C", idx)
        except Exception as e:
            print("File content Error", idx, len(full_text))
            summaries[idx] = {'error': str(e)}
    print("Final Summaries", summaries)
    return summaries



# file_paths = [
#     r'C:\Users\MONISH\practice\New folder\1. Academic achievement summary.pdf',
#     r'C:\Users\MONISH\practice\New folder\2. Students Personal Development summary.pdf',
#     r'C:\Users\MONISH\practice\New folder\3. TLA Summary.pdf',
#     r'C:\Users\MONISH\practice\New folder\4 LMG Summary.pdf'
# ]

# summary_results = process_summary_files(file_paths)
# print(summary_results)
