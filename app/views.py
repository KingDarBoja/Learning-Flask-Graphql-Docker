from app import app

# Default route for our WSGI app
@app.route("/")
def index():
    return "Hello World!"

# Another route just for showcasing
@app.route("/about")
def about():
    return "<h1 style='color: blue'>ABOUT !!</h1>"
    