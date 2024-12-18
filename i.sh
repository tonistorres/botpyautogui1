MENU_ACCES="
----------------------------------------------------
Starting Python Studies With Selenium Library
---------------------------------------------------
"

TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}


INSTALL_LIBS(){
echo "$MENU_ISNTALL_SELENIUM"
    TIME
    pip install --upgrade pip
    pip3 install requests 
    pip3 install pyautogui
    pip3 install pyinstaller
    pip3 freeze > requirements.txt
}

EXECUTING_CODE(){
echo "$MENU_ACCES"
INSTALL_LIBS
which python3

}



MAIN(){
EXECUTING_CODE
}

MAIN