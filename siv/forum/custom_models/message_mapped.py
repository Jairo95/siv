class WorryMessageMapped:
    def __init__(self, worry_user, worry_message, opinion_message_list):
        self.worry_user = worry_user
        self.worry_message = worry_message
        self.opinion_message_list = opinion_message_list


class OpinionMessageMapped:
    def __init__(self, worry_user, opinion_message):
        self.worry_user = worry_user
        self.opinion_message = opinion_message
