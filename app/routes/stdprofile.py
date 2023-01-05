from app import*
app.config['UPLOAD_FOLDER'] = '../static/images/'
app.config['SECRET_KEY'] = 'supersecretkey'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/stdprofile', methods=['GET','POST'])
def stdprofile():
    username = session['username']
    id_x = db_std.find_one({'username':username})
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
        db_std.update_one({'_id':id_x['_id']}, {"$set" : {"profile_pic" :fname}})
        return redirect(url_for("stdprofile"))

    if request.method=='POST':
        name = request.form["name"]
        number = request.form["number"]
        db_std.update_one({'_id':id_x['_id']}, {"$set" : {"name" :name}})
        db_std.update_one({'_id':id_x['_id']}, {"$set" : {"number" :number}})

        return redirect(url_for("stdprofile"))

    return render_template("stdprofile.html" , **locals())

@app.route('/stddash', methods=['GET','POST'])
def stddash():

    return render_template("stddashboard.html", **locals())