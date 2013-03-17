__author__ = 'derek'
import untappd_object


class Beer(untappd_object.UntappdObject):

    @property
    def id(self):
        """
        :type: string
        """
        return self._id

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

    def _init_attributes(self):
        self._name = untappd_object.NotSet
        self._abv = untappd_object.NotSet
        self._label = untappd_object.NotSet
        self._description = untappd_object.NotSet
        self._style = untappd_object.NotSet
        self._id = untappd_object.NotSet

    def _setup_attributes(self, attributes):
        self._name = attributes['beer_name']
        self._abv = attributes['beer_abv']
        if 'beer_style' in attributes:
            self._style = attributes['beer_style']
        if 'beer_description' in attributes:
            self._description = attributes['beer_description']
        if 'beer_label' in attributes:
            self._label = attributes['beer_label']
