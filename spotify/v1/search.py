from spotify import values


class SearchContext(object):

    def __init__(self, version):
        self.version = version

    def get(self, q, types, market=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'q': q,
            'type': ','.join(types),
            'market': market,
            'limit': limit,
            'offset': offset
        })

        response = self.version.request('GET', '/search', params=params)
        return SearchInstance(self.version, response.json())


class SearchInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def albums(self):
        from spotify.v1.album import AlbumPage
        return AlbumPage(self.version, self._properties.get('albums', []), 'items')

    @property
    def artists(self):
        from spotify.v1.artist import ArtistPage
        return ArtistPage(self.version, self._properties.get('artists', []), 'items')

    @property
    def playlists(self):
        from spotify.v1.user.playlist import PlaylistPage
        return PlaylistPage(self.version, self._properties.get('playlists', []), 'items')

    @property
    def tracks(self):
        from spotify.v1.track import TrackPage
        return TrackPage(self.version, self._properties.get('tracks', []), 'items')
