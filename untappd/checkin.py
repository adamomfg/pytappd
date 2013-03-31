import untappd_object


class Checkin(untappd_object.UntappdObject):
  
  def __init__(checkin_comment=None, media=None, created_at=None, venue=None,
               checkin_id=None, comments=None, source=None, beer=None, user=None,
               rating_score=None, toasts=None, brewery=None, badges=None)