from app import *

@app.route('/change_pass', methods=['GET', 'POST'])
def change_pass():
    if request.method == 'POST':
        stdx = False
        mentx = False
        if 'username' in session:
            username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True
        password = request.form["oldpass"]
        password1 = request.form["newpass"]
        password2 = request.form["newconfpass"]

        if password1 != password2:
            return "both new password should be same"


        id_x = db_mentor.find_one({'username': username})
        id_x2 = db_std.find_one({'username': username})
        if id_x:
            passcheck = id_x['password']
        if id_x2: 
            passcheck = id_x2['password']

        if bcrypt.checkpw(password.encode('utf-8'), passcheck):
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            if id_x:
                db_mentor.update_one({'_id': id_x['_id']}, {
                                "$set": {"password": hashed}})
            if id_x2:
                db_std.update_one({'_id': id_x2['_id']}, {
                                "$set": {"password": hashed}})
            return redirect("/login")
        else:
            return "old password don't match"

    return render_template("change_pass.html" , **locals())
