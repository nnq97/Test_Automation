# Automated test - Login to VistaSoft Monitor IoT Solution

This program will run an automated test system to login VistaSoft Monitor IoT Solution main page using Chrome.

# Installation
1. Download the **feature** folder
2. Create a virtual environment for the program
3. Install the depended packages in requirements.txt using
> pip install -r requirements.txt
4. The next important thing is setup **chromedriver**. 
* The chromedriver can be downloaded from the official link (https://chromedriver.chromium.org/downloads).
* Unzip and copy the executable to somewhere that Python and Selenium will be able to find it.
** The easiest place to put it is in C:\Windows

# Run the test case
To run the test script, use the following instruction in the virtual environemnet.
> behave feature/vistasoft.feature

