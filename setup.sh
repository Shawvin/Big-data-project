#! /bin/sh


sudo yum install -y python-matplotlib python-imaging python-pip
pip install tweepy --user
pip install textblob --user

# download and install anaconda for pandas, jupyter
# wget http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
# bash Anaconda3-4.0.0-Linux-x86_64.sh

curl -O https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh
bash Anaconda3-5.3.1-Linux-x86_64.sh

# set environment variables to load spark libs in jupyter
echo "export PYSPARK_DRIVER_PYTHON_OPTS=\"notebook\"" >> ~/.bashrc
echo "export PYSPARK_DRIVER_PYTHON=jupyter"  >> ~/.bashrc

# upgrade spark python to work with python 3
sudo yum upgrade -y spark-python


