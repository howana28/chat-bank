async function enviarMensagem() {
    const input = document.getElementById("mensagem");
    const texto = input.value;
    if (!texto.trim()) return;

    adicionarMensagem("user", texto);
    input.value = "";

    const resposta = await fetch("/mensagem", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensagem: texto })
    });

    const dados = await resposta.json();
    adicionarMensagem("bot", dados.resposta);
}

function adicionarMensagem(tipo, texto) {
    const chatbox = document.getElementById("chatbox");
    const msg = document.createElement("div");
    msg.className = `mensagem ${tipo}`;
    msg.textContent = texto;
    chatbox.appendChild(msg);
    chatbox.scrollTop = chatbox.scrollHeight;
}
