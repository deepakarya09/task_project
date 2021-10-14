from app.main import db


class Details(db.Model):
    __tablename__ = "details"
    customer_id = db.Column(db.Integer(), primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    customer_open_date = db.Column(db.String(30), nullable=True)
    last_consulted_date = db.Column(db.String(30), nullable=True)
    vaccination_type =  db.Column(db.String(5), nullable=True)
    doctor_consulted = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(10),nullable=True)
    country = db.Column(db.String(10), nullable=True)
    post_code = db.Column(db.Integer(),nullable=True)
    date_of_birth = db.Column(db.String(),nullable=True)
    active_customer = db.Column(db.String(2),nullable=True)