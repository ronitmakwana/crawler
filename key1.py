# # import pandas as pd
# # import geopandas as gpd


# # file = pd.read_excel('/home/ronit/Downloads/keyword/Station.xls', sheet_name="14.02.22")
# # # print(file)
# # # file.loc[0:]
# # f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]

# # data = f['Abnormalities/ Deficiencies found ( In Brief)']


# # list1 = data.astype(str).str.split(' ')
# # # list1
# # lo = []
# # match = ['broken']
# # for matches in match:
# # #     print(matches)
# #     print('----------')
# #     for i,index in enumerate(list1):
        
# #         # print(i)
# #         if  matches in index:
            
# #             x = ' '.join(index)
# #             # print(i,'======>',x)
# # #             print('----------')
# #             # print('matched')
# #             # print('-----------')
# # #             f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
# #             l = file.loc[i]

# #             fd = l[6]
# #             lo.append(fd)

# #             # df = pd.DataFrame(data=l)
# #             # df1_transposed = df.T
# # print(lo)

# # listofdata= []
# # for lll in lo:
# #     sc = lll.split(" ")
# #     # print(sc)
# # #     print(conset)
# #     gf = gpd.read_file('/home/ronit/Downloads/keyword/IR STATION MASTER MEITY.shp')
# #     d =gf.columns[4]
# #     data1 = gf[d]


# #     list2 = data1.astype(str).str.split(' ')
# #     # print(list1)
# #     for con in sc:
# #         for dx,cons in enumerate (list2):
# #     #         print(dx,cons)
# #             if con in cons:
# # #           
# #                 y = ' '.join(cons)
# # #                 print(y)
# #                 lc = gf.loc[dx]
# # #                 cols = lc[8]
# # #                 print(lc,'==========================================')
# #                 listofdata.append(lc)
# # # print(listofdata)
# # dataframes = pd.DataFrame(data=listofdata)
# # print(dataframes)
# # print('-----------')

# # print("Searching finished")


# import pandas as pd
# import geopandas as gpd
# import json
# from geojson import Point, Feature, FeatureCollection, dump


# file = pd.read_excel('/home/bisag/bbr/ronit/Fetch_Keywords_From_Excel/Station.xls', sheet_name="14.02.22",  index_col= False)
# # print(file)
# # file.loc[0:]
# # fa = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.','Remarks']]
# f = file.columns[7]
# # print(f)
# dc =file.columns[11]
# fo = file[f]
# # print(fo)
# data5 = file[dc]
# fe = file.columns[6]
# foe=file[fe]





# # list =[]
# # for i in f:
# #     list.append(f)
# # #     print(list[:-1])
    
# # k = list[:-1]
# # k
# # for i in f:
# #     print(i)
# # cols  = file.columns.to_list()
# # col = cols[7]
# # print(col)
# # print('---------------------------------------------')
# # list =[]
# # data = f['Abnormalities/ Deficiencies found ( In Brief)']
# list1 = fo.astype(str).str.split(' ')
# # print(list1)
# # list1
# lo = []
# da =[]
# no =[]
# match = ['broken','cabin']
# for matches in match:
# #     print(matches)
#     print('----------')
#     for i,index in enumerate(list1):
        
#         # print(i,index)
#         if  matches in index:
            
#             x = ' '.join(index)
#             # print('======>',x)
# #             print('----------')
#             # print('matched')
#             # print('-----------')
#             # a = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
#             l = data5.loc[i]
#             print(l)
            
#             da.append(l)
            
#             loa = fo.loc[i]
#             print(loa)
#             lo.append(loa)
#             lap = foe.loc[i]
#             no.append(lap)
#             df3 = pd.DataFrame(data=lo)
#             df1_transposed = df3.T
#             # print(df1_transposed)

#             # df = pd.DataFrame(data=l)
          
#             # df1_transposed = df.T
#             # print(df1_transposed)
# # print(no,'-----------------------------------------------------')
# lw = []
# ga = pd.DataFrame(data=da)
# # print(ga)
# # cg = ga.columns
# # cx = cg[11]
# # dh = ga[cx]
# # print(dh)
# # for qk in dh:
# #     # print(qk)
# #     lw.append(qk)
# # init = iter(ga)  
# dic1 = ga.to_dict('dict')
# # res_dct = dict(zip(init, init))    
# print(dic1)  
# print(lw)

# # qp = "Remarks"+str(lw)
# # print(qp)
# # dic1 = qp.to_dict('dict')
# # print(dic1)

