class User:
    def __init__(self, user_id: int, posts: list[dict], albums: list[dict], photos: list[dict]) -> None:
        self.id: int = user_id
        self.posts: list[dict] = posts
        self.albums: list[dict] = albums
        self.photos: list[dict] = photos

    def to_dict(self) -> dict:
        return {
            'userID': self.id,
            'posts': self.posts,
            'albums': self.albums,
            'photos': self.photos
        }
