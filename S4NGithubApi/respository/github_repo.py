from S4NGithubApi.domain import Event as em
import requests
import functools

class GithubRepo:

    def __init__(self, entries=None):
        self._entries = []
        self._basicRoute="https://api.github.com/users/{0}/{1}?page=1&per_page={2}"
        if entries:
            self._entries.extend(entries)

    def _check(self, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq']:
            raise ValueError('Operator {} is not supported'.format(operator))

        if (value is None):
            return False
        elif key in ['type']:
            if value in ['gists', 'events']:
                return True
            else:
                return True
        return False


    def _query_to_event(self, data):
        def to_event(element):
            return {
                "Id"        : element["id"],
                "Type"      : element["type"],
                "Repo_Id"   : element["repo"]["id"],
                "Repo_Name" : element["repo"]["name"],
                "Repo_Url"  : element["repo"]["url"],
                "User"      : element["actor"]["login"],
                "User_Url"  : element["actor"]["url"],
                "Public"    : element["public"],
                "Date"      : element["created_at"]
            }

        return { value["id"]: to_event(value) for value in data }

    def _query_to_gists(self, data):
        def to_gist(element):
            return {
                "Id"         : element["id"],
                "Url"        : element["url"],
                "ForksUrl"   : element["forks_url"],
                "CommitsUrl" : element["commits_url"],
                "HtmlUrl"    : element["html_url"],
                "Node_Id"    : element["node_id"],
                "GitPullurl" : element["git_pull_url"],
                "GitPushUrl" : element["git_push_url"],
                "Public"     : element["public"],
                "Created_at" : element["created_at"],
                "UpdatedAt"  : element["updated_at"],
                "OwnerId"    : element["owner"]["id"],
                "OwnerUrl"   : element["owner"]["url"],
            }

        return [to_gist(value) for value in data]

    def _singleUserFromGitHub(self, value, user):
        query = self._basicRoute.format(user,value, 3 if value == 'gists' else 5)
        result = requests.get(query)
        if (result.status_code == 200):
            return result.json()
        return []

    def _queryAllusersFromGitHub(self, value, users):
        result = []
        for user in users:
            result.extend(self._singleUserFromGitHub(value, user))
        if (value is 'gists'):
            return self._query_to_gists(result)
        else:
            return self._query_to_event(result)

    def _validateFilters(self, filters):
        if not filters:
            raise ValueError('you have to add a type query')
        elif len(list(filters.items())) is not 1:
            raise ValueError('you have to ads just a type query')
        else:
            key, value = list(filters.items())[0]
            if self._check(key, value) == False:
                raise ValueError('Please add a valid query [type: events] or [type: gists]')
            return key, value
    
    def _validateBody(self, body):
        if (not body) or (type(body) is not list):
            raise ValueError('you have to add users to query')
        elif len(body) is 0:
            raise ValueError('you have to add users to query')
        else:
            function = lambda a,b: (type(b) == str) and a
            result = functools.reduce(function,body,True)
            if result is not True:
                raise ValueError('you have to add a list of users to query in string format')

    def list(self, filters=None, body=None, mock=None):
        key, value = self._validateFilters(filters)
        self._validateBody(body)
        if len(self._entries) > 0: # Mock repo
            return mock
        else:
            return self._queryAllusersFromGitHub(value, body)