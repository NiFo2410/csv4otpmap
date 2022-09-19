import csv

InputFile = "C:/Users/nfom9/Documents/mg1.csv"
OutFileName = "vatinskoe_tailakovskoe.csv"


with open(OutFileName, encoding="utf-8", mode='w') as f:
  with open(InputFile, mode='r') as file:
    reader = csv.reader(file)
    i = 0
    counter1 = 0
    counter2 = 0 
    counter3 = 0
    ID = 0
    type = 25
    secondRun = 0
    polygon = 0
    point_num = 0
    arrayX = []
    arrayY = []
    arrayZero = []
    arrayDot = []
    arrayName = []
    arrayToFile = []

    #    ID,type,label,group,geometry_type,point_num,coordinates,highlight,visible
    #     +   +    +     +       +            +         +           +         +    
    # + поле печатается
    # - поле не печатается 
                   
    for row in reader:
      arrayX.append(row[43])
      arrayY.append(row[44])
      arrayDot.append(row[40])
      arrayName.append(row[3])
      if row[40] == '0':
        arrayZero.append(len(arrayX) - 1)
    


    arrayToFile.append('ID,type,label,group,geometry_type,coordinates,highlight,visible\n')

    while  i <= len(arrayZero):
      #print(arrayZero)
      #print('i',i)
      #print(len(arrayZero) - 1)
      if i == len(arrayZero) - 1:
        polnum = arrayZero[i]
        #print ('ya')
        break
      else:
        polnum = arrayZero[i+1]
        polnum = polnum - 1

      #print(arrayName[polnum])
      polygon = polygon + 1
      ID = ID + 1
      type = type + 1 
      #print('polygon', polygon)
      arrayToFile.append(str(ID) + ",")
      arrayToFile.append(str(type) + ",")
      arrayToFile.append('Polygon_%(polygon)s,' % {'polygon': polygon})
      arrayToFile.append(arrayName[polnum] + ',')
      arrayToFile.append("Polygon,")
      
      arrayToFile.append('"')
      
  
      if secondRun == 1:
        if counter3 < polnum:
          polnum = arrayZero[i+1]
          counter3 = counter3 + 1
      
      #print('counter3 in',counter3)
      #print ('polnum in', polnum)
      while counter3 <= polnum:

          if secondRun == 0:
            if counter3 == polnum:
              #print('%(pointN)s:%(geo1)s,%(geo2)s"\n' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
              arrayToFile.append(format('%(pointN)s:%(geo1)s,%(geo2)s",' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]}))
              break
            else:
              #print('%(pointN)s:%(geo1)s,%(geo2)s,' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
              arrayToFile.append(format('%(pointN)s:%(geo1)s,%(geo2)s,' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]}))
              counter3 = counter3 + 1
          else:
            if counter3 == polnum:
                  counter3 = counter3 - 1
                  #print('%(pointN)s:%(geo1)s,%(geo2)s"\n' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
                  arrayToFile.append(format('%(pointN)s:%(geo1)s,%(geo2)s",' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]}))
                  break
            else:
                  #print('%(pointN)s:%(geo1)s,%(geo2)s,' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
                  arrayToFile.append(format('%(pointN)s:%(geo1)s,%(geo2)s;' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]}))
                  counter3 = counter3 + 1
      arrayToFile.append("false" + ",")
      arrayToFile.append("true\n")
      


      #print('counter3 out',counter3)
      #print ('polnum out', polnum)
      i = i + 1
      secondRun = 1

    if i <= len(arrayZero):
        #print(counter3)
        #counter3 = counter3 + 1
        #print(counter3)
        ID = ID + 1
        type = type + 1 
        polygon = polygon + 1

        arrayToFile.append(str(ID) + ",")
        arrayToFile.append(str(type) + ",")
        arrayToFile.append('Polygon_%(polygon)s,' % {'polygon': polygon})
        arrayToFile.append(arrayName[polnum] + ',')
        arrayToFile.append("Polygon,")
        arrayToFile.append('"')


        while counter3 < len(arrayDot):
          if counter3 == len(arrayDot) - 1:
            arrayToFile.append('%(pointN)s:%(geo1)s,%(geo2)s",' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
            break
          else:
            arrayToFile.append('%(pointN)s:%(geo1)s,%(geo2)s;' % {'pointN': arrayDot[counter3], 'geo1': arrayX[counter3], 'geo2': arrayY[counter3]})
            counter3 = counter3 + 1

        arrayToFile.append("false" + ",")
        arrayToFile.append("true")
      
  counter1 = 0
  while counter1 < len(arrayToFile):
    print(arrayToFile[counter1], end= "", file=f)
    counter1 = counter1 + 1