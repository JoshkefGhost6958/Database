from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key = True,nullable=True)
    username = Column(String(22),nullable=False)
    isAdmin = Column(Boolean,server_default= "0",nullable=False)
    email = Column(String(25),nullable=False)
    account = relationship('Account',back_populates='owner')
    def __str__(self):
        status = self.isAdmin
        if(status):
            status = "Admin"
        else:
            status = "user"
        return f"User is {self.username} \nid :{self.id} \nstatus :{status}"

class Account(Base):
    __tablename__ = 'account'
    user_id = Column(Integer,ForeignKey("user.id"))
    accNo = Column(Integer,nullable=False,primary_key = True,unique=True)
    balance = Column(Integer,nullable=False,server_default="0")
    owner = relationship('UserModel',back_populates="account")

    def __str__(self):
        return f'user id :{self.user_id} account:{self.accNo}'

john = UserModel(id = 1,username="john",isAdmin=False,email="johndoe@gmail.com")
print(john)