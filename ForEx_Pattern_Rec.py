#Goal: Create dynamic trading algorithm and backtest method used to find #that algorithm.  
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
from functools import reduce


totalStart = time.time()


def bytesdate2str(fmt, encoding='utf-8'):
    '''Convert strpdate2num from bytes to string as required in Python3.

    This is a workaround as described in the following tread;
    https://github.com/matplotlib/matplotlib/issues/4126/

    Credit to github user cimarronm for this workaround.
    '''

    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

bytes2str = bytesdate2str('%Y%m%d%H%M%S')

fileName = open(r'C:\Users\Marcelo\Desktop\GBPUSD\GBPUSD1d.txt')
date,bid,ask = np.loadtxt(fileName, unpack=True,
                            delimiter=',', 
                            converters={0:bytes2str})



def percentChange(startPoint, currentPoint):
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.0
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001
            

def patternStorage():
    'make percent change patterns'
    startTime = time.time()    
    x = len(avgLine)-60
    y = 31
    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y-30], avgLine[y-28])
        p3 = percentChange(avgLine[y-30], avgLine[y-27])
        p4 = percentChange(avgLine[y-30], avgLine[y-26])
        p5 = percentChange(avgLine[y-30], avgLine[y-25])
        p6 = percentChange(avgLine[y-30], avgLine[y-24])
        p7 = percentChange(avgLine[y-30], avgLine[y-23])
        p8 = percentChange(avgLine[y-30], avgLine[y-22])
        p9 = percentChange(avgLine[y-30], avgLine[y-21])
        p10 = percentChange(avgLine[y-30], avgLine[y-20])

        p11 = percentChange(avgLine[y-30], avgLine[y-19])
        p12 = percentChange(avgLine[y-30], avgLine[y-18])
        p13 = percentChange(avgLine[y-30], avgLine[y-17])
        p14 = percentChange(avgLine[y-30], avgLine[y-16])
        p15 = percentChange(avgLine[y-30], avgLine[y-15])
        p16 = percentChange(avgLine[y-30], avgLine[y-14])
        p17 = percentChange(avgLine[y-30], avgLine[y-13])
        p18 = percentChange(avgLine[y-30], avgLine[y-12])
        p19 = percentChange(avgLine[y-30], avgLine[y-11])
        p20 = percentChange(avgLine[y-30], avgLine[y-10])

        p21 = percentChange(avgLine[y-30], avgLine[y-9])
        p22 = percentChange(avgLine[y-30], avgLine[y-8])
        p23 = percentChange(avgLine[y-30], avgLine[y-7])
        p24 = percentChange(avgLine[y-30], avgLine[y-6])
        p25 = percentChange(avgLine[y-30], avgLine[y-5])
        p26 = percentChange(avgLine[y-30], avgLine[y-4])
        p27 = percentChange(avgLine[y-30], avgLine[y-3])
        p28 = percentChange(avgLine[y-30], avgLine[y-2])
        p29 = percentChange(avgLine[y-30], avgLine[y-1])
        p30 = percentChange(avgLine[y-30], avgLine[y])
    
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        
        try:
            avgOutcome = reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)

        except Exception as e:
            print(str(e))
            avgOutcome = 0

        y += 1

        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)


        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
    '''
    print(currentPoint)
    print('_________')

    print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    '''
    
    endTime = time.time()
    print(len(patternAr))
    print(len(performanceAr))
    print('storage time took:', endTime - startTime, 'seconds')
    #previous patterns 


