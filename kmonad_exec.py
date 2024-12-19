from PyQt5 import QtGui
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from Classes.QtSingleApplication import QtSingleApplication
import sys
import os
import subprocess

def receiving(msg):
    print(msg)
    global filename
    if msg == "1":
        option1_triggered()
    elif msg == "2":
        option2_triggered()
    elif msg == "3":
        option3_triggered()
    elif msg == "4":
        option4_triggered()
    elif msg == "ctrl":
        option_ctrl_triggered()
    elif msg == "show 5": 
        option_show_triggered()
    elif msg == "show 6":
        old_filename = filename
        filename = "LAlted"
        option_show_triggered()
        filename = old_filename
    elif msg == "show 7":
        old_filename = filename
        filename = "RAlted"
        option_show_triggered()
        filename = old_filename
    elif msg == "show 8":
        old_filename = filename
        filename = "LShifted"
        option_show_triggered()
        filename = old_filename
    elif msg == "show 9":
        old_filename = filename
        filename = "LAltedSpaceSingleLAlted"
        option_show_triggered()
        filename = old_filename

def quitApp(app):
    os.system("pkill kmonad")
    app.close()
    app.quit()
    sys.exit()


class ClosingQWidget(QWidget):
    def __init__(self,app):
        super(ClosingQWidget,self).__init__()
        self._app = app

    def closeEvent(self, a0: QCloseEvent) -> None:
        quitApp(self._app)
        return super().closeEvent(a0)
def option1_triggered(timeout=500):
    global icon
    icon = QIcon("/home/craig/bin/icons/Backspace.png")
    global filename
    filename = "Normal"
    tray.setIcon(icon)
    msgBox = QMessageBox(QMessageBox.Icon.NoIcon,"Alt Mode","")
    msgBox.setIconPixmap(QPixmap("/home/craig/bin/icons/Backspace.png"))
    msgBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    timer=QTimer()
    timer.timeout.connect(msgBox.accept)
    timer.start(timeout)
    msgBox.exec_()
def option2_triggered():
    global icon
    icon = QIcon("/home/craig/bin/icons/Shift.png")
    global filename
    filename = "LShiftedSwitch"
    tray.setIcon(icon)
    msgBox = QMessageBox(QMessageBox.Icon.NoIcon,"Alt Mode","")
    msgBox.setIconPixmap(QPixmap("/home/craig/bin/icons/Shift.png"))
    msgBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    timer=QTimer()
    timer.timeout.connect(msgBox.accept)
    timer.start(500)
    msgBox.exec_()
def option3_triggered():
    global icon
    icon = QIcon("/home/craig/bin/icons/Alt.png")
    global filename
    filename = "LAltedSpaceSingle"
    tray.setIcon(icon)
    #dummyWindow =QWidget()
    msgBox = QMessageBox(QMessageBox.Icon.NoIcon,"Alt Mode","")
    msgBox.setIconPixmap(QPixmap("/home/craig/bin/icons/Alt.png"))
    msgBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    timer=QTimer()
    timer.timeout.connect(msgBox.accept)
    timer.start(500)
    msgBox.exec_()
def option_ctrl_triggered():
    global icon
    icon = QIcon("/home/craig/bin/icons/Ctrl.png")
    global filename
    filename = "LCtrlTappedInMode"
    tray.setIcon(icon)
    #dummyWindow =QWidget()
    msgBox = QMessageBox(QMessageBox.Icon.NoIcon,"Alt Mode","")
    msgBox.setIconPixmap(QPixmap("/home/craig/bin/icons/Ctrl.png"))
    msgBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    timer=QTimer()
    timer.timeout.connect(msgBox.accept)
    timer.start(250)
    msgBox.exec_()

    
    
    

def option4_triggered():
    #not used right now
    icon = QIcon("/home/craig/.local/share/icons/hicolor/16x16/apps/3365_wordpad.0.png")
    tray.setIcon(icon)
def option_edit_script():
    os.system("kate /home/craig/.kmonad_keys.cfg &")
def option_edit_script_close():
    os.system("kate /home/craig/.kmonad_keys.cfg &")
    quitApp(app)
def option_edit_python_Kate():
    os.system("kate /home/craig/bin/kmonad_exec.py")
def option_edit_python_VSCode():
    os.system("/usr/share/code/code -n /home/craig/bin /home/craig/bin/kmonad_exec.py")
