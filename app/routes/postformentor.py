from app import*
@app.route('/postformentor', methods=['GET','POST'])
def postformentor(): 
    stdx = False
    mentx = False
    if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True
        if request.method == "POST":
            name = request.form["name"]
            number = request.form["number"]
            email = request.form["email"]
            gender = request.form["gender"]
            medium = request.form["medium"]
            classes = request.form["class"]
            city = request.form["city"]
            area = request.form["area"]
            tmethod = request.form["tmethod"]
            salary = request.form['salary']
            subjects = request.form["subject"]
            
            username = session['username']

            post = {'username': username,'name':name,'number':number, 'email':email, 'gender':gender,'medium':medium, 'class':classes, 'subject':subjects, 'city':city,'area':area, 'tmethod':tmethod,'salary':salary }
            db_post_for_mentor.insert_one(post)
            return redirect(url_for("home"))
        
        
        return render_template("postformentrequest.html", **locals())
    else:
       return redirect(url_for("login"))