[![Build Status](https://travis-ci.org/asottile/no-manylinux.svg?branch=master)](https://travis-ci.org/asottile/no-manylinux)

no-manylinux
============

Install this package to disable manylinux wheels when downloading from pip.

## Usage

```
# First install no-manylinux
pip install no-manylinux
# Now subsequent invocations of pip will ignore manylinux wheels
pip install ...
# To restore the original behaviour, simply `pip uninstall no-manylinux`
```

## Note

This package was previously called `no-manylinux1` but now addresses the
following manylinux standards:

- `manylinux1`
- `manylinux2010`
- `manylinux2014`

## What? Why?

The manylinux spec requires compliant packages to vendor binary dependencies
inside the wheel that is distributed.  Take for example a library which would
(prior to manylinux) dynamically link against `libssl`.  As `libssl` received
security patches, the system binaries would received updates from the OS's
package manager.  The python library which dynamically links would receive
these updates for free without need to recompile, reinstall, etc.  Under
manylinux, `libssl` is vendored inside the wheel.  To receive security
updates, you have to wait for the upstream to produce a new wheel and need to
know to install a new version of that library.  There's almost no visibility
about these vendored wheels which makes managing them at scale impossible.  As
such, some may choose to ignore this standard.

## Links

- https://stackoverflow.com/q/37231799/812183
- https://github.com/pypa/pip/issues/3689
- https://github.com/pypa/pip/issues/3689#issuecomment-219437150
