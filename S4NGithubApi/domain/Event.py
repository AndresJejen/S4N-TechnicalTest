from S4NGithubApi.shared.domain_model import DomainModel

class Event(object):

    def __init__(
        self,
        Id: str,
        Type: str,
        Repo_Id: int,
        Repo_Name: str,
        Repo_Url: str,
        User: str,
        User_Url: str,
        Public: bool,
        Date: str):
        """Creates an object of a Github Events

        - Args:
            - Id (str): Identifier of the Event
            - Type (str): type of event
            - Repo_Id (int): Id of the repository
            - Repo_Name (str): Name of the repo
            - Repo_Url (str): URl of the repo
            - User (str): Name of the user
            - User_Url (str): Url ofthe user
            - Public (bool): Public event?
            - Date (str): date of the event
        """
        self.Id         = Id
        self.Type       = Type
        self.Repo_Id    = Repo_Id
        self.Repo_Name  = Repo_Name
        self.Repo_Url   = Repo_Url
        self.User       = User
        self.User_Url   = User_Url
        self.Public     = Public
        self.Date       = Date

    @classmethod
    def from_dict(cls, adict):
        event = Event(
            Id=adict['Id'],
            Type=adict['Type'],
            Repo_Id=adict['Repo_Id'],
            Repo_Name=adict['Repo_Name'],
            Repo_Url=adict['Repo_Url'],
            User=adict['User'],
            User_Url=adict['User_Url'],
            Public=adict['Public'],
            Date=adict['Date']
        )
        return event

    def to_dict(self):
        return {
            'Id'  : self.Id,
            'Type'  : self.Type,
            'Repo_Id'  : self.Repo_Id,
            'Repo_Name'  : self.Repo_Name,
            'Repo_Url'  : self.Repo_Url,
            'User'  : self.User,
            'User_Url'  : self.User_Url,
            'Public'  : self.Public,
            'Date'  : self.Date
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Event)