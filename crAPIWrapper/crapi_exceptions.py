class InvalidCredentials(Exception):
    def __init__(self,email: str,password: str, message: str ) -> None:
        self.email = email,
        self.password = password
        super().__init__(message)


class PostNotFound(Exception):
    def __init__(self,post_id: str, message: str ) -> None:
        self.post_id = post_id
        super().__init__(message)