import unittest

from S4NGithubApi.domain.Event import Event
from S4NGithubApi.shared.domain_model import DomainModel
from S4NGithubApi.respository import github_repo as github_repo
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
                "public": true,
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
                "public": true,
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
                "public": true,
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
                "public": true,
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
                "public": true,
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

    def _check_results(self, domain_model_list, data_list):
        self.assertEqual(len(domain_model_list), len(data_list))
        self.assertTrue(all([isinstance(dm, DomainModel) for dm in domain_model_list]))
        self.assertEqual(set([dm.Id for dm in domain_model_list]), set([d['id'] for d in data_list]))

    def test_repository_list_without_parameters(self):
        repo = github_repo.GithubRepo(self.domain_events)
        result = repo.list()

        self._check_results(
            result,
            self.domain_events
        )


    def test_repository_list_with_filters_unknown_key(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(KeyError) as context:
            repo.list(filters={'weird': 'events'})


    def test_repository_list_with_filters_unknown_operator(self):
        repo = github_repo.GithubRepo(self.domain_events)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'__in': [20, 30]})


    def test_repository_list_with_filters_IdActualSoft(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'IdActualSoft': 2}),
            [self.domain_events[1]]
        )


    def test_repository_list_with_filters_IdActualSoft_eq(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'IdActualSoft': 2}),
            [self.domain_events[1]]
        )

    def test_repository_list_with_filters_IdOldSoft(self):
        repo = github_repo.GithubRepo(self.domain_events)
        result = repo.list(filters={'IdOldSoft': None})

        self._check_results(
            result,
            [self.domain_events[1]]
        )


    def test_repository_list_with_filters_IdOldSoft_eq(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'IdOldSoft': None}),
            [self.domain_events[1]]
        )
        
    # def test_repository_list_with_filters_price_lt(self):
    #     repo = github_repo.GithubRepo(self.domain_events)

    #     self._check_results(
    #         repo.list(filters={'price__lt': 60}),
    #         [storageroom_dicts[0], storageroom_dicts[3]])


    # def test_repository_list_with_filters_price_gt(self):
    #     repo = github_repo.GithubRepo(self.domain_events)
    #     self._check_results(
    #         repo.list(filters={'price__gt': 60}),
    #         [storageroom_dicts[1]]
    #     )


    # def test_repository_list_with_filters_size(self):
    #     repo = github_repo.GithubRepo(self.domain_events)

    #     self._check_results(
    #         repo.list(filters={'size': 93}),
    #         [storageroom_dicts[3]]
    #     )


    # def test_repository_list_with_filters_size_eq(self):
    #     repo = github_repo.GithubRepo(self.domain_events)
    #     self._check_results(
    #         repo.list(filters={'size__eq': 93}),
    #         [storageroom_dicts[3]]
    #     )


    # def test_repository_list_with_filters_size_lt(self):
    #     repo = github_repo.GithubRepo(self.domain_events)
    #     self._check_results(
    #         repo.list(filters={'size__lt': 60}),
    #         [storageroom_dicts[2]]
    #     )


    # def test_repository_list_with_filters_size_gt(self):
    #     repo = github_repo.GithubRepo(self.domain_events)
    #     self._check_results(
    #         repo.list(filters={'size__gt': 400}),
    #         [storageroom_dicts[1]]
    #     )


    def test_repository_list_with_filters_id(self):
        repo = github_repo.GithubRepo(self.domain_events)

        self._check_results(
            repo.list(filters={'id': '913694c6-435a-4366-ba0d-da5334a611b2'}),
            [self.domain_events[0]]
        )

    

