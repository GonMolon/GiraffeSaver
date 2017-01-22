from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def ricard_si_ens_has_de_preguntar_preguntes_de_p3_ja_faig_flask():
    return "Hola Pau"


@app.route('/submit_image_to_study', methods=['POST'])
def addRegion():
    print("I got it!")
    print(request.form['projectFilepath'])

if __name__ == '__main__':
    app.run()