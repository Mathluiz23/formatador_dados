from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def clean_and_format_data(input_data, format_type, data_type):
    lines = input_data.splitlines()
    formatted_data = []
    unique_entries = set()

    if data_type == "sigla":
        for line in lines:
            clean_line = re.sub(r"(salvar|remover|teste|botao|onclick|ok|esge|,|\.|')", "", line, flags=re.IGNORECASE)
            clean_line = re.sub(r"\s{2,}", " ", clean_line).strip()

            if " - " in clean_line:
                sigla, valor = clean_line.split(" - ", 1)
                sigla = sigla.strip().upper()
                valor = valor.strip()
                valor = re.sub(r"\s{2,}", " ", valor)
                valor = re.sub(r"\b(salvar|remover|teste|botao|onclick|ok|esge|não|sim)\b", "", valor, flags=re.IGNORECASE)
                valor_parts = valor.split()
                valor = " ".join([word for word in valor_parts if len(word) > 1 and word.isalpha()])

                if format_type == "capitalize":
                    valor = valor.title()
                elif format_type == "uppercase":
                    valor = valor.upper()

                if valor:
                    entry = f"{sigla} - {valor}"

                    if entry not in unique_entries:
                        unique_entries.add(entry)
                        formatted_data.append(entry)

            else:
                parts = clean_line.split(maxsplit=1)
                if len(parts) == 2:
                    sigla = parts[0].strip().upper()
                    valor = parts[1].strip()
                    valor = re.sub(r"\s{2,}", " ", valor)
                    valor = re.sub(r"\b(salvar|remover|teste|botao|onclick|ok|esge|não|sim)\b", "", valor, flags=re.IGNORECASE)
                    valor_parts = valor.split()
                    valor = " ".join([word for word in valor_parts if len(word) > 1 and word.isalpha()])

                    if format_type == "capitalize":
                        valor = valor.title()
                    elif format_type == "uppercase":
                        valor = valor.upper()

                    if valor:
                        entry = f"{sigla} - {valor}"

                        if entry not in unique_entries:
                            unique_entries.add(entry)
                            formatted_data.append(entry)

    elif data_type == "sem_sigla":
        for line in lines:
            clean_line = re.sub(r"(Valor|Editar|Excluir|Desabilitado)", "", line, flags=re.IGNORECASE)
            clean_line = re.sub(r"\s{2,}", " ", clean_line).strip()

            values = re.split(r"\s{2,}", clean_line)
            for value in values:
                value = value.strip()
                if value:
                    if format_type == "capitalize":
                        value = value.title()
                    elif format_type == "uppercase":
                        value = value.upper()

                    if value not in unique_entries:
                        unique_entries.add(value)
                        formatted_data.append(value)

    return "\n".join(formatted_data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/format", methods=["POST"])
def format_data():
    input_data = request.form.get("input_data", "")
    format_type = request.form.get("format_type", "capitalize")
    data_type = request.form.get("data_type", "sigla")
    formatted_data = clean_and_format_data(input_data, format_type, data_type)
    return jsonify({"formatted_data": formatted_data})

if __name__ == "__main__":
    app.run(debug=True)
