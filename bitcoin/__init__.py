# Copyright (C) 2012-2018 The python-curiumlib developers
#
# This file is part of python-curiumlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-curiumlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import curium.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.10.2dev'

class MainParams(curium.core.CoreMainParams):
    MESSAGE_START = b'\xab\xd8\xe2\xd5'
    DEFAULT_PORT = 18745
    RPC_PORT = 18746
    DNS_SEEDS = (('dnsseed.mrmetech.me', 'dnsseed.mrmetech.me'),
)
    BASE58_PREFIXES = {'PUBKEY_ADDR':60,
                       'SCRIPT_ADDR':13,
                       'SECRET_KEY' :212}

class TestNetParams(curium.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('testnetcurium.jonasschnelli.ch', 'testnet-seed.curium.jonasschnelli.ch'),
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('curium.schildbach.de', 'testnet-seed.curium.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(curium.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
curium.core.params correctly too.
"""
#params = curium.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    curium.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = curium.core.coreparams = MainParams()
    elif name == 'testnet':
        params = curium.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = curium.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
