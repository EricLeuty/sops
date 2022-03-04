import pandas as pd
import datetime

BEHAVIOR_COLUMN_LABELS = ["Student ID", "Behavior Code", "Data Source ID"]

class DataSet(object):
    def __init__(self):
        self.data = pd.DataFrame(columns=BEHAVIOR_COLUMN_LABELS)


    def add_datum(self, data_point):
        if(isinstance(data_point, Datum)):
            self.data = self.data.append(data_point.data, ignore_index=True)
            self.data = self.data.drop_duplicates()
        else:
            print('Data is not an instance of BehaviorData.')


    def print(self):
        print(self.data.head())


class Datum(object):
    def __init__(self, student_id, behavior_code, data_source_id, start_time, end_time=None):
        self.data = {
            "Student ID": student_id,
            "Behavior Code": behavior_code,
            "Data Source ID": data_source_id,
            "Start Time": start_time,
            "End Time": end_time
        }


if __name__ == '__main__':
    date = datetime.datetime.today()
    thing = Datum(1234, "CODE1", "VID1", date)
    thing2 = Datum(1235, "CODE1", "VID1", date)

    data = DataSet()
    print(data)

    print()

    data.add_datum(thing)
    data.add_datum(thing2)
    for i in data.data.iloc[:,0]:
        print(i)


