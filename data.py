from csv import DictReader
from datetime import date, datetime, timedelta
import statistics
import math

class DataSet:
    def __init__(self,csv_path):
        self.csv_path=csv_path
        self.data = []

    def read_csv(self):
        with open(self.csv_path,"r") as fl:
            dict_reader = DictReader(fl)
            for row in dict_reader:
                self.data.append(row)
        fl.close()

    def calculate(self,start_date,end_date,pr_type):
        working_list = []
        start_day,start_month,start_year = int(start_date[0:2]),int(start_date[3:5]),int(start_date[6:10])
        end_day,end_month,end_year = int(end_date[0:2]),int(end_date[3:5]),int(end_date[6:10])
        start = date(day=start_day,month=start_month,year=start_year)
        end = date(day=end_day,month=end_month,year=end_year)
        difference = end - start
        total_days = difference.days
        price_type = pr_type

        days_list = []
        for d in range(total_days+1):
            dt = start + timedelta(days=d)
            days_list.append(dt)

        print("Days List: ",days_list)
        # print("Self.Data: ",self.data)

        data_dict = {}
        for data in self.data:
            timestamp = int(data.get("DateTime"))
            new_date = datetime.fromtimestamp(timestamp/1000).date()
            data_dict[new_date]=data

        # print("Data Dict: ", data_dict)

        for i in days_list:
            prop = data_dict.get(i)
            if prop:
                working_list.append(prop.get(price_type))
            else:
                print("No data found with the provided dates..")
        
        print("Working List: ",working_list)
        dpa = statistics.stdev([float(e) for e in working_list])
        print("Statistics Std Deviation: ",dpa)
        count = len(working_list)
        averg = sum([float(o) for o in working_list])/count
        avg = round(averg,4)
        # print("Average: ",avg)
        std_dev = []
        for i in working_list:
            sf = float(i) - avg
            sq = sf*sf
            std_dev.append(sq)
        print("STD_DEV: ",std_dev)
        deviat = sum(std_dev)/(count-1)
        print("Deviate: ",deviat)
        sq_root = math.sqrt(deviat)
        print("SqRoot: ",sq_root)
        return f"Average is {avg} and Standard Deviation is {sq_root} for Type: {price_type}"



obj = DataSet("DataQuestion1.csv")
obj.read_csv()
user_start = "27-09-2022"
user_end = "30-09-2022"
user_type = "OPEN"
print(obj.calculate(user_start,user_end,user_type))

        


