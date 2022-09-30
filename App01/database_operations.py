import json

from django.http import HttpResponse
import logging


from App01.db import check_insert_privileges, init_database

logger = logging.getLogger(__name__)


def test_connection(request):
    if request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str)
        ip = json_dict.get('ip', None)
        port = json_dict.get('port', None)
        database = json_dict.get('database', None)
        username = json_dict.get('username', None)
        password = json_dict.get('password', None)

        result = check_insert_privileges(ip, port, database, username, password)
        return HttpResponse(json.dumps(result))


def initialize_database(request):
    if request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str)
        ip = json_dict.get('ip', None)
        port = json_dict.get('port', None)
        database = json_dict.get('database', None)
        username = json_dict.get('username', None)
        password = json_dict.get('password', None)
        root_username = json_dict.get('root_username', None)
        root_password = json_dict.get('root_password', None)

        result = init_database(ip, port, database, root_username, root_password, username, password)
        return HttpResponse(json.dumps(result))
