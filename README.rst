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

If you do not have Python 3 installed, you will also need:

- VirtualBox_
- Vagrant_ (`docs <http://docs.vagrantup.com/v2/>`_)

.. _Git: http://git-scm.com/downloads
.. _A GitHub account: https://github.com
.. _The code: https://github.com/NYCPython/nycpython.com
.. _Vagrant: http://downloads.vagrantup.com/
.. _VirtualBox: https://www.virtualbox.org/wiki/Downloads

What You Need to Know
---------------------

Once you are familiar with Flask, it is recommended that you also become
familiar with blueprints_ and `application factories`_. For more information
about application factories, please check out `this post`_ by `Matt Wright`_.

.. _application factories: http://flask.pocoo.org/docs/patterns/appfactories/
.. _blueprints: http://flask.pocoo.org/docs/blueprints/
.. _Matt Wright: https://github.com/mattupstate
.. _this post: http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html

Setup
-----

After installing VirtualBox and Vagrant (see above), `fork the code on GitHub`_
and clone it locally by executing the following command, replacing ``USERNAME``
with your GitHub username::

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

Settings
--------

Most settings are read from environment variables. For a full list, please check
``nycpython/settings.py``. It can become difficult to maintain these variables,
especially when working with Vagrant. To make it easier, a file called
``settings.cfg`` can be placed inside the ``instance`` folder. Any settings
defined here will override the defaults.  ``instance/example_settings.cfg`` can
be used as an example for how to set up such a file.

Meetup API
----------

In order to work with the `Meetup API`_, you will need a `Meetup API Key`_. You
will also need to know the ID of the group for which you want to get data. In
the case of NYC Python, the group ID is ``263790``.

.. _Meetup API: http://www.meetup.com/meetup_api/
.. _Meetup API Key: http://www.meetup.com/meetup_api/key/

Twitter API
-----------

In order to work with the `Twitter API`_, you will need to create a
`Twitter Application`_. Once you have created the application, you will be able
to retrieve its OAuth settings.

.. _Twitter API: https://dev.twitter.com/docs/api/1.1
.. _Twitter Application: https://dev.twitter.com/apps/new

Contributing
++++++++++++

A list of issues can be found on GitHub_. Issues are categorized according to
specific areas of focus. The can be used to help find issues in which you are
particularly interested.

Pick one and start hacking away!

After you're done, be sure to add your name and GitHub profile to AUTHORS.rst.

.. _GitHub: https://github.com/NYCPython/nycpython.com/issues

Testing
-------

Before you push your changes back to GitHub and submit a pull request, you
probably want to run the test suite. To prepare for running the tests, install
the testing requirements::

    $ pip install -r tests/requirements.txt

The tests should be run using tox_::

    $ tox

If you are using Vagrant, make sure you connect to your virtual machine first::

    $ vagrant ssh

Once connected::

    $ workon nycpythoncom
    $ pip install -r tests/requirements.txt
    $ tox

.. _tox: http://tox.rtfd.org
