# QR_detector_api

sometext

* nihaoma
* wohenhao

Table of Contents
-----------------

* [QR_detector_api](#qrdetectorapi)
* [Table of Contents](#table-of-contents)
* [Prerequisite](#prerequisite)
* [Demo #1: Detector](#demo-1-detector)
* [Demo #2: Database](#demo-2-database)
* [Setup](#setup)
* [How to Use](#how-to-use)


Prerequisite
------------

This QR_Detector_api was tested on both Jetson Nano and Jetson AGX Xavier DevKits. In order to run the demo below, you need to make sure you have the proper python packages installed on the target Jetson system, or local machine such as a x86 PC or Mac.

Please also make sure you have Python>=3.6 installed in your device.

To install the Python3 packages, simply run the command below in your terminal:

```shell
$ pip3 install -r requirement.txt
```

Furthermore, the app requires 'cv2'(OpenCV) module in Python3. If you are using a **Jetson Device**, the OpenCV module is pre-installed with the Jetpack, you do not need to install it again. For x86 PC or Mac user, please properly install the OpenCV module before you run the app.

<a name="prerequisite"></a>

Demo #1: Detector
-----------------

This demo illustrates how to

Demo #2: Database
-----------------

This demo illustrates how to

Setup
-----

Step-by-step

**Step #1**: Clone this repository

```bash
$ cd ~
$ git clone https://github.com/yqlbu/QR_detector_api
$ cd QR_detector_api
```

**Step #2**: Check Repository Tree

```bash
$ sudo apt-get install -y tree
$ tree
```
*** Your working directory should be shown as below:
```bash
.
├── db
│   └── README.md
├── db.py
├── demo_screenshots
├── init.py
├── main.py
├── README.md
├── requirement.txt
└── utils
    ├── authentication.py
    ├── db_argparser.py
    ├── db_utils.py
    ├── __init__.py
    ├── opencv.py
    ├── qr_argparser.py
    ├── qr_code.py
    └── timer.py
```


How to Use
----------

**Step #0**: Initiate an admin account and instantiate databases

```bash
$ python3 init.py
```
*** You will notice that, your working directory has added two folders: **/data** and **/config**

*** The program will create an admin account for the first-time you run the app, and the program will generate an **access_token** as well. You will need to save this access token for future use.

*** Paste the access_token inside the main.py, as shown below:

```python
# Token is for authorizing your identity
ACCESS_TOKEN="TOKEN"
```

**Step #1**: Run the detector api by running the command below

```bash

```

### Basic Usage

### Database

### Web Module

Coming soon ...
