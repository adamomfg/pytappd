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
<<<<<<< HEAD
venue = 257163

def GetPonyCheckins(checkin):
  if checkin.get('venue'):
    if checkin['venue']['venue_name'] == 'The Pony Bar':
      return checkin
  return None

checkins = lush.GetUserCheckins({'limit': 50})
for checkin in checkins:
  if GetPonyCheckins(checkin):
    pony_checkins.append(checkin)
    continue

marker_checkin = checkins[-1]['checkin_id']

while lush.GetUserCheckins({'limit': 50, 'max_id': marker_checkin}):
  checkins = lush.GetUserCheckins({'limit': 50, 'max_id': marker_checkin})
  if len(checkins) > 1:
    for checkin in checkins:
      if GetPonyCheckins(checkin):
        pony_checkins.append(checkin)
  marker_checkin = checkins[-1]['checkin_id']
  continue
  
pony_uniques = []

for pony_checkin in pony_checkins:
  if pony_checkin['beer']['beer_name'] not in pony_uniques:
    pony_uniques.append(pony_checkin['beer']['beer_name'])
=======

checkins = GetUserCheckins(lush)
while True:
  if not checkins:
    break

  pony_checkins.extend(filter(IsPonyCheckin, checkins))
  marker_checkin = checkins[-1].get('checkin_id')
  checkins = GetUserCheckins(lush, max_id=marker_checkin)

pony_uniques = set()
pony_uniques.update([c['beer']['beer_name'] for c in pony_checkins])
>>>>>>> eef8331e57b88f16e647fa047a1dbe080614f148
