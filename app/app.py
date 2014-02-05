from flask import Flask,request,Response,render_template,g,jsonify,url_for,redirect
from config import Config


if __name__ == '__main__' :

	app = Flask(__name__, static_url_path="/static/executive")      
	
else :
	
	app = Flask(__name__, static_url_path="/static")      


app.config.from_object(Config)




 
@app.route('/support/executive/')
@app.route('/support/executive/index.html')
def support():
	page=request.args.get('page')
	return render_template("site.html",page=page)

@app.route('/support/executive/faq.html')
def faq():
	return redirect("/support/executive/index.html?page=faq")
 

@app.route('/support/executive/screenshots.html')
def screenshots():
	return redirect("/support/executive/index.html?page=screen")

 
if __name__ == '__main__':
	app.run(debug=True)
