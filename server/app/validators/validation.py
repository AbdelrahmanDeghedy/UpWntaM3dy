import re   

def check_email(field, value, error):   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(not re.search(regex,value)):   
        error(field, "Invalid Email")
      
def check_tags(field, value, error):
    regex = '\w+(\s*,\s*\w+)*'
    if(not re.search(regex,value)):   
        error(field, "Valid Tags")