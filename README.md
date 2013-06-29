nycpython.com Hackathon
=======================

The official website for the NYC Python meetup group.

This website will help us announce events and reach out to the community.

Technologies
============

We will be using the following technologies.

- python3 (http://docs.python.org/3/)  
- flask (http://flask.pocoo.org/docs/) as a micro web application framework
- jinja2 (http://jinja.pocoo.org/docs/) as a templating tool
- postgres 9.0< (http://www.postgresql.org/docs/) for data storage
- sqlite (http://www.sqlite.org/docs.html) for testing
- sqlalchemy (http://www.sqlalchemy.org/) (see: http://www.meetup.com/nycpython/events/120485002/)
- python psycopg (http://initd.org/psycopg/docs/) & sqlite3 (http://docs.python.org/2/library/sqlite3.html)
- python virtualenv (http://pypi.python.org/pypi/virtualenv) python pip (http://pypi.python.org/pypi/pip)

You won't need to manually install any of these, beyond python3 and virtualenv. You should be able to pull in all these requirements using `pip`

See requirements.txt for a more detailed listing of requirements.

Installation
============

Instructions can be found here: (https://github.com/NYCPython/nycpython.com/wiki/Installation)

Virtual Machine
===============

We have a custom-built Lubuntu (http://lubuntu.net/) VM which you should be able to directly use to get up & running.

This VM can be run from VirtualBox (https://www.virtualbox.org/) on Linux/OS X/Windows.

Lubuntu is a lightweight, fully-featured varient of Ubuntu; the virtual machine should need only 512< MiB of RAM to run it. 
Since the disk image is fairly large (4 GiB,) have a member help you install it from a USB thumbdrive.

Once you've booted into the VM, you can use the default account: nycpython/password

We've set up the virtual machine similarly to the instructions in the following section:

Setup on Your Own Machine
=========================

Note that these steps are not required if you installed the virtual machine image mentioned in the previous section.

You can use these steps to set up your own machine.

    # install Sublime http://www.sublimetext.com/2 (not required)
    $ wget 'http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.1.tar.bz2'
    $ tar xjvf Sublime\ Text\ 2.0.1\ x64.tar.bz2 

    # install some useful editing & tool-chain software: 
    # git is the version control tool; vim is a text editor; tmux is a terminal multiplexer
    $ sudo apt-get install git vim tmux
    # This is not done on the virtual machine, but this is the time to clone the repository.
    # if you already have git set up, first two aren't required.
    $ git config --global user.name "Your Name Comes Here"
    $ git config --global user.email you@yourdomain.example.com
    $ git clone https://github.com/NYCPython/nycpython.com.git


    # install all the system software & Python packages
    $ sudo apt-get install sqlite3 postgresql
    $ sudo apt-get install python3.3{,-dbg,-dev-,-doc} cython3{,-dbg} python3-pip python-virtualenv

    # create your virtualenv 
    # insert the following three lines (minus the #'s) into the top of your .bashrc file
    # export WORKON_HOME=$HOME/.virtualenvs
    # export MSYS_HOME=/c/msys/1.0
    # source /usr/local/bin/virtualenvwrapper.sh
    # And execute the following commands.
    $ source .bashrc
    $ mkvirtualenv -p `which python3` nycpython

    # install packages
    $ cd nycpython.com/
    $ pip install -r requirements.txt # comment out psycopg2

    # enter a virtualenv (already set up on the VM)
    $ workon nycpython
    
    # run the server
    $ cd src/
    $ python3 server.py

GitHub & Git
============

The first thing you should do is ensure you're familiar with `git`

The official tutorial is http://git-scm.com/docs/gittutorial

The most important steps are as follows:

    $ git config --global user.name "Your Name Comes Here"
    $ git config --global user.email you@yourdomain.example.com
    $ git clone https://github.com/NYCPython/nycpython.com.git

This is all you need to get started. If you're using the VM, you should already have a cloned repository.

Just enter the nycpython.com directory and make sure everything is up-to-date:

    $ git pull

Alternatively, you can set up a GitHub account and fork this repository https://github.com/NYCPython/nycpython.com/fork

Regardless of how you set things up, ***we will accept contributions only as pull requests on GitHub.***

Getting Started
===============

Go to https://github.com/NYCPython/nycpython.com/issues pick an issue, and start hacking away!

Issues are broadly categorised as graphics work (logos, banners, visual elements,) front-end work (HTML/CSS/JS,) and back-end work (python/flask/API integration.) 

Issues relating to the Meetup API (http://www.meetup.com/meetup_api/) will require setting up a Meetup API key (http://www.meetup.com/meetup_api/key/)

A quick tutorial: http://www.meetup.com/meetup_api/

Issues relating to the Twitter API (https://dev.twitter.com/docs/api/1.1) will require setting up a Twitter API key.
