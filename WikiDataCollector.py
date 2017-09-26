
import json
import numpy as np
#  P3739104 Natural causes
#  P10737         Suicide
#  Q171558        Accident
#  Q149086        homicide

Object = []
CollectAnObject =[]
CollectedData = []
CollectedLabel = []
n = 0
with open('latest-all.json') as WikiData:
    for line in WikiData:
        if line != '[\n' and line != '\n]':
            # data='{'+'object:{'+line+'}}'
            Object = json.loads(line[:-2])
            # print(Object['id'])
            if 'P1196' in Object['claims'] and 'datavalue' in Object['claims']['P1196'][0]['mainsnak'] and Object['claims']['P1196'][0]['mainsnak']['datavalue']['value']['numeric-id'] in [3739104,10737,171558,149086]:
               # print (Object['claims']['P1196'][0]['mainsnak']['datavalue']['value']['numeric-id'])
               # FeatureColumns = Object['claims'].keys()
               # print(Object['id'])
               FeatureColumnsX = ['P21','P103','P106','P551','P20','P119','P463']
               lenFeature = len(FeatureColumnsX)
               LabelColumnY = ['P1196']
               FeatureValue = dict.fromkeys( ['P21','P103','P106','P551','P20','P119','P463'])
               LabelValue = Object['claims']['P1196'][0]['mainsnak']['datavalue']['value']['numeric-id']
               ObjectID = Object['id']
               CollectAnObject = []
               CollectAnObject.append(ObjectID)
               # CollectedData.append(ObjectID)
               CollectedLabel.append(LabelValue)
               for f in FeatureColumnsX:
                   if f in Object['claims'] and 'datavalue' in Object['claims'][f][0]['mainsnak']:
                      FeatureValue[f] =  Object['claims'][f][0]['mainsnak']['datavalue']['value']['numeric-id']
                      CollectAnObject.append( Object['claims'][f][0]['mainsnak']['datavalue']['value']['numeric-id'])
                   else:
                       FeatureValue[f] = 0
                       CollectAnObject.append(0)
               CollectedData.append(CollectAnObject)
               np.split(CollectedData, [-lenFeature])
               n = n+1
               print(n)
               if n==47356:
                   with open('Collected.txt', 'w') as outfile1:
                       json.dump(CollectedData, outfile1)
                   with open('labels.txt', 'w') as outfile2:
                       json.dump(CollectedLabel, outfile2)


               # X = np.array(FeatureColumnsX,1)
               # Y = np.array(LabelColumnY)
               # values =  Object['claims'][Pkeys][:]['mainsnak']['datavalue']['value']




