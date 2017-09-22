from __future__ import absolute_import, unicode_literals

import logging

import pykka

from mopidy import backend
from . import library


logger = logging.getLogger(__name__)


class FileRBackend(pykka.ThreadingActor, backend.Backend):
    uri_schemes = ['filer']

    def __init__(self, config, audio):
        super(FileRBackend, self).__init__()
        self.library = library.FileRLibraryProvider(backend=self, config=config)
        self.playback = backend.PlaybackProvider(audio=audio, backend=self)
        self.playlists = None
