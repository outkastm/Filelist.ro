Filelist.ro
===========

Couchpotato provider

How-to install
===========

 Download the Filelist.ro search provider
https://github.com/outkastm/Filelist.ro/archive/master.zip and extract it somewhere.

Shut down CouchPotatoServer, either by opening it up in a browser 
and going to "settings" -> "shutdown", or by terminating the process

 Open your CouchPotatoServer folder and traverse into the following directory
cd [pathtocouchpotato]/.couchpotato/couchpotato/core/media/_base/providers/torrent
From the extracted folder, put _filelist.py in this directory.

 Now traverse into the following directory
cd [pathtocouchpotato]/.couchpotato/couchpotato/core/media/movie/providers/torrent
From the extracted folder, put filelist.py in this directory.

 Startup CouchPotatoServer

How-to use
==========

Once installed as above, go about activating the provider as you would with any other provider in CouchPotato

Info
# If you upgrade Couchpotato, check that after the upgrade this files are still there.
