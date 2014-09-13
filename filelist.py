from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent._filelist import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'Filelist'


class Filelist(MovieProvider, Base):
    cat_ids = [
        ([25], ['3d']),
        ([19], ['720p', '1080p']),
        ([3], ['dvdr']),
        ([1], ['brrip', 'dvdrip']),
    ]
    cat_backup_id = 0

    def buildUrl(self, title, media, quality):
        query = tryUrlencode({
            'search': '"%s" %s' % (title, media['info']['year']),
            'cat': self.getCatId(quality)[0],
        })
        return query
