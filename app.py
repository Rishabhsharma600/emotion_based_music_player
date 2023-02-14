from flask import Flask,request,render_template,session,url_for
import json
import numpy as np
import cv2
from keras.models import load_model
import webbrowser
app = Flask(__name__)

info = ["",""]
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

haarcascade = "haarcascade_frontalface_default.xml"
label_map = ['Anger', 'Neutral', 'Fear', 'Happy', 'Sad', 'Surprise']
print("+"*50, "loadin gmmodel")
model = load_model('model.h5')
cascade = cv2.CascadeClassifier(haarcascade)

# ----------------------------------index html-----------------------------------------------------------
@app.route("/")
def index():
    return render_template('first_page.html') 

#--------------------------------------------second html------------------------------------------------------

@app.route("/second_page/")
def second():
    return render_template('second_page.html')

@app.route('/processUserInfo/<string:songtp>', methods=['POST'])
def processUserInfo(songtp):
    songtp=json.loads(songtp)
    print()
    print('languge input recived'+songtp)
    print('----------')
    
    lang=songtp
    print(lang)
    info[0]=lang
    print(info)
    return ('/')

#-------------------------------------------------- punjabi starting------------------------------------------ 

@app.route("/3pp/")
def tpunjabi():
    return render_template('3pp.html')

@app.route('/processUserInfo_2/<string:langtp>', methods=['POST'])
def processUserInfo_2(langtp):
    langtp=json.loads(langtp)
    print()
    print('singer info recicevd---->'+langtp)
    print('----------')
    
    singer=langtp
    print(singer)
    info[1]=singer
    print("list created-->",info)
    return ('/')

#--------------------------------------english routing----------------------------------------
@app.route("/3pe/")
def tenglish():
    return render_template('3pe.html')


@app.route('/process_3/<string:langtp_3>', methods=['GET','POST'])
def process_3(langtp_3):
    langtp_3=json.loads(langtp_3)
    print()
    print('user info received '+langtp_3)
    print('----------')
    
    singer=langtp_3
    print(singer)
    info[1]=langtp_3
    print(info)
    return ('/')
#-----------------------------------------------------Hindi routing------------------------------------
@app.route("/3ph/")
def thindi():
    return render_template('3ph.html')

@app.route('/process_4/<string:langtp_4>', methods=['POST'])
def process_4(langtp_4):
    langtp_4=json.loads(langtp_4)
    print()
    print('user info received '+langtp_4)
    print('----------')
    
    singer=langtp_4
    print(singer)
    info[1]=langtp_4
    print(info)
    return ('/')
#--------------------------------------------------Korean routing------------------------------------------
@app.route("/3pk/")
def tkorean():
    return render_template('3pk.html')
@app.route('/process_5/<string:langtp_5>', methods=['POST'])
def process_5(langtp_5):
    langtp_5=json.loads(langtp_5)
    print()
    print('user info received '+langtp_5)
    print('----------')
    
    singer=langtp_5
    print(singer)
    info[1]=langtp_5
    print(info)
    return ('/')

#---------------------------------------------------final function---------------------------------------------
@app.route("/final/")
def final():
	print("hello")
	found = False
    
	cap = cv2.VideoCapture(0)
	while not(found):
		_, frm = cap.read()
		gray = cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.4, 1)

		for x,y,w,h in faces:
			found = True
			roi = gray[y:y+h, x:x+w]
			cv2.imwrite("static/face.jpg", roi)

	roi = cv2.resize(roi, (48,48))

	roi = roi/255.0
	
	roi = np.reshape(roi, (1,48,48,1))

	prediction = model.predict(roi)

	print(prediction)

	prediction = np.argmax(prediction)
	prediction = label_map[prediction]

	cap.release()

	link  = f"https://www.youtube.com/results?search_query={info[1]}+{prediction}+{info[0]}+song"
	webbrowser.open(link)

	return render_template("final.html",data=prediction,link=link)

#------------------------------------------------------main function-----------------------------------------------------
if __name__=="__main__":
    app.run(debug=True,port=80000)


