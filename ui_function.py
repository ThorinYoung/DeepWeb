import os
import signal
import subprocess
import threading
import time
import webbrowser

import cv2
import matplotlib.pyplot as plt
import psutil
from PIL import Image
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import pymysql

from main import *  # IMPORTING THE MAIN.PY FILE
from PyQt5 import QtCore, QtGui, QtWidgets
from theme import Theme
from stabmaster.vidstab import VidStab

GLOBAL_STATE = 0  # NECESSARY FOR CHECKING WEATHER THE WINDOW IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True  # NECESSARY FOR CHECKING WEATHER THE WINDOW IS FULL SCREEN OR NOT
init = False  # NECESSARY FOR INITIALIZATION OF THE WINDOW.
settings_init = False
setting_text = "Setting > Video Enhance"
visible = True
theme = Theme.Theme1()
pic = None


# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world']


# THIS CLASS HOUSES ALL FUNCTION NECESSARY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):

    # ----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE
    def initStackTab(self):
        global init
        if not init:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enhance)
            self.ui.lab_tab.setText("Video Enhance")
            self.ui.frame_enhance.setStyleSheet(
                theme.background2)  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
            init = True

    ################################################################################################

    # ----> MAXIMISE/RESTORE FUNCTION
    # THIS FUNCTION MAXIMISES OUR MAIN WINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DONE.
    # THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png"))  # CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide()  # HIDE DRAG AS NOT NECESSARY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png"))  # CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()

    ################################################################################################

    # ----> RETURN STATUS MAX OR RESTORE
    # NECESSARY OFR THE MAXIMISE FUNCTION TRO WORK.
    @staticmethod
    def returnStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # ------> TOODLE MENU FUNCTION
    # CONTROL FOUR PAGES BUTTON ( SHOW OR HIDDEN )
    # =====NEED TO BE DONE========
    def toodleMenu(self):
        global visible
        if visible:
            visible = False
            self.ui.frame_enhance.setVisible(visible)
            self.ui.frame_repair.setVisible(visible)
            self.ui.frame_setting.setVisible(visible)
            self.ui.frame_user.setVisible(visible)
            self.ui.lab_appname.setVisible(visible)
        else:
            visible = True
            self.ui.frame_enhance.setVisible(visible)
            self.ui.frame_repair.setVisible(visible)
            self.ui.frame_setting.setVisible(visible)
            self.ui.frame_user.setVisible(visible)
            self.ui.lab_appname.setVisible(visible)

    ################################################################################################

    # -----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        # -----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(50, lambda: UIFunction.maximize_restore(self))

        # ----> REMOVE NORMAL TITLE BAR
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_head.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        # -----> RESIZE USING DRAG THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        self.sizegrip = QSizeGrip(self.ui.frame_drag)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        # DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        # -----> MINIMIZE BUTTON FUNCTION
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())

    ################################################################################################################
    # ----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet(theme.background1)

        if buttonName == 'bn_enhance':
            self.filename = None
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enhance)
            self.ui.lab_tab.setText("Video Enhance")
            self.ui.frame_enhance.setStyleSheet(
                theme.background2)  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_repair':
            self.filename = None
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_repair)
            self.ui.lab_tab.setText("Video Repair")
            self.ui.frame_repair.setStyleSheet(
                theme.background2)  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_user':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_user)
            self.ui.lab_tab.setText("User")
            self.ui.frame_user.setStyleSheet(
                theme.background2)  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_settings':
            global settings_init
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            self.ui.lab_tab.setText(setting_text)
            self.ui.frame_setting.setStyleSheet(
                theme.background2)  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
            if not settings_init:
                self.ui.frame_settings1.setStyleSheet(theme.background2)
                settings_init = True

    ################################################################################################################
    # ----> BUTTON IN ENHANCE AND REPAIR PAGES
    # USE THREADING TO AVOID GUI INTERRUPTION
    class Repair(threading.Thread):
        def __init__(self, filename, timet, bar, gpu):
            super().__init__()
            self.start_flag = threading.Event()
            self.filename = filename
            self.res = None
            self.time = timet
            self.bar = bar
            self.gpu = gpu

        def run(self):
            try:
                if self.gpu == "否":
                    self.res = subprocess.Popen(
                        ["python", "remaster/remaster.py", "--input", self.filename, "--reference_dir",
                         "remaster/example/references"], shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                else:
                    self.res = subprocess.Popen(
                        ["python", "remaster/remaster.py", "--input", self.filename, "--reference_dir",
                         "remaster/example/references", "--gpu"], shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                while not self.res.poll():
                    if self.start_flag.isSet():
                        break
                    st = str(self.res.stdout.readline())
                    temp = st.split("||")
                    if len(temp) == 3:
                        per = eval(temp[1])
                        print(per, "\n")
                        self.time.setText("{:.2%}".format(per))
                        self.bar.setValue(int(per * 100))
                    temp = st.split("+")
                    if len(temp) == 3:
                        global pic
                        pic = temp[1]
            except (KeyboardInterrupt):
                print("nothing")

    class Enhance(threading.Thread):
        def __init__(self, filename, timet, bar, fill, mode, pict):
            super().__init__()
            self.start_flag = threading.Event()
            self.filename = filename
            self.res = None
            self.time = timet
            self.bar = bar
            self.fill = fill
            self.mode = mode
            self.output = "enhance_res/" + self.filename.split('/')[-1]
            self.pic = pict

        def run(self):
            try:
                if self.mode == "默认":
                    stable = VidStab()
                else:
                    stable = VidStab(kp_method=self.mode)
                if self.fill == "黑色填充":
                    stable.stabilize(input_path=self.filename, output_path=self.output, border_type="black", my_bar=self.bar, my_time=self.time, my_pic=self.pic)
                elif self.fill == "黑色填充带边界":
                    stable.stabilize(input_path=self.filename, output_path=self.output, border_type="black", border_size=100, my_bar=self.bar, my_time=self.time, my_pic=self.pic)
                elif self.fill == "镜像":
                    stable.stabilize(input_path=self.filename, output_path=self.output, border_type="reflect", my_bar=self.bar, my_time=self.time, my_pic=self.pic)
                elif self.fill == "延伸虚化":
                    stable.stabilize(input_path=self.filename, output_path=self.output, border_type="replicate", my_bar=self.bar, my_time=self.time, my_pic=self.pic)
            except (KeyboardInterrupt):
                print("nothing")

    class VipEnhance(threading.Thread):
        def __init__(self):
            super().__init__()

        def run(self):
            try:
                subprocess.Popen(
                    ["Package/SAE1.exe"])
            except (KeyboardInterrupt):
                print("nothing")

    class WebConnect(threading.Thread):
        def __init__(self):
            super().__init__()

        def run(self):
            try:
                subprocess.Popen(
                    ["python", "webpage/app.py"])
            except (KeyboardInterrupt):
                print("nothing")

    # USE TIMER TO CREATE THE PICTURE PRESENT CIRCULAR
    def show_pic(self):
        if pic:
            im = cv2.imread(pic)
            img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            y, x = im.shape[:-1]
            frame = QImage(img, x, y, QImage.Format_RGB888)
            self.scene.clear()
            pix = QPixmap.fromImage(frame)
            self.scene.addPixmap(pix)
            # self.timer.start(2000)

    def show_pic2(self):
        if self.pic[0] != []:
            im = self.pic[0]
            # img = Image.fromarray(self.pic[0])
            # img.save("tmp/test.jpg")
            # im = cv2.imread("tmp/test.jpg")
            img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            y, x = im.shape[:-1]
            frame = QImage(img, x, y, QImage.Format_RGB888)
            self.scene2.clear()
            pix = QPixmap.fromImage(frame)
            self.scene2.addPixmap(pix)

    def enhance_button(self, button_name):
        if button_name == "file1":
            self.filename, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', '视频文件(*.mp4 *.mov)')
        elif button_name == "start1":
            if not self.filename:
                self.error.e.lab_heading.setText("未选择视频文件！")
                self.error.show()
            else:
                if self.Timer:
                    self.error.e.lab_heading.setText("有其他任务正在进行！")
                    self.error.show()
                    return
                with open("remaster/process.cfg", "w")as f:
                    f.write("no")
                    f.close()
                self.scene2 = QGraphicsScene()
                self.ui.view1.setScene(self.scene2)
                self.ui.view1.show()
                self.pic = [[]]
                self.enhance_thread = UIFunction.Enhance(self.filename, self.ui.time1, self.ui.progressBar1,
                                                         self.ui.fps1.currentText(), self.ui.model1.currentText(), self.pic)
                self.enhance_thread.setDaemon(True)
                self.enhance_thread.start()

                self.timer = QTimer(self)
                self.timer.timeout.connect(lambda: UIFunction.show_pic2(self))
                self.timer.start(1000)
        elif button_name == "cancel1":
            with open("remaster/process.cfg", "w")as f:
                f.write("stop")
                f.close()
            time.sleep(1)
            self.repair_thread.res.kill()
            self.repair_thread.start_flag.set()
            global pic
            pic = None
            self.timer.stop()
            self.timer = None
            self.error.e.lab_heading.setText("任务终止成功！")
            self.error.show()
            self.repair_thread = None
            time.sleep(1)
            self.ui.progressBar2.setValue(0)
            self.ui.time2.setText("0.00%")

    def repair_button(self, button_name):
        if button_name == "file2":
            self.filename, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', '视频文件(*.mp4 *.mov)')
        elif button_name == "start2":
            if not self.filename:
                self.error.e.lab_heading.setText("未选择视频文件！")
                self.error.show()
            else:
                # self.repair_thread = threading.Thread(target=UIFunction.remaster_start, args=(self.filename,))
                # self.repair_thread.setDaemon(True)
                # self.repair_thread.start()
                if self.Timer:
                    self.error.e.lab_heading.setText("有其他任务正在进行！")
                    self.error.show()
                    return
                with open("remaster/process.cfg", "w")as f:
                    f.write("no")
                    f.close()
                self.scene = QGraphicsScene()
                self.ui.view2.setScene(self.scene)
                self.ui.view2.show()
                self.repair_thread = UIFunction.Repair(self.filename, self.ui.time2, self.ui.progressBar2,
                                                       self.ui.fps2.currentText())
                self.repair_thread.setDaemon(True)
                self.repair_thread.start()
                self.timer = QTimer(self)
                self.timer.timeout.connect(lambda: UIFunction.show_pic(self))
                self.timer.start(2000)
        elif button_name == "cancel2":
            with open("remaster/process.cfg", "w")as f:
                f.write("stop")
                f.close()
            time.sleep(1)
            self.repair_thread.res.kill()
            self.repair_thread.start_flag.set()
            global pic
            pic = None
            self.timer.stop()
            self.timer = None
            self.error.e.lab_heading.setText("任务终止成功！")
            self.error.show()
            self.repair_thread = None
            time.sleep(2)
            self.ui.progressBar2.setValue(0)
            self.ui.time2.setText("0.00%")

    ########################################################################################################################

    # ----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFORM THE TASK IN THE STACKED WIDGET PAGE
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def connectInit(self):
        self.ui.settings1.clicked.connect(lambda: UIFunction.settingStackPages(self, "page_enhance_settings"))
        self.ui.settings2.clicked.connect(lambda: UIFunction.settingStackPages(self, "page_repair_settings"))
        self.ui.settings3.clicked.connect(lambda: UIFunction.settingStackPages(self, "page_theme"))
        self.ui.settings4.clicked.connect(lambda: UIFunction.settingStackPages(self, "page_help"))
        self.ui.theme1.clicked.connect(lambda: UIFunction.setTheme(self, "theme1"))
        self.ui.theme2.clicked.connect(lambda: UIFunction.setTheme(self, "theme2"))
        self.ui.theme3.clicked.connect(lambda: UIFunction.setTheme(self, "theme3"))
        self.ui.theme4.clicked.connect(lambda: UIFunction.setTheme(self, "theme4"))
        self.ui.bn_enhance.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_enhance'))
        self.ui.bn_repair.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_repair'))
        self.ui.bn_user.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_user'))
        self.ui.bn_settings.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_settings'))
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self))
        self.ui.file1.clicked.connect(lambda: UIFunction.enhance_button(self, "file1"))
        self.ui.start1.clicked.connect(lambda: UIFunction.enhance_button(self, "start1"))
        self.ui.cancel1.clicked.connect(lambda: UIFunction.enhance_button(self, "cancel"))
        self.ui.file2.clicked.connect(lambda: UIFunction.repair_button(self, "file2"))
        self.ui.start2.clicked.connect(lambda: UIFunction.repair_button(self, "start2"))
        self.ui.cancel2.clicked.connect(lambda: UIFunction.repair_button(self, "cancel2"))
        self.diag.d.bt1.clicked.connect(lambda: UIFunction.user(self))
        self.ui.signup.clicked.connect(lambda: UIFunction.sign_up(self))
        self.ui.signin.clicked.connect(lambda: UIFunction.sign_in(self))
        self.ui.vipenhance.clicked.connect(lambda: UIFunction.vip_enhance(self))
        self.ui.edit.clicked.connect(lambda: UIFunction.edit(self))
        self.ui.save.clicked.connect(lambda: UIFunction.save(self))
        self.ui.passwdcg.clicked.connect(lambda: UIFunction.change_passwd(self))
        self.ui.avatar.clicked.connect(lambda: UIFunction.choose_img(self))
        self.ui.vipenhance.clicked.connect(lambda: UIFunction.vip_enhance(self))
        self.ui.tutorial.clicked.connect(lambda: UIFunction.tutorial(self))
        self.ui.service.clicked.connect(lambda: UIFunction.help(self))
        self.web_thread = UIFunction.WebConnect()
        self.web_thread.setDaemon(True)
        self.web_thread.start()

    # -----> FUNCTION TO CHOOSE IMAGE AS AVATAR
    def choose_img(self):
        self.avatar_pic, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        pass

    # -----> FUNCTION TO START VIP_ENHANCE
    def vip_enhance(self):
        if not self.name:
            self.error.e.lab_heading.setText("请先登录后再操作！")
            self.error.show()
            return
        if not eval(self.ui.membership.text()):
            self.error.e.lab_heading.setText("VIP等级不足！")
            self.error.show()
            return
        self.vip_thread = UIFunction.VipEnhance()
        self.vip_thread.setDaemon(True)
        self.vip_thread.start()

    # -----> FUNCTION TO ENABLE EDITING
    def edit(self):
        if not self.name:
            self.error.e.lab_heading.setText("请先登录后再操作！")
            self.error.show()
            return
        self.ui.nickname.setEnabled(True)
        self.ui.phone.setEnabled(True)
        self.ui.avatar.setEnabled(True)
        self.ui.save.setEnabled(True)
        pass

    # -----> FUNCTION TO UPDATE PERSONAL INFORMATION
    def save(self):
        if self.avatar_pic:
            try:
                fin = open(self.avatar_pic, 'rb')
                img = fin.read()
                fin.close()
            except Exception as e:
                self.error.e.lab_heading.setText("打开图像失败！")
                self.error.show()
                return
            self.database.update("update user_data set avatar=%s where name =%s ", [img, self.name])
        if self.ui.nickname.text():
            self.database.update("update user_data set nickname=%s where name=%s ", [self.ui.nickname.text(), self.name])
        if self.ui.phone.text():
            self.database.update("update user_data set phonenumber=%s where name=%s ", [self.ui.phone.text(), self.name])
        self.ui.nickname.setEnabled(False)
        self.ui.phone.setEnabled(False)
        self.ui.avatar.setEnabled(False)
        self.ui.save.setEnabled(False)
        time.sleep(0.1)
        nick_name = self.database.select_one("select nickname from user_data where name=%s", [self.name])[0]
        phone = self.database.select_one("select phonenumber from user_data where name=%s", [self.name])[0]
        avatar = self.database.select_one("select avatar from user_data where name=%s", [self.name])[0]
        if avatar and avatar[0] > 0:
            fout = open("avatar.png", "wb")
            fout.write(avatar)
            fout.close()
            pix = QPixmap("avatar.png")
            self.ui.user_img.setPixmap(pix)
            self.ui.lab_person_icon_2.setPixmap(pix)
            self.ui.user_img.setScaledContents(True)
            self.ui.lab_person_icon_2.setScaledContents(True)
        self.ui.user_name.setText(nick_name)
        self.ui.name.setText(self.name)
        self.ui.nickname.setText(nick_name)
        if phone:
            self.ui.phone.setText(phone)
        else:
            self.ui.phone.setText("")
        self.error.e.lab_heading.setText("修改成功！")
        self.error.show()

    # -----> FUNCTION TO CHANGE PASSWORD
    def change_passwd(self):
        self.diag.d.lab_heading.setText("修改密码")
        self.diag.d.bt1.setText("修改")
        self.diag.d.name_2.setText("密码：")
        self.diag.d.password.setText("确认密码：")
        self.diag.d.passwd.setText("")
        self.diag.d.name.setText("")
        self.diag.show()

    # -----> FUNCTION TO SIGN UP
    def sign_up(self):
        self.diag.d.lab_heading.setText("注册")
        self.diag.d.bt1.setText("注册")
        self.diag.d.name_2.setText("用户名：")
        self.diag.d.password.setText("密码：")
        self.diag.d.passwd.setText("")
        self.diag.d.name.setText("")
        self.diag.show()

    # -----> FUNCTION TO SIGN IN
    def sign_in(self):
        self.diag.d.lab_heading.setText("登录")
        self.diag.d.bt1.setText("登录")
        self.diag.d.name_2.setText("用户名：")
        self.diag.d.password.setText("密码：")
        self.diag.d.passwd.setText("")
        self.diag.d.name.setText("")
        self.diag.show()

    # -----> FUNCTION WHEN FINISHED SIGNING IN / UP
    def user(self):
        if self.diag.d.bt1.text() in ["登录", "注册"]:
            name = self.diag.d.name.text()
            passwd = self.diag.d.passwd.text()
            if not name:
                self.error.e.lab_heading.setText("请输入用户名！")
                self.error.show()
                return
            if not passwd:
                self.error.e.lab_heading.setText("请输入密码！")
                self.error.show()
                return
            if len(name) > 20:
                self.error.e.lab_heading.setText("用户名过长！")
                self.error.show()
                return
            if len(passwd) < 6:
                self.error.e.lab_heading.setText("密码长度不得小于6位！")
                self.error.show()
                return
            if self.diag.d.bt1.text() == "注册":
                ret = self.database.insert("insert into user_data(name,passwd) values(%s,%s)", [name, passwd])
                if ret > 0:
                    self.error.e.lab_heading.setText("注册成功！")
                    self.error.show()
                    self.diag.close()
                else:
                    self.error.e.lab_heading.setText("用户名已被使用，请更换！")
                    self.error.show()
            elif self.diag.d.bt1.text() == "登录":
                ret = self.database.select_one("select count(*) from user_data where name=%s and passwd=%s", [name, passwd])
                if ret and ret[0] > 0:
                    self.error.e.lab_heading.setText("登录成功！")
                    self.error.show()
                    self.name = name
                    nick_name = self.database.select_one("select nickname from user_data where name=%s",[self.name])[0]
                    phone = self.database.select_one("select phonenumber from user_data where name=%s", [self.name])[0]
                    balance = self.database.select_one("select balance from user_data where name=%s", [self.name])[0]
                    member_ship = self.database.select_one("select viplevel from user_data where name=%s", [self.name])[0]
                    avatar = self.database.select_one("select avatar from user_data where name=%s", [self.name])[0]
                    if avatar and avatar[0] > 0:
                        fout = open("avatar.png", "wb")
                        fout.write(avatar)
                        fout.close()
                        pix = QPixmap("avatar.png")
                        self.ui.user_img.setPixmap(pix)
                        self.ui.lab_person_icon_2.setPixmap(pix)
                        self.ui.user_img.setScaledContents(True)
                        self.ui.lab_person_icon_2.setScaledContents(True)
                    self.ui.user_name.setText(nick_name)
                    self.ui.name.setText(self.name)
                    self.ui.nickname.setText(nick_name)
                    if phone:
                        self.ui.phone.setText(phone)
                    else:
                        self.ui.phone.setText("")
                    self.ui.balance.setText(str(balance))
                    self.ui.membership.setText(str(member_ship))
                    self.diag.close()
                else:
                    self.error.e.lab_heading.setText("用户名或密码不正确，请重试！")
                    self.error.show()
        else:
            passwd1 = self.diag.d.name.text()
            passwd2 = self.diag.d.passwd.text()
            if not passwd1 or not passwd2:
                self.error.e.lab_heading.setText("请正确输入密码！")
                self.error.show()
            elif passwd1 != passwd2:
                self.error.e.lab_heading.setText("两次密码不一致！")
                self.error.show()
            elif len(passwd1) < 6:
                self.error.e.lab_heading.setText("密码长度不得小于6！")
                self.error.show()
            else:
                self.database.update("update user_data set passwd=%s where name=%s ", [passwd1, self.name])
                self.error.e.lab_heading.setText("修改成功！")
                self.error.show()

    # -----> FUNCTION TO START WEBPAGE
    def tutorial(self):
        webbrowser.open("http://127.0.0.1:5000/user/tutorial", new=0, autoraise=True)

    # -----> FUNCTION TO START WEBPAGE
    def help(self):
        webbrowser.open("http://127.0.0.1:5000/user/login", new=0, autoraise=True)

    # -----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE.
    def settingStackPages(self, page):
        # ------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_settings.findChildren(QFrame):
            each.setStyleSheet(theme.background1)
        global setting_text

        if page == "page_enhance_settings":
            setting_text = "Setting > Video Enhance"
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_enhance_settings)
            self.ui.lab_tab.setText(setting_text)
            self.ui.frame_settings1.setStyleSheet(theme.background2)

        elif page == "page_repair_settings":
            setting_text = "Setting > Video Repair"
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_repair_settings)
            self.ui.lab_tab.setText(setting_text)
            self.ui.frame_settings2.setStyleSheet(theme.background2)

        elif page == "page_theme":
            setting_text = "Setting > Theme"
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_theme)
            self.ui.lab_tab.setText(setting_text)
            self.ui.frame_settings3.setStyleSheet(theme.background2)
            with open("config.cfg", 'r') as cfg:
                choice = cfg.readline().split('=')[1].strip()
            if choice == "theme1":
                self.ui.theme1.setChecked(True)
            elif choice == "theme2":
                self.ui.theme2.setChecked(True)
            elif choice == "theme3":
                self.ui.theme3.setChecked(True)
            elif choice == "theme4":
                self.ui.theme4.setChecked(True)

        elif page == "page_help":
            setting_text = "Setting > Help"
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_help)
            self.ui.lab_tab.setText(setting_text)
            self.ui.frame_settings4.setStyleSheet(theme.background2)

    def setTheme(self, theme_get):
        global theme
        if theme_get == "theme1":
            theme = Theme.Theme1()
            with open("config.cfg", 'w') as cfg:
                cfg.write("current_theme = theme1\n")
        elif theme_get == "theme2":
            theme = Theme.Theme2()
            with open("config.cfg", 'w') as cfg:
                cfg.write("current_theme = theme2\n")
        elif theme_get == "theme3":
            theme = Theme.Theme3()
            with open("config.cfg", 'w') as cfg:
                cfg.write("current_theme = theme3\n")
        elif theme_get == "theme4":
            theme = Theme.Theme4()
            with open("config.cfg", 'w') as cfg:
                cfg.write("current_theme = theme4\n")
        # PUSH BUTTONS RATHER THAN REFORMAT THEIR STYLE
        self.ui.bn_settings.click()
        self.ui.settings3.click()
        self.ui.toodle.setStyleSheet(theme.toodle)
        self.ui.frame_toodle.setStyleSheet(theme.extra_color)
        self.ui.bn_min.setStyleSheet(theme.button1)
        self.ui.bn_max.setStyleSheet(theme.button1)
        self.ui.bn_close.setStyleSheet(theme.button1)
        self.ui.bn_close.setStyleSheet(theme.button1)
        self.ui.frame_head.setStyleSheet(theme.background1)
        # self.ui.lab_appname.setStyleSheet(theme.label)
        # self.ui.user_name.setStyleSheet(theme.label)
        self.ui.frame_bottom_west.setStyleSheet(theme.background1)
        self.ui.bn_enhance.setStyleSheet(theme.button2)
        self.ui.bn_repair.setStyleSheet(theme.button2)
        self.ui.bn_user.setStyleSheet(theme.button2)
        self.ui.bn_settings.setStyleSheet(theme.button2)
        ###################################
        self.ui.page_enhance.setStyleSheet(theme.background2)
        self.ui.progressBar1.setStyleSheet(theme.progress)
        self.ui.file1.setStyleSheet(theme.button3)
        self.ui.start1.setStyleSheet(theme.button3)
        self.ui.cancel1.setStyleSheet(theme.button3)
        self.ui.label_13.setStyleSheet(theme.label)
        self.ui.lab_res1.setStyleSheet(theme.label)
        self.ui.lab_fps1.setStyleSheet(theme.label)
        self.ui.lab_model1.setStyleSheet(theme.label)
        # ADD LISTVIEW
        self.ui.res1.setView(QListView())
        self.ui.fps1.setView(QListView())
        self.ui.model1.setView(QListView())
        self.ui.res1.setStyleSheet(theme.combo_box)
        self.ui.fps1.setStyleSheet(theme.combo_box)
        self.ui.model1.setStyleSheet(theme.combo_box)
        self.ui.time1.setStyleSheet(theme.label)
        ####################################
        self.ui.page_repair.setStyleSheet(theme.background2)
        self.ui.progressBar2.setStyleSheet(theme.progress)
        self.ui.file2.setStyleSheet(theme.button3)
        self.ui.start2.setStyleSheet(theme.button3)
        self.ui.cancel2.setStyleSheet(theme.button3)
        self.ui.label_14.setStyleSheet(theme.label)
        self.ui.res2.setView(QListView())
        self.ui.fps2.setView(QListView())
        self.ui.model2.setView(QListView())
        self.ui.res2.setStyleSheet(theme.combo_box)
        self.ui.fps2.setStyleSheet(theme.combo_box)
        self.ui.model2.setStyleSheet(theme.combo_box)
        self.ui.lab_res2.setStyleSheet(theme.label)
        self.ui.lab_fps2.setStyleSheet(theme.label)
        self.ui.lab_model2.setStyleSheet(theme.label)
        self.ui.time2.setStyleSheet(theme.label)
        ################################
        self.ui.page_user.setStyleSheet(theme.background2)
        self.ui.lab_cloud_main.setStyleSheet(theme.label)
        self.ui.label_2.setStyleSheet(theme.label)
        self.ui.label_15.setStyleSheet(theme.label)
        self.ui.label_16.setStyleSheet(theme.label)
        self.ui.label_17.setStyleSheet(theme.label)
        self.ui.label_18.setStyleSheet(theme.label)
        self.ui.name.setStyleSheet(theme.line_edit)
        self.ui.nickname.setStyleSheet(theme.line_edit)
        self.ui.balance.setStyleSheet(theme.line_edit)
        self.ui.phone.setStyleSheet(theme.line_edit)
        self.ui.membership.setStyleSheet(theme.line_edit)
        self.ui.vipenhance.setStyleSheet(theme.button3)
        self.ui.edit.setStyleSheet(theme.button3)
        self.ui.signin.setStyleSheet(theme.button4)
        self.ui.signup.setStyleSheet(theme.button4)
        self.ui.save.setStyleSheet(theme.button3)
        self.ui.avatar.setStyleSheet(theme.button3)
        self.ui.deposit.setStyleSheet(theme.button3)
        self.ui.vipup.setStyleSheet(theme.button3)
        self.ui.passwdcg.setStyleSheet(theme.button3)
        ###################################
        # PAGE SETTINGS NEED TO BE DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.ui.page_settings.setStyleSheet(theme.background2)
        self.ui.frame_settings.setStyleSheet(theme.background1)
        self.ui.lab_bug3_8.setStyleSheet(theme.label)
        self.ui.lab_bug3_9.setStyleSheet(theme.label)
        self.ui.lab_bug3_10.setStyleSheet(theme.label)
        self.ui.lab_bug3_11.setStyleSheet(theme.label)
        self.ui.lab_bug3_12.setStyleSheet(theme.label)
        self.ui.lab_bug3_13.setStyleSheet(theme.label)
        self.ui.settings1.setStyleSheet(theme.button2)
        self.ui.settings2.setStyleSheet(theme.button2)
        self.ui.settings3.setStyleSheet(theme.button2)
        self.ui.settings4.setStyleSheet(theme.button2)
        self.ui.res3.setView(QListView())
        self.ui.fps3.setView(QListView())
        self.ui.model3.setView(QListView())
        self.ui.res4.setView(QListView())
        self.ui.fps4.setView(QListView())
        self.ui.model4.setView(QListView())
        self.ui.fps3.setStyleSheet(theme.combo_box)
        self.ui.fps4.setStyleSheet(theme.combo_box)
        self.ui.res3.setStyleSheet(theme.combo_box)
        self.ui.res4.setStyleSheet(theme.combo_box)
        self.ui.model3.setStyleSheet(theme.combo_box)
        self.ui.model4.setStyleSheet(theme.combo_box)

        self.ui.page_enhance_settings.setStyleSheet(theme.background2)
        self.ui.page_repair_settings.setStyleSheet(theme.background2)
        self.ui.page_theme.setStyleSheet(theme.background2)
        self.ui.page_help.setStyleSheet(theme.background2)
        self.ui.lab_enhance.setStyleSheet(theme.label)

        self.ui.lab_repair.setStyleSheet(theme.label)

        self.ui.themes.setStyleSheet(theme.group_box)
        self.ui.theme1.setStyleSheet(theme.radio_button)
        self.ui.theme2.setStyleSheet(theme.radio_button)
        self.ui.theme3.setStyleSheet(theme.radio_button)
        self.ui.theme4.setStyleSheet(theme.radio_button)

        self.ui.help.setStyleSheet(theme.group_box)
        self.ui.tutorial.setStyleSheet(theme.button3)
        self.ui.service.setStyleSheet(theme.button3)

        ###################
        self.ui.frame_tab.setStyleSheet(theme.background1)
        self.ui.lab_tab.setStyleSheet(theme.label)
        self.ui.frame_drag.setStyleSheet(theme.background1)


###############################################################################################################################################################
