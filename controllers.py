import datetime
import random

from py4web import action, request, abort, redirect, URL, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_username

url_signer = URLSigner(session)

# Some constants.
MAX_RETURNED_USERS = 20  # Our searches do not return more than 20 users.
MAX_RESULTS = 20  # Maximum number of returned stories.


@action('index')
@action.uses('index.html', db, auth.user, url_signer)
def index():
    return dict(
        # COMPLETE: return here any signed URLs you need.
        submit_story_url=URL('submit_story', signer=url_signer),
        get_stories_url=URL('get_stories', signer=url_signer),
        vote_url=URL('vote', signer=url_signer)
    )


@action("submit_story", method="POST")
@action.uses(db, auth.user, url_signer.verify())
def submit_story():
    title = request.json.get('title')
    body = request.json.get('body')
    photos = request.json.get('photos')
    radius = request.json.get('radius')

    if not title or not body:
        return HTTP(400, "Missing required fields")

    story_id = db.story.insert(
        title=title,
        body=body,
        photos=photos,
        radius=radius,
        created_by=get_username(),
        created_on=datetime.datetime.utcnow()
    )

    return dict(story_id=story_id)


@action("get_stories")
@action.uses(db, auth.user, url_signer.verify())
def get_stories():
    stories = db(db.story).select(orderby=~db.story.created_on, limitby=(0, MAX_RESULTS)).as_list()
    return dict(stories=stories)


@action("vote", method="POST")
@action.uses(db, auth.user, url_signer.verify())
def vote():
    story_id = request.json.get('story_id')
    value = request.json.get('value')

    if not story_id or value not in (-1, 1):
        return HTTP(400, "Invalid vote parameters")

    story = db.story(story_id)
    if story is None:
        return HTTP(404, "Story not found")

    user = get_username()
    existing_vote = db((db.vote.story == story_id) & (db.vote.user == user)).select().first()

    if existing_vote:
        existing_vote.update_record(value=value)
    else:
        db.vote.insert(story=story_id, user=user, value=value)

    query = (db.vote.story == db.story.id) & (db.vote.value == 1) & (db.vote.story == story_id)
    upvotes = db(query).count()

    query = (db.vote.story == db.story.id) & (db.vote.value == -1) & (db.vote.story == story_id)
    downvotes = db(query).count()

    story.update_record(upvotes=upvotes, downvotes=downvotes)

    return dict(message="Vote submitted successfully")
