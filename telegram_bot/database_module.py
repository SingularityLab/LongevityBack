```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.user import User
from .models.test_results import TestResults

class DatabaseModule:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, user_id, username):
        session = self.Session()
        user = User(id=user_id, username=username)
        session.add(user)
        session.commit()
        session.close()

    def add_test_result(self, user_id, test_result):
        session = self.Session()
        test_result = TestResults(user_id=user_id, **test_result)
        session.add(test_result)
        session.commit()
        session.close()

    def get_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        return user

    def get_test_results(self, user_id):
        session = self.Session()
        test_results = session.query(TestResults).filter_by(user_id=user_id).all()
        session.close()
        return test_results
```