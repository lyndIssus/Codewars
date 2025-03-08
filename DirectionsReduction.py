def dir_reduc(arr):
    newArr = arr
    for i in range(len(arr)-1):
        if(arr[i+1]=="NORTH" and arr[i]=="SOUTH") or (arr[i]=="NORTH" and arr[i+1]=="SOUTH") or (arr[i]=="EAST" and arr[i+1]=="WEST") or (arr[i]=="WEST" and arr[i+1]=="EAST"):
            newArr.pop(i)
            newArr.pop(i)
            return dir_reduc(newArr)
    return arr

a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]
print(dir_reduc(a))