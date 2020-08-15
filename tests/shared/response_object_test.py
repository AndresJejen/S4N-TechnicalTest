from S4NGithubApi.shared import response_object as res
from S4NGithubApi.shared import request_object as req
import unittest

class TestSharedResponseObject(unittest.TestCase):

    def setUp(self):
        """ setUp """
        
        self.response_value = {'key': ['value1', 'value2']}
        self.response_type = 'ResponseError'
        self.response_message = 'This is a response error'

    def test_valid_request_object_cannot_be_used(self):
        with self.assertRaises(NotImplementedError) as context:
            req.ValidRequestObject.from_dict({})

    def test_response_success_is_true(self):
        self.assertEqual(bool(res.ResponseSuccess(self.response_value)), True)


    def test_response_failure_is_false(self):
        self.assertEqual(bool(res.ResponseFailure(self.response_type, self.response_message)), False)

    def test_response_success_contains_value(self):
        response = res.ResponseSuccess(self.response_value)
        self.assertEqual(response.value, self.response_value)

    def test_response_failure_has_type_and_message(self):
        response = res.ResponseFailure(self.response_type, self.response_message)

        self.assertEqual(response.type, self.response_type)
        self.assertEqual(response.message, self.response_message)


    def test_response_failure_contains_value(self):
        response = res.ResponseFailure(self.response_type, self.response_message)

        self.assertEqual(response.value, {'type': self.response_type, 'message': self.response_message})

    def test_response_failure_initialization_with_exception(self):
        response = res.ResponseFailure(self.response_type, Exception('Just an error message'))

        self.assertEqual(bool(response), False)
        self.assertEqual(response.type, self.response_type)
        self.assertEqual(response.message, "Exception: Just an error message")


    def test_response_failure_from_invalid_request_object(self):
        response = res.ResponseFailure.build_from_invalid_request_object(req.InvalidRequestObject())

        self.assertEqual(bool(response), False)


    def test_response_failure_from_invalid_request_object_with_errors(self):
        request_object = req.InvalidRequestObject()
        request_object.add_error('path', 'Is mandatory')
        request_object.add_error('path', "can't be blank")

        response = res.ResponseFailure.build_from_invalid_request_object(request_object)

        self.assertEqual(bool(response), False)
        self.assertEqual(response.type, res.ResponseFailure.PARAMETERS_ERROR)
        self.assertEqual(response.message, "path: Is mandatory\npath: can't be blank")

    def test_response_failure_build_resource_error(self):
        response = res.ResponseFailure.build_resource_error("test message")

        self.assertEqual(bool(response), False)
        self.assertEqual(response.type, res.ResponseFailure.RESOURCE_ERROR)
        self.assertEqual(response.message, "test message")


    def test_response_failure_build_parameters_error(self):
        response = res.ResponseFailure.build_parameters_error("test message")

        self.assertEqual(bool(response), False)
        self.assertEqual(response.type, res.ResponseFailure.PARAMETERS_ERROR)
        self.assertEqual(response.message, "test message")


    def test_response_failure_build_system_error(self):
        response = res.ResponseFailure.build_system_error("test message")

        self.assertEqual(bool(response), False)
        self.assertEqual(response.type, res.ResponseFailure.SYSTEM_ERROR)
        self.assertEqual(response.message, "test message")