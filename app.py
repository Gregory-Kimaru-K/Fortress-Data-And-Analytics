from flask import Flask, render_template
import secrets


temmplate_folder = 'temp/templates'
static_folder = 'temp/static'


app = Flask(__name__, template_folder=temmplate_folder, static_folder=static_folder)

# current_dir = os.path.abspath(os.path.dirname(__file__))
# database_path = os.path.join(current_dir, 'data.db')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)

app.config['SECRET_KEY'] = secrets.token_hex(16)

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     is_admin = db.Column(db.Boolean, default=True)
#     is_super = db.Column(db.Boolean, default=False)

# class Client(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=False, nullable=False)
#     tel_no = db.Column(db.String(30), unique=False, nullable=False)
#     email = db.Column(db.String(60), unique=False, nullable=False)
#     reason = db.Column(db.String(1000), unique=False, nullable=False)
#     description = db.Column(db.String(1000), unique=False, nullable=False)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# Services endpoints
@app.route("/services/tech_cosultance")
def tech_cosultance():
    return render_template("services/consulting.html")

@app.route("/services/bsintel")
def bsintel():
    return render_template("services/bsintel.html")

@app.route("/services/customsoftwaredev")
def customsoftware():
    return render_template('services/customsoftwaredev.html')


@app.route("/services/datawarehousing")
def datawarehousing():
    return render_template("services/datawarehousing.html")

@app.route("/services/webdev")
def webdev():
    return render_template("services/webdev.html")

@app.route("/services/product")
def product():
    return render_template("services/product.html")

@app.route("/services/softwaretesting")
def softwaretesting():
    return render_template("services/softwaretesting.html")

@app.route("/services/mobileapp")
def mobileapp():
    return render_template("services/mobileapp.html")

@app.route("/services/datavisualzation")
def datavisualzation():
    return render_template("services/datavisualization.html")

@app.route("/services/datascience")
def datascience():
    return render_template("services/datascience.html")


@app.route("/services/iot")
def iot():
    return render_template("services/iot.html")


# about endpoints

@app.route("/about/team")
def team():
    return render_template("about/team.html")

@app.route("/about/contact")
def contact():
    return render_template("about/contact.html")

@app.route("/about/privacypolicy")
def privacypolicy():
    return render_template("about/privacypolicy.html")


# technology endpoints
@app.route("/tech/backend")
def backend():
    return render_template("tech/backend.html")

@app.route("/tech/bianalytics")
def bianalytics():
    return render_template("tech/bianalytics.html")

@app.route("/tech/cloud")
def cloud():
    return render_template("tech/cloud.html")

@app.route("/tech/frontend")
def frontend():
    return render_template("tech/frontend.html")

@app.route("/tech/mobile")
def mobile():
    return render_template("tech/mobile.html")

@app.route("/tech/trending")
def trending():
    return render_template("tech/trending.html")

#industry endpoints
@app.route("/ind/fintech")
def fintech():
    return render_template("ind/fintech.html")

@app.route("/ind/retail")
def retail():
    return render_template("ind/retail.html")

@app.route("/ind/manufacturing")
def manufacturing():
    return render_template("ind/manufacturing.html")

@app.route("/ind/healthcare")
def healthcare():
    return render_template("ind/healthcare.html")

@app.route("/ind/supplychain")
def supplychain():
    return render_template("ind/supplychain.html")

@app.route("/ind/education")
def education():
    return render_template("ind/education.html")

@app.route("/ind/energy")
def energy():
    return render_template("ind/energy.html")

@app.route("/ind/adverts")
def adverts():
    return render_template("ind/adverts.html")

@app.route("/ind/fitness")
def fitness():
    return render_template("ind/fitness.html")

@app.route("/ind/travel")
def travel():
    return render_template("ind/travel.html")

@app.route("/ind/entertain")
def entertain():
    return render_template("ind/entertain.html")

# bs sol
@app.route('/bs_sol/ERP')
def erp():
    return render_template("bs/erp.html")

@app.route('/bs_sol/crm')
def crm():
    return render_template("bs/crm.html")

@app.route('/bs_sol/maintain')
def maintain():
    return render_template("bs/maintain.html")


@app.route('/bs_sol/sfa')
def sfa():
    return render_template("bs/sfa.html")

# hire
@app.route('/talent/dev')
def dev():
    return render_template("hire/dev.html")


@app.route('/talent/bidev')
def bidev():
    return render_template("hire/bidev.html")


@app.route('/talent/ui')
def ui():
    return render_template("hire/ui.html")


@app.route('/talent/tester')
def tester():
    return render_template("hire/tester.html")


@app.route('/talent/back')
def back():
    return render_template("hire/back.html")


@app.route('/talent/mobiledev')
def mobiledev():
    return render_template("hire/mobile.html")


@app.route('/talent/full')
def full():
    return render_template("hire/full.html")



# @app.route('/sending', methods = ["POST", "GET"])
# def sending():
#     if request.method == 'POST':
#         customer_name = request.form.get('customer_name')
#         email = request.form.get('email')
#         customer_contact = request.form.get('customer_contact')
#         topic = request.form.get('topic')
#         brief = request.form.get('brief')

#         new_client = Client(name=customer_name, tel_no=customer_contact, email=email, reason=topic, description=brief)

#         db.session.add(new_client)
#         db.session.commit()

        # whatsapp_message = f'New client: {customer_name}\nEmail: {email}\nContact: {customer_contact}\nTopic: {topic}\nBrief: {brief}'
        # try:
        #     message = client.messages.create(
        #         from_='whatsapp:+14155238886',
        #         body=whatsapp_message,
        #         to='whatsapp:+254797245933' 
        #     )
        #     print(f"WhatsApp message sent successfully: {message.sid}")
        # except Exception as e:
        #     print("Error sending WhatsApp message:", str(e))

        # return redirect(request.referrer)
  

if __name__ == '__main__':
    app.run(debug=True)