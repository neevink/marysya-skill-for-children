from skill.entities.state import State


class SkillResponse:

    def __init__(self, skill_request: dict):
        self.request_json = skill_request
        self._is_start = skill_request['session']['new']
        self.answer = ''

        self.state = State.START
        self.current_path = None  # Текущий рисунок
        self.current_step = None  # Шаг текущего рисунка
        self.passed = []  # Нарисованные уже рисунки

        if 'state' in skill_request and 'session' in skill_request['state']:
            session_saves = skill_request['state']['session']
            try:
                self.state = State(session_saves['state'])
                self.current_path = session_saves['current_path']
                self.current_step = session_saves['current_step']
                self.passed = session_saves['passed']
            except:
                pass

        self.end_session = False  # Нужно ли завершить сессию

    @property
    def is_start(self):
        return self._is_start

    def get_user_input(self):
        # Список токенов, которые сказал пользователь
        return self.request_json['request']['nlu']['tokens']

    def get_json_response(self):
        response = {
            'version': self.request_json['version'],
            'session': self.request_json['session'],
            'response': {
                'end_session': self.end_session,
                'text': self.answer
            },
            'session_state': {
                'current_path': self.current_path,
                'current_step': self.current_step,
                'passed': self.passed,
                'state': self.state.value
            }
        }

        return response
