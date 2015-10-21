#Auto-Store
**Demo of an online automobile store.**

The app
code and template code is currently based on examples from the book
"Flask Web Development" by Miguel Grinberg. This will change as the project
matures.


##Prerequisites
- Linux OS (might work on Windows with some minor tweaking)
- python
- python-dev
- git
- pip
- virtualenv


##Prequisite Installation Instructions (Ubuntu)
**Update package lists**
```
sudo apt-get update
```

**Install python**

*It is very likely that python is already installed.*
```
sudo apt-get install python
```

**Install pip**
```
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
sudo apt-get update
sudo apt-get install python-pip
```

**Install virtualenv**
```
sudo pip install virtualenv
```

**Install python-dev**
```
sudo apt-get install python-dev
```

**Install git**
```
sudo apt-get install git
```


##Prequisite Installation Instructions (Debian)
**Update package lists**
```
sudo apt-get update
```

**Install python**

*It is very likely that python is already installed.*
```
sudo apt-get install python
```

**Install pip**
```
sudo apt-get install python-pip
```

**Install virtualenv**
```
sudo pip install virtualenv
```

**Install python-dev**
```
sudo apt-get install python-dev
```

**Install git**
```
sudo apt-get install git
```


##Prequisite Installation Instructions (other Linux distros / Windows)
To be added at a later time...


##Run the App
Your shiny new app comes with the Flask-Script extension, which allows a
finer level of control over your app's execution from the command line. Also
included, thanks to Miguel Grinberg, is a ```manage.py``` script which makes
use of Flask-Script to provide some necessary commands. The
following command executes your app on the development server with debugging
and auto-restarts enabled.
```
git clone https://github.com/richgieg/auto-store.git
cd auto-store
source setup
./manage.py runserver
```


##Connect
Now that your app is running on the development server, you can access it
from your browser by visiting the following address:
```
http://localhost:5000
```


##Stop
*Press CTRL+C in your terminal to stop development server.*
```
```


##Deactivate the Virtual Environment
When you're done developing and testing your app, you can return your shell
back to its original state by deactivating the virtual environment.
```
deactivate
```


##Reactivating the Virtual Environment
In order to run the app again after deactivating the virtual environment, you
will need to reactivate it.
```
source activate
```
