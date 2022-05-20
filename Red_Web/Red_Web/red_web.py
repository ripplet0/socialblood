import smtplib

from flask import Flask,render_template,request,session,redirect,url_for,flash
from DBConnection import Db
from itsdangerous import URLSafeSerializer
from flask_mail import Message,Mail,MIMEText,MIMEBase
import os

app = Flask(__name__)
# app.config['MAIL_SERVER']='localhost'
# app.config['MAIL_PORT'] = 1025
# app.config['MAIL_USERNAME'] =os.environ.get(My_Email')
# app.config['MAIL_PASSWORD'] = os.environ.get('My_sheet')
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

app.secret_key="abc"
mail=Mail(app)


@app.errorhandler(404)
def not_found(error):
        return render_template('Error/404.html'), 404



'''-----------------------------------------------------------------------------------------------------------------------------------
                                                  Admin Module
   -----------------------------------------------------------------------------------------------------------------------------------'''
@app.route('/logout')
def logout():
    session.clear()
    session['log']=""
    return redirect('/')


@app.route('/',methods=['get','post'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        db=Db()
        ss=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if ss is not None:
            if ss['usertype']=="admin":
                session['log']="lin"
                return redirect(url_for('admin_home'))
            elif ss['usertype']=="bank":
                session['log'] = "lin"
                session['b_id']=ss['login_Id']
                return redirect(url_for('myhome'))
            elif ss['usertype']=="user":
                session['log'] = "lin"
                session['u_id'] = ss['login_Id']
                return redirect(url_for('home'))
            else:
                return '''<script>alert("Invalid Username/Password");window.location="/"</script>'''

        else:
            return '''<script>alert("Invalid Username/Password");window.location="/"</script>'''
    else:
        return render_template('login/login1.html')



@app.route('/forgot',methods=['GET','POST'])
def forgot():
    db=Db()
    if request.method=='POST':
        email=request.form['textfield']
        otp=db.selectOne("select password from login where username='"+email+"'")
        # otp=session['otp']
        # print(otp)
        qry = db.selectOne("select * from user,blood_bank where user.email='" + email + "' or blood_bank.email='"+email+"' ")
        if qry is not None:

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login(email, passwww )

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("CURRENT PASSWORD IS "+str(otp))

            msg['Subject'] = 'EMISSION VALIDITY'

            msg['To'] = email

            msg['From'] = 'redapp516@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("Mail Send successfully");window.location='/'</script>'''

    return render_template('Password Manager/forgotten_pass.html')



@app.route('/Pchange',methods=['get','post'])
def Pchange():
    if request.method=='post':
        new_password=request.form['password']
        confirm_pass=request.form['conform']
        if new_password==confirm_pass:
            db=Db()
            x=db.update("update login set password='"+new_password+"' where login.login_Id='"+str(session['u_id'])+"' or login.login_Id='"+str(session['b_id'])+"'")
            return '''<script>alert("Success");window.location="/"</script>'''
        else:
            return '''<script>alert("password  does't match ");window.location='/Pchange'</script>'''

    return render_template('Password Manager/new_password.html')


@app.route('/admin_home')
def admin_home():
    if session['log']=="lin":
         return render_template('admin/AdminHome.html')
    else:
        return redirect('/')


@app.route('/accept_bank')
def accept_bank():
    if session['log'] == "lin":
        db=Db()
        ss=db.select("select * from blood_bank,login where blood_bank.bank_id=login.login_Id and login.usertype='bank'")
        return render_template('admin/accepted_bank_view.html',data=ss)
    return redirect('/')

'''
@app.route('/acceptReject_users')
def acceptReject_users():
    db=Db()
    ss=db.select("select * from user,login where user.user_id=login.login_Id and login.usertype='pending'")
    return render_template('admin/admin_view.html',data=ss)
'''

@app.route('/accepted_users/<p>')
def accepted_users(p):
    if session['log'] == "lin":
        db=Db()
        db.update("update user_request set status='user' where user_request_id='"+str(p)+"'")

        return '<script>alert("accepted");window.location="/user_requests"</script>'
    else:
        return redirect('/')

@app.route('/view_blood_bank')
def view_blood_bank():
    if session['log'] == "lin":
        db=Db()
        ss=db.select("select * from  blood_bank,login where blood_bank.bank_id=login.login_Id and login.usertype='pending'")
        return render_template('admin/blood_bankaccept.html',data=ss)
    else:
        return redirect('/')

@app.route('/view_user')
def view_user():
    if session['log'] == "lin":
        db=Db()
        ss=db.select("select * from user,login where login.login_Id=user.user_id and login.usertype!='pending'")
        return render_template('admin/viewUser.html',data=ss)
    return redirect('/')

@app.route('/feedback')
def feedback():
    if session['log'] == "lin":
        db=Db()
        s=db.select("select * from feedback,user where feedback.user_id=user.user_id")
        return  render_template('admin/feedbackView.html',data=s)
    else:
        return redirect('/')




@app.route('/accepted_bank/<p>')
def accepted_bank(p):

        db=Db()
        db.update("update login set usertype='bank' where login_Id='"+str(p)+"'")
        return '<script>alert("accepted");window.location="/view_blood_bank"</script>'

@app.route('/rejected_bank/<p>')
def rejected_bank(p):
    db=Db()
    db.delete("delete from login where login_Id='"+str(p)+"'")
    db.delete("delete from blood_bank where bank_id='"+str(p)+"'")

    return '<script>alert("rejected");window.location="/view_blood_bank"</script>'

@app.route('/rejected_donor/<p>')
def rejected_donor(p):
    db=Db()
    db.delete("delete from user_request where user_request_id='"+str(p)+"'")
    return '<script>alert("rejected");window.location="/user_requests"</script>'


'''-------------------------------------------------------------------------------------------------------------------------------------------
                                                       Bank Module
   --------------------------------------------------------------------------------------------------------------------------------------------
'''
@app.route('/myhome')
def myhome():
    return render_template('bank/bank_home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['textfield']
        place=request.form['textfield2']
        pin=request.form['textfield3']
        phone=request.form['textfield4']
        db = Db()
        s = db.select("select phone from blood_bank where phone='"+phone+"'")
        for i in s:
            return '''<script>alert("this phone number already taken");window.location="/register"</script>'''
        else:
            pass
        email=request.form['textfield6']
        db = Db()
        s = db.select("select email from blood_bank where email='" + email + "'")
        for i in s:
            return '''<script>alert("this email already exist");window.location="/register"</script>'''
        else:
            pass
        password=request.form['textfield5']
        confirm_password=request.form['textfield7']
        if password==confirm_password:
            db=Db()
            re=db.insert("insert into login (username,password,usertype) VALUES ('"+email+"','"+password+"','pending')")
            db.insert("insert into blood_bank values('"+str(re)+"','"+name+"','"+place+"','"+pin+"','"+phone+"','"+email+"')")
            return '''<script>alert("Success");window.location="/"</script>'''
        else:
            return '''<script>alert("Passwords are not matching");window.location="/register"</script>'''

    else:
        return render_template('bank/registeration.html')
'''
@app.route('/logout')
def logout():
     session.pop('b_id', None)
     return render_template('login1.html') '''

'''
@app.route('/manage_donor')
def manage_donor():
    db=Db()
    ss=db.select("select * from donor,login where donor.donor_id=login.login_Id and login.usertype='pending'")
    return render_template('bank/donor_add_remove.html',data=ss)
'''

@app.route('/donor')
def donor():
    return render_template('Bank/approve_donor.html')

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        Blood_Group=request.form['select']
        unit=request.form['textfield2']
        db=Db()
        s=0
        q=db.selectOne("select * from stock where blood_group='"+Blood_Group+"' and blood_bank_id='"+str(session['b_id'])+"'")
        if q:
            unit1=q['unit']
            sid=q['stock_id']
            s=int(unit)+int(unit1)
            db.update("update stock set unit='"+str(s)+"' where stock_id='"+str(sid)+"'")
            return '''<script>alert("Success");window.location="/add_stock"</script>'''
            #return "ok"
        else:
            db.insert("insert into stock values('','"+str(session['b_id'])+"','"+Blood_Group+"','"+unit+"')")
            return '''<script>alert("Success");window.location="/add_stock"</script>'''
    else:
        return  render_template('bank/stock_add.html')

@app.route('/blood_stock')
def view_stock():
    db=Db()
    print(str(session['b_id']))
    ss=db.select("select * from blood_bank,stock where blood_bank.bank_id=stock.blood_bank_id and stock.blood_bank_id='"+str(session['b_id'])+"'")

    return render_template('bank/stock_view.html',data=ss)


@app.route('/donor_requests')
def donor_requests():

    return render_template('admin/blood_bankaccept.html')


@app.route('/user_requests')
def user_requests():
    db=Db()
    print(session['b_id'])
    s=db.select("select * from user_request,user where user_request.user_id=user.user_id AND blood_bank_id='"+str(session['b_id'])+"' and status='pending'")
    print(s)
    return  render_template('bank/approve_user.html',data=s)


# @app.route('/accepted_user_requset/<t>')
# def accepted_user(t):
#     db=Db()
#     db.update("update user_request set status='accepted' where user_request_id='"+t+"'")
#     return '''<script>alert("Accepted");window.location="/myhome"</script>'''

# @app.route('/rejected_user/<a>')
# def rejected_user(a):
#     db=Db()
#     db.update("update user_request set status='rejected' where user_request_id='"+a+"'" )
#     return '''<script>alert("Rejected");window.location="/myhome"</script>'''


'''-------------------------------------------------------------------------------------------------------------------------------------
                                                    User Module
  -----------------------------------------------------------------------------------------------------------------------------------------'''

@app.route('/home')
def home():
   return render_template('user/user_home.html')


@app.route('/create_acc',methods=['GET','POST'])
def create_acc():
    if request.method=='POST':
        username=request.form['textfield']
        blood_group=request.form['select']
        gender=request.form['select0']
        phone=request.form['textfield3']
        db = Db()
        s = db.select("select phone from user where phone='" + phone + "'")
        for i in s:
            return '''<script>alert("this phone number already taken");window.location="/register"</script>'''
        else:
            pass
        email=request.form['textfield2']
        db = Db()
        s = db.select("select email from user where email='" + email + "'")
        for i in s:
            return '''<script>alert("this email number already exist");window.location="/register"</script>'''
        else:
            pass
        address=request.form['textarea']
        password=request.form['textfield4']
        confirm_password=request.form['textfield6']
        if password==confirm_password:
            db=Db()
            rs=db.insert("insert into login(username,password,usertype)VALUES('"+username+"','"+password+"','user') ")
            db.insert("insert into user VALUES('"+str(rs)+"','"+username+"','"+gender+"','"+phone+"','"+address+"','"+email+"','"+blood_group+"')")
            return '''<script>alert("Success");window.location="/"</script>'''
        else:
            return '''<script>alert("Password not matching");window.location="/create_acc"</script>'''
    else:
        return render_template('user/uregister.html')


@app.route('/donor_reg',methods=['GET','POST'])
def donor_reg():

    if request.method=='POST':
        name=request.form['textfield']
        blood_group=request.form['select']
        place=request.form['textfield2']
        post=request.form['textfield3']
        pin=request.form['textfield4']
        state=request.form['textfield5']
        phone=request.form['textfield1']
        email=request.form['textfield6']
        av=request.form['select2']
        district=request.form['select3']
        print(email,phone)

        db = Db()
        s = db.selectOne("select * from user where email='" + email + "' and phone='"+phone+"'  ")
        if s is not None:
            db = Db()
            db.insert("insert into donor VALUES('" + str(s['user_id']) + "','" + name + "','" + blood_group + "','" + phone + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + state + "','"+email+"')")
            return '''<script>alert("Success");window.location="/donor_reg"</script>'''
        else:
            return '''<script>alert("verification failed");window.location="/donor_reg"</script>'''
    else:
        return render_template('user/donor_reg.html')



'''@app.route('/logout')
def logout():
     session.pop('u_id', None)
     return render_template('login1.html')'''

@app.route('/view_bank')
def view_bank():
    db=Db()
    s=db.select("select * from blood_bank")
    return render_template('user/view_bank.html',data=s)

@app.route('/user_request/<i>',methods=['get','post'])
def user_request(i):
    if request.method=='POST':
        bd=request.form['select']
        unit=request.form['textfield2']

        db=Db()
        db.insert("insert into user_request VALUES ('','"+str(session['u_id'])+"',curdate(),'"+i+"','"+unit+"','pending','"+bd+"')")
        return '''<script>alert("Your request sended successfully");window.location="/home"</script>'''
    else:
        db=Db()
        res=db.select("select * from blood_bank ")
        return  render_template("user/user_request.html")

@app.route('/donate')
def donate():
    db=Db()
    d=db.select("select * from blood_bank")
    return render_template('user/donate.html',data=d)


@app.route('/ufeedback',methods=['GET','POST'])
def feedbacks():
    if request.method=='POST':
        feedback=request.form['textarea']
        db=Db()
        s=db.insert("insert into feedback values('','"+feedback+"','"+str(session['u_id'])+"',curdate())")
        return '''<script>alert("success");window.location="/ufeedback"</script>'''

    else:
        return render_template('user/feedback.html')

@app.route('/ustatus')
def ustatus():
    db=Db()
    c=db.select("select * from user_request,user where  user_request.user_id=user.user_id and user_request.user_id='"+str(session['u_id'])+"'")
    return render_template('user/status.html',data=c)




if __name__ == '__main__':
    app.run(port=4000)






