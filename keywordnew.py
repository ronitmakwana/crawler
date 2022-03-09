import pandas as pd
import geopandas as gpd
import json
from geojson import Point, Feature, FeatureCollection, dump


file = pd.read_excel('/home/bisag/bbr/ronit/Fetch_Keywords_From_Excel/Station.xls', sheet_name="14.02.22")
f = file.columns[7]
# print(f)
dc =file.columns[[10,11]]
print(dc)
fo = file[f]
# print(fo)
data5 = file[dc]
fe = file.columns[6]
foe=file[fe]

list1 = fo.astype(str).str.split(' ')
# print(list1)
# list1
lo = []
kd =[]
da =[]
no =[]
match = ['broken','Cleanliness','Abnormalities','non-Abnormalities','Dense','Vegetation']
for matches in match:
#     print(matches)
    # print('----------')
    for i,index in enumerate(list1):
        
        # print(i,index)
        if  matches in index:
            
            x = ' '.join(index)
          
            l = data5.loc[i]
            # print(l)
            kd.append(l)
            print(l)

            
            da.append(l)
            
            loa = fo.loc[i]
            # print(loa)
            lo.append(loa)
            lap = foe.loc[i]
            no.append(lap)
            
     
lw = []
ga = pd.DataFrame(data=da)
# ha = ga.head(6)
# print(ga)
xc = ga.reset_index(drop=True)
print(xc)


print('====================================================\n')
listofdata= []
properties = []
geojson = {"type": "FeatureCollection", "features": []}
apl=[]
for lll in no:
    # print(lll)
    sc = lll.split(" ")
    # print(sc)
#     print(conset)
    gf = gpd.read_file('/home/bisag/bbr/ronit/Fetch_Keywords_From_Excel/shapefiles/IR STATION MASTER MEITY.shp')
    d =gf.columns[4]
    b = gf.columns[[4,5,7,8]]
    dataa=gf[b]
    lat = gf.columns[7]
    long = gf.columns[8]
    al = gf[lat]
    lq = gf[long]
    # dc =file.columns[11]
    # fo = file[f]

    data = gf[d]

    # dl = []
    # dl.append(data)
    # print(dl)

    list1 = data.astype(str).str.split(' ')
    # print(list1)
    for con in sc:
        for dx,cons in enumerate (list1):
            if con in cons:
#                 print('matched-----------------------------------------------------yyyyyyyyyyyyyyyyy')
                y = ' '.join(cons)
                # print(y)
               
                lc = dataa.loc[dx]
                # print(lc)
                # properties.append(lc)
                print("=======")
                # l = data5.loc[i]
                # print(l)
                lats = al.loc[dx]
                # print(lats)
                print('=====')
                lons = lq.loc[dx]
                # print(lons)
     
                listofdata.append(lc)


daf = pd.DataFrame(data=listofdata)
af = daf.reset_index(drop=True)
print(af)
# dv = daf.merge(ha, left_on='', right_index=True).reset_index()
# print(dv)
ud = daf.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
du=ud.reset_index(drop=True)
print(du)

print('-----------')

 
du = du.append(xc,ignore_index=True)
print(du)

bv = pd.merge(daf, ga, left_index=True, right_index=True)
qo = xc.join(af)
udx = qo.drop_duplicates(subset='STATION CO', keep='first', inplace=False, ignore_index=False)
print(udx)
geojson = {"type": "FeatureCollection", "features": []}

    
for _, row in udx.iterrows():
    
    feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [row['LOGITUDE'], row['LATITUDE']]}, "properties": {"STATION CO": row['STATION CO'],"STATION FU": row['STATION FU'],"Remarks":str(row['Remarks'])}}
    geojson['features'].append(feature)

with open('geojsonfile.geojson', 'w') as fp:
    json.dump(geojson, fp) 


print('-------finished---------')


