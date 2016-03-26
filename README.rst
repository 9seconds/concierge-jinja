concierge-jinja
===============

|PyPI| |Build Status| |Code Coverage|

``concierge-jinja`` provides support of Jinja2_ templates for
concierge_.

To interpret your ``~/.conciergerc`` as Jinja2 template, just use ``-u``
flag:

.. code-block:: shell

    $ concierge -u jinja2 -o ~/.ssh/config

or

.. code-block:: shell

    $ concierge-check -u jinja2 -o ~/.ssh/config


.. _Jinja2: http://jinja.pocoo.org
.. _concierge: https://github.com/9seconds/concierge

.. |PyPI| image:: https://img.shields.io/pypi/v/concierge-jinja.svg
    :target: https://pypi.python.org/pypi/concierge-jinja

.. |Build Status| image:: https://travis-ci.org/9seconds/concierge-jinja.svg?branch=master
    :target: https://travis-ci.org/9seconds/concierge-jinja

.. |Code Coverage| image:: https://codecov.io/github/9seconds/concierge-jinja/coverage.svg?branch=master
    :target: https://codecov.io/github/9seconds/concierge-jinja?branch=master
