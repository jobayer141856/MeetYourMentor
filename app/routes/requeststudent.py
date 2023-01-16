from bson.objectid import ObjectId
from app import*
from datetime import datetime

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
             std_username = k['username']
        
        print(maill)
        username = session['username']
        for y in db_mentor.find({"username": username}):
            number = y['number']
            print(y)
        msg = Message('Are you looking for a mentor? ', sender='meetyourmentor150@gmail.com', recipients=[maill])
        msg.body = "Message from requester for you: " + message + "\n""Requested by  " + name + "\n" "For Details Contact with " + email + " And Phone Number: " + number
        mail.send(msg)
        post = {'std_username': std_username, 'ment_username': username, 'ment_name': name, 'email' :email, 'message':message, 'current_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
        db_request_student.insert_one(post)
        return redirect(url_for('findstudents'))
 

    return render_template("requeststudent.html" , **locals())


    