# # print(dh)
# # file = 'keywprds.txt'
# # with open(file,'a') as f:
# #     f.write(str(lo))
# #     print('=======saved=======')
# # for il in lo:
# #     print(il)
# #             print(df1_transposed)
# #             li = []
# #             lo.append(df1_transposed)
# #             print(li)
# #             for ll in li:
# #                 print(ll[0:2])
# # for kk in lo:

# #     df1 = pd.DataFrame(data=kk)
# # # df1 = df1.T
# #     print (df1)

# # for i,index in enumerate(list1):
# #     d = i,index
# # #     print(d)
# #     k = index[81:93]
# #     for ik in k:
# # #         print(ik)
    
# # #         s = ik.split(' ')
# #     #     print(s)
# #         if 'Broken' in s:
# #             print('matched')
# #             print(k)
# #         else:
# #             print('matched not')


# # import pandas as pd
  
    
# # fo = pd.read_csv('keywprds.txt')
# # # fo
# # # print(fo)
# # list = [""]
# # for ff in fo:
# # #     print(len(ff))
# #     spl = ff.split(" ")
# #     spl.pop(0)
# #     #print(spl)
# #     for sp in spl:
        
# #         st= str(sp)
# #         re = st.replace("]",' ')
# #         rep = re.replace("'"," ")
     
# #         list.append(rep)
# # print(type(list))
# # conset = set(list)
# # print(conset)
# # for ll in list:
# #     print(ll)
# # conset = set(lo)
# # sc = lo.split(" ")
# print('====================================================\n')
# listofdata= []
# for lll in no:
#     # print(lll)
#     sc = lll.split(" ")
#     print(sc)

# #     print(conset)
#     gf = gpd.read_file('/home/bisag/bbr/ronit/Fetch_Keywords_From_Excel/shapefiles/IR STATION MASTER MEITY.shp')
#     d =gf.columns[4]
#     b = gf.columns[[7,8]]
#     dataa=gf[b]
#     data = gf[d]

#     # dl = []
#     # dl.append(data)
#     # print(dl)

#     list1 = data.astype(str).str.split(' ')
#     # print(list1)
#     for con in sc:
# #         print(con)

#     # # data
#         for dx,cons in enumerate (list1):
#     #         print(dx,cons)
#     #     for dm,i in e/numerate(data,0):
#     #         print(i)
#             if con in cons:
# #                 print('matched-----------------------------------------------------yyyyyyyyyyyyyyyyy')
#                 y = ' '.join(cons)
# #                 print(y)
               
#                 lc = dataa.loc[dx]
#                 # print(lc)
# #                 cols = lc[8]
# #                 print(lc,'==========================================')
#                 listofdata.append(lc)
                

# # print(listofdata)
# daf = pd.DataFrame(data=listofdata)
# print(daf)
# df1_transposed1 = daf.T
# print(df1_transposed1)




# dic = df1_transposed1.to_dict('dict')
# # js = str(dic)
# r = json.dumps(dic)
# print(r)
# # loaded_r = json.loads(js)
# # loaded_r['rating'] #Output 3.5
# print(type(r)) #Output str
# # print(type(loaded_r)) #Output dict
# # init = iter(new)  
# # res_dct = dict(zip(init, init))  
# # print(res_dct)
                
                
# # print(listofdata)
# # pq =[]
# # dataframes = pd.DataFrame(data=listofdata)
# # # print(dataframes)
# # va = dataframes.columns
# # q = va[[4,5,7,8]]
# # dat = dataframes[q]
# # w = dat.values
# # print(dat)
# # for dw in dat:
# #     # print()
# #     pq.append(w)


# # p = pq[0]
# # ak= []
# # for qp in p:
# #     aa= "Station : "+str(qp)
#     # ak.append(aa)
# #     for aq in qp:
# #         print(aq)
# #         ak.append(aq)
# # qt = ak.split(' ')
# # print(qt)


# # daf = pd.DataFrame(data=ak)
# # print(daf)
# # dfq = daf.to_dict('dict')
# # print(dfq)
# # df_reset=dat.set_index('STATION CO')
# # dic = dat.to_dict('dict')
# # print(dic)
# print('-----------')

# point = dic
# features = []
# features.append(Feature(Point=point))

# # add more features...
# # features.append(...)

# feature_collection = FeatureCollection(features)

# with open('myfile24.geojson', 'w') as f:
#    dump(feature_collection, f)
# print("Searching finished")
# import pandas as pd
# import geopandas as gpd


# file = pd.read_excel('/home/ronit/Downloads/keyword/Station.xls', sheet_name="14.02.22")
# # print(file)
# # file.loc[0:]
# f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]

