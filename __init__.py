from mycroft import MycroftSkill, intent_file_handler
import datetime


class BabyTalk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.time_turned_on = datetime.datetime.now()

    def age_to_string(self, value, word):
        age_string = ''
        if (value > 0):
            if (value > 1):
                age_string = str(value) + ' ' + word + 's'
            else:
                age_string = str(value) + ' ' + word
        return str(age_string)

    @intent_file_handler('beautiful.eyes.intent')
    def handle_beautiful_eyes(self, message):

        self.speak_dialog('talk.beautiful.eyes')

    @intent_file_handler('age.query.intent')
    def handle_age_query(self, message):
        age_datetime = datetime.datetime.now() - self.time_turned_on
        age_years = int(age_datetime.days/365)
        age_days = int(age_datetime.days%365)
        age_minutes = int(age_datetime.seconds/60)
        age_seconds = int(age_datetime.seconds%60)

        age_string = self.age_to_string(age_years, 'year') + ' '\
            + self.age_to_string(age_days, 'day') + ' '         \
            + self.age_to_string(age_minutes, 'minute') + ' '  \
            + self.age_to_string(age_seconds, 'second')

        self.speak_dialog('talk.baby.age', data={
            'age': age_string
        })

    @intent_file_handler('good.baby.intent')
    def handle_good_baby(self, message):

        self.speak_dialog('talk.good.baby')

def create_skill():
    return BabyTalk()