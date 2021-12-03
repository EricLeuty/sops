import pandas as pd
import datetime

behaviorColumnLabels = ["Student ID", "Behavior Code", "Data Source ID", "Start Time", "End Time"]

class BehaviorSet(object):
    def __init__(self):
        self.behaviors = pd.DataFrame(columns=behaviorColumnLabels)


    def addDataPoint(self, dataPoint):
        if(isinstance(dataPoint, BehaviorData)):
            self.behaviors = self.behaviors.append(dataPoint.data, ignore_index=True)
            self.behaviors = self.behaviors.drop_duplicates()
        else:
            print('Data is not an instance of BehaviorData.')


    #def deleteDataPoint(index):



class BehaviorData(object):
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
    thing = BehaviorData(1234, "CODE1", "VID1", date)
    data = BehaviorSet()
    print(data)

    print()

    data.addDataPoint(thing)
    data.addDataPoint(thing)
    print(data.behaviors.head())


