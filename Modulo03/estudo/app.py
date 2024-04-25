from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

# Rotas


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/about")
def about():
    return "Página Sobre"

# Subindo a aplicação


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run(debug=False)