def currentPattern():

    currentPattern1 = percentChange(avgLine[-31], avgLine[-30])
    currentPattern2 = percentChange(avgLine[-31], avgLine[-29])
    currentPattern3 = percentChange(avgLine[-31], avgLine[-28])
    currentPattern4 = percentChange(avgLine[-31], avgLine[-27])
    currentPattern5 = percentChange(avgLine[-31], avgLine[-26])
    currentPattern6 = percentChange(avgLine[-31], avgLine[-25])
    currentPattern7 = percentChange(avgLine[-31], avgLine[-24])
    currentPattern8 = percentChange(avgLine[-31], avgLine[-23])
    currentPattern9 = percentChange(avgLine[-31], avgLine[-22])
    currentPattern10 = percentChange(avgLine[-31], avgLine[-21])

    currentPattern11 = percentChange(avgLine[-31], avgLine[-20])
    currentPattern12 = percentChange(avgLine[-31], avgLine[-19])
    currentPattern13 = percentChange(avgLine[-31], avgLine[-18])
    currentPattern14 = percentChange(avgLine[-31], avgLine[-17])
    currentPattern15 = percentChange(avgLine[-31], avgLine[-16])
    currentPattern16 = percentChange(avgLine[-31], avgLine[-15])
    currentPattern17 = percentChange(avgLine[-31], avgLine[-14])
    currentPattern18 = percentChange(avgLine[-31], avgLine[-13])
    currentPattern19 = percentChange(avgLine[-31], avgLine[-12])
    currentPattern20 = percentChange(avgLine[-31], avgLine[-11])

    currentPattern21 = percentChange(avgLine[-31], avgLine[-10])
    currentPattern22 = percentChange(avgLine[-31], avgLine[-9])
    currentPattern23 = percentChange(avgLine[-31], avgLine[-8])
    currentPattern24 = percentChange(avgLine[-31], avgLine[-7])
    currentPattern25 = percentChange(avgLine[-31], avgLine[-6])
    currentPattern26 = percentChange(avgLine[-31], avgLine[-5])
    currentPattern27 = percentChange(avgLine[-31], avgLine[-4])
    currentPattern28 = percentChange(avgLine[-31], avgLine[-3])
    currentPattern29 = percentChange(avgLine[-31], avgLine[-2])
    currentPattern30 = percentChange(avgLine[-31], avgLine[-1])

    patForRec.append(currentPattern1)
    patForRec.append(currentPattern2)
    patForRec.append(currentPattern3)
    patForRec.append(currentPattern4)
    patForRec.append(currentPattern5)
    patForRec.append(currentPattern6)
    patForRec.append(currentPattern7)
    patForRec.append(currentPattern8)
    patForRec.append(currentPattern9)
    patForRec.append(currentPattern10)

    patForRec.append(currentPattern11)
    patForRec.append(currentPattern12)
    patForRec.append(currentPattern13)
    patForRec.append(currentPattern14)
    patForRec.append(currentPattern15)
    patForRec.append(currentPattern16)
    patForRec.append(currentPattern17)
    patForRec.append(currentPattern18)
    patForRec.append(currentPattern19)
    patForRec.append(currentPattern20)

    patForRec.append(currentPattern21)
    patForRec.append(currentPattern22)
    patForRec.append(currentPattern23)
    patForRec.append(currentPattern24)
    patForRec.append(currentPattern25)
    patForRec.append(currentPattern26)
    patForRec.append(currentPattern27)
    patForRec.append(currentPattern28)
    patForRec.append(currentPattern29)
    patForRec.append(currentPattern30)

    print(patForRec)
    #Most recent Pattern

