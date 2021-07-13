import pytest
from theplease.types import Command
from theplease.rules.brew_reinstall import get_new_command, match


output = ("Warning: theplease 9.9 is already installed and up-to-date\nTo "
          "reinstall 9.9, run `brew reinstall theplease`")


def test_match():
    command = Command('brew install theplease', output)
    assert match(command)


@pytest.mark.parametrize('script', [
    'brew reinstall theplease',
    'brew install foo'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, formula, ', [
    ('brew install foo', 'foo'),
    ('brew install bar zap', 'bar zap')])
def test_get_new_command(script, formula):
    command = Command(script, output)
    new_command = 'brew reinstall {}'.format(formula)
    assert get_new_command(command) == new_command
