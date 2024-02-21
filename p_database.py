import pymysql
import hashlib
from pymysql.converters import escape_string
from personalsql import MysqlHelper

##使用前请安装pymysql模块
##将personalsql.py放在统一目录下
##所有获取用户信息的返回值都注释了，需要使用返回值可直接用


#1 注册功能
def register():
    name=input("<用户名：>")
    while(len(name)>20 or len(name)==0):
        print("用户名不合法！")
        name = input("<用户名：>")
    passwd = input("<设置密码：>")
    while(len(passwd)<6):
        print("密码长度至少需要6位，请重新输入！")
        passwd = input("<设置密码：>")

    checkpwd=input("<确认密码：>")
    while(checkpwd!=passwd):
        print("密码不一致，请重新输入！")
        checkpwd = input("<确认密码：>")

    ms = MysqlHelper()  # 输入数据库的名称
    ret = ms.insert("insert into user_data(name,passwd) values(%s,%s)", [name, passwd])
    if ret> 0:
        print("注册成功")
    else:
        print("用户名已被使用，注册失败！")


#2 登录功能
def login():
    name = input("<用户名：>")
    passwd = input("<密码：>")
    ms = MysqlHelper()  # 输入数据库的名称
    ret = ms.select_one("select count(*) from user_data where name=%s and passwd=%s", [name, passwd])
    if ret[0]>0:
        print("登录成功！")
    else:
        print("用户名或密码不正确，登录失败！")

#3 修改性别，前端做成button即可，传入参数为用户名
def update_gender(name):
    ms = MysqlHelper()  # 输入数据库的名称
    gender= input("<性别：>")
    ret=ms.update("update  user_data set gender=%s where name=%s ",[gender,name])
    if ret>0:
        print("修改成功！")
    else:
        print("修改失败！")

#4 修改昵称功能 传入参数为用户名
def update_nickname(name):
    ms = MysqlHelper()  # 输入数据库的名称
    nickname= input("<昵称：>")
    ret=ms.update("update  user_data set nickname=%s where name=%s ",[nickname,name])
    if ret>0:
        print("修改成功！")
    else:
        print("修改失败！")


#5 修改手机号码 传入参数为用户名
def update_phonenumber(name):
    ms = MysqlHelper()  # 输入数据库的名称
    phonenumber= input("<电话号码：>")
    while(len(phonenumber)!=11):
        print("电话号码格式错误，请重新输入！")
        phonenumber = input("<电话号码：>")
    ret=ms.update("update  user_data set phonenumber=%s where name=%s ",[phonenumber,name])
    if ret>0:
        print("修改成功！")
    else:
        print("修改失败！")

#6 修改密码 传入参数为用户名
def update_passwd(name):
    ms = MysqlHelper()  # 输入数据库的名称
    opasswd = input("<输入原密码：>")
    res = ms.select_one("select passwd from user_data where name=%s", [name])[0]
    while (res!=opasswd):
        opasswd=input("密码错误，请重新输入：")

    passwd=input("<输入新密码：>")
    while(len(passwd)<6):
        print("密码长度至少需要6位，请重新输入！")
        passwd = input("<设置新密码：>")

    checkpwd=input("<确认新密码：>")
    while(checkpwd!=passwd):
        print("密码不一致，请重新输入！")
        checkpwd = input("<确认新密码：>")
    ret=ms.update("update  user_data set passwd=%s where name=%s ",[passwd,name])
    if ret>0:
        print("修改成功！")
    else:
        print("修改失败！")



#7 修改/上传用户头像 传入参数为用户名，照片路径
def update_avatar(name,picname):
    try:
        fin = open(picname,'rb')
        img = fin.read()
        fin.close()

    except Exception as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.update("update user_data set avatar=%s where name =%s ",[img,name])
    if(ret>0):
        print("修改成功！")
    else:
        print("修改失败！")


