nycpython.com
=============

The official website of the NYC Python meetup group.

Technologies
++++++++++++

We will be using the following technologies

- `Python 3`_
- Flask_, a microframework
- Jinja2_, a template engine

.. _Flask: http://flask.pocoo.org/docs/
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Python 3: http://docs.python.org/3/

Getting Started
+++++++++++++++

Here's everything you need to know to get a copy of nycpython.com running
locally.

What You Need
-------------

- Git_
- `A GitHub account`_
- `The code`_
- VirtualBox_
- Vagrant_ (`docs <http://docs.vagrantup.com/v2/>`_)

.. _Git: http://git-scm.com/downloads
.. _A GitHub account: https://github.com
.. _The code: https://github.com/NYCPython/nycpython.com
.. _Vagrant: http://downloads.vagrantup.com/
.. _VirtualBox: https://www.virtualbox.org/wiki/Downloads

Setup
-----

After installing VirtualBox and Vagrant, `fork the code on GitHub`_ and clone it
locally by executing the following command, replacing ``USERNAME`` with your
GitHub username::

    $ git clone git@github.com:USERNAME/nycpython.com.git

After doing that, execute the following command to build your local virtual
machine::

    $ vagrant up

You can access all of your code locally, but you will need the virtual machine
to access the server. To access the virtual machine's command line interface,
execute the following command::

    $ vagrant ssh

To run the nycpython.com server, execute the following commands on the virtual
machine::

    $ workon nycpythoncom
    $ python wsgi.py

The site can be accessed in your browser by visiting `localhost:5050`_.

.. _fork the code on GitHub: https://github.com/NYCPython/nycpython.com/fork
.. _localhost:5050: http://localhost:5050

Meetup API
----------

In order to work with the `Meetup API`_, you will first need to create a `Meetup
API Key`_.

.. _Meetup API: http://www.meetup.com/meetup_api/
.. _Meetup API Key: http://www.meetup.com/meetup_api/key/

Twitter API
-----------

In order to work with the `Twitter API`_, you will first need to create a
`Twitter Application`_. Once you have created the application, you will be able
to retrieve its OAuth settings.

.. _Twitter API: https://dev.twitter.com/docs/api/1.1
.. _Twitter Application: https://dev.twitter.com/apps/new

Contributing
++++++++++++

A list of issues can be found on GitHub_. Issues are categorized as graphics
(e.g., logos, banners), front-end (e.g., HTML, CSS, JavaScript), and back-end
(e.g., Python, API Integration).

Pick one and start hacking away!

Testing
-------

Before you push your changes back to GitHub and submit a pull request, you
probably want to run the test suite. To prepare for running the tests, install
the testing requirements::

    $ pip install -r tests/requirements.txt

The test suite can be run with tox_::

    $ tox

After you're done, be sure to add your name and GitHub profile to AUTHORS.rst.

.. _GitHub: https://github.com/NYCPython/nycpython.com/issues
.. _tox: http://tox.rtfd.org
