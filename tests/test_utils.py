import pytest

from nycpython import utils


@pytest.fixture(scope='module')
def config():
    return {
        'KEY1': 1,
        'KEY2': 2,
    }


def test_check_required_settings(config):
    assert utils.check_required_settings(config, ('KEY1', 'KEY2')) is None


def test_check_required_settings_missing_key(config):
    with pytest.raises(RuntimeError) as e:
        utils.check_required_settings(config, ('KEY1', 'KEY3'))
    assert 'KEY3' in e.value.args[0]
