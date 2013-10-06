import user

lush = user.User(user_name='adampsyche')

pony_checkins = []
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
    
marker_checkin = checkins[-1]['checkin_id']

while lush.GetUserCheckins({'limit': 50, 'max_id': marker_checkin}):
  checkins = lush.GetUserCheckins({'limit': 50, 'max_id': marker_checkin})
  if len(checkins) > 1:
    for checkin in checkins:
      if GetPonyCheckins(checkin):
        pony_checkins.append(checkin)
  marker_checkin = checkins[-1]['checkin_id']
  
pony_uniques = []

for pony_checkin in pony_checkins:
  if pony_checkin['beer']['beer_name'] not in pony_uniques:
    pony_uniques.append(pony_checkin['beer']['beer_name'])