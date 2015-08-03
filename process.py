#-*- coding: UTF-8 -*-
"""
Author:deli
File:process.py
Time:2015/3/24 21:27:17
"""
def combine_info():   
    f_content = file('tweet12.content.corpus', 'r') 
    f_info = file('tweet12.otherinfo.corpus', 'r')
    fw = file('combine', 'w')
    fabort = file('abort', 'w')
    for line in f_content:
        line = line.strip()
        line_no = line[0:17]
        info_line = f_info.readline().strip()
        info_line_no = info_line[0:17]
        info_line_content = info_line[48:]
        new_line = ""
        if line_no == info_line_no:
            new_line = line + info_line_content + '\n'
        else:
            fabort.write(line_no +"!="+ info_line_no+"\n")
        fw.write(new_line)
    f_content.close()
    f_info.close
    fw.close()
    fabort.close()
def trans():    
    fr = file('dect_language_output', 'r') 
    fw = file('ans', 'w')
    pattern = ["<DOC><DOCNO>","</DOCNO><TEXT>","</TEXT></DOC>\n"]
    i = 1
    for line in fr:
        line = line.strip()
        doc_no = line[0:17]
        text = str(line[18:]).strip()
        ans = pattern[0] + doc_no + pattern[1] + text + pattern[2]
        fw.write(ans)
    fr.close()
    fw.close()  
def filter_rt():
    f_content = file('content_filter_rt1', 'r')
    fw = file('content_filter_rt2', 'w')
    i = 0
    for line in f_content:
        line = line.strip()
        line = re.sub(r'(Rt ).*', "",line) 
        fw.write(str(line) + '\n')
    f_content.close()
    fw.close()
def filter_url():
    f_url = file('content_url_title', 'r')
    fw = file('content_url_title_withouturl', 'w')
    dict_url = dict()
    i = 0
    for line in f_url:
        line = line.strip()
        line = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "",line)
        fw.write(line + '\n')
    f_url.close()
    fw.close()
def result_to_mid():
    f_topic = file('mb2012.topic', 'r') 
    fw = file('mid_ans', 'w')
    key_num = 51
    dict_searchid = dict() 
    for line in f_topic:
        line = line.strip()
        if key_num < 100:
            key = 'MB0' + str(key_num)
        else:
            key = 'MB' + str(key_num)
        value = str(line[0:17]).strip()
        dict_searchid[str(key)] = value
        key_num = key_num + 1
    f_topic.close()
    for k in sorted(dict_searchid.keys()):
        fw.write(k + " " + dict_searchid[k]+ "\n")
    fw.close()  
def mid_to_waggle():    
    f_mid = file('mid_ans', 'r')
    f_result = file('result.txt', 'r')
    fw = file('waggle', 'w')
    dict_mid = dict()
    dict_result = dict()
    i = 0
    result_waggle = []
    for line in f_mid:
        line = line.strip()
        value = str(line[0:5]).strip()
        key = str(line[5:30]).strip()
        dict_mid[str(key)] = value
    for result_line in f_result:
        result_line = result_line.strip()
        result_array = result_line.split(" ")
        if dict_mid.has_key(str(result_array[0])):
            result_waggle.append(dict_mid[str(result_array[0])] + " " + result_array[2] + " " + result_array[4] + " accepted\n")
    for re in range(len(result_waggle)):
        fw.write(result_waggle[re])
    print "搞定"    
    f_mid.close()
    f_result.close()
    fw.close()
    
    
    
    
    
    
    
    作业地址：http://webkdd.org/assignment/2015_a1.html
微博搜索系统， 给定Twitter数据集和60个查询，返回和查询最相关的1000条英文微博.   
Windows7 x86 Lemur 4.12 python 2.7.9
