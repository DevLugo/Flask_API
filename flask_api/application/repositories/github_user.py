from application import db
from ..models.github_user import GitHubUser

def batch_insert(user_list:list)->bool:
    try:
        db.session.bulk_save_objects(user_list)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("ERROR")
        print(e)

    return False

def get_all():
    return db.session.query(GitHubUser).all()

def get_page(page=1, per_page=25):
    return GitHubUser.query.paginate(page, per_page, False).items

def clean_table():
    db.session.query(GitHubUser).delete()
    db.session.commit()

