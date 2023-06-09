import datetime
import random
from py4web.utils.populate import FIRST_NAMES, LAST_NAMES, IUP
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_username():
    return auth.current_user.get('username') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

db.define_table(
    'story',
    Field('title', 'string', requires=IS_NOT_EMPTY()),
    Field('body', 'text', requires=IS_NOT_EMPTY()),
    Field('photos', 'list:string'),
    Field('radius', 'integer', default=0),
    Field('created_by', 'reference auth_user', default=get_user_email),
    Field('created_on', 'datetime', default=get_time),
    Field('upvotes', 'integer', default=0),
    Field('downvotes', 'integer', default=0),
)

db.define_table(
    'vote',
    Field('story', 'reference story'),
    Field('user', 'reference auth_user', default=get_user_email),
    Field('value', 'integer', default=0),
)

db.commit()

def add_users_for_testing(num_users):
    # Test user names begin with "_".
    # Counts how many users we need to add.
    db(db.auth_user.username.startswith("_")).delete()
    num_test_users = db(db.auth_user.username.startswith("_")).count()
    num_new_users = num_users - num_test_users
    print("Adding", num_new_users, "users.")
    for k in range(num_test_users, num_users):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        username = "_%s%.2i" % (first_name.lower(), k)
        user = dict(
            username=username,
            email=username + "@ucsc.edu",
            first_name=first_name,
            last_name=last_name,
            password=username,  # To facilitate testing.
        )
        auth.register(user, send=False)
    db.commit()

# Comment out this line if you are not interested.
add_users_for_testing(5)
