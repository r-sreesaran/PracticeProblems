def convert(number):
    result = ""
    names = [[3,'Pling'],[5,'Plang'],[7,'Plong']]
    for no,name in names:
        if not int(number) % no:
            result += name
    if result=="": return f'{number}'
    return result
