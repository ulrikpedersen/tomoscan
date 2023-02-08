tomoscan
===========================

|code_ci| |docs_ci| |coverage| |license|

.. note::

    This project is in very early development and intended for
    demonstration purposes only.

This project demonstrates the use of BlueSky to orchestrate a Tomography scan
for the new EPAC laser facility at Harwell Campus, UK.

============== ==============================================================
Source code    https://github.com/ulrikpedersen/tomoscan
Documentation  https://ulrikpedersen.github.io/tomoscan
Releases       https://github.com/ulrikpedersen/tomoscan/releases
============== ==============================================================

Some very brief examples of use:

.. code-block:: python

    from tomoscan import __version__

    print(f"Hello tomoscan {__version__}")

.. |code_ci| image:: https://github.com/ulrikpedersen/tomoscan/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/ulrikpedersen/tomoscan/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/ulrikpedersen/tomoscan/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/ulrikpedersen/tomoscan/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/ulrikpedersen/tomoscan/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/ulrikpedersen/tomoscan
    :alt: Test Coverage

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://ulrikpedersen.github.io/tomoscan for more detailed documentation.
