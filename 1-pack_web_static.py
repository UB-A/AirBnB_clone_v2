#!/usr/bin/python3
"""Fabric script to generate archive"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create .tgz archive from eb_static folder"""

    datim = datetime.now().strftime("%Y%m%d%H%M%S")
    tgzfile = "versions/web_static_" + datim + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + tgzfile + " web_static")
    if os.path.exists(tgzfile):
        return tgzfile
    else:
        return None
