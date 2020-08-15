from S4NGithubApi.domain.Gist import Gist
import unittest
import uuid
import os

class TestGist(unittest.TestCase):

    def test_gist_model_init(self):
        gist = Gist(
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
            OwnerId = "7890",
            OwnerUrl = "https://github.com/user",
        )

        self.assertEqual(gist.Id, "12345")
        self.assertEqual(gist.Url, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.ForksUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.CommitsUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.HtmlUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.Node_Id, "123456")
        self.assertEqual(gist.GitPullurl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.GitPushUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.Public, True)
        self.assertEqual(gist.Created_at, "2019-10-13T23:08:50Z")
        self.assertEqual(gist.UpdatedAt, "2019-10-13T23:08:50Z")
        self.assertEqual(gist.OwnerId, "7890")
        self.assertEqual(gist.OwnerUrl, "https://github.com/user")

    def test_gist_model_from_dict(self):
        gist = Gist.from_dict(
            {
                'Id': "12345", 
                'Url': "https://github.com/user/gist/gistName", 
                'ForksUrl': "https://github.com/user/gist/gistName", 
                'CommitsUrl': "https://github.com/user/gist/gistName", 
                'HtmlUrl': "https://github.com/user/gist/gistName", 
                'Node_Id': "123456", 
                'GitPullurl': "https://github.com/user/gist/gistName", 
                'GitPushUrl': "https://github.com/user/gist/gistName", 
                'Public': True, 
                'Created_at': "2019-10-13T23:08:50Z", 
                'UpdatedAt': "2019-10-13T23:08:50Z", 
                'OwnerId': "7890", 
                'OwnerUrl': "https://github.com/user", 
            }
        )
        self.assertEqual(gist.Id, "12345")
        self.assertEqual(gist.Url, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.ForksUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.CommitsUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.HtmlUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.Node_Id, "123456")
        self.assertEqual(gist.GitPullurl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.GitPushUrl, "https://github.com/user/gist/gistName")
        self.assertEqual(gist.Public, True)
        self.assertEqual(gist.Created_at, "2019-10-13T23:08:50Z")
        self.assertEqual(gist.UpdatedAt, "2019-10-13T23:08:50Z")
        self.assertEqual(gist.OwnerId, "7890")
        self.assertEqual(gist.OwnerUrl, "https://github.com/user")

    def test_gist_model_to_dict(self):
        gist_dict = {
                'Id': "12345", 
                'Url': "https://github.com/user/gist/gistName", 
                'ForksUrl': "https://github.com/user/gist/gistName", 
                'CommitsUrl': "https://github.com/user/gist/gistName", 
                'HtmlUrl': "https://github.com/user/gist/gistName", 
                'Node_Id': "123456", 
                'GitPullurl': "https://github.com/user/gist/gistName", 
                'GitPushUrl': "https://github.com/user/gist/gistName", 
                'Public': True, 
                'Created_at': "2019-10-13T23:08:50Z", 
                'UpdatedAt': "2019-10-13T23:08:50Z", 
                'OwnerId': "7890", 
                'OwnerUrl': "https://github.com/user", 
            }

        gist = Gist.from_dict(gist_dict)

        self.assertEqual(gist.to_dict(), gist_dict)


    def test_gist_model_comparison(self):
        gist_dict = {
                'Id': "12345", 
                'Url': "https://github.com/user/gist/gistName", 
                'ForksUrl': "https://github.com/user/gist/gistName", 
                'CommitsUrl': "https://github.com/user/gist/gistName", 
                'HtmlUrl': "https://github.com/user/gist/gistName", 
                'Node_Id': "123456", 
                'GitPullurl': "https://github.com/user/gist/gistName", 
                'GitPushUrl': "https://github.com/user/gist/gistName", 
                'Public': True, 
                'Created_at': "2019-10-13T23:08:50Z", 
                'UpdatedAt': "2019-10-13T23:08:50Z", 
                'OwnerId': "7890", 
                'OwnerUrl': "https://github.com/user", 
            }
        gist1 = Gist.from_dict(gist_dict)
        gist2 = Gist.from_dict(gist_dict)

        self.assertEqual(gist1, gist2)

if __name__ == "main":
    unittest.main()