from app import *

otp = randint(000000,999999)
@app.route('/verify', methods=['GET','POST'])
def verify():
    msg_otp = ""
    username = session["username"]
    name = session["name"] 
    email = session["email"] 
    number = session["number"]
    hashed = session["password"]
    role = 'mentor'

    role =  session["user"]

    profile_pic = "https://bootdey.com/img/Content/avatar/avatar7.png"

    msg = Message('Verify Email-OTP',sender='meetyourmentor150@gmail.com',recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    if request.method=='POST':
        userotp = request.form["otp"]
        if otp==int(userotp):
            msg_otp = "OTP Verified Successfully!"
            user_input = {'username': username, 'name': name,  'email': email,'number': number, 'password': hashed , 'profile_pic': role}
            if role == 'mentor':
                db_mentor.insert_one(user_input)
            else:
                db_std.insert_one(user_input)
            session.clear()
            return redirect(url_for("login"))
        else:
            return "Wrong OTP"

    
    return render_template("verify.html")