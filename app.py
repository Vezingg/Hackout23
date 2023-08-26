from flask import Flask, render_template, request
from model import model

app = Flask(__name__)

symptoms = ["Cough", "Fever", "Headache", "Nausea", "Fatigue"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = list("00000")  # Initialize with all zeros

        for idx, symptom in enumerate(symptoms):
            if request.form.get(symptom) == 'yes':
                user_input[idx] = "1"

        # Find the nearest "0" to a "1" and change it to "1"
        nearest_zero_index = user_input.index("0", user_input.index("1"))
        user_input[nearest_zero_index] = "1"

        predicted_disease = model.predict([list(map(int, user_input))])[0]

        return render_template('index.html', symptoms=symptoms, predicted_disease=predicted_disease)

    return render_template('index.html', symptoms=symptoms, predicted_disease=None)

if __name__ == '__main__':
    app.run(debug=True)
