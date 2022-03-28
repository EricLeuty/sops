import pandas as pd
import datetime

BEHAVIOR_COLUMN_LABELS = ["Student ID", "Behavior Code", "Start Time", "End Time"]

class DataSet(object):
    def __init__(self):
        self.data = pd.DataFrame(columns=BEHAVIOR_COLUMN_LABELS)


    def add_datum(self, data_point):
        self.data = self.data.append(data_point.data, ignore_index=True)
        self.data = self.data.drop_duplicates()


    def print(self):
        print(self.data.head())


class Datum(object):
    def __init__(self, student_id, behavior_code, start_time, end_time=None):
        if isinstance(student_id, int):
            self.data = {
                "Student ID": student_id,
                "Behavior Code": behavior_code,
                "Start Time": start_time,
                "End Time": end_time
            }


if __name__ == '__main__':
    date = datetime.datetime.today()
    thing = Datum(1234, "CODE1", date)
    thing2 = Datum(1235, "CODE1", date)

    data = DataSet()
    print(data)

    print()

    data.add_datum(thing)
    data.add_datum(thing2)
    for i in data.data.iloc[:,0]:
        print(i)


