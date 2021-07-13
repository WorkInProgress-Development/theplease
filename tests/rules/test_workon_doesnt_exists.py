import pytest
from theplease.rules.workon_doesnt_exists import match, get_new_command
from theplease.types import Command


@pytest.fixture(autouse=True)
def envs(mocker):
    return mocker.patch(
        'theplease.rules.workon_doesnt_exists._get_all_environments',
        return_value=['theplease', 'code_view'])


@pytest.mark.parametrize('script', [
    'workon tehplease', 'workon code-view', 'workon new-env'])
def test_match(script):
    assert match(Command(script, ''))


@pytest.mark.parametrize('script', [
    'workon theplease', 'workon code_view', 'work on tehplease'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, result', [
    ('workon tehplease', 'workon theplease'),
    ('workon code-view', 'workon code_view'),
    ('workon zzzz', 'mkvirtualenv zzzz')])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, ''))[0] == result
