from flask_restplus import Namespace, fields

class DetailsDto:
    api = Namespace('Details', description='data Details')

    res_save_data = api.model("request Register", {
        'message': fields.String(required=True, description='message')
    })
    res_items = api.model("res_items",{
        "customer_id":fields.Integer(),
        "customer_name":fields.String(),
        "customer_open_date":fields.String(),
        "last_consulted_date":fields.String(),
        "vaccination_type":fields.String(),
        "doctor_consulted":fields.String(),
        "state":fields.String(),
        "country":fields.String(),
        "post_code":fields.Integer(),
        "date_of_birth":fields.String(),
        "active_customer":fields.String(),
    })

    res_all_data = api.model("responsea all",{
        "items":fields.List(fields.Nested(res_items))
    })