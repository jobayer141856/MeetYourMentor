from app import*

@app.route('/stdpost', methods=['GET','POST'])
def stdpost(): 
    if request.method == "POST":
        name = request.form['name']
        occupation = request.form['occupation']
        message = request.form['message']
        username =  session['username']

        stdpost2 = {'username': username, 'name': name, 'occupation' :occupation, 'message':message }
        db_std_thoughts.insert_one(stdpost2)
        return redirect(url_for('home'))
        
    return render_template("stdpost.html", **locals())