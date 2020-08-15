import unittest

from S4NGithubApi.domain.Empresa import Empresa
from S4NGithubApi.shared.domain_model import DomainModel
from S4NGithubApi.respository import empresarepo as memrepo
import uuid


class TestEmpresasEmpresaMemRepo(unittest.TestCase):

    def setUp(self):
        """ setUp """
        
        self.domain_empresas = [
            {
                'id': '913694c6-435a-4366-ba0d-da5334a611b2',
                'Name': "EmpresaTest0",
                'IdActualSoft': 0,
                'IdOldSoft': 1,
                'DBName': "DBEmpresaName0",
                'IdStatus': 0
            },
            {
                'id': uuid.uuid4(),
                'Name': "EmpresaTest1",
                'IdActualSoft': 2,
                'IdOldSoft': None,
                'DBName': "DBEmpresaName1",
                'IdStatus': 1
            }
        ]

    def _check_results(self, domain_model_list, data_list):

        self.assertEqual(len(domain_model_list), len(data_list))
        self.assertTrue(all([isinstance(dm, DomainModel) for dm in domain_model_list]))
        self.assertEqual(set([dm.id for dm in domain_model_list]), set([d['id'] for d in data_list]))

    def test_repository_list_without_parameters(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)
        result = repo.list()

        self._check_results(
            result,
            self.domain_empresas
        )


    def test_repository_list_with_filters_unknown_key(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        with self.assertRaises(KeyError) as context:
            repo.list(filters={'name': 'aname'})


    def test_repository_list_with_filters_unknown_operator(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        with self.assertRaises(ValueError) as context:
            repo.list(filters={'price__in': [20, 30]})


    def test_repository_list_with_filters_IdActualSoft(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        self._check_results(
            repo.list(filters={'IdActualSoft': 2}),
            [self.domain_empresas[1]]
        )


    def test_repository_list_with_filters_IdActualSoft_eq(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        self._check_results(
            repo.list(filters={'IdActualSoft': 2}),
            [self.domain_empresas[1]]
        )

    def test_repository_list_with_filters_IdOldSoft(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)
        result = repo.list(filters={'IdOldSoft': None})

        self._check_results(
            result,
            [self.domain_empresas[1]]
        )


    def test_repository_list_with_filters_IdOldSoft_eq(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        self._check_results(
            repo.list(filters={'IdOldSoft': None}),
            [self.domain_empresas[1]]
        )
        
    # def test_repository_list_with_filters_price_lt(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)

    #     self._check_results(
    #         repo.list(filters={'price__lt': 60}),
    #         [storageroom_dicts[0], storageroom_dicts[3]])


    # def test_repository_list_with_filters_price_gt(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)
    #     self._check_results(
    #         repo.list(filters={'price__gt': 60}),
    #         [storageroom_dicts[1]]
    #     )


    # def test_repository_list_with_filters_size(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)

    #     self._check_results(
    #         repo.list(filters={'size': 93}),
    #         [storageroom_dicts[3]]
    #     )


    # def test_repository_list_with_filters_size_eq(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)
    #     self._check_results(
    #         repo.list(filters={'size__eq': 93}),
    #         [storageroom_dicts[3]]
    #     )


    # def test_repository_list_with_filters_size_lt(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)
    #     self._check_results(
    #         repo.list(filters={'size__lt': 60}),
    #         [storageroom_dicts[2]]
    #     )


    # def test_repository_list_with_filters_size_gt(self):
    #     repo = memrepo.EmpresaMemRepo(self.domain_empresas)
    #     self._check_results(
    #         repo.list(filters={'size__gt': 400}),
    #         [storageroom_dicts[1]]
    #     )


    def test_repository_list_with_filters_id(self):
        repo = memrepo.EmpresaMemRepo(self.domain_empresas)

        self._check_results(
            repo.list(filters={'id': '913694c6-435a-4366-ba0d-da5334a611b2'}),
            [self.domain_empresas[0]]
        )

    

