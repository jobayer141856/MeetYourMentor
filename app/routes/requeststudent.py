from bson.objectid import ObjectId
from app import*

@app.route('/request_student/<string:s>', methods=['GET','POST'])
def request_student(s):
    s = str(s)
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        email = request.form["email"]
        print(message)
        print(request.form)
        print(s)
        for k in db_post_for_mentor.find({'_id': ObjectId(s)}):
             maill = k['email']

        print(maill)
        username = session['username']
        for y in db_mentor.find({"username": username}):
            number = y['number']
            print(y)
        msg = Message('want to be hired as a mentor? ', sender='meetyourmentor150@gmail.com', recipients=[maill])
        msg.body = "Message from requester for you: " + message + "\n""Requested by  " + name + "\n" "For Details Contact with " + email + " And Phone Number: " + number
        mail.send(msg)
        return "Request Successfull"
 
 
    return render_template("requeststudent.html" , **locals())


    