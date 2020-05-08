# QR_detector_api

This QR_detector_api demonstrates how to read/write identification data(JSON form) in a local database with a real-time detector. It can be used as a **real-ime employee check-in system**. Moreover, other IoT modules can be easily integrated with this api module.

The identification data JSON string will be encoded in a form of QR_Code.

* Each identification data object has two attributes: the **_id** and the **name** associated with that _id

* The Detector API runs at ~40 FPS on Jetson Xavier.
* All demos work on any Nvidia Jetson Devices such as TX2, Nano, and Xavier
* Furthermore, all demos should work on x86_64 PC or Mac as well.
* The embbed **Database Module** allows the user to retrieve any important data created by the detector.

The**Web Module** and the **Cloud Database Module** will be coming up soon ...

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

**[Step-by-step]**

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

**Step #1**: Add data

*** "-n" flag is for creating a new QR_Code data object, you need to speciy the name of the data in the console

eg: $ python3 main.py -n kevin

```bash
$ python3 main.py -n name
```

**Step #2**: Run the detector api by running the command below

```bash
$ python3 main.py -r

```

Basic Usage
-----------

App flag Table

Database

Other Usage
------------

Web Module
----------

Coming soon ...
