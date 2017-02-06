"""计算A文件中有经纬度的点，在B文件中最近的有经纬度点及距离"""
#已完成，但运行效率低，7000*7000的2个表，需要10分钟以上
import math
import xlwt

def rad(d):
    return d*math.pi/180.0
def distance(lat1,lng1,lat2,lng2):
    radlat1=rad(lat1)
    radlat2=rad(lat2)
    a=radlat1-radlat2
    b=rad(lng1)-rad(lng2)
    s=2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius=6378.137
    s=s*earth_radius
    if s<0:
        return -s
    else:
        return s

afile=open('e://temp/gsmcell20160415.csv','r')
bfile=open('e://temp/ltecell20160415.csv','r')
book=xlwt.Workbook()
sheet1=book.add_sheet(sheetname='main',cell_overwrite_ok=True)

rfileh=0    #写入EXCEL表时行
for aline in afile:
    MinDisc=999999999
    MinDiscCI=12345
    if aline[:4]!='2016':
        continue
    else:
        for bline in bfile:
            if bline[:4]!='2016':
                continue
            elif bline.split(",")[8]=='':
                break
            elif distance(float(aline.split(",")[13]),float(aline.split(",")[12]),float(bline\
                        .split(",")[8]),float(bline.split(",")[9]))<MinDisc:
                    MinDisc=distance(float(aline.split(",")[13]),float(aline.split(",")[12]),float(bline\
                                         .split(",")[8]),float(bline.split(",")[9]))
                    MinDiscCI=bline.split(",")[2]
        sheet1.write(rfileh,0,aline.split(",")[4])  #写入计算表的CI
        sheet1.write(rfileh,1,MinDiscCI)    #写入计算结果的CI
        sheet1.write(rfileh,2,MinDisc)  #写入计算结果的距离
        rfileh+=1
    bfile.seek(0)   #被计算文件跳回文件首
book.save('e://temp/resultdata.xls')
afile.close()
bfile.close()