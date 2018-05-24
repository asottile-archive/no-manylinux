import subprocess
import sys

import pytest


@pytest.fixture
def venv(tmpdir):
    env = tmpdir.join('venv')
    subprocess.check_call((
        sys.executable, '-m', 'virtualenv', env.strpath, '-p', sys.executable,
    ))
    return env


def _download_libsass(tmpdir, venv):
    dest = tmpdir.join('dest').ensure_dir()
    subprocess.check_call((
        venv.join('bin/pip').strpath, 'download',
        '--dest', dest.strpath, '--no-deps',
        'libsass==0.12.3',
    ))
    ret = dest.listdir()
    dest.remove()
    return [x.basename for x in ret]


def test_normal(tmpdir, venv):
    ret = _download_libsass(tmpdir, venv)
    assert ret == ['libsass-0.12.3-cp36-cp36m-manylinux1_x86_64.whl']


def test_with_no_manylinux_installed(tmpdir, venv):
    subprocess.check_call((venv.join('bin/pip').strpath, 'install', '.'))
    ret = _download_libsass(tmpdir, venv)
    assert ret == ['libsass-0.12.3.tar.gz']


def test_uninstall_restores_original_behaviour(tmpdir, venv):
    pip = venv.join('bin/pip').strpath
    subprocess.check_call((pip, 'install', '.'))
    subprocess.check_call((pip, 'uninstall', '-y', 'no-manylinux1'))
    test_normal(tmpdir, venv)
