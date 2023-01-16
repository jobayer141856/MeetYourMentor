from app import*
from bson.objectid import ObjectId
app.config['UPLOAD_FOLDER'] = '../static/images/'
app.config['SECRET_KEY'] = 'supersecretkey'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/mentorprofile', methods=['GET','POST'])
def mentorprofile():
    username = session['username']
    id_x = db_mentor.find_one({'username':username})
    username = id_x["username"]
    email = id_x['email']
    number = id_x['number']
    fname = id_x['profile_pic']
    name = id_x['name']

    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.filename = id_x["username"]
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        fname=file.filename
        db_mentor.update_one({'_id':id_x['_id']}, {"$set" : {"profile_pic" :fname}})
        return render_template('mentorprofile.html', **locals())

    if request.method=='POST':
        name = request.form["name"]
        number = request.form["number"]

        db_mentor.update_one({'_id':id_x['_id']}, {"$set" : {"name" :name}})
        db_mentor.update_one({'_id':id_x['_id']}, {"$set" : {"number" :number}})

        return redirect(url_for("mentorprofile"))

    return render_template("mentorprofile.html" , **locals())


@app.route('/mentordash', methods=['GET','POST'])
def mentordash():
    std_name = []
    std_email = []
    std_msg = []
    current_time = []
    id = []
    cnt = 0
    username = session['username']
    for z in db_request_mentor.find():
        if username == z['std_username']:
            std_name.append(z["std_name"])
            std_email.append(z["email"])
            current_time.append(z["current_time"])
            std_msg.append(z["message"])
            id.append(z["_id"])
            cnt += 1
    return render_template("mentordash.html", **locals())


@app.route('/delete_ment/<string:s>',  methods=['GET', 'POST'])
def delete_ment(s):
    if "username" in session:
        username = session["username"]
        s = str(s)
        print("Object id " +s)
        db_request_student.delete_many({'_id': ObjectId(s)})
        return redirect(url_for('mentordash'))

    return render_template("mentordash.html", **locals()) 