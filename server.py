from flask import Flask,render_template
import requests

app=Flask(__name__)
@app.route("/geuss/<name>")
def geuss(name):
    url=f"https://api.genderize.io?name={name}"
    response=requests.get(url)
    data=response.json()
    gender=data["gender"]
    url2=f"https://api.agify.io?name={name}"
    response2=requests.get(url2)
    data2=response2.json()
    age=data2["age"]
    return render_template("index.html",name=name,gender=gender,age=age)

if __name__=="__main__":
    app.run(debug=True)
