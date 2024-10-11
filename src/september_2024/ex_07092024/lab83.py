#doubt pls check again the concept of static 


class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("reading from excel")


class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("reading from SQL")




class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()

tc1 = TC1()
tc1.runTC()