def option_reload_script():
    global icon
    global previousIcon
    global tray
    return_value = subprocess.run(["/home/craig/.local/bin/kmonad","/home/craig/.kmonad_keys.cfg", "-d"],shell=False,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    if return_value.returncode == True:
        
        print(return_value.stderr)
        
        ErrorWindow = QWidget(window)
        edit=QPushButton("Edit Config",ErrorWindow)
        edit.clicked.connect(option_edit_script)
        doc = QPlainTextEdit(ErrorWindow)
        doc.setPlainText(return_value.stderr)
        doc.setFixedSize(800,500)
        font=QFont()
        font.setPointSize(12)
        font.setFamily("monospace")
        doc.setFont(font)
        shortcut = QShortcut(Qt.Key.Key_Escape,ErrorWindow,lambda: myClose_Window(ErrorWindow))
        shortcut.setAutoRepeat(False)
        layout = QVBoxLayout()
        layout.addWidget(doc)
        layout.addWidget(edit)
        ErrorWindow.setLayout(layout)
        ErrorWindow.show()
        previousIcon = icon
        icon = QIcon("/home/craig/bin/icons/RedX.png")
        tray.setIcon(icon)
        window.setVisible(True)
        ErrorWindow.setVisible(True)


        # msgBox = QMessageBox(QMessageBox.Icon.NoIcon,"Alt Mode","")
        # msgBox.setIconPixmap(QPixmap("/home/craig/bin/icons/RedX.png"))
        # msgBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
        # timer=QTimer()
        # timer.timeout.connect(msgBox.accept)
        # timer.start(500)
        # msgBox.exec_()
    else:

        option1_triggered(2000)
        os.system("pkill kmonad; /home/craig/.local/bin/kmonad /home/craig/.kmonad_keys.cfg &")
def myClose_Window(window2):
    #window2.setVisible(False)
    window2.close()
    
    
def option_show_triggered():
    file ="/home/craig/.kmonad_keys.cfg"
    window2 = QWidget()
    doc = QPlainTextEdit(window2)
    text=open(file).read()
    text = text[text.find("(deflayer "+filename):]
    text = '\n'.join(text.splitlines()[1:7])
    text = f"layer: {filename}\n-------------------------------------\n\n{text}"
    doc.setPlainText(text)
    doc.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    doc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    doc.setFixedSize(2700,400)
    font=QFont()
    font.setPointSize(22)
    font.setFamily("monospace")
    doc.setFont(font)
    
    shortcut = QShortcut(Qt.Key.Key_Escape,window2,lambda: myClose_Window(window2))
    shortcut.setAutoRepeat(False)
    layout = QVBoxLayout()
    layout.addWidget(doc)
    window2.setLayout(layout)
    window2.show()
def choose_keyboard(myText):
    
    global keyboardDict
    global current_keyboard
    file = keyboardDict[myText]["file"]
    cmd = """sed -i -E "s@(.*input\(device-file )\\".*\\"\)@\\1\\"{file}\\"\)@g" /home/craig/.kmonad_keys.cfg  """.format(file=file)
    os.system(cmd)
    current_keyboard = myText
    option_reload_script()

def showSubMenu(menu: QMenu):
    global keyboardOptions
    global keyboardDict
    #check current keyboard
    hwinfo = subprocess.Popen("sudo hwinfo --keyboard --short | grep /dev/input",shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    #hwinfo = subprocess.run(["grep","/dev/input"],shell=False,stdin=hwinfo.stdout,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    hwinfo = hwinfo.communicate()[0]
    hwinfo = hwinfo.splitlines()
    for action in keyboardOptions:
        kmOptionGroup.removeAction(action)
        chooseKeyboardMenu.removeAction(action)
    keyboardOptions = []
    keyboardDict = {}
    for i in hwinfo:
        mySplit = i.split("   ")
        myFile = mySplit[0].lstrip(" ").rstrip(" ")
        event = myFile.split("/dev/input/")[1]
        myName = mySplit[1].lstrip(" ").rstrip(" ")
        action = QAction(myName + "," + event)
        action.setCheckable(True)
        if action.text() == current_keyboard:
            action.setChecked(True)
        action.triggered.connect(lambda checked, item=action: choose_keyboard(item.text()))
        keyboardOptions.append(action)
        kmOptionGroup.addAction(action)
        keyboardDict[action.text()]={"file":myFile,"event":event,"name":action.text()}
    chooseKeyboardMenu.addActions(keyboardOptions)
    chooseKeyboardMenu.adjustSize()
def myContextMenuShow():
    global menu
    cursor = QCursor().pos()
    menu.exec_(QPoint(cursor.x()-100,cursor.y()-240))

        

#QSystemTrayIcon.ActivationReason.Context

filename='/home/craig/.kmonad_Normal.layer'
sendMsg="null"
if (len(sys.argv) > 1):
    sendMsg=sys.argv[1]
if (len(sys.argv) > 2):
    sendMsg=f"{str(sys.argv[1])} {str(sys.argv[2])}"
appGuid = 'F3FF80BA-BA05-4277-8063-82A6DB9245A2'
app = QtSingleApplication(appGuid, sys.argv)
icon=QIcon("/home/craig/bin/icons/Backspace.png")
previousIcon = QIcon("/home/craig/bin/icons/Backspace.png")
if app.isRunning():
    app.sendMessage(sendMsg)
    app.close()
    sys.exit()
else:
    app.messageReceived.connect(receiving )
    app.setQuitOnLastWindowClosed(False)
    
        
         
    
    window = QWidget()
    window.show()
    window.setVisible(False)

    
    # Adding an icon
    icon = QIcon("/home/craig/bin/icons/Backspace.png")
    
    # Adding item on the menu bar
    tray = QSystemTrayIcon(app)
    tray.setIcon(icon)
    tray.setVisible(True)
    
    # Creating the options
    menu = QMenu()
    option1 = QAction("Show Keyboard")
    option2 = QAction("Edit Kmonad Script")
    option3 = QAction("Edit Python Script - Kate")
    option5 = QAction("Edit Python Script - VS Code")
    option4 = QAction("Reload Script")
    
    current_keyboard=subprocess.Popen("grep input\(device-file ~/.kmonad_keys.cfg",shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    current_keyboard = current_keyboard.communicate()[0].decode("utf-8")
    current_keyboard = current_keyboard.replace("input(device-file \"","").replace("\")","").replace(" ","").replace("\t","").replace("\n","")
    chooseKeyboardMenu = QMenu("Choose Keyboard")
    menu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    chooseKeyboardMenu.aboutToShow.connect(lambda : showSubMenu(chooseKeyboardMenu))
    hwinfo = subprocess.Popen("sudo hwinfo --keyboard --short | grep /dev/input",shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    #hwinfo = subprocess.run(["grep","/dev/input"],shell=False,stdin=hwinfo.stdout,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    hwinfo = hwinfo.communicate()[0]
    hwinfo = hwinfo.splitlines()
    kmOptionGroup = QActionGroup(chooseKeyboardMenu)
    kmOptionGroup.setExclusive(True)
    keyboardOptions = []
    keyboardDict = {}
    for i in hwinfo:
        mySplit = i.split("   ")
        myFile = mySplit[0].replace(" ","")
        event = myFile.split("/dev/input/")[1]
        myName = mySplit[1].lstrip(" ").rstrip(" ")
        action = QAction(myName + "," + event)
        action.setCheckable(True)
        myText = action.text()

        if current_keyboard == myFile:
            current_keyboard = myText
            action.setChecked(True)
        action.triggered.connect(lambda checked,item=action: choose_keyboard(item.text()))
        keyboardOptions.append(action)
        kmOptionGroup.addAction(action)
        keyboardDict[action.text()]={"file":myFile,"event":event,"name":action.text()}
    chooseKeyboardMenu.addActions(keyboardOptions)
    chooseKeyboardMenu.adjustSize()
 

    
    option1.triggered.connect(option_show_triggered)
    option2.triggered.connect(option_edit_script)
    option4.triggered.connect(option_reload_script)
    option3.triggered.connect(option_edit_python_Kate)
    option5.triggered.connect(option_edit_python_VSCode)
    menu.addAction(option1)
    menu.addSeparator()
    menu.addAction(option2)
    menu.addAction(option3)
    menu.addAction(option5)
    menu.addSeparator()
    menu.addAction(option4)
    menu.addSeparator()
    menu.addMenu(chooseKeyboardMenu)
    menu.addSeparator()
    
    
    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(lambda: quitApp(app))
    menu.addAction(quit)
    menu.adjustSize()
    # Adding options to the System Tray
    contextMenu = QMenu()
    contextMenu.aboutToShow.connect(myContextMenuShow)
    tray.setContextMenu(contextMenu)
    """@grisuthedragon The workaround I can think of is, show the menu by yourself, not through setContextMenu.
    You can handle the QSystemTrayIcon::activated signal.
    When the ActivationReason is QSystemTrayIcon::Context, popup your QMenu on the tray icon, whose position could be got from QSystemTrayIcon::geometry().
    """
    #return_value = subprocess.run(["/home/craig/.local/bin/kmonad","/home/craig/.kmonad_keys.cfg", "-d"], shell=False, stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    option_reload_script()
    
    app.exec_()
