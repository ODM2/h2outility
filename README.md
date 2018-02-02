# H2O Utility #

A GUI-based and optionally headless tool to select times series values from a HydroServer, write the data to CSV files, and upload them to their respective HydroShare resources. The VisualUpdater must be used to intially select which HydroServer, HydroShare, and ODM Series should be used.

###### Requirements ######

These tools are written for Python 2.7.X 64-bit. Depending on the size of your datasets, 32-bit Python may run out of usable memory and cause requests to fail.

To download, install, and run this project, execute the following commands:

> Note: To use a virtual environment with this project, create and activate your virtual environment before running these commands.

```sh
git clone https://github.com/UCHIC/h2outility.git
cd h2outility
python -m pip install -r ./src/requirements.txt
python ./src/VisualUpdater.py
python ./src/SilentUpdater.py
```

***

#### H2O Utility Installer ####

To create a new installer, simply open the command prompt in the root folder, then run the following commands:

```sh
source windows_venv/Scripts/activate.bat
pynsist ./src/installer.cfg
```

The installer is in "src/build". The nsis folder contains the installer and all necessary packages.
