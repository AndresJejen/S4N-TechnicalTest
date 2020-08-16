from S4NGithubApi.domain.Gist import Gist
from S4NGithubApi.use_cases import gist_list_use_case as uc
from S4NGithubApi.use_cases import gist_list_request_objects as req
from S4NGithubApi.shared import response_object as res
import unittest
from unittest import mock
import uuid

class TestUseCaseGistList(unittest.TestCase):

    def setUp(self):
        """ setUp """
        
        self.domain_gist = [
            Gist(
                Id = "12345",
                Url = "https://github.com/user/gist/gistName",
                ForksUrl = "https://github.com/user/gist/gistName",
                CommitsUrl = "https://github.com/user/gist/gistName",
                HtmlUrl = "https://github.com/user/gist/gistName",
                Node_Id = "123456",
                GitPullurl = "https://github.com/user/gist/gistName",
                GitPushUrl = "https://github.com/user/gist/gistName",
                Public = True,
                Created_at = "2019-10-13T23:08:50Z",
                UpdatedAt = "2019-10-13T23:08:50Z",
                OwnerId = 7890,
                OwnerUrl = "https://github.com/user",
            ),
            Gist(
                Id = "1234589",
                Url = "https://github.com/user/gist/gist1Name",
                ForksUrl = "https://github.com/user/gist/gist1Name",
                CommitsUrl = "https://github.com/user/gist/gist1Name",
                HtmlUrl = "https://github.com/user/gist/gist1Name",
                Node_Id = "12345666",
                GitPullurl = "https://github.com/user/gist/gist55Name",
                GitPushUrl = "https://github.com/user/gist/gist55Name",
                Public = False,
                Created_at = "2019-10-13T23:08:60Z",
                UpdatedAt = "2019-10-13T23:08:60Z",
                OwnerId = 7890888,
                OwnerUrl = "https://github.com/user1",
            )
        ]

    def test_gist_list_without_parameters(self):
        repo = mock.Mock()
        repo.list.return_value = self.domain_gist

        gist_list_use_case = uc.GistListUseCase(repo)
        request_object = req.GistListRequestObject.from_dict({})

        respose_object = gist_list_use_case.execute(request_object)

        self.assertEqual(bool(respose_object), True)
        repo.list.assert_called_with(filters=None)

        self.assertEqual(respose_object.value, self.domain_gist)


    def test_gist_list_with_filters(self):
        repo = mock.Mock()
        repo.list.return_value = self.domain_gist

        gist_list_use_case = uc.GistListUseCase(repo)
        qry_filters = {'a': 5}
        request_object = req.GistListRequestObject.from_dict({'filters': qry_filters})

        response_object = gist_list_use_case.execute(request_object)

        self.assertTrue(bool(response_object))
        repo.list.assert_called_with(filters=qry_filters)
        self.assertEqual(response_object.value, self.domain_gist)

    def test_gist_list_handles_generic_error(self):
        repo = mock.Mock()
        repo.list.side_effect = Exception('Just an error message')

        gist_list_use_case = uc.GistListUseCase(repo)
        request_object = req.GistListRequestObject.from_dict({})

        response_object = gist_list_use_case.execute(request_object)

        self.assertFalse(bool(response_object))
        self.assertEqual(response_object.value, {
            'type': res.ResponseFailure.SYSTEM_ERROR,
            'message': "Exception: Just an error message"
        })


    def test_gist_list_handles_bad_request(self):
        repo = mock.Mock()

        gist_list_use_case = uc.GistListUseCase(repo)
        request_object = req.GistListRequestObject.from_dict({'filters': 5})

        response_object = gist_list_use_case.execute(request_object)

        self.assertFalse(bool(response_object))
        self.assertEqual(response_object.value, {
            'type': res.ResponseFailure.PARAMETERS_ERROR,
            'message': "filters: Is not iterable"
        })