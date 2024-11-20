from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def clean_and_format_data(input_data):
    lines = input_data.splitlines()
    formatted_data = []

    for line in lines:
        clean_line = re.sub(r"[^a-zA-Z0-9\s\-]", "", line)
        clean_line = re.sub(r"(salvar|remover)", "", clean_line, flags=re.IGNORECASE)
        clean_line = clean_line.strip()

        parts = clean_line.split("-")
        if len(parts) == 2:
            sigla = parts[0].strip().upper()
            valor = parts[1].strip().capitalize()
            formatted_data.append(f"{sigla} - {valor}")

    return "\n".join(formatted_data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/format", methods=["POST"])
def format_data():
    input_data = request.form.get("input_data", "")
    formatted_data = clean_and_format_data(input_data)
    return jsonify({"formatted_data": formatted_data})

if __name__ == "__main__":
    app.run(debug=True)
