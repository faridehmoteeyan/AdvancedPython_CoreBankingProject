class Response():
    def __init__(self,is_successed:bool,message:str,data=None):
        self.is_successed = is_successed
        self.message = message
        self.data = data