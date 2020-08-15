from S4NGithubApi.shared import request_object as req
import unittest

class TestRequestObject(unittest.TestCase):

    def test_invalid_request_object_is_false(self):
        request = req.InvalidRequestObject()
        self.assertFalse(bool(request))


    def test_invalid_request_object_accepts_errors(self):
        request = req.InvalidRequestObject()
        request.add_error(parameter='aparam', message='wrong value')
        request.add_error(parameter='anotherparam', message='wrong type')

        self.assertTrue(request.has_errors())
        self.assertEqual(len(request.errors), 2)


    def test_valid_request_object_is_true(self):
        request = req.ValidRequestObject()

        self.assertTrue(bool(request))