# -*- coding: utf-8 -*-
# Quick Python Script Explanation for Progeaments
# 给程序员的超快速Py脚本解说
import os

def main():
    print ('hello world')

    print ('这是wangy265\'的问候')

    print ("这是wangy265有一次\'的问候")

    foo(5,10)

    print('='*10)

    print('这将直接执行'+os.getcwd())

    counter = 0
    counter +=1

    food = ['苹果','荔枝','杏子','李子']

    for i in food:
        print('水果:'+i)

    print('数到10')
    for i in range(10):
        print(i)

def foo(param1,param2):
    res = param1 + param2
    print (" %s 加 %s 等于 %s !" %(param1,param2,res))
    if res<50:
        print("这个")
    elif (res>=50) and ((param2==42) or (param2==24)):
        print("那个")     
    else:
        print("嗯。。。。")
    return res #单行注释
    '''
    多行注释
    '''



if __name__ == '__main__':
    main()