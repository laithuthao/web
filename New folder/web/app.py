from flask import Flask

# 1. Create app/server
app=Flask(__name__) 

# 2. Building route
# function binding (dinh ham def voi thu gi do)
@app.route("/")
def home():
    return "C4E34"

@app.route("/say-hi")
def say_hi():
    return "Hi everyone"

@app.route("/say-hi/<name>/<age>")
def say_hi_everyone(name, age):
    return "Hi {0}, {1} years old".format(name, age)

@app.route("/add/<int:va1>/<int:va2>")
def add(va1, va2):
    total = va1 + va2
    return str(total)

# 3. Run server
if __name__ == "__main__": #De xac dinh day la server chu hay server phu
    app.run(debug=True) #De cho no chay lien tuc va tu dong update cac code minh thay doi
