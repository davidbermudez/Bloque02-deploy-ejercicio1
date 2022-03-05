from flask import Flask, render_template
from datetime import datetime
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')

@app.route("/")
def index():
    # Get current date and time
    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1  

    # Overwrite the count
    f = open("count.txt", "w")  
    f.write(str(count)) 
    f.close()   

    # Render HTML with count variable
    return render_template("index.html", count=count, the_time=the_time, tema="gold")


if __name__ == "__main__":
    app.run()
