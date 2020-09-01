from pathlib import Path as ph
# import  


def check_file(file_name):
    file_checker = ph(file_name).exists()
    if(file_checker == True):
        print(f'Since file checker says  {file_checker} ,this spreadsheet file exists .... \n Processing....')  
    else:
        print("this file doesn't exits, to it cant be processed")



if __name__ == '__main__':
    check_file("transactions.xlsx")

