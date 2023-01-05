from app import*

@app.route('/register', methods=['GET','POST'])
def register(): 
    return render_template("register.html", **locals())

@app.route('/mentor_register', methods=['GET','POST'])
def m_register():
     
    if request.method=='POST':
        username = request.form["username"]
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["number"]
        password1 = request.form["pass1"]
        password2 = request.form["pass2"]
        print(request.form)
        print(number)

        if " " in username:
            message = 'Username should not have any space'
            return message  
        user_found = db_mentor.find_one({"username": username})
        email_found = db_mentor.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return message
        elif email_found:
            message = 'This email already exists in database'
            return message
           
        elif len(number) != 11:
            return 'number invalid. must be 11 digit'
        
        elif number[0] != '0' and number[1] != '1':
                return 'Invalid Number Number will be start 0 and 1'
        elif password1 != password2:
            message = 'Passwords should match!'
            return message
        else:
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            # print(session[username])
            session["username"] = username
            session["name"] = name
            session["email"] = email
            session["password"] = hashed
            session["number"] = number
            session["user"] = 'mentor'
            return redirect(url_for("verify"))

    return render_template("mentorregister.html", **locals())

@app.route('/std_register', methods=['GET','POST'])
def std_register(): 
    if request.method=='POST':
        username = request.form["username"]
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["number"]
        password1 = request.form["pass1"]
        password2 = request.form["pass2"]
        print(request.form)

        if " " in username:
            message = 'Username should not have any space'
            return message  
        user_found = db_std.find_one({"username": username})
        email_found = db_std.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return message
        elif email_found:
            message = 'This email already exists in database'
            return message
        elif password1 != password2:
            message = 'Passwords should match!'
            return message
        elif len(number) != 11:
            return 'number invalid. must be 11 digit'
        elif number[0] != '0' and number[1] != '1':
            return 'Invalid Number Number will be start 0 and 1 '
        else:
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            session["username"] = username
            session["name"] = name
            session["email"] = email
            session["number"] = number
            session["password"] = hashed
            session["user"] = 'std'
            return redirect(url_for("verify"))

    return render_template("stdregister.html", **locals())