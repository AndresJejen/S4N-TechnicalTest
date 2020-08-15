import json


class EventEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'Id': o.Id,
                'Type': o.Type,
                'Repo_Id': o.Repo_Id,
                'Repo_Name': o.Repo_Name,
                'Repo_Url': o.Repo_Url,
                'User': o.User,
                'User_Url': o.User_Url,
                'Public': o.Public,
                'Date': o.Date
            }
            return to_serialize
        except AttributeError:
            return super().default(o)