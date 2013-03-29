__author__ = 'derek'
import untappd_object


class Beer(untappd_object.UntappdObject):

  def __init__(self, id=None, name=None, label=None, abv):
    self.id = id
    self.name = name

    @property
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def label(self):
        """
        :type: string
        """
        return self._label

    @property
    def abv(self):
        """
        :type: string
        """
        return self._abv

    @property
    def description(self):
        """
        :type: string
        """
        return self._description

    @property
    def style(self):
        """
        :type: string
        """
        return self._style

    def brewery(self):
        pass
