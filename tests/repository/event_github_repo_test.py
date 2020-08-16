import unittest

from S4NGithubApi.domain.Event import Event
from S4NGithubApi.shared.domain_model import DomainModel
from S4NGithubApi.respository import github_repo
import uuid


class TestEventGithubRepo(unittest.TestCase):

    def setUp(self):
        """ setUp """
        
        self.domain_events = [
            {
                "id": "13151049797",
                "type": "PushEvent",
                "actor": {
                    "id": 26096411,
                    "login": "AndresJejen",
                    "display_login": "AndresJejen",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/AndresJejen",
                    "avatar_url": "https://avatars.githubusercontent.com/u/26096411?"
                },
                "repo": {
                    "id": 286255903,
                    "name": "BeitlabDataScience/SQL-Python--DataScience-Show-c3",
                    "url": "https://api.github.com/repos/BeitlabDataScience/SQL-Python--DataScience-Show-c3"
                },
                "public": True,
                "created_at": "2020-08-09T14:50:42Z",
                "org": {
                    "id": 69426515,
                    "login": "BeitlabDataScience",
                    "gravatar_id": "",
                    "url": "https://api.github.com/orgs/BeitlabDataScience",
                    "avatar_url": "https://avatars.githubusercontent.com/u/69426515?"
                }
            },
            {
                "id": "13151049761",
                "type": "PullRequestEvent",
                "actor": {
                    "id": 26096411,
                    "login": "AndresJejen",
                    "display_login": "AndresJejen",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/AndresJejen",
                    "avatar_url": "https://avatars.githubusercontent.com/u/26096411?"
                },
                "repo": {
                    "id": 286255903,
                    "name": "BeitlabDataScience/SQL-Python--DataScience-Show-c3",
                    "url": "https://api.github.com/repos/BeitlabDataScience/SQL-Python--DataScience-Show-c3"
                },
                "public": True,
                "created_at": "2020-08-09T14:50:42Z",
                "org": {
                    "id": 69426515,
                    "login": "BeitlabDataScience",
                    "gravatar_id": "",
                    "url": "https://api.github.com/orgs/BeitlabDataScience",
                    "avatar_url": "https://avatars.githubusercontent.com/u/69426515?"   
                }
            },
            {
                "id": "13151049367",
                "type": "PullRequestEvent",
                "actor": {
                    "id": 26096411,
                    "login": "AndresJejen",
                    "display_login": "AndresJejen",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/AndresJejen",
                    "avatar_url": "https://avatars.githubusercontent.com/u/26096411?"
                },
                "repo": {
                    "id": 286255903,
                    "name": "BeitlabDataScience/SQL-Python--DataScience-Show-c3",
                    "url": "https://api.github.com/repos/BeitlabDataScience/SQL-Python--DataScience-Show-c3"
                },
                "public": True,
                "created_at": "2020-08-09T14:50:34Z",
                "org": {
                    "id": 69426515,
                    "login": "BeitlabDataScience",
                    "gravatar_id": "",
                    "url": "https://api.github.com/orgs/BeitlabDataScience",
                    "avatar_url": "https://avatars.githubusercontent.com/u/69426515?"
                }
            },
            {
                "id": "13151049047",
                "type": "CreateEvent",
                "actor": {
                    "id": 26096411,
                    "login": "AndresJejen",
                    "display_login": "AndresJejen",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/AndresJejen",
                    "avatar_url": "https://avatars.githubusercontent.com/u/26096411?"
                },
                "repo": {
                    "id": 286255903,
                    "name": "BeitlabDataScience/SQL-Python--DataScience-Show-c3",
                    "url": "https://api.github.com/repos/BeitlabDataScience/SQL-Python--DataScience-Show-c3"
                },
                "public": True,
                "created_at": "2020-08-09T14:50:28Z",
                "org": {
                    "id": 69426515,
                    "login": "BeitlabDataScience",
                    "gravatar_id": "",
                    "url": "https://api.github.com/orgs/BeitlabDataScience",
                    "avatar_url": "https://avatars.githubusercontent.com/u/69426515?"
                }
            },
            {
                "id": "13151046844",
                "type": "PushEvent",
                "actor": {
                    "id": 26096411,
                    "login": "AndresJejen",
                    "display_login": "AndresJejen",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/AndresJejen",
                    "avatar_url": "https://avatars.githubusercontent.com/u/26096411?"
                },
                "repo": {
                    "id": 286255903,
                    "name": "BeitlabDataScience/SQL-Python--DataScience-Show-c3",
                    "url": "https://api.github.com/repos/BeitlabDataScience/SQL-Python--DataScience-Show-c3"
                },
                "public": True,
                "created_at": "2020-08-09T14:49:52Z",
                "org": {
                    "id": 69426515,
                    "login": "BeitlabDataScience",
                    "gravatar_id": "",
                    "url": "https://api.github.com/orgs/BeitlabDataScience",
                    "avatar_url": "https://avatars.githubusercontent.com/u/69426515?"
                }
            }
        ]

        self.mockEvents = {
                "13151049797": {
                    'Id' : "13151049797", 
                    'Type' : "Push", 
                    'Repo_Id' : 12345, 
                    'Repo_Name' : "Repo", 
                    'Repo_Url' : "https://github.com/user/repoName", 
                    'User' : "user", 
                    'User_Url' : "https://github.com/user", 
                    'Public' : True, 
                    'Date' : "2019-10-13T23:08:50Z" 
                },
                "13151049761": {
                    'Id' : "13151049761", 
                    'Type' : "Push", 
                    'Repo_Id' : 12345, 
                    'Repo_Name' : "Repo", 
                    'Repo_Url' : "https://github.com/user/repoName", 
                    'User' : "user", 
                    'User_Url' : "https://github.com/user", 
                    'Public' : True, 
                    'Date' : "2019-10-13T23:08:50Z" 
                },
                "13151049367": {
                    'Id' : "13151049367", 
                    'Type' : "Push", 
                    'Repo_Id' : 12345, 
                    'Repo_Name' : "Repo", 
                    'Repo_Url' : "https://github.com/user/repoName", 
                    'User' : "user", 
                    'User_Url' : "https://github.com/user", 
                    'Public' : True, 
                    'Date' : "2019-10-13T23:08:50Z" 
                },
                "13151049047": {
                    'Id' : "13151049047", 
                    'Type' : "Push", 
                    'Repo_Id' : 12345, 
                    'Repo_Name' : "Repo", 
                    'Repo_Url' : "https://github.com/user/repoName", 
                    'User' : "user", 
                    'User_Url' : "https://github.com/user", 
                    'Public' : True, 
                    'Date' : "2019-10-13T23:08:50Z" 
                },
                "13151046844": {
                    'Id' : "13151046844", 
                    'Type' : "Push", 
                    'Repo_Id' : 12345, 
                    'Repo_Name' : "Repo", 
                    'Repo_Url' : "https://github.com/user/repoName", 
                    'User' : "user", 
                    'User_Url' : "https://github.com/user", 
                    'Public' : True, 
                    'Date' : "2019-10-13T23:08:50Z" 
                }
            }

    def _check_results(self, domain_model_list, data_list):
        self.assertEqual(len(domain_model_list), len(data_list))
        #self.assertTrue(all([isinstance(dm, DomainModel) for dm in domain_model_list]))
        #self.assertEqual(set([dm.Id for dm in domain_model_list]), set([d['id'] for d in data_list]))

    def test_repository_list_without_parameters(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list()

    def test_repository_list_with_empty_parameters(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list({})

    def test_repository_list_with_filters_unknown_key(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'weird': 'events'})

    def test_repository_list_with_body_null(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'type': 'events'}, body=None)

    def test_repository_list_with_body_not_list(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'type': 'events'}, body=2)

    def test_repository_list_with_body_empty_list(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'type': 'events'}, body=[])

    def test_repository_list_with_body_not_string_list(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'type': 'events'}, body=["1", "2", 2])

    def test_repository_list_with_filters_unknown_operator(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'__in': [20, 30]})

    def test_repository_list_with_filters_events(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'type': 'events'}, body=["AndresJejen"], mock=self.mockEvents),
            self.domain_events
        )

    def test_repository_list_with_filters_events_eq(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'type': 'events'}, body=["AndresJejen"], mock=self.mockEvents),
            self.domain_events
        )

    def test_repository_list_with_filters_gists(self):
        repo = github_repo.GithubRepo(self.domain_events)
        result = repo.list(filters={'type': 'gists'}, body=["AndresJejen"], mock=self.mockEvents)

        self._check_results(
            result,
            self.domain_events
        )

    def test_repository_list_with_filters_gists_eq(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'type': 'gists'}, body=["AndresJejen"], mock=self.mockEvents),
            self.domain_events
        )

    def test_repository_list_with_filters_events_from_api(self):
        repo = github_repo.GithubRepo()
        result = repo.list(filters={'type': 'events'}, body=["AndresJejen"])
        self.assertGreater(len(result.keys()), 0)

    def test_repository_list_with_filters_gists_from_api(self):
        repo = github_repo.GithubRepo()
        result = repo.list(filters={'type': 'gists'}, body=["AndresJejen"])
        self.assertGreater(len(result), 0)

    def test_repository_list_with_filters_events_from_api_wrong_user(self):
        repo = github_repo.GithubRepo()
        result = repo.list(filters={'type': 'events'}, body=["AndresaJejen"])
        self.assertEqual(len(result.keys()), 0)

    def test_repository_list_with_filters_gists_from_api_wrong_user(self):
        repo = github_repo.GithubRepo()
        result = repo.list(filters={'type': 'gists'}, body=["AndresaJejen"])
        self.assertEqual(len(result), 0)

    

if __name__ == "main":
    unittest.main()