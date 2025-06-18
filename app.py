from flask import Flask, render_template, request, send_file
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_file = request.files['resume']
        
        if resume_file:
            resume_path = os.path.join('uploads', resume_file.filename)
            resume_file.save(resume_path)
            
            optimized_resume = tailor_resume(job_description, resume_path)
            return send_file(optimized_resume, as_attachment=True)

    return render_template('index.html')

def tailor_resume(job_description, resume_path):
    # Call to LLM API to analyze job description and tailor resume
    # This is a placeholder for the actual API call
    optimized_resume_path = resume_path  # Replace with actual optimized resume path
    return optimized_resume_path

if __name__ == '__main__':
    app.run(debug=True)