def patternRecognition():
    predictedOutcomeAr = []
    patFound = 0
    plotPatAr = []
    
    for eachPattern in patternAr:
        similarity1 = 100.0 - abs(percentChange(eachPattern[0], patForRec[0]))
        similarity2 = 100.0 - abs(percentChange(eachPattern[1], patForRec[1]))
        similarity3 = 100.0 - abs(percentChange(eachPattern[2], patForRec[2]))
        similarity4 = 100.0 - abs(percentChange(eachPattern[3], patForRec[3]))
        similarity5 = 100.0 - abs(percentChange(eachPattern[4], patForRec[4]))
        similarity6 = 100.0 - abs(percentChange(eachPattern[5], patForRec[5]))
        similarity7 = 100.0 - abs(percentChange(eachPattern[6], patForRec[6]))
        similarity8 = 100.0 - abs(percentChange(eachPattern[7], patForRec[7]))
        similarity9 = 100.0 - abs(percentChange(eachPattern[8], patForRec[8]))
        similarity10 = 100.0 - abs(percentChange(eachPattern[9], patForRec[9]))

        similarity11 = 100.0 - abs(percentChange(eachPattern[10], patForRec[10]))
        similarity12 = 100.0 - abs(percentChange(eachPattern[11], patForRec[11]))
        similarity13 = 100.0 - abs(percentChange(eachPattern[12], patForRec[12]))
        similarity14 = 100.0 - abs(percentChange(eachPattern[13], patForRec[13]))
        similarity15 = 100.0 - abs(percentChange(eachPattern[14], patForRec[14]))
        similarity16 = 100.0 - abs(percentChange(eachPattern[15], patForRec[15]))
        similarity17 = 100.0 - abs(percentChange(eachPattern[16], patForRec[16]))
        similarity18 = 100.0 - abs(percentChange(eachPattern[17], patForRec[17]))
        similarity19 = 100.0 - abs(percentChange(eachPattern[18], patForRec[18]))
        similarity20 = 100.0 - abs(percentChange(eachPattern[19], patForRec[19]))

        similarity21 = 100.0 - abs(percentChange(eachPattern[20], patForRec[20]))
        similarity22 = 100.0 - abs(percentChange(eachPattern[21], patForRec[21]))
        similarity23 = 100.0 - abs(percentChange(eachPattern[22], patForRec[22]))
        similarity24 = 100.0 - abs(percentChange(eachPattern[23], patForRec[23]))
        similarity25 = 100.0 - abs(percentChange(eachPattern[24], patForRec[24]))
        similarity26 = 100.0 - abs(percentChange(eachPattern[25], patForRec[25]))
        similarity27 = 100.0 - abs(percentChange(eachPattern[26], patForRec[26]))
        similarity28 = 100.0 - abs(percentChange(eachPattern[27], patForRec[27]))
        similarity29 = 100.0 - abs(percentChange(eachPattern[28], patForRec[28]))
        similarity30 = 100.0 - abs(percentChange(eachPattern[29], patForRec[29]))


        howSimilar = (similarity1+similarity2+similarity3+similarity4+similarity5+similarity6+similarity7+similarity8+similarity9+similarity10+
                      similarity11+similarity12+similarity13+similarity14+similarity15+similarity16+similarity17+similarity18+similarity19+similarity20+
                      similarity21+similarity22+similarity23+similarity24+similarity25+similarity26+similarity27+similarity28+similarity29+similarity30)/30.00

        if howSimilar > 65:
            patdex = patternAr.index(eachPattern)

            patFound = 1

            '''print('##########')
            print(patForRec)
            print('==========')
            print(eachPattern)
            print('==========')
            print('predicated outcome',performanceAr[patdex])'''
            xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]
            plotPatAr.append(eachPattern)

    predAr = []
    if patFound == 1:
        #fig = plt.figure(figsize = (10,6))

        for eachPat in plotPatAr:

            futurePoints= patternAr.index(eachPat)

            if performanceAr[futurePoints] > patForRec[29]:
                pcolor = '#24bc00'
                predAr.append(1.00)

            else:
                pcolor = '#ff0000'
                predAr.append(-1.000)
            
            #plt.plot(xp, eachPat)
            predictedOutcomeAr.append(performanceAr[futurePoints])
            
            #plt.scatter(35, performanceAr[futurePoints], c=pcolor, alpha = .3)

        realOutcomeRange = allData[toWhat+20:toWhat+30]
        realAvgOutcome = reduce(lambda x, y: x+y, realOutcomeRange) / len(realOutcomeRange)
        realMovement = percentChange(allData[toWhat], realAvgOutcome)
        predictedAvgOutcome = reduce(lambda x, y: x+y, predictedOutcomeAr) / len(predictedOutcomeAr)

        print(predAr)
        predictionAvg = reduce(lambda x, y: x+y, predictedOutcomeAr) / len(predictedOutcomeAr)


        print(predictionAvg)
        if predictionAvg < 0:
            print('drop predicted')
            print(patForRec[29])
            print(realMovement)
            if realMovement < patForRec[29]:
                accuracyAr.append(100)
            else:
                accuracyAr.append(0)

        if predictionAvg > 0:
            print('rise predicted')
            print(patForRec[29])
            print(realMovement)
            if realMovement > patForRec[29]:
                accuracyAr.append(100)
            else:
                accuracyAr.append(0)
                
        #plt.scatter(40,realMovement, c='#54fff7')
        #plt.scatter(40, predictedAvgOutcome, c='b')
        
        #plt.plot(xp, patForRec, '#54fff7', linewidth = 3)
        #plt.grid(True)
        #plt.title('Pattern Recognition')
        #plt.show()
        #generate similar patterns and print them out and predicted outcome
    
def graphRawFX():
    
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0,), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)
    #SPREAD
    plt.subplots_adjust(bottom=.23)
    plt.show()


dataLength = int(bid.shape[0])
print('data length is',dataLength)

toWhat = 3700
allData = ((bid+ask)/2)

avgLine = ((bid+ask)/2)


patternAr = []
performanceAr = []
patternStorage()

accuracyAr = []

samps = 0
while toWhat < dataLength:
    
    avgLine = avgLine[:toWhat]
    
    
    patForRec = []
    
    
    currentPattern()
    patternRecognition()
    totalTime = time.time() - totalStart
    print('entire processing time took', totalTime, 'seconds')
    moveOn = input('press enter to continue...')

    samps +=1
    
    toWhat +=1
    accuracyAvg = reduce(lambda x, y: x + y, accuracyAr) / len(accuracyAr)
    
    print('Backtested Accuracy is', str(accuracyAvg)+'% after',samps,'samples')
