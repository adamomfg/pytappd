


class _NotSetType:
    def __repr__(self):
        return "NotSet"  # pragma no cover
NotSet = _NotSetType()


class BasicUntappdObject(object):

    def __init__(self, attributes):
        self._setup_attributes(attributes)



class UntappdObject(BasicUntappdObject):
    pass