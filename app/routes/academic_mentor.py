from app import*

@app.route('/academic_mentor', methods=['GET','POST'])
def academic_mentor():
    username = session['username']
    db_x = db_mentor.find_one({'username':username})
    username = db_x["username"]
    email = db_x['email']
    number = db_x['number']
    name = db_x['name']

    db_x_p = db_mentor_academic.find_one({'username': username})
    if db_x_p:
        occupation = db_x_p['occupation']
        institution = db_x_p['institution']
        experience = db_x_p['experience']
        salary = db_x_p['salary']
        selfint = db_x_p['selfint']
        selfint = str(selfint)
        gender = db_x_p['gender']
        tmethod = db_x_p['tmethod']
        city = db_x_p['city']
        area = db_x_p['area']
        area = area.split(',')
        lena = len(area)
        print(area)
        classes = db_x_p['class']
        classes = classes.split(',')
        lenc = len(classes)
        print(classes)
        subjects = db_x_p['subject']
        subjects = subjects.split(',')
        lens = len(subjects)
        print(subjects)
        medium = db_x_p['medium']
        medium = medium.split(',')
        lenm = len(medium)

    if request.method=='POST':
        maoccupation = request.form['occupation']
        mainstitution = request.form['institution']
        maexperience = request.form['experience']
        masalary = request.form['salary']
        maselfint = request.form['selfint']
        magender = request.form['gender']
        matmethod = request.form['tmethod']
        macity = request.form['city']
        maarea = request.form['area']
        maclasses = request.form['class']
        masubjects = request.form['subject']
        mamedium = request.form['medium']
        
        db_amentor = db_mentor_academic.find_one({'username': username})
        if db_amentor:
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"name" :name}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"username" :username}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"email" :email}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"occupation" :maoccupation}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"institution" :mainstitution}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"experience" :maexperience}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"salary" :masalary}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"selfint" :maselfint}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"gender" :magender}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"tmethod" :matmethod}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"city" :macity}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"area" :maarea}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"class" :maclasses}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"subject" :masubjects}})
            db_mentor_academic.update_one({'_id':db_amentor['_id']}, {"$set" : {"medium" :mamedium}})

            return redirect(url_for('academic_mentor'))

        else:
            user_input = {'username': username, 'name': name, 'email': email, 'occupation': maoccupation, 'institution':mainstitution, 'experience': maexperience, 'salary': masalary, 'selfint':maselfint, 'gender': magender, 'tmethod':matmethod, 'city': macity, 'area':maarea, 'class':maclasses,'subject': masubjects,'medium':mamedium}
            db_mentor_academic.insert_one(user_input)
            return redirect(url_for('academic_mentor'))

    return render_template("mentoracademicprofile.html" , **locals())