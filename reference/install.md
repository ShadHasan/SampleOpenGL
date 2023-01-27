### PIP install
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
```

It is important you use python3.9 instead of just python3, to ensure pip is installed for python 3.9.

If you see any permissions errors, you may need to use

```
python3.9 get-pip.py --user
```

If you get an error like No module named 'distutils.util' when you run python3.9 get-pip.py, and you are on a Debian-based Linux distribution, run

```
sudo apt install python3.9-distutils
```

### Sample OpenGL for python
```
# sudo apt-get install gcc python-dev python3-dev python<version of python>-dev

In my python3.9
sudo apt-get install gcc python3.9-dev

# install python openGL
python3.9 -m pip install PyOpenGL PyOpenGL_accelerate

# install glut
sudo apt-get install freeglut3-dev
```

### Reinstall numpy
````
$> python3.9 -m pip install --upgrade --force-reinstall numpy
```