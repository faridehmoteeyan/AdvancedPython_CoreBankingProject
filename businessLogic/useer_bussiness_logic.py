from Common.DTOs.response import Response
class UserBusinessLogic():
    def login(self, username, password):
        if len(username)<3 or len(password)<3:
            return Response(False,"Invalid password or user name")
        return Response(True,None,None)
