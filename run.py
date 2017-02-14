#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def mb_substr(s,start,length=None,encoding="UTF-8") :
    u_s = s.decode(encoding)
    return (u_s[start:(start+length)] if length else u_s[start:]).encode(encoding)

def mb_strlen(string,encoding='utf-8'):
     return len(string.decode(encoding))


word_width_min=2
word_width_max=15



r=open('a.txt')

stop_words=[',','，','。','．','、','"','“','”','：',' '
    ,'\n','\r','\t'
    ,'1','2','3','4','5','6','7','8','9','0'
    ,'１','２','３','４','５','６','７','８','９','０'
    ,'Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ'
    ,'Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ'
    ,'ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ'
    ,'ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙｚ'
]

for word_width in range(word_width_min,word_width_max+1):
    r.seek(0)
    buff=[]
    for line in r.readlines():
        print line
        i=0;
        accepted_count=0;
        while(i < mb_strlen(line)-word_width):
            i+=1;
            word = mb_substr(line,i,word_width)
            print word
            flag_stop=0
            for sw in stop_words:
                if word.find(sw) >= 0:
                    #print '  stoped for %s' %sw
                    flag_stop+=1
                    continue
            if flag_stop==0:
                buff.append('%s\n'%(word))
                accepted_count+=1
            print '    %s acceped' %(accepted_count)
    w=open('output-%d.txt'%(word_width),'w+')
    w.writelines(buff)
    w.flush()
    w.close()

    print  len(buff)

