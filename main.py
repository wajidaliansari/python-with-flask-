#integrate HTML with Flask
#HTTP verb GET and POST


#jinja2 template
...
##{%...%} for for loop statement
##{{   }} expressions to print output
##{#....#}this is for comment 
...
from flask import Flask,redirect,url_for,render_template,request
###WSGI Application

app = Flask(__name__)
@app.route('/')
def welcome(): 
   return render_template('index.html')

@app.route('/success/<int:score>')
def success(score): 
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

    
###Building Url Dynamically In Flask Web Framework
###building Url Dynamically
###Variable Rules And URL Building

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is " + str(score)

###result cheker 
@app.route('/result/<int:marks>')
def check_marks(marks):
    if marks < 50:
        print("Fail")
    else:
        print("Pass")

    return redirect(url_for(result,score=marks))   
 
### result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
     science=float(request.form['science'])    
     maths=float(request.form['maths']) 
     c=float(request.form['c']) 
     data_science=float(request.form['datascience']) 
     total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score)) 
   

if __name__=='__main__':
   app.run(debug=True)