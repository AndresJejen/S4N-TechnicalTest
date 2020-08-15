from S4NGithubApi.shared.domain_model import DomainModel

class Gist(object):
    def __init__(
        self,
        Id: str,
        Url: str,
        ForksUrl: str,
        CommitsUrl: str,
        HtmlUrl: str,
        Node_Id: str,
        GitPullurl: str,
        GitPushUrl: str,
        Public: bool,
        Created_at: str,
        UpdatedAt: str,
        OwnerId: str,
        OwnerUrl: str,
    ):
        """Creates a Gist Object

        Args:
            Id (str): Id of the Gist
            Url (str): [description]
            ForksUrl (str): [description]
            CommitsUrl (str): [description]
            HtmlUrl (str): [description]
            Node_Id (str): [description]
            GitPullurl (str): [description]
            GitPushUrl (str): [description]
            Public (bool): [description]
            Created_at (str): [description]
            UpdatedAt (str): [description]
            OwnerId (str): [description]
            OwnerUrl (str): [description]
        """
        self.Id = Id
        self.Url = Url
        self.ForksUrl = ForksUrl
        self.CommitsUrl = CommitsUrl
        self.HtmlUrl = HtmlUrl
        self.Node_Id = Node_Id
        self.GitPullurl = GitPullurl
        self.GitPushUrl = GitPushUrl
        self.Public = Public
        self.Created_at = Created_at
        self.UpdatedAt = UpdatedAt
        self.OwnerId = OwnerId
        self.OwnerUrl = OwnerUrl

    @classmethod
    def from_dict(cls, adict):
        gist = Gist(
            Id = adict['Id'],
            Url = adict['Url'],
            ForksUrl = adict['ForksUrl'],
            CommitsUrl = adict['CommitsUrl'],
            HtmlUrl = adict['HtmlUrl'],
            Node_Id = adict['Node_Id'],
            GitPullurl = adict['GitPullurl'],
            GitPushUrl = adict['GitPushUrl'],
            Public = adict['Public'],
            Created_at = adict['Created_at'],
            UpdatedAt = adict['UpdatedAt'],
            OwnerId = adict['OwnerId'],
            OwnerUrl = adict['OwnerUrl']
        )

        return gist

    def to_dict(self):
        return {
            'Id': self.Id,
            'Url': self.Url,
            'ForksUrl': self.ForksUrl,
            'CommitsUrl': self.CommitsUrl,
            'HtmlUrl': self.HtmlUrl,
            'Node_Id': self.Node_Id,
            'GitPullurl': self.GitPullurl,
            'GitPushUrl': self.GitPushUrl,
            'Public': self.Public,
            'Created_at': self.Created_at,
            'UpdatedAt': self.UpdatedAt,
            'OwnerId': self.OwnerId,
            'OwnerUrl': self.OwnerUrl
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Gist)