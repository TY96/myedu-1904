import pytest

from day_04 import Shell

if __name__ == '__main__':
    # pytest.main(['-s','-q','day_04'])
    pytest.main(['-s', '-q', '--alluredir', './Report/xml/', 'day_04'])
    # shell = Shell.Shell
    #
    #
    #
    # shell.invoke(['allure generate ./Report/xml -o ./Report/html --clean'])