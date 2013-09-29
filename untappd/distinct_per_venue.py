import user

lush = user.User('adampsyche')

dpv = []
venue = 257163

# iterate over all distinct beers, check for venue, if found, add to list
# iterate all at venue, 

results = lush.GetDistinctBeers()
dpv.append(results)
while lush.GetDistinctBeers(params={'offset': 25}):
  dpv.append(results)