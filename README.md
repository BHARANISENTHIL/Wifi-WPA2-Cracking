# Wifi-WPA2-Cracking
Cracking/Bruteforcing  Wifi WPA2 passwords using python

Requirements:
  Python 3 or higher
  Wordlist File
  Network adapter

Steps:
  1. Save the program with the filename wifi_cracker.py in a new folder.
  
  2. Create a text file wihin the same folder with the filename Wordlist.txt.
     This wordlist should contain a list of passwords in the consecutive lines.
  
  3.Connect a network adapter in your computer such as an Alfa network adapter.
    Make sure it works or install the required drivers.
     
  3.Install Python3 or higher in your Windows compueter.
  
  4.Install the pywifi library using the following commmands in Command Prompt:
      import pywifi
      pip install pywifi / pip3 install pywifi (for python version 3)
      
  3.Locate to you project folder and Create a virtual environment to your project by entering the commands:
        pip install virtualenv 
        python -m venv myenv
        myenv\Scripts\activate
       Now a virtual environment is created in your project folder and the code can be executed within the environment.
  
  5.After setting up the virtual environment, run the program using the command:
        python wifi_cracker.py
  
  6.To deactivate the virtual environment you can use the command:
        deactivate

      
  
      
