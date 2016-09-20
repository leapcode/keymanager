import pytest

from leap.keymanager.keys import build_key_from_dict
from common import ADDRESS
from common import KEY_FINGERPRINT
from common import PUBLIC_KEY
from common import PRIVATE_KEY
from common import ADDRESS_2
from common import KEY_FINGERPRINT_2
from common import PUBLIC_KEY_2
from common import PRIVATE_KEY_2
from leap.keymanager.wrapper import TempGPGWrapper


@pytest.fixture
def wrapper(keys=None):
    return TempGPGWrapper(keys=keys)


def _get_key(address, key_fingerprint, key_data, private):
    kdict = {
        'uids': [address],
        'fingerprint': key_fingerprint,
        'key_data': key_data,
        'private': private,
        'length': 4096,
        'expiry_date': 0,
        'refreshed_at': 1311239602,
    }
    key = build_key_from_dict(kdict)
    return key


@pytest.fixture
def public_key():
    return _get_key(ADDRESS, KEY_FINGERPRINT, PUBLIC_KEY, False)


@pytest.fixture
def public_key_2():
    return _get_key(ADDRESS_2, KEY_FINGERPRINT_2, PUBLIC_KEY_2, False)


@pytest.fixture
def openpgp_keys():
    return [
        _get_key(ADDRESS, KEY_FINGERPRINT, PUBLIC_KEY, False),
        _get_key(ADDRESS_2, KEY_FINGERPRINT_2, PUBLIC_KEY_2, False),
        _get_key(ADDRESS, KEY_FINGERPRINT, PRIVATE_KEY, True),
        _get_key(ADDRESS_2, KEY_FINGERPRINT_2, PRIVATE_KEY_2, True),
    ]
