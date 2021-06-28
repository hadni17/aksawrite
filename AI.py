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
    nya = []
    pa =[]
    sa =[]
    ta =[]
    tha =[]
    wa =[]
    ya =[]


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
    
    for file in os.listdir("nya"):
        img = Image.open("nya/" + file)
        img = np.array(img)
        img = img.flatten()
        nya.append(img)

    for file in os.listdir("pa"):
        img = Image.open("pa/" + file)
        img = np.array(img)
        img = img.flatten()
        pa.append(img)
     
    for file in os.listdir("sa"):
        img = Image.open("sa/" + file)
        img = np.array(img)
        img = img.flatten()
        sa.append(img)
    
    for file in os.listdir("ta"):
        img = Image.open("ta/" + file)
        img = np.array(img)
        img = img.flatten()
        ta.append(img)

    for file in os.listdir("tha"):
        img = Image.open("tha/" + file)
        img = np.array(img)
        img = img.flatten()
        tha.append(img)
    
    for file in os.listdir("wa"):
        img = Image.open("wa/" + file)
        img = np.array(img)
        img = img.flatten()
        wa.append(img)

    for file in os.listdir("ya"):
        img = Image.open("ya/" + file)
        img = np.array(img)
        img = img.flatten()
        ya.append(img)


    return ha, na, ca,ra,ba,ka,ga,da,dha,ja,la,ma,nga, nya, pa,sa,ta,tha, wa,ya

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    ha, na, ca, ra , ba, ka, ga,da,dha,ja,la,ma,nga,nya,pa,sa,ta,tha,wa,ya = load_dataset()
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
    y_nya = np.ones(len(nya))*13
    y_pa = np.ones(len(pa))*14
    y_sa = np.ones(len(sa))*15
    y_ta = np.ones(len(ta))*16
    y_tha = np.ones(len(tha))*17
    y_wa = np.ones(len(wa))*18
    y_ya = np.ones(len(ya))*19
    X = ha + na + ca + ra + ba + ka + ga + da + dha + ja + la + ma + nga + nya + pa + sa + ta + tha + wa + ya
    y = np.concatenate([y_ha, y_na, y_ca,y_ra,y_ba,y_ka,y_ga,y_da,y_dha,y_ja,y_la,y_ma,y_nga,y_nya,y_pa,y_sa,y_ta,y_tha,y_wa,y_ya])
    model.fit(X, y)
   
    return model