import json
import logging

from clients.http import HTTPClient
from models.user import User
from config.app_environments import JSON_RESULT_FILENAME
from exceptions.user import UserNotFoundException


def __get_user_by_email(users: list[dict], email: str) -> dict:
    user = next((user for user in users if user['email'] == email), None)

    if user is None:
        raise UserNotFoundException()

    return user


if __name__ == '__main__':
    client = HTTPClient()

    users = client.get('/users')

    # These definitions can be standardized abstracting the endpoints of the HTTP client.
    # But, for this basic sample, it's not necessary at all
    user_id = __get_user_by_email(users, 'Nathan@yesenia.net')['id']
    posts = client.get(f'/posts?userId={user_id}')
    albums = client.get(f'/albums?userId={user_id}')
    photos = client.get(f'/photos?albumId=3')

    nathan_user = User(
        user_id=user_id,
        posts=posts,
        albums=albums,
        photos=photos,
    )

    # Save the JSON response instead of sending the consolidated data to stdout
    # to have a record of the example functionality
    with open(JSON_RESULT_FILENAME, 'w') as file:
        json.dump(nathan_user.to_dict(), file, indent=4)

    logging.info(f'Data consolidated and saved as {JSON_RESULT_FILENAME}')
