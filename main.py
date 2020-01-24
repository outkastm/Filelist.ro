import re
import time
import urllib,json
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt, getIdentifier
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback

log = CPLog(__name__)


class Filelist(MovieProvider, TorrentProvider):

    urls = {
        'test': 'https://filelist.ro/',
        'search': 'https://filelist.ro/api.php?%s',
        'detail': 'https://filelist.ro/detail.php?id=%s',
        'download': 'https://filelist.ro/download.php?id=%s&passkey=%s',
    }

    http_time_between_calls = 1  # Seconds

    cat_ids = [
        ([25], ['3d']),
        ([20], ['bd50']),
        ([19, 4], ['720p', '1080p']),
        ([6],  ['2160p']),
        ([19, 4, 1], ['brrip']),
        ([3, 19, 2, 4], ['dvdr']),
        ([1], ['dvdrip', 'scr', 'r5', 'tc', 'ts', 'cam']),
    ]
    cat_backup_id = 19
    def buildUrl(self, media, cat_id):
        return tryUrlencode({
            'username': self.conf('username'),
            'passkey': self.conf('passkey'),
            'action': 'search-torrents',
            'type': 'imdb',
            'query': getIdentifier(media),
            'category': cat_id,
        })

    def _search(self, movie, quality, results):
        matched_category_ids = self.getCatId(quality)
        cat_id = my_string = ','.join(map(str, matched_category_ids))
        url = self.urls['search'] % self.buildUrl(movie, cat_id)
        data = self.getJsonData(url)

        try:
            for result in data:
                freeleech = tryInt(result['freeleech'])
                torrent_score = 1
                torrent_score += self.conf('extra_score')
                if freeleech:
                    torrent_score += self.conf('freeleech_score')
                elif self.conf('freeleech_only'):
                    continue
                results.append({
                    'id': tryInt(result['id']),
                    'name': result['name'],
                    'url': self.urls['download'] % (result['id'],self.conf('passkey')),
                    'detail_url': self.urls['detail'] % result['id'],
                    'imdb_id': result['imdb'],
                    'size': tryInt(result['size']) / (1024 * 1024),
                    'seeders': tryInt(result['seeders']),
                    'leechers': tryInt(result['leechers']),
                    'score': torrent_score,
                })
        except:
            log.error('Failed getting results from %s: %s' % (self.getName(), traceback.format_exc()))
