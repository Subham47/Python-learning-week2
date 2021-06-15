def problem2_8(temp_list):
    sum=0
    for i in temp_list:
        sum=sum+i;
    avg=sum/len(temp_list)
    print("Average:",avg)
    print("High:",max(temp_list))    
    print("Low:",min(temp_list))