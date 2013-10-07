import user

VENUE = 257163


def GetUserCheckins(user_obj, limit=50, max_id=None):
  request = {'limit': limit}
  if max_id is not None:
    request['max_id'] = max_id
  return user_obj.GetUserCheckins(request)


def IsPonyCheckin(checkin):
  if 'venue' not in checkin:
    return False
  return checkin['venue'].get('venue_name') == 'The Pony Bar'


lush = user.User(user_name='adampsyche')
pony_checkins = []

checkins = GetUserCheckins(lush)
while True:
  if not checkins:
    break

  pony_checkins.extend(filter(IsPonyCheckin, checkins))
  marker_checkin = checkins[-1].get('checkin_id')
  checkins = GetUserCheckins(lush, max_id=marker_checkin)

pony_uniques = set()
pony_uniques.update([c['beer']['beer_name'] for c in pony_checkins)
