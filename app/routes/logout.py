from app import *


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.clear()
    return redirect("/")
