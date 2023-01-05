from app import*
otp = randint(000000,999999)
@app.route('/forgot', methods=['GET','POST'])

def forgot():
    if request.method == "POST":
        username = request.form['username']
        db_x = db_mentor.find_one({'username': username})
        db_y = db_std.find_one({'username': username})
        if db_x:
            email = db_x['email']
            email = str(email)
            msg = Message('Verify Email-OTP',sender='meetyourmentor150@gmail.com',recipients=[email])
            msg.body = str(otp)
            mail.send(msg)
            return render_template("verify_otp.html", **locals())
        elif db_y:
            email = db_y['email']
            email = str(email)
            msg = Message('Verify Email-OTP',sender='meetyourmentor150@gmail.com',recipients=[email])
            msg.body = str(otp)
            mail.send(msg)
            return render_template("verify_otp.html", **locals())
        else:
            return 'username not found'     
    return render_template("forgot_pass.html" , **locals())

@app.route('/verify_otp/<string:s>', methods=['GET','POST'])
def verify_otp(s):
    username = str(s)
    print(username)
    if request.method == 'POST':
        userotp = request.form["otp"]
        print(userotp)
        if otp==int(userotp):
            msg_otp = "OTP Verified Successfully!"
            return render_template("pass_recovery.html" , **locals())
        else:
            return "Wrong OTP"
    return render_template("verify_otp.html")

@app.route('/pass_recovery/<string:s>', methods=['GET','POST'])
def pass_recovery(s):
    username = str(s)
    db_x = db_mentor.find_one({'username': username})
    db_y = db_std.find_one({'username': username})
    if request.method == 'POST':
        password = request.form["pass"]
        password1 = request.form["pass2"]
        print(password)
        if len(password)<6:
            return 'password must  be 6 or greater than 6' 
        elif password != password1:
            return 'password does not match'
        elif db_x:
            db_mentor.update_one({'_id':db_x['_id']}, {"$set" : {"password" :password}})
            return redirect(url_for('login'))
        elif db_y:
            db_std.update_one({'_id':db_y['_id']}, {"$set" : {"password" :password}})
            return redirect(url_for('login'))

    return render_template("pass_recovery.html", **locals())

