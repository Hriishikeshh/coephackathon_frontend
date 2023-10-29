import csv
import matplotlib.pyplot as plt

# Open the CSV file for reading
with open('DataSet.csv', 'r') as csvfile:
    # Create a DictReader object
    reader = csv.DictReader(csvfile)
    data = []
    # Iterate through the rows, where each row is a dictionary
    for row in reader:
        data.append(row)


    # print(data)
def shorter_list(lis,state,ins_type,lower,upper):
    res = []
    for x in lis:
        if x[' Region        '] == state and x[' InstallationType '] == ins_type and int(x[' Cost  '])>lower and int(x[' Cost  '])<upper:
            res.append(x)
    return res

def usage_pattern(res):
    value = [0,0,0,0,0,0,0,0,0,0,0]
    index = ['0-1000','1000-2000','2000-3000','3000-4000','4000-5000','5000-6000','6000-7000','7000-8000','8000-9000','9000-10000','10000-11000']
    for x in res:
        if int(x[' EnergyProduced (kWh) ']) >0 and int(x[' EnergyProduced (kWh) ']) <1000:
            value[0]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=1000 and int(x[' EnergyProduced (kWh) ']) <2000:
            value[1]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=2000 and int(x[' EnergyProduced (kWh) ']) <3000:
            value[2]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=3000 and int(x[' EnergyProduced (kWh) ']) <4000:
            value[3]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=4000 and int(x[' EnergyProduced (kWh) ']) <5000:
            value[4]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=5000 and int(x[' EnergyProduced (kWh) ']) <6000:
            value[5]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=6000 and int(x[' EnergyProduced (kWh) ']) <7000:
            value[6]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=7000 and int(x[' EnergyProduced (kWh) ']) <8000:
            value[7]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=8000 and int(x[' EnergyProduced (kWh) ']) <9000:
            value[8]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=9000 and int(x[' EnergyProduced (kWh) ']) <10000:
            value[9]+=1
        elif int(x[' EnergyProduced (kWh) ']) >=10000 and int(x[' EnergyProduced (kWh) ']) <11000:
            value[10]+=1


    plt.bar(index, value, color="hotpink")
    plt.show()
def optimization(res):
    value = [0, 0, 0]
    index = ['Polycrystalline','Monocrystalline','Thin film']
    for x in res:
        if x[' PanelType      '] == ' Polycrystalline  ':
            value[0] += 1
        elif x[' PanelType      '] == ' Monocrystalline ':
            value[1] += 1
        elif x[' PanelType      '] == ' Thin Film       ':
            value[2] += 1
    plt.bar(index, value, color="hotpink")
    plt.show()
def ROI(res):
    value = [0,0,0]
    index = ['0-50000','50000-100000','above 100000']
    for x in res:
        if int(x[' AnnualSavings']) <50000:
            value[0] += 1
        elif int(x[' AnnualSavings']) >=50000 and int(x[' AnnualSavings']) <100000:
            value[1] += 1
        elif int(x[' AnnualSavings']) >100000:
            value[2] += 1

    plt.bar(index, value, color="hotpink")
    plt.xlabel("annual savings")
    plt.show()
def location(res):
    value =[0,0,0,0]
    index = ["10-20;70-80","10-20;80-90","20-30;70-80","20-30;80-90"]
    for x in res:
        if float(x[' Latitude '])>10 and float(x[' Latitude '])<20 and float(x[' Longitude '])>70 and float(x[' Longitude '])<80:
            value[0]+=1
        elif float(x[' Latitude '])>10 and float(x[' Latitude '])<20 and float(x[' Longitude '])>80 and float(x[' Longitude '])<90:
            value[1]+=1
        elif float(x[' Latitude ']) > 20 and float(x[' Latitude ']) < 30 and float(x[' Longitude ']) > 70 and float(x[' Longitude ']) < 80:
            value[2] += 1
        elif float(x[' Latitude ']) > 20 and float(x[' Latitude ']) < 30 and float(x[' Longitude ']) > 70 and float(x[' Longitude ']) < 80:
            value[3] += 1
    plt.bar(index, value, color="hotpink")
    plt.xlabel("latitude and longitude")
    plt.show()


res = shorter_list(data,' West Bengal  ',' Industrial       ',0,130000)

location(res)

# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# @app.route('/receive-data', methods=['POST'])
# def receive_data():
#     data = request.json  # Assuming the data is sent in JSON format
#     # Process the received data
#     # ...
#
#     return jsonify({'message': 'Data received successfully'})
#
