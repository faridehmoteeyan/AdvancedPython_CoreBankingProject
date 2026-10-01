from abc import ABC,abstractmethod
from Common.Entities.employee import Employee

class IEmployeeRepository(ABC):
    @abstractmethod
    def get_by_username_pasword(self,username:str,password:str)->Employee:
        pass

    def insert_into_db(self,employee:Employee): #به جای دادن تمامی ورودی ها مشتری رو ریترن کنیم
        pass