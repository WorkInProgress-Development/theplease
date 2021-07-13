import pytest
from theplease.argument_parser import Parser
from theplease.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['theplease'], _args()),
    (['theplease', '-a'], _args(alias='please')),
    (['theplease', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='please', enable_experimental_instant_mode=True)),
    (['theplease', '-a', 'fix'], _args(alias='fix')),
    (['theplease', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['theplease', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['theplease', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['theplease', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['theplease', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['theplease', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['theplease', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['theplease', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
