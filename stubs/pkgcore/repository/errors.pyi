from ..exceptions import PkgcoreException, PkgcoreUserException

class RepoError(PkgcoreException):
    def __init__(self, msg: str):
        self.msg: str = ...

class InitializationError(RepoError, PkgcoreUserException):
    def __str__(self) -> str: ...
