#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:22:35 2018

@author: Alex
"""

import math

JLT="ㄱ,ㄲ,ㄴ,ㄷ,ㄸ,ㄹ,ㅁ,ㅂ,ㅃ,ㅅ,ㅆ,ㅇ,ㅈ,ㅉ,ㅊ,ㅋ,ㅌ,ㅍ,ㅎ".split(",")
JTT=",ㄱ,ㄲ,ㄱㅅ,ㄴ,ㄴㅈ,ㄴㅎ,ㄷ,ㄹ,ㄹㄱ,ㄹㅁ,ㄹㅂ,ㄹㅅ,ㄹㅌ,ㄹㅍ,ㄹㅎ,ㅁ,ㅂ,ㅂㅅ,ㅅ,ㅆ,ㅇ,ㅈ,ㅊ,ㅋ,ㅌ,ㅍ,ㅎ".split(",")
JVT="ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅗ,ㅘ,ㅙ,ㅚ,ㅛ,ㅜ,ㅝ,ㅞ,ㅟ,ㅠ,ㅡ,ㅢ,ㅣ".split(",")
SBase=0xAC00
SCount=11172
TCount=28
NCount=588

def HangulName(a):
    # this comines each letter to one complete korean letter
    b=a.decode('utf8')
    sound=''
    for i in b:
        if i == u' ':
            sound = sound + ' ' # also include the space
        else:
            cp=ord(i)
            SIndex = cp - SBase
            if (0 > SIndex or SIndex >= SCount):
                #  "Not a Hangul Syllable"
                pass
    
            LIndex = int(math.floor(SIndex / NCount))
            VIndex = int(math.floor((SIndex % NCount) / TCount))
            TIndex = int(SIndex % TCount)
            sound=sound+(JLT[LIndex] + JVT[VIndex] + JTT[TIndex]).lower()
    
    return sound

print HangulName("안녕하세요")