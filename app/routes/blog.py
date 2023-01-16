from app import*
from datetime import datetime
from bson.objectid import ObjectId

@app.route('/blogs', methods=['GET','POST'])
def blogs():
    stdx = False
    mentx = False
    if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True
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
    
    return render_template("blog.html", **locals())