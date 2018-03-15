import ConfigParser
import os
import email_sender

parser = ConfigParser.ConfigParser()
parser.read("../monitor.conf")
log_file_path = parser.get("config", "log_file_path")
email_list = parser.get("config", "email_list")

f = open(log_file_path, "r")
file_content = f.read()
f.close()

file_content_split = file_content.split('\n\n')

msg_list = []
for one_content in file_content_split:
    data_split = one_content.split('\n')
    data = data_split[0]
    data_item = data.split(' ')


    def not_empty(s):
        return s and s.strip()


    data_item = list(filter(not_empty, data_item))
    data_item_len = len(data_item)

    item_dict = {}
    i = 0
    while i < data_item_len:
        if i == 0:
            item_dict['Count'] = data_item[1]
            i = 2
        elif i == 2:
            item_dict['Time'] = (data_item[2][data_item[2].index('=') + 1:len(data_item[2])]) + data_item[3]
            i = 4
        elif i == 4:
            item_dict['Lock'] = data_item[4][data_item[4].index('=') + 1:len(data_item[4])] + data_item[5]
            i = 6
        elif i == 6:
            item_dict['Lock'] = data_item[6][data_item[6].index('=') + 1:len(data_item[6])] + data_item[7][
                                                                                              0:len(data_item[7]) - 1]
            i = 8
        else:
            item_dict['Session'] = data_item[8]
            i = data_item_len

    sql = ''
    for j in range(1, len(data_split)):
        sql = sql + data_split[j].strip()
    item_dict['SQL'] = sql
    msg_list.append(item_dict)

# already done
# def msg_cmp(x, y):
#     return float(y['Time'].split('s')[0])-float(x['Time'].split('s')[0])
#
#
# msg_list.sort(msg_cmp)

email_sender.send_email(email_list.split(","), "The slow sql report for your MySQL", msg_list)

os.remove(log_file_path)

