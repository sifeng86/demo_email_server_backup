from flask import Flask,request 
import sendmail_api


app = Flask(__name__)

@app.route("/")
@app.route('/', methods = ['POST'])
def send_mail():
    if request.method == 'POST':
       email = request.form['email']
       server = request.form['emailserver']
       message = request.form['message']
       if server == '200':
            sendmail_api.sendgrid_send(email,message)
            return 'sent by Primary Server:sendgrid'
       elif server == '400':
            sendmail_api.custom_send(email,message)
            return 'sent by Secondary Server:cachigo'
       else:
            return 'something wrong'
    else:
        return 'something wrong'
    
if __name__ == "__main__":
    app.run(debug=True)