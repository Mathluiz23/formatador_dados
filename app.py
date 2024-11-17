from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/format", methods=["POST"])
def format_data():
    input_data = request.form.get("input_data", "")
    lines = input_data.splitlines()
    formatted_data = []
    for line in lines:
        parts = line.split("-")
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip().split()[0]  # Remove informações extras
            formatted_data.append(f"{key} - {value}")
    return jsonify({"formatted_data": "\n".join(formatted_data)})

if __name__ == "__main__":
    app.run(debug=True)
