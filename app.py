from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    nome = request.form["nome"]
    nota1 = float(request.form["nota1"])
    nota2 = float(request.form["nota2"])
    nota3 = float(request.form["nota3"])

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return render_template(
        "resultado.html",
        nome=nome,
        nota1=nota1,
        nota2=nota2,
        nota3=nota3,
        media=media,
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)