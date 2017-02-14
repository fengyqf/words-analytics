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
word_width_max=10



r=open('a.txt')

for word_width in range(word_width_min,word_width_max+1):
    r.seek(0)
    buff=[]
    for line in r.readlines():
        print line;
        i=0;
        while(i < mb_strlen(line)-word_width):
            print mb_substr(line,i,word_width)
            buff.append('%s\n'%(mb_substr(line,i,word_width)))
            i+=1;
    w=open('output-%d.txt'%(word_width),'w+')
    w.writelines(buff)
    w.flush()
    w.close()

    print  len(buff)

