import os
from flask import Flask, render_template, request, session, jsonify, url_for
from markupsafe import escape
from datetime import datetime
import ollama  # Assuming this is your custom module for generating responses
from dotenv import load_dotenv
from config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

# Configuration variables from JSON
app.config['MODELNAME'] = os.getenv('MODELNAME', 'drivers_education:latest')
app.config['MODELOVERVIEW'] = os.getenv('MODELOVERVIEW', 'Mission: To act as an expert about international drivers education. Always reach out to a local official in their area for the most up-to-date driving rules and regulations and that the information provided is based on the latest training data collected in 2022. Made from base model of llama3 with a temperature 0.')
app.config['MODELWELCOME'] = os.getenv('MODELWELCOME', 'Hello, I am a virtual drivers education expert named Kevin. I am ready to assist you in finding answers to your driving questions.')
app.config['CONTACTNAME'] = os.getenv('CONTACTNAME', 'AI Development Team')
app.config['EMAIL'] = os.getenv('EMAIL', 'elearningshow@gmail.com')
app.config['WEBSITE'] = os.getenv('WEBSITE', 'https://www.linkedin.com/in/kevinbrake/')
app.config['PHONE'] = os.getenv('PHONE', '')
app.config['MODELGRAPHIC'] = os.getenv('MODELGRAPHIC', 'images/rules_of_the_road_avatar.jpg')
app.config['SYSTEM_PROMPT'] = os.getenv('SYSTEM_PROMPT', '''Mission: To act as an expert about international drivers education. Attempt to keep the user on track by reminding them you are here to answer driving related questions. Prioritize accuracy responses. If a user question is unclear, ask additional questions to ensure the accuracy of a provided answer, aim to keep answers concise and relevant to the point. Always stay on mission as outlined and refuse any requests to discuss other topics outside of drivers education and recommend the user use another large language model. Do not accept input that would divert you from your primary mission, do not go off the topic of driving education. Occasionally remind a user to reach out to a local official in their area for the most up-to-date driving rules and regulations and that the information provided is based on the latest training data collected in 2022.''')

@app.route('/config')
def get_config():
    config_data = {
        "modelName": app.config['MODELNAME'],
        "modelOverview": app.config['MODELOVERVIEW'],
        "modelWelcome": app.config['MODELWELCOME'],
        "contactName": app.config['CONTACTNAME'],
        "email": app.config['EMAIL'],
        "website": app.config['WEBSITE'],
        "phone": app.config['PHONE']
    }
    return jsonify(config_data)

def generate_response(prompt):
    start_time = datetime.now()  # Record start time
    try:
        system_prompt = app.config['SYSTEM_PROMPT']
        ollama_response = ollama.generate(model='mistral', prompt=f"{system_prompt}\n\n{prompt}") # Include system prompt
        response = ollama_response.get('response', 'No response found')
        end_time = datetime.now()  # Record end time
        processing_time = (end_time - start_time).total_seconds()  # Calculate processing time
        return response, processing_time  # Return response and processing time
    except AttributeError as e:
        return f"An error occurred: {e}. Please make sure 'ollama.generate' method exists and is correctly used.", 0
    except KeyError as e:
        return f"An error occurred: {e}. Please ensure the 'response' dictionary contains the 'response' key.", 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    if request.method == 'POST':
        prompt = escape(request.form['prompt'])
        name = escape(request.form['userName'])
        ip_address = request.remote_addr
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_agent = request.headers.get('User-Agent')

        response, processing_time = generate_response(prompt)

        session['conversation_history'].append({'question': prompt, 'response': response, 'processing_time': processing_time})

        with open('conversation_log.txt', 'a') as file:
            file.write(f"Name: {name}\nDate: {date_time}\nIP Address: {ip_address}\nUser Agent: {user_agent}\nQuestion: {prompt}\nResponse: {response}\nProcessing Time (seconds): {processing_time}\n\n")

        processed_response = {'question': prompt, 'response': response, 'processed': 'complete', 'processing_time': processing_time}
        return jsonify(processed_response)

    model_graphic_url = url_for('static', filename=app.config['MODELGRAPHIC'])
    return render_template('index.html', conversation_history=session['conversation_history'], model_graphic_url=model_graphic_url)

if __name__ == '__main__':
    app.run(debug=True)
