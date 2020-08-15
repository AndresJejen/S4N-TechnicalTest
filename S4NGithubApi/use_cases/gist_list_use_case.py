from S4NGithubApi.shared import response_object as res
from S4NGithubApi.shared import use_case as uc

class GistListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_gist = self.repo.list(filters= request_object.filters)
        return res.ResponseSuccess(domain_gist)
