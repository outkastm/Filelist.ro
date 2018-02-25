import time
from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback

log = CPLog(__name__)


class Filelist(MovieProvider, TorrentProvider):

    urls = {
        'test': 'https://filelist.ro/',
        'login': 'https://filelist.ro/takelogin.php',
        'login_check': 'https://filelist.ro/my.php',
        'search': 'https://filelist.ro/browse.php?%s',
        'baseurl': 'https://filelist.ro/%s',
    }

    http_time_between_calls = 1  # Seconds

    cat_ids = [
        ([25], ['3d']),
        ([20], ['bd50']),
        ([19, 4], ['720p', '1080p']),
        ([6], ['2160p']),
        ([3, 2], ['dvdr']),
        ([1], [['brrip', 'dvdrip', 'scr', 'r5', 'tc', 'ts', 'cam']),
    ]
    cat_backup_id = 0

    def buildUrl(self, title, media, cat_id):
        return tryUrlencode({
            'search': '"%s" %s' % (title, media['info']['year']),
            'cat': cat_id,
            'searchin': 1,
        })

    def _searchOnTitle(self, title, movie, quality, results):
        matched_category_ids = self.getCatId(quality)
        for cat_id in matched_category_ids:
            url = self.urls['search'] % self.buildUrl(title, movie, cat_id)
            data = self.getHTMLData(url)

            if not data:
                continue

            html = BeautifulSoup(data)

            try:
                result_table = html.find('div', attrs = {'class': 'visitedlinks'})
                if not result_table or 'Nu s-a gasit nimic!' in data.lower():
                    continue

                entries = result_table.find_all('div', attrs = {'class': 'torrentrow'})
                for result in entries:

                    all_cells = result.find_all('div')

                    torrent = all_cells[1].find('a')
                    download = all_cells[3].find('a')

                    freeleech = all_cells[1].find("img", {"alt": "FreeLeech"}) is not None
                    torrent_score = 0
                    if freeleech:
                        torrent_score += self.conf('freeleech_score')
                    elif self.conf('freeleech_only'):
                        continue

                    torrent_id = torrent['href']
                    torrent_id = torrent_id.replace('details.php?id=', '')

                    torrent_name = torrent.getText()

                    try:
                        added_date_tuple = time.strptime(all_cells[5].getText(), '%H:%M:%S%d/%m/%Y')
                        torrent_added = int(time.mktime(added_date_tuple))
                    except (ValueError, TypeError):
                        log.error('Unable to convert datetime from %s: %s', (self.getName(), traceback.format_exc()))
                        torrent_added = 0
                    torrent_age_in_days = int((time.time() - torrent_added) / 86400)

                    torrent_size = self.parseSize(all_cells[6].getText())
                    torrent_seeders = tryInt(all_cells[8].getText())
                    torrent_leechers = tryInt(all_cells[9].getText())
                    torrent_url = self.urls['baseurl'] % download['href']
                    torrent_detail_url = self.urls['baseurl'] % torrent['href']

                    results.append({
                        'id': torrent_id,
                        'name': torrent_name,
                        'size': torrent_size,
                        'seeders': torrent_seeders,
                        'leechers': torrent_leechers,
                        'url': torrent_url,
                        'detail_url': torrent_detail_url,
                        'score': torrent_score,
                        'date': torrent_added,
                        'age': torrent_age_in_days,
                    })

            except:
                log.error('Failed getting results from %s: %s' % (self.getName(), traceback.format_exc()))

    def getLoginParams(self):
        log.info('Logging in to filelist.ro with user [%s]' % (self.conf('username')))
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
            'ssl': 'yes',
        }

    def loginSuccess(self, output):
        return 'logout.php' in output.lower()

    loginCheckSuccess = loginSuccess
