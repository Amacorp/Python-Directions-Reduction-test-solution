def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res
    
    
    
or


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
    
    
    
or



def dirReduc(arr):
    i = 1
    while i < len(arr) and len(arr) > 1:
        if sorted([arr[i], arr[i-1]]) in [["NORTH", "SOUTH"], ["EAST", "WEST"]]:
            del arr[i-1:i+1]
            i = 1
        else:
            i += 1
    return arr
