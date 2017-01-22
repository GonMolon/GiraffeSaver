from flask import Flask
app = Flask(__name__)


@app.route('/')
def ricard_si_ens_has_de_preguntar_preguntes_de_p3_ja_faig_flask():
    return "Hola Pau"


if __name__ == '__main__':
    app.run()