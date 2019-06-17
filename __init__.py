from mycroft import MycroftSkill, intent_file_handler


class BabyTalk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('talk.baby.intent')
    def handle_talk_baby(self, message):
        age = ''

        self.speak_dialog('talk.baby', data={
            'age': age
        })


def create_skill():
    return BabyTalk()

