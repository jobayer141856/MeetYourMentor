from app import*

@app.route('/mentorpost', methods=['GET','POST'])
def mentorpost(): 
    if request.method == "POST":
        name = request.form['name']
        occupation = request.form['occupation']
        message = request.form['message']
        username =  session['username']
        post = {'username': username, 'name': name, 'occupation' :occupation, 'message':message }
        db_mentor_thoughts.insert_one(post)
        return redirect(url_for('home'))
    return render_template("mentorpost.html", **locals())