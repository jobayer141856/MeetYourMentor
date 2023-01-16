from app import*



@app.route('/findmentor', methods=['GET','POST'])
def findmentor():
    stdx = False
    mentx = False
    if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
            stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True
        if request.method == 'POST':
            form_subjects = request.form["subject"]
            form_medium = request.form["medium"]
            form_classes = request.form["class"]
            form_gender = request.form["gender"]
            form_city = request.form["city"]
            form_area = request.form["area"]
            print(request.form)
           
            name = []
            occupation = []
            institution = []
            experience = []
            salary = []
            gender1 = []
            tmethod = []
            city1= []
            area1 = []
            subjects1 = []
            classes1 = []
            medium1 = []
            id = []
            cnt = 0
            for userx in db_mentor_academic.find({'gender': form_gender}):
                if form_subjects in userx["subject"] and form_medium in userx["medium"] and form_classes in userx["class"] and form_area in userx["area"]:
                    print(form_city)
                    print("whooooo")
                    print(userx)
                    id.append(userx["_id"])
                    name.append(userx["name"])
                    occupation.append(userx["occupation"])
                    institution.append(userx["institution"])
                    experience.append(userx["experience"])
                    salary.append(userx["salary"])
                    gender1.append(userx["gender"])
                    tmethod.append(userx["tmethod"])
                    city1.append(userx["city"])
                    area1.append(userx["area"])
                    subjects1.append(userx["subject"])
                    classes1.append(userx["class"])
                    medium1.append(userx["medium"])
                    cnt = cnt+1
            return render_template("findmentorbysearch.html", **locals())
          
        name = []
        occupation = []
        institution = []
        experience = []
        salary = []
        gender = []
        tmethod = []
        city= []
        area = []
        subjects = []
        classes = []
        medium = []
        id = []
        cnt = 0
        for x in db_mentor_academic.find():
            id.append(x["_id"])
            name.append(x["name"])
            occupation.append(x["occupation"])
            institution.append(x["institution"])
            experience.append(x["experience"])
            salary.append(x["salary"])
            gender.append(x["gender"])
            tmethod.append(x["tmethod"])
            city.append(x["city"])
            area.append(x["area"])
            subjects.append(x["subject"])
            classes.append(x["class"])
            medium.append(x["medium"])
            cnt = cnt+1
        return render_template("findmentor.html", **locals())
    else:
        return redirect(url_for("login"))