#8 修改余额 传入参数为用户名
def update_balance(name):
    ms = MysqlHelper()  # 输入数据库的名称
    balance=input("<余额>：")
    ret = ms.update("update user_data set balance=%s where name =%s ", [balance, name])
    if (ret > 0):
        print("修改成功！")
    else:
        print("修改失败！")

#9 修改VIP等级 传入参数为用户名
def update_viplevel(name):
    ms = MysqlHelper()  # 输入数据库的名称
    viplevel = input("<VIP等级>：")
    ret = ms.update("update user_data set viplevel=%s where name =%s ", [viplevel, name])
    if (ret > 0):
        print("修改成功！")
    else:
        print("修改失败！")

#10 获取用户头像保存到本地目录 传入参数为用户名
def get_avatar(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select avatar from user_data where name=%s",[name])
    if ret[0][0]>0:
        fout=open(name+"_image.png","wb")
        fout.write(ret[0])
        fout.close()
        print("读取成功！")
    else:
        print("读取失败")


#11 获取用户电话号码 传入参数为用户名
def get_phonenumber(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select phonenumber from user_data where name=%s",[name])
    if ret[0]:
        print("用户电话号码：",ret[0])
        #return ret[0]
    else:
        print("读取失败")


#12 获取用户余额 传入参数为用户名
def get_balance(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select balance from user_data where name=%s",[name])
    if ret[0]>=0:
        print("用户余额：",ret[0])
        #return ret[0]
    else:
        print("读取失败")

#13 获取用户vip等级 传入参数为用户名
def get_viplevel(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select viplevel from user_data where name=%s",[name])
    if ret[0]>=0:
        print("用户VIP等级：",ret[0])
        #return ret[0]
    else:
        print("读取失败")

#14 获取用户性别 传入参数为用户名
def get_gender(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select gender from user_data where name=%s",[name])
    if ret[0]:
        print("用户性别：",ret[0])
        #return ret[0]
    else:
        print("读取失败")

#15 获取用户昵称 传入参数为用户名
def get_nickname(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select nickname from user_data where name=%s",[name])
    if ret[0]:
        print("用户昵称：",ret[0])
        #return ret[0]
    else:
        print("读取失败")


#16 获取用户密码 传入参数为用户名
def get_passwd(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_one("select passwd from user_data where name=%s",[name])
    if ret[0]:
        print("用户密码：",ret[0])
        return ret[0]
    else:
        print("读取失败")

#17 获取用户全部信息 传入参数为用户名
def viewinfo(name):
    ms = MysqlHelper()  # 输入数据库的名称
    ret=ms.select_all("select * from user_data where name=%s",[name])
    if ret[0][0]>0:
        print("----------------------")
        print("用户ID:",ret[0][0])
        print("用户名:", ret[0][1])
        print("用户昵称:", ret[0][2])
        #print("用户密码:", ret[0][3])
        print("用户性别:", ret[0][4])
        print("用户余额:", ret[0][5],"元")
        print("用户VIP等级:", ret[0][7])
        print("用户电话号码:", ret[0][9])
        print("----------------------")
    else:
        print("用户不存在,查询失败！")



def main():
    #注册
    #register()

    #登录
    #login()

    #修改昵称
    #update_nickname("乔丹")

    #绑定/修改电话号码
    #update_phonenumber("乔丹")

    #修改余额
    #update_balance("乔丹")

    #修改VIP等级
    #update_viplevel("乔丹")


    #修改性别
    #update_gender("乔丹")

    #修改密码
    #update_passwd("乔丹")


    #上传头像
    #update_avatar("詹姆斯","詹姆斯_image.png")

    #获取昵称
    get_nickname("乔丹")

    #获取电话号码
    get_phonenumber("乔丹")

    #获取用户余额
    get_balance("乔丹")

    #获取用户VIP等级
    get_viplevel("乔丹")

    #获取用户密码
    get_passwd("乔丹")

    #获取用户性别
    get_gender("乔丹")




    #查看用户信息
    viewinfo("杜兰特")
    viewinfo("詹姆斯")
    viewinfo("乔丹")


if __name__ == '__main__':
    main()