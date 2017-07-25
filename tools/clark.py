'''
    CLARK - metagenomics tool
'''

import logging
import subprocess

import tools

TOOL_NAME = 'clark'
TOOL_VERSION = '1.2.3.1'

_log = logging.getLogger(__name__)   # pylint: disable=C0103

class ClarkTool(tools.Tool):
    """Tool wrapper for the CLARK metagenomics tool"""

    def __init__(self, install_methods=None):
        if install_methods is None:
            install_methods = [tools.CondaPackage(TOOL_NAME, version=TOOL_VERSION, executable='CLARK')]
        tools.Tool.__init__(self, install_methods=install_methods)

    def version(self):
        return TOOL_VERSION

    def execute(self, args, variant='standard', stdout=None):  # pylint: disable=W0221
        '''Run a CLARK command.

        Args:
            args: list of command-line arguments
            variant: CLARK variant to run ('standard' or 'light')
        '''

        assert variant in ('standard', 'light')
        tool_cmd = [self.install_and_get_path()+('-l' if variant=='light' else '')] + args
        _log.debug(' '.join(tool_cmd))
        if stdout:
            stdout = open(stdout, 'w')
        subprocess.check_call(tool_cmd, stdout=stdout)
        if stdout:
            stdout.close()
