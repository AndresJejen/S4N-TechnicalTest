import json
import unittest
from unittest import mock
import requests

from S4NGithubApi.domain.Event  import Event
from S4NGithubApi.shared import response_object as res

event_dict = {
            'Id' : "Identificador0", 
            'Type' : "Push", 
            'Repo_Id' : 12345, 
            'Repo_Name' : "Repo", 
            'Repo_Url' : "https://github.com/user/repoName", 
            'User' : "user", 
            'User_Url' : "https://github.com/user", 
            'Public' : True, 
            'Date' : "2019-10-13T23:08:50Z" 
        }

event_domain_model = Event.from_dict(event_dict)

events = [event_domain_model]

class TestRestEvents(unittest.TestCase):

    @mock.patch('S4NGithubApi.use_cases.event_list_use_case.EventListUseCase')
    def test_get(self, mock_use_case, client):
        mock_use_case().execute.return_value = res.ResponseSuccess(events)

        http_response = client.post('/', json=)

        assert json.loads(http_response.data.decode('UTF-8')) == {
            "Identificador0": event_dict
        }
        assert http_response.status_code == 200
        assert http_response.mimetype == 'application/json'