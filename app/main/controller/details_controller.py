from app.main.services.details_query import get_all, save_data
from werkzeug import abort
from flask_restplus import Resource
from http import HTTPStatus
from app.main.controller import error_m
from flask import request
from app.main.utils.details_dto import DetailsDto

api = DetailsDto.api
_res_user_info = DetailsDto.res_save_data
_res_all_data = DetailsDto.res_all_data

@api.route("api/v1.0/save/<filelocation>")
class saveData(Resource):
    @api.marshal_with(_res_user_info)
    def get(self,filelocation):
        return save_data(filelocation)


@api.route("api/v1.0/data")
class Getall(Resource):
    @api.marshal_with(_res_all_data)
    def get(self):
        country = request.args.get("country")
        return get_all(country)
