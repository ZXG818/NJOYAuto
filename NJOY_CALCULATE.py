# coding:utf-8
''' 
	自动化调用NJOY99程序来计算，
	不同温度下适用于MCNP程序的ACE格式核素截面。
'''
import os
import os.path
import shutil
import time


# 更新go.bat文件
def GOBAT(front_filename, filename):
    content = []
    
    with open('C:\\Users\\Administrator\\Desktop\\NJOY\\go.bat', 'r') as f:
        lines = f.readlines()
        
        content = [line.replace(front_filename, filename) for line in lines]
    
    print(content)
    
    with open('C:\\Users\\Administrator\\Desktop\\NJOY\\go.bat', 'w') as f:
        f.writelines(content)


# 获取ENDF文件的MAT标识
def GetMAT(filename):
    content = ''
    MAT = 0
    with open(filename, 'r') as f:
        content = f.read()
        
        index = content.index('MATERIAL ')
        MAT = content[index+len('MATERIAL'):index+len('MATERIAL')+5].strip()
    
    print("********   MAT = ", MAT)
    
    return MAT


# 更新900K NJOY输入程序文件
def NJOY_INPUT(front_MAT, MAT, filename):
    content = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        content = [line.replace(front_MAT, MAT) for line in lines]
    
    print(content)
    
    with open(filename, 'w') as f:
        f.writelines(content)



if __name__ == '__main__':
    
    # 获取要转换的DAT文件名称
    DAT = os.listdir('C:\\Users\\Administrator\\Desktop\\DAT\\')
    DAT = [each.split('.')[0] for each in DAT] # 仅仅是文件名，没有后缀名！
    
    # 获取各个文件的MAT
    MAT = list(map(GetMAT, ['C:\\Users\\Administrator\\Desktop\\DAT\\' + each + '.DAT' for each in DAT]))
    

    for i in range(0, len(DAT)):
        
        # 如果是第一次进行转换
        if i == 0:
            
            # 更新go.bat文件
            GOBAT('FUCK', DAT[i])
            
            # 更新NJOY 900K 输入文件
            NJOY_INPUT('9546', MAT[i], 'C:\\Users\\Administrator\\Desktop\\NJOY\\inp900')
            
            # 更新NJOY 1200K 输入文件
            NJOY_INPUT('9546', MAT[i], 'C:\\Users\\Administrator\\Desktop\\NJOY\\inp1200')
            
            # 拷贝DAT文件到NJOY计算文件夹中
            shutil.copy('C:\\Users\\Administrator\\Desktop\\DAT\\' + DAT[i] + '.DAT', 'C:\\Users\\Administrator\\Desktop\\NJOY\\')
            
            # Sleep 1s and wait the windows refresh.
            time.sleep(1)
            
            # 进行NJOY计算
            os.system('C:\\Users\\Administrator\\Desktop\\NJOY\\go.bat')
            
            # 保存文件
            # 利用CMD命令中的通配符来解决这个问题
            # 保存900K数据文件
            os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_900 C:\\Users\\Administrator\\Desktop\\RESULT\\900K\\")
            os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_900_XSDIR C:\\Users\\Administrator\\Desktop\\RESULT\\900K\\")
            # 保存1200K数据文件
            os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_1200 C:\\Users\\Administrator\\Desktop\\RESULT\\1200K\\")
            os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_1200_XSDIR C:\\Users\\Administrator\\Desktop\\RESULT\\1200K\\")  
            
            time.sleep(1)
            
            continue
        
        # 
        # 更新go.bat文件
        GOBAT(DAT[i-1], DAT[i])
        
        # 更新NJOY 900K 输入文件
        NJOY_INPUT(MAT[i-1], MAT[i], 'C:\\Users\\Administrator\\Desktop\\NJOY\\inp900')
        
        # 更新NJOY 1200K 输入文件
        NJOY_INPUT(MAT[i-1], MAT[i], 'C:\\Users\\Administrator\\Desktop\\NJOY\\inp1200')
        
        # 拷贝DAT文件到NJOY计算文件夹中
        shutil.copy('C:\\Users\\Administrator\\Desktop\\DAT\\' + DAT[i] + '.DAT', 'C:\\Users\\Administrator\\Desktop\\NJOY\\')
        
        time.sleep(1)
        
        # 进行NJOY计算
        os.system('C:\\Users\\Administrator\\Desktop\\NJOY\\go.bat')
        
        # 保存文件
        # 利用CMD命令中的通配符来解决这个问题
        # 保存900K数据文件
        os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_900 C:\\Users\\Administrator\\Desktop\\RESULT\\900K\\")
        os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_900_XSDIR C:\\Users\\Administrator\\Desktop\\RESULT\\900K\\")
        # 保存1200K数据文件
        os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_1200 C:\\Users\\Administrator\\Desktop\\RESULT\\1200K\\")
        os.system("move C:\\Users\\Administrator\\Desktop\\NJOY\\*_1200_XSDIR C:\\Users\\Administrator\\Desktop\\RESULT\\1200K\\")
        time.sleep(1)