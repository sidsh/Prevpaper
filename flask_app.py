import sqlite3
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
import pymysql
import sqlalchemy.dialects.sqlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///paper_database.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"
db = SQLAlchemy(app)   #db object
data_base = 'paper_database.db'
class sem1(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem2(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
   
class sem3(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.Integer, nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem4(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem5(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem6(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)

class sem7(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem8(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String,nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)

db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload_papers():
    return render_template("upload_download.html",param_btn="upload",param="Upload your papers make selection appropriately")

@app.route("/about")
def About():

    return render_template("about.html")
@app.route("/getpapers")
def gwtpaper():

    return  render_template("upload_download.html",param_btn="get-papers",param="Download your papers make selection appropriately")

#below fxn gets value from drop of semster in upload paper
@app.route("/fetch_sem_upload_download" , methods=['GET', 'POST'])
def return_sem():
    #select = request.form['sem']
    select = request.form.get('sem')
    
    #makin this var global so i can use sem value in other fxns
    global sem_keep
    sem_keep=str(select) 
    radio_val = request.form['upload_download']
    radio_val=request.form.get('upload_download')
    if str(radio_val)=='upload':
        return render_template('uploadtemplate.html',param=str(select),param1=str(radio_val))
    elif str(radio_val=='download'):
        return render_template('download.html',param=str(select),param1=str(radio_val))
      
        
        
        

@app.route("/upload_papertodb" , methods=['GET', 'POST'])
def upload_papertodb():
    subject_get=request.form['subject']
    batch_get = request.form['batch']
    papertype_get = request.form['papertype'].upper()
    
    paper_file = request.files['paper'].read()#request.files['paper']
    global save_Sem_Status
    save_Sem_Status=sem_keep
    print("save sem is ",save_Sem_Status)
    if(request.method=='POST' and save_Sem_Status=='semster1' ):
        entry = sem1(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")
    elif(request.method=='POST' and save_Sem_Status=='semster2' ):
        entry = sem2(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster3' ):
        entry = sem3(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster4' ):
        entry = sem4(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster5' ):
        entry = sem5(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")   
    elif(request.method=='POST' and save_Sem_Status=='semster6' ):
        entry = sem6(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")    
    
    elif(request.method=='POST' and save_Sem_Status=='semster7' ):
        entry = sem7(subject=subject_get,batch=batch_get,papertype=papertype_get)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster8' ):
        entry = sem8(subject=subject_get,batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    else:
        return render_template("uploadtemplatte.html")
paper_file = request.files['paper'].read()
paper_file.decode('base64')


@app.route("/download_paper" , methods=['GET', 'POST'])
def download_paper():
    with sqlite3.connect(data_base) as conn:
        cursor =conn.cursor()
        cursor.execute("""SELECT * FROM sem1""")
        save_Sem_Status=sem_keep
       
        
        if(request.method=='POST' and save_Sem_Status=='semster1' ):
            row = sem1.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster2' ):
            row = sem2.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster3' ):
            row = sem3.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster4' ):
            row = sem4.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster5' ):
            row = sem5.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster6' ):
            row = sem6.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster7' ):
            row = sem7.query.all()
        elif(request.method=='POST' and save_Sem_Status=='semster8' ):
            row = sem8.query.all()
        else:
            return render_template("sorry.html")
    return render_template("paper_show.html",param=row)

if __name__ == "__main__":
    app.run(debug=True,port=1125)    
