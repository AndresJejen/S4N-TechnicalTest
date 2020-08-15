from S4NGithubApi.domain import Empresa as em

class GithubRepo:

    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if (value is None):
            return element[key] is None

        elif key in ['type']:
            return getattr(str(element[key]), operator)(str(value))
        return getattr(element[key], operator)(value)

    def list(self, filters):
        result = []
        result.extend(self._entries)

        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return [em.Empresa.from_dict(r) for r in result]