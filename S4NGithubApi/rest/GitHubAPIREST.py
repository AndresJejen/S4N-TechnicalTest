import json
from flask import Blueprint, Response

from S4NGithubApi.shared import request_object as req
from S4NGithubApi.respository import github_repo as gr

from S4NGithubApi.use_cases import event_list_use_case as E_uc
from S4NGithubApi.use_cases import gist_list_use_case as G_uc

from S4NGithubApi.use_cases import event_list_request_objects as r_E_uc
from S4NGithubApi.use_cases import gist_list_request_objects as r_G_uc

from S4NGithubApi.serializers import gist_serializer as G_ser
from S4NGithubApi.serializers import event_serializer as E_ser

blueprint = Blueprint('storageroom', __name__)


@blueprint.route('/', methods=['GET'])
def query():
    request_object = r_E_uc.EventListRequestObject.from_dict({})

    repo = gr.GithubRepo()
    use_case = E_uc.EventListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value),
                    mimetype='application/json',
                    status=200)