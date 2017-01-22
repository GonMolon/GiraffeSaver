from flask import Flask, request, render_template
import json
from crop import crop
import cv2
from giraffe_db import search_giraffe
app = Flask(__name__)


@app.route('/')
def ricard_si_ens_has_de_preguntar_preguntes_de_p3_ja_faig_flask():
    return render_template('index.html')


@app.route('/submit_image_to_study', methods=['GET', 'POST'])
def study_img():
    points = request.form['obj']
    points = json.loads(points)

    f = request.files['file']
    print f
    f.save('inputImages/input.png')
    img = cv2.imread('inputImages/input.png')
    path = [(p['x'], p['y']) for p in points]

    img_cropped = crop(img, path)
    cv2.imwrite('cropped.png', img_cropped)
    results = search_giraffe('cropped.png')

    print("I got it!")
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run()