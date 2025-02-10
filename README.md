
# Formatador de Dados W3K ▶️

[Deploy Formatador App](https://formatador-dados.vercel.app/)

Um aplicativo web simples para formatar dados de entrada no formato padrão `SIGLA - VALOR` ou somente `VALOR` podendo ser selecionado. Ele remove caracteres desnecessários, palavras extras e espaços, garantindo que os dados sejam limpos e bem estruturados, após a conversão terá um número garantindo a quantidade convertida e um botão simples para copiar toda a lista ajustada.

---

### **Funcionalidades**
- Limpa dados bagunçados, removendo caracteres como `.` e `,`.
- Remove palavras como `salvar`, `remover` entre outras palavras fora de SIGLA e VALOR. 
- Garante que os dados sejam formatados no padrão `SIGLA - VALOR`.
- Possui interface agradável e responsiva.
- Permite copiar os dados formatados com um botão.

---

### **Exemplo de Entrada**

```plaintext
    ARQ - ARQUITETURA. salvar remover
  CIV -      CIVIL salvar remover      
AUT -  AUTOMAÇĀO,      
```

### **Exemplo de Saída**

```plaintext
ARQ - Arquitetura
CIV - Civil
AUT - Automação
```

---


### **Estrutura do Projeto**

```
formatador_dados/
│
├── api/
│   └── index.py         # Código principal do Flask
├── templates/
│   └── index.html       # Página HTML
├── static/
│   ├── styles.css       # Arquivo de estilos
│   └── W3K.jpg          # Imagem de fundo
├── requirements.txt     # Dependências do Python
├── vercel.json          # Configuração do Vercel
├── app.py               # Arquivo principal do servidor local
└── README.md            # Este arquivo
```

---
### **Como Rodar o Projeto Localmente**

#### **Pré-requisitos**
Certifique-se de ter o seguinte instalado:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Vercel CLI](https://vercel.com/docs/cli) (opcional, se quiser deploy em Vercel)

#### **Passos**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para macOS/Linux
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o servidor localmente:
   ```bash
   python app.py
   ```

5. Acesse o aplicativo no navegador:
   ```
   http://127.0.0.1:5000
   ```

---
