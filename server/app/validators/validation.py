import re   
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check_email(email):   
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      

# from server.app.validators.validation import *
#     signup_schema = {'require_all': True,
#         'email':{'type':'string', 'check_with': check_email},
#         'name':{'type':'string'},
#         'password':{'type':'str'}
#     }