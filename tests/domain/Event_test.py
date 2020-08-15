from S4NGithubApi.domain.Event import Event
import unittest
import uuid
import os

class TestEvent(unittest.TestCase):

    def test_event_model_init(self):

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

        self.assertEqual(event.Id, "Identificador0")
        self.assertEqual(event.Type, "Push")
        self.assertEqual(event.Repo_Id, 12345)
        self.assertEqual(event.Repo_Name, "Repo")
        self.assertEqual(event.Repo_Url, "https://github.com/user/repoName")
        self.assertEqual(event.User, "user")
        self.assertEqual(event.User_Url, "https://github.com/user")
        self.assertEqual(event.Public, True)
        self.assertEqual(event.Date, "2019-10-13T23:08:50Z")

    def test_event_model_from_dict(self):
        
        event = Event.from_dict(
            {
                'Id' : "Identificador0", 
                'Type' : "Push", 
                'Repo_Id' : 12345, 
                'Repo_Name' : "Repo", 
                'Repo_Url' : "https://github.com/user/repoName", 
                'User' : "user", 
                'User_Url' : "https://github.com/user", 
                'Public' : True, 
                'Date' : "2019-10-13T23:08:50Z" 
            }
        )
        self.assertEqual(event.Id,  "Identificador0")
        self.assertEqual(event.Type,    "Push")
        self.assertEqual(event.Repo_Id,     12345)
        self.assertEqual(event.Repo_Name,   "Repo")
        self.assertEqual(event.Repo_Url,    "https://github.com/user/repoName")
        self.assertEqual(event.User,    "user")
        self.assertEqual(event.User_Url,    "https://github.com/user")
        self.assertEqual(event.Public,  True)
        self.assertEqual(event.Date,    "2019-10-13T23:08:50Z")

    def test_event_model_to_dict(self):
        event_dict = {
            'Id' : "Identificador0", 
            'Type' : "Push", 
            'Repo_Id' : 12345, 
            'Repo_Name' : "Repo", 
            'Repo_Url' : "https://github.com/user/repoName", 
            'User' : "user", 
            'User_Url' : "https://github.com/user", 
            'Public' : True, 
            'Date' : "2019-10-13T23:08:50Z" 
        }

        event = Event.from_dict(event_dict)

        self.assertEqual(event.to_dict(), event_dict)

    def test_event_model_comparison(self):
        event_dict = {
            'Id' : "Identificador0", 
            'Type' : "Push", 
            'Repo_Id' : 12345, 
            'Repo_Name' : "Repo", 
            'Repo_Url' : "https://github.com/user/repoName", 
            'User' : "user", 
            'User_Url' : "https://github.com/user", 
            'Public' : True, 
            'Date' : "2019-10-13T23:08:50Z" 
        }
        
        event1 = Event.from_dict(event_dict)
        event2 = Event.from_dict(event_dict)

        self.assertEqual(event1, event2)

if __name__ == "main":
    unittest.main()