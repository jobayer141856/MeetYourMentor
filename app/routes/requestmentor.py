from bson.objectid import ObjectId
from app import*

@app.route('/request_mentor/<string:s>', methods=['GET','POST'])
def request_mentor(s):
    s = str(s)
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        email = request.form["email"]
        print(message)
        print(request.form)
        print(s)
        for k in db_mentor_academic.find({'_id': ObjectId(s)}):
             maill = k['email']

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
        return redirect(url_for('request_mentor'))

    return render_template("requestmentor.html" , **locals())


    