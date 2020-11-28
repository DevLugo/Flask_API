# Standard library imports...
import json 
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true

# Local Imports...
from application.services.github.github_service import GithubService
from application.models.github_user import GitHubUser
from application.repositories import github_user as git_repository
from application.facades.github_process import GitHubProcess
from basetestcase import BaseTestCase


class UserTest(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super(UserTest, cls).setUpClass()

    def setUp(self):
        super(UserTest, self).setUp()
        self.git_process = GitHubProcess()
        self.mock_json = open('./application/mock/users.mock.json') 

    def tearDown(self):
        super(UserTest, self).tearDown()

    @patch('application.services.github.github_service.requests.get')
    def test_download_and_store(self, mock_get):
        mock_users = json.load(self.mock_json)  
        total_mock_users = len(mock_users)
        
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_users

        self.git_process.download_and_store(amount=100)
        db_users = git_repository.get_all()

        assert_true(len(db_users) == total_mock_users)
        for i in range(total_mock_users):
            assert_true(mock_users[i]['login'] == db_users[i].username)
            assert_true(mock_users[i]['id'] == db_users[i].github_id)
            assert_true(mock_users[i]['avatar_url'] == db_users[i].image_url)
            assert_true(mock_users[i]['type'] == db_users[i].type)
            assert_true(mock_users[i]['url'] == db_users[i].github_url)

    @patch('application.services.github.github_service.requests.get')
    def test_download_specific_amount(self, mock_get):
        mock_users = json.load(self.mock_json)  
        total_mock_users = len(mock_users)
        
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_users
        expected_amount = 84

        self.git_process.download_and_store(expected_amount)
        db_users = git_repository.get_all()
        assert_true(len(db_users) == expected_amount)

    @patch('application.services.github.github_service.requests.get')
    def test_download_more_than_100(self,mock_get):
        mock_users = json.load(self.mock_json)  
        total_mock_users = len(mock_users)
        
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_users
        expected_amount = 84

        self.git_process.download_and_store(expected_amount)
        db_users = git_repository.get_all()
        assert_true(len(db_users) == expected_amount)
