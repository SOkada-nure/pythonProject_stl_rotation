import numpy as np
from stl import mesh

# stl_dataにstlの情報が入る
stl_data = mesh.Mesh.from_file('notre.stl')


##軸回転をさせる。どの軸回りに回転させるかを適宜選ぶ。np.deg2rad()は角度をラジアン表記に変換する関数。
"""
#x軸回転
matrix = np.array([[1, 0, 0], 
                   [0, np.cos(np.deg2rad(90)), - np.sin(np.deg2rad(90))],
                   [0, np.sin(np.deg2rad(90)), np.cos(np.deg2rad(90))]])
"""
#y軸回転
matrix = np.array([[np.cos(np.deg2rad(90)), 0, np.sin(np.deg2rad(90))],
                   [0, 1, 0],
                   [- np.sin(np.deg2rad(90)), 0, np.cos(np.deg2rad(90))]])
"""
#z軸回転
matrix = np.array([[np.cos(np.deg2rad(90)), - np.sin(np.deg2rad(90)), 0],
                   [np.sin(np.deg2rad(90)), np.cos(np.deg2rad(90)), 0],
                   [0, 0, 1]])
"""

##


#この行は本当は要らないはず。エラーが出るので追加。
R = np.eye(4)


R[:3, :3] = matrix
print(R)
stl_data.transform(R)


stl_data.save('norte_yrotated90.stl')




