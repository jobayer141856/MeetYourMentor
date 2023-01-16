from bson.objectid import ObjectId
from app import*
from datetime import datetime

@app.route('/request_mentor/<string:s>', methods=['GET','POST'])
def request_mentor(s):
    s = str(s)
    stdx = False
    mentx = False
    if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        email = request.form["email"]
        print(message)
        print(request.form)
        print(s)
        for k in db_mentor_academic.find({'_id': ObjectId(s)}):
             maill = k['email']
             ment_username = k['username']

        print(maill)
        username = session['username']
        for y in db_std.find({"username": username}):
            number = y['number']
            # name = y['name']
            # email = ['email']
            print(y)

        msg = Message('want to be hired as a mentor? ', sender='meetyourmentor150@gmail.com', recipients=[maill])
        msg.body = "Message from requester for you: " + message + "\n""Requested by  " + name + "\n" "For Details Contact with " + email + " And Phone Number: " + number
        mail.send(msg)
        post = {'ment_username': ment_username, 'std_username': username, 'std_name': name, 'email' :email, 'message':message, 'current_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
        db_request_mentor.insert_one(post)
        return redirect(url_for('findmentor'))

    return render_template("requestmentor.html" , **locals())


    