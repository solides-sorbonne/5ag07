# 5AG07 - Introduction aux calculs non linéaires de structures par éléments finis
This repository collects the material to the class 5AG07 

* Some links to online resources [here](LINKS.md)

To use git and fenics in the classroom:

1. At the command line
```
subl $HOME/.bashrc
```
Then add these lines in the file opened and save (modify with your student number and password

```
export PATH=/opt/fenics/hashstack/fenics-2016.1-sl72/bin/:$PATH
git config --global  http.proxy https://studentnumber:password@134.157.103.2:3128
export https_proxy=https://studentnumber:password@134.157.103.2:3128
```
