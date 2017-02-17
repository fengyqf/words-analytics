#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime
import ConfigParser


def mb_substr(s,start,length=None,encoding="UTF-8") :
    u_s = s.decode(encoding)
    return (u_s[start:(start+length)] if length else u_s[start:]).encode(encoding)

def mb_strlen(string,encoding='utf-8'):
     return len(string.decode(encoding))


script_dir=os.path.split(os.path.realpath(__file__))[0]+'/'

stop_words=[',','，','。','．','、','"','“','”','：',' ','／'
    ,'…','〕','〔','《','》','（','）','；','·','？'
    ,'\n','\r','\t'
    ,'1','2','3','4','5','6','7','8','9','0'
    ,'１','２','３','４','５','６','７','８','９','０'
    ,'Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ'
    ,'Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ'
    ,'ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ'
    ,'ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ'
]

config_file=script_dir+'/rconfig.ini'

cp=ConfigParser.ConfigParser()
cp.read(config_file)

try:
    word_width_min=int(cp.get('main','word_width_min'))
    word_width_max=int(cp.get('main','word_width_max'))
    output_words_min_count=int(cp.get('main','output_words_min_count'))
except :
    #raise ConfigParser.NoOptionError(e)
    print "rconfig.ini ERROR.  You can copy it from rconfig.ini.sample "
    exit()



for file in os.listdir(script_dir):
    if not (file[0:2] in ['a_','a.'] and file[-4:]=='.txt') :
        continue
    r=open(script_dir+file)
    counts={}
    #buff=[]
    for word_width in range(word_width_min,word_width_max+1):
        r.seek(0)
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
                    counts[word] = counts.get(word, 0) + 1
                    #buff.append(word)
                    accepted_count+=1
                print '    %s acceped' %(accepted_count)

    r.close()

    print '## finished cutting, %d words.' %len(counts)


    sorted_counts = list(counts.items())
    sorted_counts.sort(lambda a,b: -cmp((a[1], a[0]), (b[1], b[0])))

    output='times\tword\n'
    for item in sorted_counts:
        if item[1] < output_words_min_count:
            break
        output+= '%d\t%s\n' %(item[1],item[0])

    output_file_path=script_dir+'output_'+file[:-4]+'.txt'
    if os.path.exists(output_file_path):
        timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        os.rename(output_file_path,'%soutput_%s_bak%s.txt'%(script_dir,file[:-4],timestamp))

    w=open(output_file_path,'w+')
    w.write(output)
    w.flush()
    w.close()

print 'write done to file output.txt'

