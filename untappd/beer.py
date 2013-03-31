import untappd_object


class Beer(untappd_object.UntappdObject):

  def __init__(self, beer_id=None, name=None, label=None, abv=None, style=None,
               description=None, brewery=None):

    self.name = name
    self.id = beer_id
    self.label = label
    self.abv = abv
    self.style = style
    self.description = description
    self.brewery = brewery
    self.style = style