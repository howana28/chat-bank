def reconhecer_intencao(mensagem):
    if "oi" in mensagem:
        return "saudacao"
    elif "sair" in mensagem:
        return "encerrar"
    elif "cliente" in mensagem:
        return "sou_cliente"
    elif "quero" in mensagem and "cliente" in mensagem:
        return "virar_cliente"
    else:
        return "desconhecida"
