# Chatbot

USCIS-chatbot assignment

Welcome to the USCIS Manual Chatbot project! This application allows users to interact with a chatbot that answers questions based on the contents of the provided USCIS manual.

## Features

Interactive Chatbot: Ask questions related to the USCIS manual.
Contextual Responses: The chatbot provides answers using the manual as a reference.
Streamlit UI: A user-friendly web interface for seamless interaction.

## Technologies Used

Python: Programming language for the application.
Streamlit: Framework for building the web application.
Transformers: Library by Hugging Face for leveraging pre-trained language models.
pdfplumber: Tool for extracting text from PDF files.
Hugging Face: Model hub for loading the LLaMA language model.

## Installation

To get started, clone this repository and install the required dependencies.
streamlit==1.25.0        # For UI creation
transformers==4.33.2     # For pre-trained models (LLaMA, etc.)
huggingface-hub==0.18.0  # For accessing Hugging Face models
torch==2.0.1             # For PyTorch backend
pdfplumber==0.9.0        # For PDF text extraction
sentencepiece==0.1.99    # Tokenization support for some models
bitsandbytes==0.41.1     # For 8-bit quantization (memory-efficient models)
accelerate==0.21.0       # Device management and performance optimization
scipy==1.11.2            # Optional dependency for certain models

Create a virtual environment (optional but recommended):
python -m venv chatbot-env
source chatbot-env/bin/activate  

Download the USCIS manual PDF:
Place the USCIS manual PDF in the data/ directory and name it uscis_manual.pdf.
Usage

To run the application, use the following command:
streamlit run app.py
This will open a new tab in your web browser where you can interact with the chatbot.

Enter your question in the text input field.
Click the "Submit" button to receive an answer based on the USCIS manual.

Folder Structure

graphql
Copy code
uscis-chatbot/
├── app.py                # Main application file
├── utils/                # Utility functions and classes
│   ├── chatbot.py        # Chatbot logic
│   └── document_loader.py # Functions to load the USCIS manual
└── data/                 # Folder for storing the USCIS manual
    └── uscis_manual.pdf  # The USCIS manual PDF file
    






