def work_with_phonebook():
  

    choice=show_menu()
    phone_book=read_txt('phonebook.txt')

    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))        
        elif choice==4:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6: 
            file_r = input('name file to read ')
            file_w = input('name file to write ')
            num = input('line number ')
            cope_file(file_r, file_w, num)
        choice=show_menu()
    write_txt('phonebook.txt',phone_book)

def print_result(pb):
    slav = ['last_name', 'name', 'number', 'comment']
    for a in slav:
        print(a.ljust(11), end = "")
    print()
    for i in pb:
        for a in slav:
            print(i.get(a).ljust(11), end = "")
        print()

def find_by_lastname(pb, lstn):
    res = []
    for i in pb:
        if i.get('last_name') == lstn:
            for key in i:
                res.append(i[key])
    return res 

def find_by_number(pb, num):
    res = []
    for i in pb:
        if i.get('number') == num:
            for key in i:
                res.append(i[key])
    return res

def change_number(pb,lstn,nn):
    res = []
    for i in pb:
        if i.get('last_name') == lstn:
            i['number'] = nn
            for key in i:
                res.append(i[key])
    return res 

def delete_by_lastname(pb, lstnm):
    for i in range(len(pb)):
        if pb[i].get('last_name') == lstnm:
            pb.pop(i)
            return
    
def cope_file(filename_r,filename_w,num_s):
    with open(filename_r,'r') as f_r:
        for i in range(int(num_s)+1):
            line = f_r.readline()
    with open(filename_w,'w') as f_w:
        f_w.write(line)

        

def show_menu():
    print("\n menu:\n"
          "1. out spravochnic\n"
          "2. find by lastname\n"
          "3. change number\n"
          "4. delete by lastname\n"
          "5. find by number\n"
          "6. copy to another file  \n"
          "7. exit")
    print(">>", end = " ")
    choice = int(input())
    return choice




def read_txt(filename): 
    phone_book=[]
    fields=['last_name', 'name', 'number', 'comment']
    with open(filename,'r') as pbh:
        for line in pbh:
            if line != '\n':
                li = []
                for x in line.split(','):
                    s = x
                    for a in [' ','\n','\t']:
                        s = s.replace(a,'')
                    li.append(s)            
                record = dict(zip(fields, li))
                phone_book.append(record)
    return phone_book



def write_txt(filename , phone_book):

    with open('phonebook.txt','w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')


work_with_phonebook()
