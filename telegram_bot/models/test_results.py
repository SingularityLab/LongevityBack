from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database_module import Base

class TestResults(Base):
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    test_name = Column(String(100))
    test_result = Column(String(100))
    test_date = Column(DateTime)

    user = relationship("User", back_populates="test_results")

    def __init__(self, user_id, test_name, test_result, test_date):
        self.user_id = user_id
        self.test_name = test_name
        self.test_result = test_result
        self.test_date = test_date