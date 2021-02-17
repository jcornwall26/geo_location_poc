from geo.store import Store


class GeoStore(Store):

    def __init__(self, store, geo_result):
        self._number = None

        if geo_result is None:
            print('geo_result is None')

        self.geo_result = geo_result
        super().__init__(store)

    @property
    def store(self) -> str:
        return self._store

    @property
    def number(self) -> str:
        if self._number is not None:
            return self._number
        return self.geo_result['number']

    @number.setter
    def number(self, value) -> str:
        self._number = value

    @property
    def street(self) -> str:
        return self.geo_result['street']

    @property
    def locality(self):
        return self.geo_result['locality']

    @property
    def country(self) -> str:
        return self.geo_result['country']

    @property
    def latitude(self) -> str:
        return self.geo_result['latitude']

    @property
    def longitude(self) -> str:
        return self.geo_result['longitude']

    def args(self, *args, **kwargs):
        y = { x: x for x in args}
        for i in y:
            print(i)
