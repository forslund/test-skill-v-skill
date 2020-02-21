from mycroft import MycroftSkill, intent_file_handler


class TestSkillV(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('v.skill.test.intent')
    def handle_v_skill_test(self, message):
        self.speak_dialog('v.skill.test')


def create_skill():
    return TestSkillV()

