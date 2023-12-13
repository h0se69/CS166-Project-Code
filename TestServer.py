from flask import Flask, request, Response, render_template
from flask_limiter.util import get_remote_address

flaskobj = Flask(__name__)

# Random function to simulate a long process in upload like a blog idk what else to put lol
def testing_upload_post_function(post_id):
    if(post_id <= 1):
        return post_id
    return testing_upload_post_function(post_id - 1) + testing_upload_post_function(post_id - 2)


@flaskobj.route("/blog/api/upload-post/<int:post_id>")
def api_upload_post(post_id):
    request_user_ip_address = request.remote_addr
    try:
        outcome = testing_upload_post_function(post_id)
        return f"{outcome} | USER_IP: {request_user_ip_address}"
    except:
        return f"UPLOAD SIMULATION ERROR"

    
@flaskobj.route("/")
def home():
    return render_template("HomePage.html")


flaskobj.run(debug=True, port=9999)
