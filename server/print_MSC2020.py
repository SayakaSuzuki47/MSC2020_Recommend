import fileinput
def print_msc2020(lst,msc_array):
    try:
        len(lst) == 0
    except ValueError:
        print("Alert! : Please include words that are characteristic of the sentence.")
    for line in lst:
        (msc_num, num) = line
        msc_num_lst = msc_array[msc_array[:,0] == msc_num]
        if len(msc_num_lst)>0:
            msc_name =  msc_num_lst[0][1]
            sentence = str(msc_num) +' : ' + str(msc_name) + ' (The frequency is '+ str(num) + '.)'
            print(sentence)