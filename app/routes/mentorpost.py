from app import*
from datetime import datetime
from bson.objectid import ObjectId

@app.route('/mentorpost', methods=['GET','POST'])
def mentorpost(): 
    exist = False
    ex = db_mentor_thoughts.find_one({'username': session['username']})
    if ex:
        exist = True

    if request.method == "POST":
        name = request.form['name']
        occupation = request.form['occupation']
        message = request.form['message']
        username =  session['username']
        
        post = {'username': username, 'name': name, 'occupation' :occupation, 'message':message, 'current_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
        db_mentor_thoughts.insert_one(post)
        return redirect(url_for('mentorpost'))
    
    name = []
    occupation = []
    message = []
    current_time = []
    username = []
    id = []
    cnt = 0
    for z in db_mentor_thoughts.find():
        name.append(z["name"])
        occupation.append(z["occupation"])
        current_time.append(z["current_time"])
        username.append(z["username"])
        message.append(z["message"])
        id.append(z["_id"])
        cnt += 1
    
    return render_template("mentorpost.html", **locals())



@app.route('/delete/<string:s>',  methods=['GET', 'POST'])
def delete(s):
    if "username" in session:
        username = session["username"]
        s = str(s)
        print("Object id " +s)
        print("username: "+ username)
        for x in db_mentor_thoughts.find({"username": username}):
            id = x["_id"]
            print(str(id))
            if str(id) == s:
                db_mentor_thoughts.delete_many({'_id': ObjectId(s)})
                return redirect(url_for('mentorpost'))

    return render_template("mentorpost.html", **locals())


@app.route('/postblog', methods=['GET','POST'])
def postblog(): 

    if request.method == "POST":
        title = request.form['title']
        blog = request.form['blog']
        username =  session['username']
        x = db_mentor.find_one({'username': username})
        name = x['name']
        post = {'username': username, 'name': name, 'title' :title, 'blog':blog, 'current_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
        db_post_blog.insert_one(post)
        return redirect(url_for('postblog'))
    
    name = []
    title = []
    blog = []
    current_time = []
    username = []
    id = []
    cnt = 0
    for z in db_post_blog.find():
        name.append(z["name"])
        title.append(z["title"])
        current_time.append(z["current_time"])
        username.append(z["username"])
        blog.append(z["blog"])
        id.append(z["_id"])
        cnt += 1
    
    return render_template("postblog.html", **locals())


@app.route('/delete_post/<string:s>',  methods=['GET', 'POST'])
def delete_post(s):
    if "username" in session:
        username = session["username"]
        s = str(s)
        print("Object id " +s)
        print("username: "+ username)
        for x in db_post_blog.find({"username": username}):
            id = x["_id"]
            print(str(id))
            if str(id) == s:
                db_post_blog.delete_many({'_id': ObjectId(s)})
                return redirect(url_for('postblog'))

    return render_template("postblog.html", **locals())