# resume-tailor-app

This project is a web application named "resume-tailor-app" that allows users to input a job description and an existing resume. The application utilizes a Large Language Model (LLM) API to analyze the job description and tailor the resume accordingly, providing an optimized version for the user.

## Project Structure

```
resume-tailor-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd resume-tailor-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Run the application:**
   ```
   python app/main.py
   ```

2. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

3. **Input your data:**
   - Enter the job description in the provided field.
   - Upload your existing resume.

4. **Receive your optimized resume:**
   After processing, the application will return a tailored resume based on the job description.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.