# data = f['Abnormalities/ Deficiencies found ( In Brief)']


# list1 = data.astype(str).str.split(' ')
# # list1
# lo = []
# match = ['broken']
# for matches in match:
# #     print(matches)
#     print('----------')
#     for i,index in enumerate(list1):
        
#         # print(i)
#         if  matches in index:
            
#             x = ' '.join(index)
#             # print(i,'======>',x)
# #             print('----------')
#             # print('matched')
#             # print('-----------')
# #             f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
#             l = file.loc[i]

#             fd = l[6]
#             lo.append(fd)

#             # df = pd.DataFrame(data=l)
#             # df1_transposed = df.T
# print(lo)

# listofdata= []
# for lll in lo:
#     sc = lll.split(" ")
#     # print(sc)
# #     print(conset)
#     gf = gpd.read_file('/home/ronit/Downloads/keyword/IR STATION MASTER MEITY.shp')
#     d =gf.columns[4]
#     data1 = gf[d]


#     list2 = data1.astype(str).str.split(' ')
#     # print(list1)
#     for con in sc:
#         for dx,cons in enumerate (list2):
#     #         print(dx,cons)
#             if con in cons:
# #           
#                 y = ' '.join(cons)
# #                 print(y)
#                 lc = gf.loc[dx]
# #                 cols = lc[8]
# #                 print(lc,'==========================================')
#                 listofdata.append(lc)
# # print(listofdata)
# dataframes = pd.DataFrame(data=listofdata)
# print(dataframes)
# print('-----------')

# print("Searching finished")


import pandas as pd
import geopandas as gpd
import json
from geojson import Point, Feature, FeatureCollection, dump


file = pd.read_excel('/home/bisag/bbr/ronit/Fetch_Keywords_From_Excel/Station.xls', sheet_name="14.02.22")
# print(file)
# file.loc[0:]
# fa = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.','Remarks']]
f = file.columns[7]
# print(f)
dc =file.columns[[10,11]]
print(dc)
fo = file[f]
# print(fo)
data5 = file[dc]
fe = file.columns[6]
foe=file[fe]





# list =[]
# for i in f:
#     list.append(f)
# #     print(list[:-1])
    
# k = list[:-1]
# k
# for i in f:
#     print(i)
# cols  = file.columns.to_list()
# col = cols[7]
# print(col)
# print('---------------------------------------------')
# list =[]
# data = f['Abnormalities/ Deficiencies found ( In Brief)']
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
            # print('======>',x)
#             print('----------')
            # print('matched')
            # print('-----------')
            # a = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
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
            
            # df3 = pd.DataFrame(data=lo)
            # df1_transposed = df3.T
            # print(df1_transposed)

            # df = pd.DataFrame(data=l)
          
            # df1_transposed = df.T
            # print(df1_transposed)
# print(kd)
# print(no,'-----------------------------------------------------')
# print(da)
lw = []
ga = pd.DataFrame(data=da)
# ha = ga.head(6)
# print(ga)
xc = ga.reset_index(drop=True)
print(xc)
# cg = ga.columns
# cx = cg[10]
# dh = ga[cx]
# print(dh)
# for qk in dh:
#     # print(qk)
#     lw.append(qk)
# init = iter(ga)  
# dic1 = ga.to_dict('dict')
# res_dct = dict(zip(init, init))    
# print(dic1)  
# print(lw)

# qp = "Remarks"+str(lw)
# print(qp)
# dic1 = qp.to_dict('dict')
# print(dic1)

# print(dh)
# file = 'keywprds.txt'
# with open(file,'a') as f:
#     f.write(str(lo))
#     print('=======saved=======')
# for il in lo:
#     print(il)
#             print(df1_transposed)
#             li = []
#             lo.append(df1_transposed)
#             print(li)
#             for ll in li:
#                 print(ll[0:2])
# for kk in lo:

#     df1 = pd.DataFrame(data=kk)
# # df1 = df1.T
#     print (df1)

# for i,index in enumerate(list1):
#     d = i,index
# #     print(d)
#     k = index[81:93]
#     for ik in k:
# #         print(ik)
    
# #         s = ik.split(' ')
#     #     print(s)
#         if 'Broken' in s:
#             print('matched')
#             print(k)
#         else:
#             print('matched not')


# import pandas as pd
  
    
# fo = pd.read_csv('keywprds.txt')
# # fo
# # print(fo)
# list = [""]
# for ff in fo:
# #     print(len(ff))
#     spl = ff.split(" ")
#     spl.pop(0)
#     #print(spl)
#     for sp in spl:
        
