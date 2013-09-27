#!/usr/bin/env bash

apt-get update > /dev/null
apt-get install -y python-software-properties
add-apt-repository ppa:fkrull/deadsnakes
apt-get update > /dev/null
apt-get install -y emacs git-core nano python3.3-dev python-pip vim

# Upgrade Pip before installing anything with it.
sudo pip install -U pip
sudo pip install -U virtualenvwrapper

# Make virtualenvwrapper available to vagrant
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc

# Set up a virtualenv. Make sure to use vagrant's home, otherwise it will be
# created in /root.
export WORKON_HOME=/home/vagrant/.virtualenvs
mkdir $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3.3 -a /vagrant nycpythoncom
sudo chown -R vagrant:vagrant $WORKON_HOME

# Install the requirements. Without the `--pre` flag Pip would see pytz's
# releases as pre-release versions and fail.
sudo -u vagrant /home/vagrant/.virtualenvs/nycpythoncom/bin/pip install --upgrade --pre --requirement /vagrant/requirements.txt
