"""����A�ļ����о�γ�ȵĵ㣬��B�ļ���������о�γ�ȵ㼰����"""
#����ɣ�������Ч�ʵͣ�7000*7000��2������Ҫ10��������
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

rfileh=0    #д��EXCEL��ʱ��
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
        sheet1.write(rfileh,0,aline.split(",")[4])  #д�������CI
        sheet1.write(rfileh,1,MinDiscCI)    #д���������CI
        sheet1.write(rfileh,2,MinDisc)  #д��������ľ���
        rfileh+=1
    bfile.seek(0)   #�������ļ������ļ���
book.save('e://temp/resultdata.xls')
afile.close()
bfile.close()