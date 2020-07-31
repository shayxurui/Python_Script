import os
import smtplib
from email.mime.text import MIMEText
import  csv
import pandas as pd
import xlwt
from xlrd import open_workbook
import xlwt
import time
import math


msg_from = 'xxxxx@foxmail.com'  # 发送方邮箱
passwd = 'xxxxxxx'  # 填入发送方邮箱的授权码


xls_path=r'C:\Users\xxxxx\Desktop\助教\成绩一览表final.xlsx'



infos=list()
average_score=0
middle_score=0
scores=list()

def parse_xls(xls_path):
    workbook=open_workbook(xls_path)
    sheet=workbook.sheet_by_index(4)

    # for row in range(sheet.nrows):
    #     content=sheet.row_values(row)
    #
    #     if (content[1].isdigit()):
    #         sum=0
    #         for i in range(5, 12, 1):
    #             sum=sum+content[i]
    #
    #
    #         if(sum!=content[13]):
    #             print(content[1],content[2],sum,content[13])





    for row in range(sheet.nrows):
        content=sheet.row_values(row)
        # print(content[0])
        if (content[0].isdigit()):
            # if(content[2]!=10):
            #     content[2]=content[2]+1
            #
            # content[2]=content[2]*10
            #
            # print(int(content[2]))
            sum=0
            # print(content[2],content[3],content[4],content[5])
            sum=math.ceil(content[2]*0.1+content[3]*0.15+content[4]*0.2+content[5]*0.55)
            # print(sum,content[2]*0.1+content[3]*0.15+content[4]*0.2+content[5]*0.55)
            print(sum,content[6])
            if(sum!=int(content[6])):
                print(content[0],content[1],sum,content[6])


            # print(content[1],sum)# for i in range(2,6,1):

                # sum=sum+int(content[i])


                # tmp=[content[1],content[2],content[5],content[6]]
                # scores.append(content[5])
                # infos.append(tmp)







def parse_info():
    for info in infos:
        # print(info)
        id = info[0]
        name = info[1]
        score1 = info[2]
        score2=info[3]

        print(id,name,score1,score2)


def write_to_xlxs(xls_path):
    workbook = open_workbook(xls_path)
    sheet = workbook.sheet_by_index(0)
    for row in range(sheet.nrows):
        content=sheet.row_values(row)



    wb=xlwt.Workbook()






def sendMail():
    subject = "期中考试成绩"


    for info in infos:
        id=info[0]
        name=info[1]
        score=info[2]

        content=name+'同学，你好! 你在这次计算机网络课程期中考试成绩为:'+str(int(score))+"分。" \
                                                                 "本次考试的平均分为"+str(average_score)+", 分数中位数为"+str(middle_score)+"。\n希望再接再厉！"
        print(content)
        msg_to = id+'@fudan.edu.cn'  # 收件人邮箱
        # msg_to='17212010044@fudan.edu.cn'
        print(msg_to)

        # msg = MIMEText(content)
        # msg['Subject'] = subject
        # msg['From'] = msg_from
        # msg['To'] = msg_to
        # try:
        #     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        #     s.login(msg_from, passwd)
        # except Exception as e:
        #     print('qq邮箱登录失败')
        #
        # try:
        #     s.sendmail(msg_from, msg_to, msg.as_string())
        #     print(msg_to+' '+name+" 发送成功")
        #
        # except s.SMTPException as e:
        #     print(msg_to+' '+name+" 发送失败")

        # time.sleep(30)


if __name__=='__main__':
    parse_xls(xls_path)
    # sendMail()
    # parse_info()




