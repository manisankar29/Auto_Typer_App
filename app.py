from flask import Flask, render_template, request, jsonify
import pyautogui
import time
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'manismile79294@gmail.com'
app.config['MAIL_PASSWORD'] = 'hrcs kqdf ghtt xaoa'

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_typing", methods=["POST"])
def start_typing():
    content = request.json.get("content")
    if not content:
        return jsonify({"status": "error", "message": "No content provided"})
    
    time.sleep(5)  # Allow user to switch windows
    for char in content:
        pyautogui.typewrite(char)
        time.sleep(0.05)  # Adjust typing speed

    return jsonify({"status": "success", "message": "Typing completed!"})

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    feedback = request.json.get("feedback")
    if not feedback:
        return jsonify({"status": "error", "message": "No feedback provided"})
    
    # Send feedback to email
    msg = Message("New Feedback", sender="manismile79294@gmail.com", recipients=["manismile79294@gmail.com"])
    msg.body = f"Feedback received:\n\n{feedback}"
    mail.send(msg)

    return jsonify({"status": "success", "message": "Feedback submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
