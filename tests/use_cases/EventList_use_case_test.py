from S4NGithubApi.domain.Event import Event
from S4NGithubApi.use_cases import event_list_use_case as uc
from S4NGithubApi.use_cases import event_list_request_objects as req
from S4NGithubApi.shared import response_object as res
import unittest
from unittest import mock
import uuid
import os

class TestUseCaseEventList(unittest.TestCase):

    def setUp(self):
        """ setUp """
        
        self.domain_events = [
            Event(
                Id = "Identificador0",
                Type = "Push",
                Repo_Id = "12345",
                Repo_Name = "Repo",
                Repo_Url = "https://github.com/user/repoName",
                User = "user",
                User_Url = "https://github.com/user",
                Public = True,
                Date = "2019-10-13T23:08:50Z"
            ),
            Event(
                Id = "Identificador1",
                Type = "pull",
                Repo_Id = "1234589",
                Repo_Name = "Repo",
                Repo_Url = "https://github.com/user/repoName",
                User = "user",
                User_Url = "https://github.com/user",
                Public = True,
                Date = "2019-12-13T23:08:50Z"
            )
        ]

    def test_event_list_without_parameters(self):
        repo = mock.Mock()
        repo.list.return_value = self.domain_events

        event_list_use_case = uc.EventListUseCase(repo)
        request_object = req.EventListRequestObject.from_dict({})
        
        respose_object = event_list_use_case.execute(request_object)

        self.assertTrue(bool(respose_object))
        repo.list.assert_called_with(filters=None)

        self.assertEqual(respose_object.value, self.domain_events)

    def test_event_list_with_filters(self):
        repo = mock.Mock()
        repo.list.return_value = self.domain_events

        event_list_use_case = uc.EventListUseCase(repo)
        qry_filters = {'a': 5}
        request_object = req.EventListRequestObject.from_dict({'filters': qry_filters})

        response_object = event_list_use_case.execute(request_object)

        self.assertTrue(bool(response_object))
        repo.list.assert_called_with(filters=qry_filters)
        self.assertEqual(response_object.value, self.domain_events)

    def test_event_list_handles_generic_error(self):
        repo = mock.Mock()
        repo.list.side_effect = Exception('Just an error message')

        event_list_use_case = uc.EventListUseCase(repo)
        request_object = req.EventListRequestObject.from_dict({})

        response_object = event_list_use_case.execute(request_object)

        self.assertFalse(bool(response_object))
        self.assertEqual(response_object.value, {
            'type': res.ResponseFailure.SYSTEM_ERROR,
            'message': "Exception: Just an error message"
        })


    def test_event_list_handles_bad_request(self):
        repo = mock.Mock()

        event_list_use_case = uc.EventListUseCase(repo)
        request_object = req.EventListRequestObject.from_dict({'filters': 5})

        response_object = event_list_use_case.execute(request_object)

        self.assertFalse(bool(response_object))
        self.assertEqual(response_object.value, {
            'type': res.ResponseFailure.PARAMETERS_ERROR,
            'message': "filters: Is not iterable"
        })