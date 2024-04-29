import requests

# URL of the FastAPI endpoint
url = "http://localhost:8080/pdf"

# Sample data to fill the content
data = {
    "name": "Alice",
    "items": ["Apple", "Banana", "Orange"],
    "show_items": True
}

# Make a GET request to the FastAPI endpoint with the data
response = requests.get(url, params=data)

# Save the generated PDF to a file
with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF file generated successfully.")