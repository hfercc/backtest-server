import re

import tempfile
import os.path
import functools
import mimetypes

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files import File as FileWrapper
def store_file(fd):
    """
    Given a file-like object and stores it with default storage system.

    Returns a tuple (file_name, mime_type), where the file name is relative to
    MEDIA_ROOT.
    """

    name = default_storage.save(os.path.basename(fd.name), fd)

    return name, mimetypes.guess_type(name)[0] or ''
