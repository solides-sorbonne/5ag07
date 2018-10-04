# How to install FEniCS

## In the computer rooms in Jussieu:
To use git and fenics in the classroom:

At the command line open your `.bashrc` file in a text editor
```
subl $HOME/.bashrc
```
Then add these lines in the file opened and save (modify with your student number and password

```
git config --global  http.proxy https://studentnumber:password@134.157.103.2:3128
export https_proxy=https://studentnumber:password@134.157.103.2:3128
source /opt/fenics-2018.1/activate-fenics-2018.1.sh
```


## Cloud-based installations
You can run python programs jupyter notebooks and FEniCS on online servers. The basic service is free and can be a solution if all other installation systems fail.

* *advantages:* You do not need to install anything on your machine and you do note use the ressources of your machine

* *disadvantages:* It can be slow (especially Azure, colab seems better). You can use only jupyter notebooks, you share your date with google or microsoft, you do not a full control of the system, you need to be online with a good network connection.

### Google colab
* You need a google account
* You can use this example to start https://colab.research.google.com/drive/1yhw-E21eEa4-ej27abiJiHj064iRaetS#scrollTo=iF68ZCvDTvo5
* You can save the notebooks and your working environment on your google drive

### Microsoft Azure
Another possibility is using azure notebbok (you need a Microsoft account)
https://fenics-cmaurini.notebooks.azure.com/nb/notebooks/FEniCS%20demo.ipynb

## On your personal machine

### On ubuntu (preferred installation):
````
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:fenics-packages/fenics
sudo apt-get update
sudo apt-get install --no-install-recommends fenics
````

### Using Anaconda (should theoretically work on linux/macosx/windows):
* Install Anaconda https://www.anaconda.com/download/
* At the command line
```
!conda config --add channels conda-forge
!conda install -y fenics
```

### Using docker virtual machines (suggested method if other fail).:
* See https://fenicsproject.org/download/ on the docker section and https://fenics-containers.readthedocs.io/en/latest/index.html
