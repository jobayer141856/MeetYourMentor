from app import*
from datetime import datetime
from bson.objectid import ObjectId

@app.route('/stdpost', methods=['GET','POST'])
def stdpost(): 
    exist = False
    ex = db_std_thoughts.find_one({'username': session['username']})
    if ex:
        exist = True
    if request.method == "POST":
        name = request.form['name']
        occupation = request.form['occupation']
        message = request.form['message']
        username =  session['username']

        stdpost2 = {'username': username, 'name': name, 'occupation' :occupation, 'message':message, 'current_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
        db_std_thoughts.insert_one(stdpost2)
        return redirect(url_for('stdpost'))

    name = []
    occupation = []
    message = []
    current_time = []
    username = []
    id = []
    cnt = 0
    for z in db_std_thoughts.find():
        name.append(z["name"])
        occupation.append(z["occupation"])
        current_time.append(z["current_time"])
        username.append(z["username"])
        message.append(z["message"])
        id.append(z["_id"])
        cnt += 1
        
    return render_template("stdpost.html", **locals())

@app.route('/deletestd/<string:s>',  methods=['GET', 'POST'])
def deletestd(s):
    if "username" in session:
        username = session["username"]
        s = str(s)
        print("Object id " +s)
        print("username: "+ username)
        for x in db_std_thoughts.find({"username": username}):
            id = x["_id"]
            print(str(id))
            if str(id) == s:
                db_std_thoughts.delete_many({'_id': ObjectId(s)})
                return redirect(url_for('stdpost'))

    return render_template("stdpost.html", **locals())