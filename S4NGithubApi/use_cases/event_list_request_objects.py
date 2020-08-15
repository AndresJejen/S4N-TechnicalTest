from S4NGithubApi.shared.request_object import InvalidRequestObject, ValidRequestObject
import collections

class EventListRequestObject(object):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return EventListRequestObject(filters=adict.get('filters', None))

    def __nonzero__(self):
        return True