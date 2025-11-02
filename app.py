# integrate HTML with Flask
# HTTP verb GET and POST

# jinja2 template
# {%...%} for loop statement
# {{   }} expressions to print output
# {#....#} this is for comment

'''from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# ✅ Add route decorator here
@app.route('/')
def welcome():
    return render_template('index.html')

# ✅ success route returns a dictionary (not int)
@app.route('/success/<int:score>')
def success(score):
    res = "PASS" if score >= 50 else "FAIL"
    exp = {'Score': score, 'Result': res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks are " + str(score)

# Fixed indentation and dictionary passing
@app.route('/result/<int:marks>')
def result(marks):
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

# Submit form calculates average and redirects properly
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for('success', score=total_score))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)'''

#OpenCV Face And Eye Detection In Flask Web Framework
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
