from flask import Flask, request, render_template
import json
app = Flask(__name__)


@app.route('/')
def ricard_si_ens_has_de_preguntar_preguntes_de_p3_ja_faig_flask():
    return render_template('index.html')


@app.route('/submit_image_to_study', methods=['GET', 'POST'])
def study_img():
    print request.form
    points = request.form['obj']
    points = json.loads(points)
    print("I got it!")
    return render_template('result.html', name='pepa')

if __name__ == '__main__':
    app.run()