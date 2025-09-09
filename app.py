
from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    """Analyzes the strength of a password based on several criteria."""
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*()]', password) is not None

    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    suggestions = []

    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        suggestions.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        suggestions.append("Password should include at least one number.")
    if not special_char_criteria:
        suggestions.append("Password should include at least one special character (e.g., !@#$%^&*()).")

    return strength, suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        strength, suggestions = check_password_strength(password)
        result = {'strength': strength, 'suggestions': suggestions}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
