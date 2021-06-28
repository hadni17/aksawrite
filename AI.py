from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    ha = []
    na = []
    ca = []
    ra = []
    ba = []
    ka = []
    ga = []
    da = []
    dha = []
    ja = []
    la = []
    ma = []
    nga = []

    for file in os.listdir("ha"):
        img = Image.open("ha/" + file)
        img = np.array(img)
        img = img.flatten()
        ha.append(img)

    for file in os.listdir("na"):
        img = Image.open("na/" + file)
        img = np.array(img)
        img = img.flatten()
        na.append(img)

    for file in os.listdir("ca"):
        img = Image.open("ca/" + file)
        img = np.array(img)
        img = img.flatten()
        ca.append(img)

    for file in os.listdir("ra"):
        img = Image.open("ra/" + file)
        img = np.array(img)
        img = img.flatten()
        ra.append(img)
    
    for file in os.listdir("ba"):
        img = Image.open("ba/" + file)
        img = np.array(img)
        img = img.flatten()
        ba.append(img)
    
    for file in os.listdir("ka"):
        img = Image.open("ka/" + file)
        img = np.array(img)
        img = img.flatten()
        ka.append(img)

    for file in os.listdir("ga"):
        img = Image.open("ga/" + file)
        img = np.array(img)
        img = img.flatten()
        ga.append(img)
    
    for file in os.listdir("da"):
        img = Image.open("da/" + file)
        img = np.array(img)
        img = img.flatten()
        da.append(img)

    for file in os.listdir("dha"):
        img = Image.open("dha/" + file)
        img = np.array(img)
        img = img.flatten()
        dha.append(img)

    for file in os.listdir("ja"):
        img = Image.open("ja/" + file)
        img = np.array(img)
        img = img.flatten()
        ja.append(img)

    for file in os.listdir("la"):
        img = Image.open("la/" + file)
        img = np.array(img)
        img = img.flatten()
        la.append(img)
    for file in os.listdir("ma"):
        img = Image.open("ma/" + file)
        img = np.array(img)
        img = img.flatten()
        ma.append(img)
    
    for file in os.listdir("nga"):
        img = Image.open("nga/" + file)
        img = np.array(img)
        img = img.flatten()
        nga.append(img)

    return ha, na, ca,ra,ba,ka,ga,da,dha,ja,la,ma,nga

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    ha, na, ca, ra , ba, ka, ga,da,dha,ja,la,ma,nga= load_dataset()
    print("[INFO] Loading Model")
    y_ha = np.zeros(len(ha))
    y_na = np.ones(len(na))
    y_ca = np.ones(len(ca)) *2
    y_ra = np.ones(len(ra))*3
    y_ba = np.ones(len(ba))*4
    y_ka = np.ones(len(ka))*5
    y_ga = np.ones(len(ga))*6
    y_da = np.ones(len(da))*7
    y_dha = np.ones(len(dha))*8
    y_ja = np.ones(len(ja))*9
    y_la = np.ones(len(la))*10
    y_ma = np.ones(len(ma))*11
    y_nga = np.ones(len(nga))*12
    X = ha + na + ca + ra + ba + ka + ga + da + dha + ja + la + ma + nga
    y = np.concatenate([y_ha, y_na, y_ca,y_ra,y_ba,y_ka,y_ga,y_da,y_dha,y_ja,y_la,y_ma,y_nga])
    model.fit(X, y)
   
    return model