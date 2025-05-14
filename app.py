from flask import Flask, request, jsonify, render_template
from intents import reconhecer_intencao
from fsm import ChatbotFSM

app = Flask(__name__)
fsm = ChatbotFSM()

@app.route('/')
def index():
    return render_template('chatbot-bancario.html')

@app.route('/mensagem', methods=['POST'])
def mensagem():
    try:
        dados = request.get_json()
        mensagem_usuario = dados.get("mensagem", "").lower()
        resposta_fsm = fsm.transitar(mensagem_usuario)
        return jsonify({"resposta": resposta_fsm})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
