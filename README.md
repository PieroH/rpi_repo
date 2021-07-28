## RaspberryPi ServerApp Configuration

#### Python-Django

[[1] - developer.mozilla.org ](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)


[[2] -  virtualenvwrapper ](https://virtualenvwrapper.readthedocs.io/en/latest/)


[[3] - Django Documentation](https://docs.djangoproject.com/en/3.2/)



# HOW TO RUN THE VIRTUAL ENVIRONMENT FOR THE Raspberry Server

``` bash

# Get pip and upgrade
sudo apt-get install pip
python3 -m pip install --upgrade pip
```

=> Installing virtual environment package
``` bash
sudo pip3 install virtualenvwrapper

```
=> Navigating into .bashrc configuration file & adding the code from below

```bash 
nano ~/.bashrc
```
=> Adding Python VirtualEnv config.

```bash 
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

=> Applying changes

```bash 
source ~/.bashrc
```

=> Creating and enabling working virtual envirnment with mkvirtualenv <name_of_Venv>

```bash 
# mkvirtualenv <name_of_environment>
mkvirtualenv rpienv
```

=> Should return: 
``` bash
created virtual environment CPython3.8.5.final.0-64 in 99ms
  creator CPython3Posix(dest=/home/piero/.virtualenvs/fitenv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/piero/.local/share/virtualenv)
    added seed packages: pip==20.3.3, setuptools==51.3.3, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```
=> Install pip and all required packages with compatible versions from requirements.txt file

```bash 
# Install all packages from Requirements.txt
pip install -r requirements.txt
```



# DEV - RUN APP OPERATIONS
### 1. Check Your IP Address for Raspberry Pi, which should be on the same network as Fitminder Application
### 2. Navigate to  ..rpi_repo/rpi_server/rpi_server/  directory
### 3. Open settings.py file and search for "ALLOWED_HOSTS = []" 
### 4. Change the values to ALLOWED_HOSTS = ['0.0.0.0','<your_ip_address>'] then SAVE file
### 5. Run Main Server from Rpi_Server  (path with manage.py)
```bash 
  python3 manage.py runserver 0.0.0.0:8080
```
# Raspberry Pi Should Be ready for Incomming Messages from Fitminder Django WebApplication
