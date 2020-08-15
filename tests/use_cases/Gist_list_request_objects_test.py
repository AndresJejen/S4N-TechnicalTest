from S4NGithubApi.use_cases import gist_list_request_objects as ro
import unittest

class TestUseCaseGistListRequestObjects(unittest.TestCase):

    def test_build_gist_list_request_object_without_parameters(self):
        req = ro.GistListRequestObject()
        self.assertEqual(req.filters, None)
        self.assertTrue(bool(req))

    def test_build_file_list_request_object_from_empty_dict(self):
        req = ro.GistListRequestObject.from_dict({})
        self.assertEqual(req.filters, None)
        self.assertTrue(bool(req))

    def test_build_gist_list_request_object_with_empty_filters(self):
        req = ro.GistListRequestObject(filters={})

        self.assertEqual(req.filters, {})
        self.assertTrue(bool(req))

    def test_build_gist_list_request_object_from_dict_with_empty_filters(self):
        req = ro.GistListRequestObject.from_dict({'filters': {}})

        self.assertEqual(req.filters,{})
        self.assertTrue(bool(req))

    def test_build_gist_list_request_object_with_filters(self):
        req = ro.GistListRequestObject(filters={'a': 1, 'b': 2})

        self.assertEqual(req.filters, {'a': 1, 'b': 2})
        self.assertTrue(bool(req))

    def test_build_gist_list_request_object_from_dict_with_filters(self):
        req = ro.GistListRequestObject.from_dict({'filters': {'a': 1, 'b': 2}})

        self.assertEqual(req.filters, {'a': 1, 'b': 2})
        self.assertTrue(bool(req))

    def test_build_gist_list_request_object_from_dict_with_invalid_filters(self):
        req = ro.GistListRequestObject.from_dict({'filters': 5})

        self.assertTrue(req.has_errors())
        self.assertEqual(req.errors[0]['parameter'], 'filters')
        self.assertFalse(bool(req))
