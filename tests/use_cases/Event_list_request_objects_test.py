from S4NGithubApi.use_cases import event_list_request_objects as ro
import unittest

class TestUseCaseEventListRequestObjects(unittest.TestCase):


    def test_build_event_list_request_object_without_parameters(self):
        req = ro.EventListRequestObject()
        self.assertEqual(req.filters, None)
        self.assertEqual(bool(req), True)

    def test_build_file_list_request_object_from_empty_dict(self):
        req = ro.EventListRequestObject.from_dict({})
        self.assertEqual(req.filters, None)
        self.assertEqual(bool(req), True)

    def test_build_event_list_request_object_with_empty_filters(self):
        req = ro.EventListRequestObject(filters={})

        self.assertEqual(req.filters, {})
        self.assertEqual(bool(req), True)


    def test_build_event_list_request_object_from_dict_with_empty_filters(self):
        req = ro.EventListRequestObject.from_dict({'filters': {}})

        self.assertEqual(req.filters,{})
        self.assertEqual(bool(req),True)


    def test_build_event_list_request_object_with_filters(self):
        req = ro.EventListRequestObject(filters={'a': 1, 'b': 2})

        self.assertEqual(req.filters, {'a': 1, 'b': 2})
        self.assertEqual(bool(req), True)


    def test_build_event_list_request_object_from_dict_with_filters(self):
        req = ro.EventListRequestObject.from_dict({'filters': {'a': 1, 'b': 2}})

        self.assertEqual(req.filters, {'a': 1, 'b': 2})
        self.assertEqual(bool(req), True)


    def test_build_event_list_request_object_from_dict_with_invalid_filters(self):
        req = ro.EventListRequestObject.from_dict({'filters': 5})

        self.assertTrue(req.has_errors())
        self.assertEqual(req.errors[0]['parameter'], 'filters')
        self.assertEqual(bool(req), False)
