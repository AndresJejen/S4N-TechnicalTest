import datetime
import json
import uuid
import unittest

from S4NGithubApi.serializers import gist_serializer as srs
from S4NGithubApi.domain.Gist import Gist


class TestGistSerializer(unittest.TestCase):

    def test_serializer_domain_gist(self):
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
            OwnerUrl = "https://github.com/user"
        )

        expected_json = """
            {{
                "Id": "12345", 
                "Url": "https://github.com/user/gist/gistName", 
                "ForksUrl": "https://github.com/user/gist/gistName", 
                "CommitsUrl": "https://github.com/user/gist/gistName", 
                "HtmlUrl": "https://github.com/user/gist/gistName", 
                "Node_Id": "123456", 
                "GitPullurl": "https://github.com/user/gist/gistName", 
                "GitPushUrl": "https://github.com/user/gist/gistName", 
                "Public": true, 
                "Created_at": "2019-10-13T23:08:50Z", 
                "UpdatedAt": "2019-10-13T23:08:50Z", 
                "OwnerId": "7890", 
                "OwnerUrl": "https://github.com/user"
            }}
        """

        json_gist = json.dumps(gist, cls=srs.GistEncoder)

        json1, json2 = json.loads(json_gist), json.loads(expected_json)

        self.assertEqual(json1, json2)


    def test_serializer_domain_gist_wrong_type(self):
        with self.assertRaises(Exception) as context:
            json.dumps(datetime.datetime.now(), cls=srs.GistEncoder)
        
if __name__ == "main":
    unittest.main()