class Employee:
    def __init__(self,id,firstname,lastname,username,password,mobile,employee_status_id):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.mobile = mobile
        self.employee_status_id = employee_status_id

    def grt_fullname(self):
        return f"{self.firstname} {self.lastname}"