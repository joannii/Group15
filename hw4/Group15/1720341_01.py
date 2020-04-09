#问题：（鸡兔同笼问题）假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

#1.鸡加兔30只。
#2.鸡两只脚，兔四只脚。
#3.鸡加兔的脚一共90只。
#4.鸡小于等于30只，兔小于等于30只。（隐藏条件）
#列出方程式:X + Y = 30;2X + 4Y = 90

#脚：foots;总数：amount
#ck代表鸡，30-ck代表兔


foots = 90
amount = 30

for ck in range(0,31):
    if 2*ck+(30-ck)*4==90:
        print("鸡有{}只,兔有{}只".format(ck,30-ck))
