import json


class GistEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'Id': o.Id,
                'Url': o.Url,
                'ForksUrl': o.ForksUrl,
                'CommitsUrl': o.CommitsUrl,
                'HtmlUrl': o.HtmlUrl,
                'Node_Id': o.Node_Id,
                'GitPullurl': o.GitPullurl,
                'GitPushUrl': o.GitPushUrl,
                'Public': o.Public,
                'Created_at': o.Created_at,
                'UpdatedAt': o.UpdatedAt,
                'OwnerId': o.OwnerId,
                'OwnerUrl': o.OwnerUrl
            }
            return to_serialize
        except AttributeError:
            return super().default(o)