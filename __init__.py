from main import Filelist

def start():
    return Filelist()

config = [{
    'name': 'filelist',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'providers',
            'list': 'torrent_providers',
            'name': 'Filelist.ro',
            'description': 'See <a href="http://filelist.ro">Filelist.ro</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                }
            ],
        }
    ]
}]
