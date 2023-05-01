import fileinput
def print_msc2020(lst,msc_array):
    try:
        len(lst) == 0
    except ValueError:
        print("Alert! : Please include words that are characteristic of the sentence.")
    for line in lst:
        (msc_num, num) = line
        msc_name = msc_array[msc_array[:,0] == msc_num][0][1]
        if len(msc_name)>0:
            sentence = str(msc_num) +' : ' + str(msc_name) + ' (The frequency is '+ str(num) + '.)'
            print(sentence)