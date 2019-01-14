# (C) British Crown Copyright 2017, Met Office
#
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#

# Functions for getting data from NERSC.

from . import version_2c
from . import version_3
from . import observations
import datetime

def fetch(variable,dtime,version='none',user='pbrohan'):
    """Get data for one variable, from the 20CR archive at NERSC.

    Data wil be stored locally in directory $SCRATCH/20CR, to be retrieved by :func:`load`. If the local file that would be produced already exists, this function does nothing.

    Args:
        variable (:obj:`str`): Variable to fetch (e.g. 'prmsl').
        dtime (:obj:`datetime.datetime`): Date and time to get data for.
        version (:obj:`str`): 20CR version to retrieve data for.
        user (:obj:`str`): NERSC userid to use in retrieval. Only needed for v3-preliminary data. Defaults to 'pbrohan'. This should be your NERSC username.

    Raises:
        StandardError: If version is not a supported value.
 
    |
    """

    if variable=='observations':
        return observations.fetch_observations(dtime,
                                      version=version,
                                      user=user)

    if version=='2c':
        return version_2c.fetch(variable,dtime)
    if version in ('4.5.1','4.5.2'):
        return version_3.fetch(variable,dtime,version,user=user)

    raise Exception("Unsupported version %s" % version)
