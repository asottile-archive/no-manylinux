import subprocess
import sys

import pytest


@pytest.fixture
def venv(tmpdir):
    env = tmpdir.join('venv')
    subprocess.check_call((sys.executable, '-mvirtualenv', env))
    return env


@pytest.fixture
def venv_installed(venv):
    subprocess.check_call((venv.join('bin/pip'), 'install', '.'))
    return venv


def _download_pkg(tmpdir, venv, pkg):
    dest = tmpdir.join('dest').ensure_dir()
    pip = venv.join('bin/pip')
    subprocess.check_call((pip, 'download', '--dest', dest, '--no-deps', pkg))
    ret = dest.listdir()
    dest.remove()
    return [x.basename for x in ret]


def test_normal(tmpdir, venv):
    pkg, = _download_pkg(tmpdir, venv, 'libsass==0.19.4')
    assert 'manylinux1' in pkg


def test_with_no_manylinux_installed(tmpdir, venv_installed):
    ret = _download_pkg(tmpdir, venv_installed, 'libsass==0.12.3')
    assert ret == ['libsass-0.12.3.tar.gz']


def test_no_manylinux2010(tmpdir, venv_installed):
    ret = _download_pkg(tmpdir, venv_installed, 'coincurve==12.0.0')
    assert ret == ['coincurve-12.0.0.tar.gz']


# TODO: test manylinux2014


def test_uninstall_restores_original_behaviour(tmpdir, venv_installed):
    pip = venv_installed.join('bin/pip')
    subprocess.check_call((pip, 'uninstall', '-y', 'no-manylinux'))
    test_normal(tmpdir, venv_installed)
