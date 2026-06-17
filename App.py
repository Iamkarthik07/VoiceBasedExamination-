from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import mysql.connector
import base64, os
import sys

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/NewQuestion')
def NewQuestion():
    return render_template('NewQuestion.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            return render_template('AdminHome.html')

        else:
            flash('Username or Password is wrong')
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    return render_template('AdminHome.html')


@app.route("/SUserInfo")
def SUserInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('SUserInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" +
                username + "','" + password + "')")
            conn.commit()
            conn.close()

            import LiveRecognition  as liv
            liv.att()
            del sys.modules["LiveRecognition"]

            flash('Record Saved!')
            return render_template('NewUser.html')
        else:
            flash('Already Register This  UserName!')
            return render_template('NewUser.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1blindexamdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
            data1 = cur.fetchall()
            flash('Login Successfully')
            return render_template('UserHome.html', data=data1)


@app.route("/newquestion", methods=['GET', 'POST'])
def newquestion():
    if request.method == 'POST':
        question = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        option4 = request.form['option4']
        answer = request.form['answer']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from questb where Question='" + question + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO questb VALUES ('','" + question + "','" + option1 + "','" + option2 + "','" + option3 + "','" +
                option4 + "','" + answer + "')")
            conn.commit()
            conn.close()

            flash('Record Saved!')
            return render_template('NewQuestion.html')
        else:
            flash('Already Register This  Question!')
            return render_template('NewQuestion.html')


@app.route("/Remove")
def Remove():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cursor = conn.cursor()
    cursor.execute(
        "Delete from   questb  where id='" + id + "'")
    conn.commit()
    conn.close()
    flash('Record Delete Successfully!')

    return QuestionInfo()


@app.route("/QuestionInfo")
def QuestionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM questb ")
    data = cur.fetchall()
    return render_template('QuestionInfo.html', data=data)


@app.route('/Exam1')
def Exam1():
    return resultt()


@app.route('/Exam')
def Exam():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cursor = conn.cursor()
    cursor.execute("truncate table temptb")
    conn.commit()
    conn.close()

    import LiveRecognition1  as liv1
    del sys.modules["LiveRecognition1"]

    return resultt()


def resultt():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from temptb ")
    data = cursor.fetchone()
    if data is None:
        flash('Face Not Found..!')
        return render_template('index.html')
    else:
        unn = data[1]
        sptex = "Welcome " + unn + " For Online Exam"
        text_to_speech(sptex)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM questb  ")
        data2 = cursor.fetchone()
        if data2:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM questb ORDER BY id ")
            data = cur.fetchall()
            for row in data:
                print(row[0])

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
                cursor = conn.cursor()
                cursor.execute("SELECT * from questb where id = '" + str(row[0]) + "' ")
                data = cursor.fetchone()
                if data:
                    q1 = data[1]
                    o1 = data[2]
                    o2 = data[3]
                    o3 = data[4]
                    o4 = data[5]
                    A1 = data[6]

                    spetext = "Question is " + q1 + " Option A  " + o1 + " Option B  " + o2 + " Option C " + o3 + " Option D " + o4 + ",tell Answer"

                    print(spetext)
                    text_to_speech(spetext)

                    session['ques'] = str(row[0])
                    session['ans'] = A1

                    return render_template('Menu.html')


        else:
            flash('No Question & Answer  Found..!')
            return render_template('index.html')


@app.route("/menu")
def menu():
    command = request.args.get('search')
    print(command)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from questb where id = '" + str(session['ques']) + "' and 	Answer='" + command + "' ")
    data = cursor.fetchone()
    if data:
        text_to_speech('Answer Is Correct')
        qid = int(session['ques']) + 1

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from questb where id = '" + str(qid) + "' ")
        data = cursor.fetchone()
        if data:
            q1 = data[1]
            o1 = data[2]
            o2 = data[3]
            o3 = data[4]
            o4 = data[5]
            A1 = data[6]

            spetext = "Question is " + q1 + " Option A  " + o1 + " Option B  " + o2 + " Option C " + o3 + " Option D " + o4 + ", tell Answer"

            print(spetext)
            text_to_speech(spetext)

            session['ques'] = str(qid)
            session['ans'] = A1
            return render_template('Menu.html')

        else:
            flash('Exam Completed..!')
            return render_template('index.html')


    else:
        text_to_speech('Answer Is Wrong')
        spetext = "Correct Answer is " + session['ans']
        print(spetext)

        text_to_speech(spetext)

        qid = int(session['ques']) + 1
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1blindexamdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from questb where id = '" + str(qid) + "' ")
        data = cursor.fetchone()
        if data:
            q1 = data[1]
            o1 = data[2]
            o2 = data[3]
            o3 = data[4]
            o4 = data[5]
            A1 = data[6]

            spetext = "Question is " + q1 + " ,Option A  " + o1 + " Option B  " + o2 + " Option C " + o3 + " Option D " + o4 + ",tell Answer"

            print(spetext)
            text_to_speech(spetext)

            session['ques'] = str(qid)
            session['ans'] = A1
            return render_template('Menu.html')

        else:
            flash('Exam Completed..!')
            return render_template('index.html')

    return render_template('Menu.html')


import pyttsx3


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 100)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, port=5000)
    app.run(debug=True, use_reloader=True)
