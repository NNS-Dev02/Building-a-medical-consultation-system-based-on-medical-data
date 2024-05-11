import pandas as pd
import numpy as np
import tensorflow
from tensorflow.keras.models import*
from tensorflow.keras.layers import*

file = pd.read_csv('data.csv')
time_tb = file['Thoi gian kh TB (phut)']
maso_room = file['Phong kham']
time_now = file['Thoi gian kham']
ghecho = file['So nguoi trong phong']
ghechong = file['So cho trong (1-10)']
print(maso_room)

def save_result(result_text):
    with open('result.txt', 'w') as result_file:
        result_file.write(result_text)
    print(result_text)

def choose_room(maso_room, ghechong, time_now, time_tb, ghecho, index, Time_now):
    ghechong_gut = []
    ghechong_td  = []
    ghechong_st  = []
    soghe_gut    = []
    soghe_td     = []
    soghe_st     = []
    time_gut     = []
    time_td      = []
    time_st      = []
    room_gut     = []
    room_td      = []
    room_st      = []
    time_gut_tb  = []
    time_td_tb   = []
    time_st_tb   = []
    total_time   = 1000
    ID = -1
    for i in range(len(maso_room)):
        if maso_room[i][0] == '1':
            ghechong_gut.append(ghechong[i])
            room_gut.append(maso_room[i])
            time_gut.append(time_now[i])
            time_gut_tb.append(time_tb[i])
            soghe_gut.append(ghecho[i])
        if maso_room[i][0] == '2':
            ghechong_td.append(ghechong[i])
            room_td.append(maso_room[i])
            time_td.append(time_now[i])
            time_td_tb.append(time_tb[i])
            soghe_td.append(ghecho[i])
        if maso_room[i][0] == '3':
            ghechong_st.append(ghechong[i])
            room_st.append(maso_room[i])
            time_st.append(time_now[i])
            time_st_tb.append(time_tb[i])
            soghe_st.append(ghecho[i])
    if index == 1:
        for i in range(len(time_gut)):
            if Time_now < float(time_gut[i])+1 and Time_now > float(time_gut[i]) -1:
                if float(soghe_gut[i])*float(time_gut_tb[i])<total_time and float(ghechong_gut[i])>0:
                    total_time=float(soghe_gut[i])*float(time_gut_tb[i])
                    ID=i
        if ID>-1:
            result_text = "1\n" + str(room_gut[ID])
            save_result(result_text)

    if index == 2:
        for i in range(len(time_td)):
            if Time_now < float(time_td[i])+1 and Time_now > float(time_gut[i]) -1:
                if float(soghe_td[i])*float(time_td_tb[i])<total_time and float(ghechong_td[i])>0:
                    total_time=float(soghe_td[i])*float(time_td_tb[i])
                    ID=i
        if ID>-1:
            result_text = "2\n" + str(room_td[ID])
            save_result(result_text)

    if index == 3:
        for i in range(len(time_st)):
            if Time_now < float(time_st[i])+1 and Time_now > float(time_gut[i]) -1:
                if float(soghe_st[i])*float(time_st_tb[i])<total_time and float(ghechong_st[i])>0:
                    total_time=float(soghe_st[i])*float(time_st_tb[i])
                    ID=i
        if ID>-1:
            result_text = "3\n" + str(room_st[ID])
            save_result(result_text)

    if index == 0:
        with open('result.txt', 'w') as result_file:
            result_text = "4\n" + "999"
            save_result(result_text)

def test(Time_now, input):
    DD    = 0
    maxs  = 0
    index = model.predict(np.array(input).reshape(1,-1))[0]
    for i in range(len(index)):
        if index[i] > maxs:
               maxs = index[i]
               DD   = i

    choose_room(maso_room, ghechong, time_now, time_tb, ghecho, DD, Time_now)

def create_data(data):
      lis_number  = ['0','1','2','3']
      Data        = []
      Data_socap  = []
      data_output = []
      for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in lis_number and len(Data_socap) == 6:
                data_output.append(int(data[i][j]))
            if data[i][j] in lis_number and len(Data_socap) < 6:
                Data_socap.append(int(data[i][j]))
        Data.append(Data_socap)
        Data_socap = []
      return Data,data_output

Input,Output=create_data(file["DF"])
print(len(Input))
print(len(Output))

Input  = np.array(Input).reshape(len(Input), -1)
Output = np.array(Output)

model=Sequential()
model.add(Dense(50,activation='relu'))
model.add(Dense(52,activation='relu'))
model.add(Dense(50,activation='relu'))
model.add(Dense( 4,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='Adamax',metrics=['accuracy'])
model.fit(Input,Output,epochs=20)

with open('params.txt', 'r') as params_file:
    params = params_file.read().strip().split(', ')
    params = [int(val) for val in params]

if len(params) == 7:
    test(params[0], params[1:])
else:
    print("Số lượng tham số không hợp lệ đọc từ params.txt")