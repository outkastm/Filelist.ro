from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
import traceback

log = CPLog(__name__)


class Base(TorrentProvider):

    urls = {
        'test': 'http://filelist.ro/',
        'login': 'http://filelist.ro/takelogin.php',
        'login_check': 'http://filelist.ro/my.php',
        'search': 'http://filelist.ro/browse.php?%s',
        'baseurl': 'http://filelist.ro/%s',
    }

    http_time_between_calls = 1  # Seconds

    def _searchOnTitle(self, title, movie, quality, results):

        url = self.urls['search'] % self.buildUrl(title, movie, quality)
        data = self.getHTMLData(url)

        if data:
            html = BeautifulSoup(data)

            try:
                result_table = html.find('div', attrs = {'class': 'visitedlinks'})
                if not result_table or 'Nu s-a gasit nimic!' in data.lower():
                    return

                entries = result_table.find_all('div', attrs = {'class': 'torrentrow'})
                for result in entries[0:]:

                    all_cells = result.find_all('div')

                    torrent = all_cells[1].find('a')
                    download = all_cells[2].find('a')

                    torrent_id = torrent['href']
                    torrent_id = torrent_id.replace('details.php?id=', '')

                    torrent_name = torrent.getText()

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
                    })

            except:
                log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))

    def getLoginParams(self):
        log.info('Logging in to filelist.ro with user [%s] and password [%s]', (self.conf('username'), self.conf('password')))
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
            'ssl': 'yes',
        }

		
    def loginSuccess(self, output):
        return 'logout.php?id=428896' in output.lower()

    loginCheckSuccess = loginSuccess
