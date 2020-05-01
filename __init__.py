from .main import Filelist


def autoload():
    return Filelist()


config = [{
    'name': 'filelist',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'Filelist',
            'description': 'See <a href="https://filelist.io">Filelist</a>',
            'wizard': True,
            'icon': ('AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAClhCylhCylhCylh'
                     'CylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLS'
                     'wvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSw'
                     'vLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwv'
                     'LSwvLSwvLSylhCylhCwvLSwvLSwvLSzVoh8vLSwvLSwvLSwvLSzVoh/Voh/Voh/Voh8vLSwvLSylhCylhCwvLSwvLSyeeyPVo'
                     'h8vLSwvLSwvLSyeeyPVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSx8ZCbVoh/Voh/Voh9bTCl8ZCbVoh8vLSwvLSwvLS'
                     'wvLSwvLSylhCylhCwvLSwvLSxbTCnVoh8vLSwvLSwvLSx8ZCbVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSxbTCnVoh8'
                     'vLSwvLSwvLSxbTCnVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSxbTCnVoh/Voh/Voh/Voh9bTCnVoh8vLSwvLSwvLSwv'
                     'LSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvL'
                     'SwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLS'
                     'wvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCylhCylhCylhCylhCylhCy'
                     'lhCylhCylhCylhCylhCylhCylhCylhCylhCylhCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                     'AAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'passkey',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 48,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                },
                {
                    'name': 'freeleech_score',
                    'advanced': True,
                    'label': 'Freeleech Extra',
                    'type': 'int',
                    'default': 0,
                    'description': 'Favours [FreeLeech] releases by giving them extra score eg. 100'
                },
                {
                    'name': 'freeleech_only',
                    'advanced': True,
                    'label': 'Freeleech Only',
                    'default': False,
                    'type': 'bool',
                    'description': 'Only search for [FreeLeech] torrents.',
                }
            ],
        },
    ],
}]
