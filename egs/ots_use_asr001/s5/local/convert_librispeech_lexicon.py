import os
Vowels = ['AH0', 'AH1', 'AH2', 
        'AA0','AA1','AA2',
        'AE0','AE1', 'AE2',
        'EH0','EH1','EH2',
        'ER0','ER1','ER2',
        'IH0','IH1','IH2',
        'IY0','IY1','IY2',
        'AO0','AO1','AO2',
        'UH0','UH1','UH2',
        'UW0','UW1','UW2',
        'AY0','AY1','AY2',
        'EY0','EY1','EY2',
        'OY0','OY1','OY2',
        'AW0','AW1','AW2',
        'OW0','OW1','OW2']


dict_map = {"AH0":"@0",
        "AH1":"V1",
        "AH2":"V2",
        "AA0":"A0",
        "AA1":"A1",
        "AA2":"A2",
        "AE0":"{0",
        "AE1":"{0",
        "AE2":"{2",
        "ER0":"@`0",
        "ER1":"3`1",
        "ER2":"3`2",
        "IH0":"I0",
        "IH1":"I1",
        "IH2":"I2",
        "IY0":"i0",
        "IY1":"i1",
        "IY2":"i2",
        "AO0":"O0",
        "AO1":"O1",
        "AO2":"O2",
        "UH0":"U0",
        "UH1":"U1",
        "UH2":"U2",
        "UW0":"u0",
        "UW1":"u1",
        "UW2":"u2",
        "AY0":"aI0",
        "AY1":"aI1",
        "AY2":"aI2",
        "EY0":"eI0",
        "EY1":"eI1",
        "EY2":"eI2",
        "OY0":"OI0",
        "OY1":"OI1",
        "OY2":"OI2",
        "AW0":"aU0",
        "AW1":"aU1",
        "AW2":"aU2",
        "OW0":"oU0",
        "OW1":"oU1",
        "OW2":"oU2",
        "P":"p",
        "B":"b",
        "D":"d",
        "K":"k",
        "G":"g",
        "CH":"tS",
        "JH":"dZ",
        "F":"f",
        "V":"v",
        "TH":"T",
        "DH":"D",
        "S":"s",
        "Z":"z",
        "SH":"S",
        "ZH":"Z",
        "HH":"h",
        "M":"m",
        "N":"n",
        "NG":"N",
        "R":"r",
        "L":"l",
        "Y":"j",
        "W":"w"
        }

librispeech_lexicon = '/home/ubuntu/src/kaldi/egs/ots_use_asr001/s5/local/librispeech-lexicon.txt'
fid  = open(librispeech_lexicon)
all_lexicon = fid.readlines()
fid.close()

for ln in all_lexicon:
    temp = ln.strip().split('\t')
    temp2= temp[1].split(' ')
    new_lex = []
    intervocalic = False
    if "T" in temp2:
        for i in range(len(temp2)):
            if (i ==0) and (temp2[i]== "T"):
                intervocalic = False
            elif (i == len(temp2)-1) and (temp2[i]== "T"):
                intervocalic = False
            elif temp2[i] == "T":
                if (temp2[i-1] in Vowels) and (temp2[i+1] in Vowels):
                    intervocalic = True
                    #print(ln.strip())
                    break;
            else:
                continue
    for i in range(len(temp2)):
        if ("EH" in temp2[i]):
            if (i+1)<= (len(temp2)-1):
                if (temp2[i+1]== "R") :
                    new_lex.append(temp2[i].replace("EH","E:"))
                    continue
                else:
                    new_lex.append(temp2[i].replace("EH","E"))
                    continue
            else:
                new_lex.append(temp2[i].replace("EH","E"))
                continue
        elif ("T" == temp2[i]):
            if intervocalic:
                new_lex.append("4")
            else:
                new_lex.append("t")
        else:
                new_lex.append(dict_map[temp2[i]])
    print(ln.strip())
    print(' '.join(new_lex))
    print('\n')            
  #      print(dict_map[temp2[i]])
    
    #print('\n')        

