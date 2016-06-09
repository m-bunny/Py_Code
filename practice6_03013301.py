from pylab import *
import numpy
from matplotlib import pyplot
from prettytable import PrettyTable

def getAverage(numlist):
    #计算平均值
    length=len(numlist)
    total=0
    for num in numlist:
        total += num
    return float(total/length)

def getVariance(numlist):
    #计算方差
    avg=getAverage(numlist)
    length=len(numlist)
    total=0
    for num in numlist:
        total += (num-avg)**2
    return float(total/length)

def getCorrCoeff(numlistX,numlistY):
    #计算相关系数
    if(len(numlistX)!=len(numlistY)):
        print("输入有误")
        return -1
    length=len(numlistX)
    #计算平均值
    avgX=getAverage(numlistX)
    avgY=getAverage(numlistY)
    #计算标准差
    StandardDevX=getVariance(numlistX)**0.5
    StandardDevY=getVariance(numlistY)**0.5
    #计算协方差
    total=0
    for i in range(length):
        total+=(numlistX[i]-avgX)*(numlistY[i]-avgY)
    covXY=total/length
    #返回相关系数
    return covXY/(StandardDevX*StandardDevY)

def readDataFromTxt(fileName):
    #从指定文件中读取x,y的值形成Python列表
    inputFile=open(fileName,'r')
    numlistX=[]
    numlistY=[]
    for line in inputFile:
        if("x" in line):
            continue
        nums=line.split()
        numlistX.append(float(nums[0]))
        numlistY.append(float(nums[1]))
    return numlistX,numlistY

#main function
figure("Python作业6_拟合直线--03013301王路")
pTable=PrettyTable(["FileName","XAverage","XVariance","XStandDev",
                    "YAverage","YVariance","YStandDev","XYCorrCoeff"])

for i in range(4):
    fileName="pyData"+str(i+1)+".txt"
    numX,numY=readDataFromTxt(fileName)
    
    #画表
    pTable.add_row([fileName,getAverage(numX),round(getVariance(numX),3),
                    round(getVariance(numX)**0.5,3),round(getAverage(numY),3),
                    round(getVariance(numY),3),round(getVariance(numY)**0.5,3),
                   round(getCorrCoeff(numX, numY),3)])
    
    #画图
    subplot(2,2,i+1)
    pyplot.title(fileName)
    xlim(0,20)
    ylim(2,14)
    pyplot.plot(numX,numY,"bo")
    coeffK,coeffB=numpy.polyfit(numX,numY,1)
    lineX=numpy.linspace(0,20,20)
    lineY=coeffK*lineX+coeffB
    pyplot.plot(lineX,lineY)
    
print(pTable)
show() 