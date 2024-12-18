from sqlalchemy.orm import sessionmaker
from .models import UserState, engine

Session = sessionmaker(bind=engine)

class BotStateStorage:
    def __init__(self):
        self.session = Session()

    def get_state(self, user_id):
        state = self.session.query(UserState).filter_by(telegram_user_id=user_id).first()
        return state.state if state else None

    def set_state(self, user_id, state):
        existing_state = self.session.query(UserState).filter_by(telegram_user_id=user_id).first()
        if not existing_state:
            new_state = UserState(telegram_user_id=user_id, state=state)
            self.session.add(new_state)
        else:
            existing_state.state = state
        self.session.commit()

    def clear_state(self, user_id):
        state = self.session.query(UserState).filter_by(telegram_user_id=user_id).first()
        if state:
            self.session.delete(state)
            self.session.commit()
