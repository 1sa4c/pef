from SupportType import SupportType

class Support():
    _total_number_of_reactions = 0

    @classmethod
    def _increment_number_of_reactions(cls, x):
        cls._total_number_of_reactions += x

    def __init__(self, support_type: SupportType):
        if support_type == SupportType.ROLLER:
            self._increment_number_of_reactions(1)
        else:
            self._increment_number_of_reactions(2)

        self.support_type = support_type
        self.reaction_force = [None, None]

