from math import pi
var=input("请输入带单位的待转换变量：")
if var[-1] in ["a"]:
    S=pi*eval(var[0:-1])**2
    print("求得结果为：{:.2f}".format(S))
elif var[-1] in ["b"]:
    r=(eval(var[0:-1])/pi)**(1/2)
    print("求得结果为：{:.2f}".format(r))
else:
    print("error")