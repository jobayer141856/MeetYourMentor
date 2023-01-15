from app import*
@app.route('/', methods=['GET','POST'])
def home(): 
    std = 0
    ment = 0
    stpost = 0
    stdx = False
    mentx = False
    for x in db_std.find():
        std+=1
    for y in db_mentor.find():
        ment += 1
    for z in db_post_for_mentor.find():
        stpost += 1
    if 'username' in session:
        username = session["username"]
        if db_std.find_one({'username':username}):
             stdx = True
        if db_mentor.find_one({'username':username}):
            mentx = True

    return render_template("index.html", **locals())
