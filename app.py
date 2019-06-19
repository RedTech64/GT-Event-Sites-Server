import os

from flask import Flask,render_template
from google.cloud import firestore

db = firestore.Client();

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello"

@app.route('/<path:path>')
def catch_all(path):
    target = os.environ.get('TARGET', 'World')
    print(path)
    try:
        data = db.collection(u'sites').document(path).get()
        data = data.to_dict()
        siteData = SiteData("{}".format(data[u"title"]),"{}".format(data[u"description"]))
        return render_template('template.html',siteData = siteData)
    except Exception as e:
        print(e)
        return "404"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
	
class SiteData:
    def __init__(self,title,description):
        self.title = title
        self.description = description