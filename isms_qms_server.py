
from flask import Flask, request, render_template, jsonify, session
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import base64
from io import BytesIO
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

def format_response(text):
    """Format the response text for better display in the UI"""
    if not text:
        return text
    
    # Clean up the text
    formatted_text = text.strip()
    
    # Add proper spacing after periods in numbered lists
    formatted_text = formatted_text.replace('. **', '.\n\n**')
    
    # Ensure proper spacing between sections
    formatted_text = formatted_text.replace('For the QMS', '\n\nFor the QMS')
    formatted_text = formatted_text.replace('These components', '\n\nThese components')
    
    # Clean up any multiple newlines
    import re
    formatted_text = re.sub(r'\n{3,}', '\n\n', formatted_text)
    
    return formatted_text

# IMPORTANT: Replace with your actual Flowise API URL for ISMS/QMS queries
FLOWISE_API_URL = "https://xcelerate.cogniwide.com/api/v1/prediction/3bfc0bf9-c71e-447b-aa48-15d053598da2"
latest_image = None

@app.route("/")
def home():
    return render_template("basic.html")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return jsonify({"status": "session cleared"})

@app.route("/message", methods=["POST"])
def message():
    user_message = request.json.get("message")
    
    # Generate a unique session ID for the flowise call if not exists
    if 'flowise_session_id' not in session:
        session['flowise_session_id'] = os.urandom(16).hex()
    
    flowise_session_id = session.get('flowise_session_id')
    
    # Prepare the message for ISMS/QMS context
    contextual_message = f"ISMS/QMS Query: {user_message}"
    
    payload = {
        "question": contextual_message,
        "sessionId": flowise_session_id,
        "chatId": flowise_session_id
    }
    
    try:
        response = requests.post(FLOWISE_API_URL, json=payload)
        response.raise_for_status()
        bot_response = response.json().get("text", "Sorry, I could not process your request.")
        
        # Format the response for better display
        formatted_response = format_response(bot_response)
        
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        formatted_response = "Sorry, there was an error communicating with the service. Please try again later."

    return jsonify({"reply": formatted_response})


@app.route("/chart")
def chart():
    return render_template("index.html")

@app.route("/run-chart", methods=["POST"])
def run_chart():
    global latest_image
    data = request.json
    code = data.get("code", "")

    try:
        # Execute chart code
        local_vars = {}
        exec(code, {"pd": pd, "plt": plt}, local_vars)

        # Save figure to Base64
        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        latest_image = "data:image/png;base64," + base64.b64encode(buf.read()).decode("utf-8")

        return jsonify({"image": latest_image})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/get-latest-image")
def get_latest_image():
    return jsonify({"image": latest_image})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
