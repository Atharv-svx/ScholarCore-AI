async function send() {
    let input = document.getElementById("input").value;

    let res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: input})
    });

    let data = await res.json();
    document.getElementById("output").innerText = data.reply;
}