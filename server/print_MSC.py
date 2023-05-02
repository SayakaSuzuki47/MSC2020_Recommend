import fileinput
def print_msc(lst,msc_array):
    try:
        if len(lst) == 0:
            raise ValueError("Alert! : Please include words that are characteristic of the sentence.")
    except ValueError as e:
        print(e)
        return
    for line in lst:
        (msc_num, num) = line
        msc_num_lst = msc_array[msc_array[:,0] == msc_num]
        if len(msc_num_lst)>0:
            msc_name =  msc_num_lst[0][1]
            sentence = str(msc_num) +' : ' + str(msc_name) + ' (The frequency is '+ str(num) + '.)'
            print(sentence)
