from app import*



@app.route('/findmentor', methods=['GET','POST'])
def findmentor():
    stdx = False
    mentx = False
    if 'username' in session:
        if db_std.find_one({'username':session['username']}):
            stdx = True
        if db_mentor.find_one({'username':session['username']}):
            mentx = True
        if request.method == 'POST':
            subjects = request.form["subject"]
            medium = request.form["medium"]
            classes = request.form["class"]
            gender = request.form["gender"]
            city = request.form["city"]
            area = request.form["area"]
            gender = str(gender)
            city = str(city)

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
            for user in db_mentor_academic.find({'gender': gender, 'city': city}):
                if subjects in user["subject"] and medium in user["medium"] and classes in user["class"] and area in user["area"]:
                    print(city)
                    print("whooooo")
                    print(user)
                    id.append(user["_id"])
                    name.append(user["name"])
                    occupation.append(user["occupation"])
                    institution.append(user["institution"])
                    experience.append(user["experience"])
                    salary.append(user["salary"])
                    gender1.append(user["gender"])
                    tmethod.append(user["tmethod"])
                    city1.append(user["city"])
                    area1.append(user["area"])
                    subjects1.append(user["subject"])
                    classes1.append(user["class"])
                    medium1.append(user["medium"])
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

