from intents import reconhecer_intencao

class ChatbotFSM:
    def __init__(self):
        self.estado = "inicio"
        self.nome = ""

    def transitar(self, mensagem):
        intencao = reconhecer_intencao(mensagem)

        if self.estado == "inicio":
            self.estado = "perguntar_nome"
            return "Olá! Qual é o seu nome?"

        elif self.estado == "perguntar_nome":
            self.nome = mensagem.title()
            self.estado = "opcoes"
            return f"Muito prazer, {self.nome}! Você já é nosso cliente ou quer virar cliente?"

        elif self.estado == "opcoes":
            if intencao == "sou_cliente":
                self.estado = "cliente_opcoes"
                return "Ótimo! Como posso te ajudar? (consultar saldo, atendimento humano, etc.)"
            elif intencao == "virar_cliente":
                self.estado = "cadastro"
                return "Perfeito! Para começarmos, me diga seu CPF e e-mail, por favor."
            else:
                return "Desculpe, não entendi. Você já é cliente ou quer virar cliente?"

        elif self.estado == "cliente_opcoes":
            return "Estamos em desenvolvimento, em breve mais opções estarão disponíveis."

        elif self.estado == "cadastro":
            return "Cadastro recebido! Em breve entraremos em contato. Obrigado!"

        if intencao == "encerrar":
            self.estado = "fim"
            return "Sessão encerrada. Até logo!"

        return "Desculpe, não entendi."
