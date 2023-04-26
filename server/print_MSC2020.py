import fileinput
def print_msc2020(lst,msc_array):
    if len(lst) == 0:
        print("Alert! : Please include words that are characteristic of the sentence.")
    else:
        for line in lst:
            (msc_num, num) = line
            msc_name = msc_array[msc_array[:,0] == msc_num][1]
            sentence = str(msc_num) +' : ' + str(msc_name) + ' (The frequency is '+ str(num) + '.)'
            print(sentence)