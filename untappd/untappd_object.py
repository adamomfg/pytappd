#TODO do we want to set a base object for untappd objects? do they share enough
# qualities to need a shared type?


class _NotSetType:
  def __repr__(self):
    return "NotSet"  # pragma no cover
NotSet = _NotSetType()


class BasicUntappdObject(object):

  def __init__(self, attributes):
    self._init_attributes()
    self._setup_attributes(attributes)


#TODO determine what an Untappdobject vs a BasicUntappdObject would require
class UntappdObject(BasicUntappdObject):
    pass