#         st= str(sp)
#         re = st.replace("]",' ')
#         rep = re.replace("'"," ")
     
#         list.append(rep)
# print(type(list))
# conset = set(list)
# print(conset)
# for ll in list:
#     print(ll)
# conset = set(lo)
# sc = lo.split(" ")

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
#         print(con)

    # # data

        for dx,cons in enumerate (list1):
    #         print(dx,cons)
    #     for dm,i in e/numerate(data,0):
    #         print(i)
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
                print(lons)
                # latlong ={'type': 'GeometryCollection', 'geometries':[{'types':'point','cordinates':[lats,longs],'properties':['']}}
                
                
                # feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [[lats],[lons]]}, "properties": {"Remarks": l}}
                # geojson['features'].append(feature)
              


# {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-115.81, 37.24]}, "properties": {"country": "Spain"}}]}
                # latlong={'type': 'FeatureCollection','features': [{'type': 'Feature','geometry': {'type': 'Point','coordinates': [lats,longs]},'properties':{'Remarks': l}}]}
                # jsongeo = json.dumps(latlong)
                # print(jsongeo)
                # print(latlong)
                # apl.append(latlong)
                # point = Point((lats, longs))

                # features = []
                # features.append(Feature(geometry=point))

                # # add more features...
                # # features.append(properties={"Remarks": "adfag"})

                # feature_collection = FeatureCollection(features)
                # with open('geojsonnew3.geojson', 'a') as f:
                #     dump(feature_collection, f)
                
               

                
                # for ks in kd:
                

#                 cols = lc[8]
#                 print(lc,'==========================================')
                listofdata.append(lc)
# print(geojson)
# jsongeo = json.dumps(geojson)
# print(jsongeo)
# with open('lc2.geojson','w') as fdd:
#     fdd.write(jsongeo)
# print('------')
           
# print(apl)  
# for geoj in apl:
#     # print(geoj)
#     # spj = geoj.split(" ")
#     dum = json.dumps(geoj)
#     print(dum)

# print(properties)
# for il in properties:
#     # print(il)
#     for idb,ada in enumerate(il):
#         print(idb,ada)
# print(listofdata,l)

daf = pd.DataFrame(data=listofdata)
af = daf.reset_index(drop=True)
print(af)
# dv = daf.merge(ha, left_on='', right_index=True).reset_index()
# print(dv)
ud = daf.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
du=ud.reset_index(drop=True)
print(du)

# dic = daf.to_dict('dict')
# js = str(dic)
# r = json.dumps(dic)
# print(r)
# loaded_r = json.loads(js)
# loaded_r['rating'] #Output 3.5
# print(type(r)) #Output str
# print(type(loaded_r)) #Output dict
# init = iter(new)  
# res_dct = dict(zip(init, init))  
# print(res_dct)
                
                
# print(listofdata)
# pq =[]
# dataframes = pd.DataFrame(data=listofdata)
# # print(dataframes)
# va = dataframes.columns
# q = va[[4,5,7,8]]
# dat = dataframes[q]
# w = dat.values
# print(dat)
# for dw in dat:
#     # print()
#     pq.append(w)


# p = pq[0]
# ak= []
# for qp in p:
#     aa= "Station : "+str(qp)
    # ak.append(aa)
#     for aq in qp:
#         print(aq)
#         ak.append(aq)
# qt = ak.split(' ')
# print(qt)


# daf = pd.DataFrame(data=ak)
# print(daf)
# dfq = daf.to_dict('dict')
# print(dfq)
# df_reset=dat.set_index('STATION CO')
# dic = dat.to_dict('dict')
# print(dic)
print('-----------')
# ae = daf.insert(4, 'new_column', ['Remarks'])

# print(ae)
# ad = daf['Remarks'] = ha['Remarks'].values
# print(ad)
# kadf = pd.DataFrame(data=ad)
# # print(kadf)
# dat1 = pd.concat([daf, ha])
# print(dat1)
# dat2 = dat1.dropna() 
# print(dat2)
# L2 = [{k: v for k, v in x.items() if pd.notnull(v)} for x in ga.to_dict('r')]
# print(L2)
# print(x)
# print('--------')
# # print(k,'---------',v)
# dict_gammabid = ga.to_dict()
# # print(dict_gammabid)
# for adfs in dict_gammabid:
#     print(adfs)
# for lep in L2:
#     ap = lep
 
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

with open('result2.geojson', 'w') as fp:
    json.dump(geojson, fp) 


print('-------finished---------')


