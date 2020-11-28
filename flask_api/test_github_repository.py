# Standard library imports...
from unittest.mock import Mock, patch
import json 

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true

# Local Imports...
from application.facades.github_process import GitHubProcess
from application.models.github_user import GitHubUser
from application.models.github_user import GitHubUser as git_u_model
from application.repositories import github_user as git_repository

from basetestcase import BaseTestCase


class UserTest(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super(UserTest, cls).setUpClass()

    def setUp(self):
        super(UserTest, self).setUp()
        self.mock_json = open('application/mock/users.mock.json') 

    def tearDown(self):
        super(UserTest, self).tearDown()

    def test_batch_insert(self):
        mock_users = json.load(self.mock_json)
        total_mock_users = len(mock_users)

        user_list_git:dict = [GitHubUser(u['login'],u['id'],u['avatar_url'],u['type'], u['url']) for u in mock_users]
        git_repository.batch_insert(user_list_git)
        db_users = git_repository.get_all()
        assert_true(len(db_users) == total_mock_users)

    def test_get_page_page_1(self):
        mock_users = json.load(self.mock_json)
        total_mock_users = len(mock_users)

        user_list_git:dict = [GitHubUser(u['login'],u['id'],u['avatar_url'],u['type'], u['url']) for u in mock_users]
        git_repository.batch_insert(user_list_git)
        
        db_users = git_repository.get_page()
        current_id = 1
        for user in db_users:
            assert_true(user.id == current_id)
            current_id+=1

    def test_get_page_page_3(self):
        mock_users = json.load(self.mock_json)
        total_mock_users = len(mock_users)

        user_list_git:dict = [GitHubUser(u['login'],u['id'],u['avatar_url'],u['type'], u['url']) for u in mock_users]
        git_repository.batch_insert(user_list_git)
        
        db_users = git_repository.get_page(3)
        current_id = 51
        for user in db_users:
            assert_true(user.id == current_id)
            current_id+=1



