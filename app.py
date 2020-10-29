from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
    nombre="DIEGO"
    return render_template("index.html",nombre=nombre)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__=="__main__":
    app.run(debug=True)


@app.route("/registro")
def registro():
    return render_template("auth/registro.html")
    