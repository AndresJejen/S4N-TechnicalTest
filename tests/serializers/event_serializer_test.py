import datetime
import json
import uuid
import unittest

from S4NGithubApi.serializers import event_serializer as srs
from S4NGithubApi.domain.Event import Event


class TestEventSerializer(unittest.TestCase):

    def test_serializer_domain_event(self):
        event = Event(
            Id = "Identificador0",
            Type = "Push",
            Repo_Id = 12345,
            Repo_Name = "Repo",
            Repo_Url = "https://github.com/user/repoName",
            User = "user",
            User_Url = "https://github.com/user",
            Public = True,
            Date = "2019-10-13T23:08:50Z"
        )

        expected_json = """
            {
                "Id": "Identificador0", 
                "Type": "Push", 
                "Repo_Id": 12345, 
                "Repo_Name": "Repo", 
                "Repo_Url": "https://github.com/user/repoName", 
                "User": "user", 
                "User_Url": "https://github.com/user", 
                "Public": true, 
                "Date": "2019-10-13T23:08:50Z" 
            }
        """

        json_event = json.dumps(event, cls=srs.EventEncoder)

        self.assertEqual(json.loads(json_event), json.loads(expected_json))


    def test_serializer_domain_event_wrong_type(self):
        with self.assertRaises(Exception) as context:
            json.dumps(datetime.datetime.now(), cls=srs.EventEncoder)
        
if __name__ == "main":
    unittest.main()