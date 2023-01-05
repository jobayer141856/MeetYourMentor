from app import*

@app.route('/findstudents', methods=['GET','POST'])
def findstudents(): 
    
   if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True

        if request.method == 'POST':
            subjects = request.form["subject"]
            medium = request.form["medium"]
            classes = request.form["class"]
            city = request.form["city"]
            area = request.form["area"]
            city = str(city)

            name = []
            number = []
            salary = []
            tmethod = []
            gender1 = []
            city1= []
            area1 = []
            subjects1 = []
            classes1 = []
            medium1 = []
            id = []
            cnt = 0
            for user in db_post_for_mentor.find({'city': city}):

                if subjects in user["subject"] and medium in user["medium"] and classes in user["class"] and area in user["area"]:
                    print(city)
                    print("whooooo")
                    print(user)
                    id.append(user["_id"])
                    name.append(user["name"])
                    number.append(user["number"])
                    salary.append(user["salary"])
                    gender1.append(user["gender"])
                    tmethod.append(user["tmethod"])
                    city1.append(user["city"])
                    area1.append(user["area"])
                    subjects1.append(user["subject"])
                    classes1.append(user["class"])
                    medium1.append(user["medium"])
                    cnt = cnt+1
            return render_template("resultfindstudent.html", **locals())
          
        name = []
        occupation = []
        number = []
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
        for user in db_post_for_mentor.find():
            id.append(user["_id"])
            name.append(user["name"])
            number.append(user["number"])
            salary.append(user["salary"])
            gender.append(user["gender"])
            tmethod.append(user["tmethod"])
            city.append(user["city"])
            area.append(user["area"])
            subjects.append(user["subject"])
            classes.append(user["class"])
            medium.append(user["medium"])
            cnt = cnt+1
        return render_template("findastudent.html", **locals())

   else:
       return redirect(url_for("login"))
