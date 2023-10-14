def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open('data01.txt',"r")
    data = f.read().split(",")
   
    return data
    # for i in data:
    #     l.append(str(i))
    #     return l
print(main("data01.txt"))