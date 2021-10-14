from werkzeug.wrappers import Response
from app.main.model.details import Details
from werkzeug.exceptions import BadRequest
from http import HTTPStatus
from app.main import db


def save_data(filelocation):
    try:
        x = open(f"{filelocation}")
    except Exception as e:
        raise BadRequest(f"File Location not found {e}")
    
    try:
        datas = []
        for line in x:
            if line.startswith("|D|"):
                datas.append(line.split("|"))

        
        for data in datas:
            check = Details.query.filter(Details.customer_id==data[3]).first()
            if check:
                raise BadRequest("Data of this coustomer already available")
            try:
                save = Details(
                    customer_name = data[2],
                    customer_id = data[3],
                    customer_open_date = data[4],
                    last_consulted_date = data[5],
                    vaccination_type =  data[6],
                    doctor_consulted = data[7],
                    state = data[8],
                    country = data[9],
                    date_of_birth = data[10],
                    active_customer = data[11]
                )
                db.session.add(save)
                db.session.commit()
            except Exception as e:
                raise BadRequest(f"Somthing error in saving data {e}")
        return {"message":"Data saved successfully"}
    except Exception as e:
        raise BadRequest(f"Not able to perform saving data due to : {e}")


def get_all(country):
    if country:
        data = Details.query.filter(Details.country==country).all()
    else:
        data = Details.query.all()
    return {"items":data}