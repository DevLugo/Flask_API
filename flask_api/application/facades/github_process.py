from ..services.github.github_service import GithubService
from ..repositories import github_user
from ..models.github_user import GitHubUser

class GitHubProcess():
    def __init__(self):
        self.git_service = GithubService()

    def download_and_store(self, amount=150):
        user_list_json = []
        if amount > 100: 
            #Do all the necesary request and store the values on users
            requested_amount = 0
            while requested_amount < amount:
                user_list_json = user_list_json + self.git_service.get_users(100, requested_amount).json()
                requested_amount += 100
        else:
            users = self.git_service.get_users()
            user_list_json = users.json()
        
        #cut the result
        user_list_json = user_list_json[:amount]
        user_list_git:dict = [GitHubUser(u['login'],u['id'],u['avatar_url'],u['type'], u['url']) for u in user_list_json]
        
        github_user.batch_insert(user_list_git)
