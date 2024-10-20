# chatbot
USCIS-chatbot assignment

Welcome to the USCIS Manual Chatbot project! This application allows users to interact with a chatbot that answers questions based on the contents of the provided USCIS manual.

Table of Contents

Features
Technologies Used
Installation
Usage
Folder Structure
Contributing
License
Features

Interactive Chatbot: Ask questions related to the USCIS manual.
Contextual Responses: The chatbot provides answers using the manual as a reference.
Streamlit UI: A user-friendly web interface for seamless interaction.
Technologies Used

Python: Programming language for the application.
Streamlit: Framework for building the web application.
Transformers: Library by Hugging Face for leveraging pre-trained language models.
pdfplumber: Tool for extracting text from PDF files.
Hugging Face: Model hub for loading the LLaMA language model.
Installation

To get started, clone this repository and install the required dependencies.

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/uscis-chatbot.git
cd uscis-chatbot
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv chatbot-env
source chatbot-env/bin/activate  # On Windows use `chatbot-env\Scripts\activate`
Install required packages:
bash
Copy code
pip install -r requirements.txt
Download the USCIS manual PDF:
Place the USCIS manual PDF in the data/ directory and name it uscis_manual.pdf.
Usage

To run the application, use the following command:

bash
Copy code
streamlit run app.py
This will open a new tab in your web browser where you can interact with the chatbot.

Enter your question in the text input field.
Click the "Submit" button to receive an answer based on the USCIS manual.
Folder Structure

graphql
Copy code
uscis-chatbot/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── utils/                # Utility functions and classes
│   ├── chatbot.py        # Chatbot logic
│   └── document_loader.py # Functions to load the USCIS manual
└── data/                 # Folder for storing the USCIS manual
    └── uscis_manual.pdf  # The USCIS manual PDF file
Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request. Make sure to adhere to the following guidelines:

Follow the code style used in the project.
Write clear commit messages.
Ensure that your code is well-documented.
License

This project is licensed under the MIT License. See the LICENSE file for more details.






