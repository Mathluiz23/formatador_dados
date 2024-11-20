from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def clean_and_format_data(input_data):
    lines = input_data.splitlines()
    formatted_data = []
    unique_entries = set()

    for line in lines:
        # Remover palavras específicas e caracteres desnecessários
        clean_line = re.sub(r"(salvar|remover|teste|testess)", "", line, flags=re.IGNORECASE)
        clean_line = re.sub(r"[^\w\s\-çáéíóúâêîôûãõàèìòù]", "", clean_line, flags=re.UNICODE)
        clean_line = clean_line.strip()

        # Corrigir formato sem o separador "-"
        if "-" not in clean_line:
            parts = clean_line.split(maxsplit=1)
            if len(parts) == 2:
                clean_line = f"{parts[0].strip()} - {parts[1].strip()}"

        # Verificar se a linha segue o formato correto "SIGLA - VALOR"
        parts = clean_line.split("-", maxsplit=1)
        if len(parts) == 2:
            sigla = parts[0].strip().upper()
            valor = parts[1].strip()

            # Validar SIGLA (deve conter apenas letras maiúsculas)
            if re.match(r"^[A-Z]+$", sigla):
                # Manter apenas palavras válidas no VALOR
                valor_parts = valor.split()
                valor = " ".join(
                    [word for word in valor_parts if len(word) > 1 and word.isalpha()]
                )

                # Remover qualquer coisa além do primeiro valor válido
                valor = re.sub(r"\s+[^\s]*$", "", valor)

                # Garantir que o valor final é válido e não vazio
                if valor:
                    entry = f"{sigla} - {valor}"
                    if entry not in unique_entries:  # Evitar duplicatas
                        unique_entries.add(entry)
                        formatted_data.append(entry)

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
