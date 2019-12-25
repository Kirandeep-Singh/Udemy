import sys
import pandas as pd
import logger
class excel_valid ():
    def __init__ (self,fname):
        #fname = r"C:\Users\ekirand\Desktop\Pic_Auto\CSAF_CICD\cicd_template.xlsx"
        # fname=input("please provide excel file path\n")
        self.f = pd.ExcelFile(fname)

        self.sheets = self.f.sheet_names
        self.x = len(self.sheets)
        self.jn = []
        self.vali=""
        self.nwname = []
        self.ini1 = []
        self.ini2 = []
        self.quest = []
        k = 0
        df = {}
        while k < self.x:
            df[k] = pd.read_excel(fname, self.sheets[k])
            # print(df[k].at[0, 'Value'])
            self.jn.append(df[k].at[0, 'Value'])
            self.nwname.append(df[k].at[7, 'Value'])
            self.ini1.append(df[k].at[8, 'Value'])
            self.ini2.append(df[k].at[9, 'Value'])
            self.quest.append(df[k].at[10, 'Value'])
            k += 1

    def vexcel(self):
        '''
        This Function of class excel_valid will verify the inputs provided in Excel Sheet.
        If any of the file names or jobnames are repeated by user, the this Function will return False.
        :return:
        False if any of the input file names are repeated. True if File Names are unique.
        '''
        print ("Starting the validation of excel")
        # print (jn, nwname, ini1, ini2, quest)
        if len(set(self.nwname)) < len(self.nwname):
            print("Network File Names are not unique in all sheets      [NOT OK]")
            self.vali = "fail"
        if len(set(self.jn)) < len(self.jn):
            print("Job names not unique in all sheets                   [NOT OK]")
            self.vali = "fail"
        if len(set(self.ini1)) < len(self.ini1):
            print("INI1 File Name not unique in all sheets              [NOT OK]")
            self.vali = "fail"
        if len(set(self.ini2)) < len(self.ini2):
            print("INI2 File Name not unique in all sheets              [NOT OK]")
            self.vali = "fail"
        if len(set(self.quest)) < len(self.quest):
            print("Quest File Name not unique in all sheets             [NOT OK]")
            self.vali = "fail"
        if self.vali == "fail":
            return False
        else:
            return True

    def csv(self,out):
        k = 0
        while k < self.x:
            sn=self.sheets[k]
            df = self.f.parse(sheet_name=sn, index_col=None, na_values=['NA'])
            #out=r"C:\Users\ekirand\Desktop\Pic_Auto\CSAF_CICD\out_"
            outname = out + sn + ".csv"
            df.to_csv(outname)
            k += 1

def fun(fname):
    return excel_valid(fname)

fname = r"C:\Users\ekirand\Desktop\Pic_Auto\CSAF_CICD\cicd_template.xlsx"
out = r"C:\Users\ekirand\Desktop\Pic_Auto\CSAF_CICD\out_"
logpath = r"C:\Users\ekirand\Desktop\Pic_Auto\CSAF_CICD\log.txt"

logger.log("Exiting because Excel fields validation failed. Please check the NOT OK statuses shown above", logpath)



'''
t = fun(fname)

if not t.vexcel():
    #logger.log("Exiting because Excel fields validation failed. Please check the NOT OK statuses shown above", logpath)
    sys.exit("Exiting because Excel fields validation failed. Please check the NOT OK statuses shown above")
else:
    print("Excel File has been validated Successfully. Proceeding Further")

t.csv(out)
'''