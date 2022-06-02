from colorama import init, Fore, Back, Style
import os

init(autoreset = True)

def print_logo():
    os.system('clear')
    gr = Fore.GREEN
    print(Fore.YELLOW + ''' ____  ____  ____  ____  ____  ____ 
||''' + gr + '''t''' + Fore.YELLOW + ''' ||||'''  + gr + '''a''' + Fore.YELLOW + ''' ||||''' + gr + '''b''' + Fore.YELLOW + ''' ||||''' + gr + '''l ''' + Fore.YELLOW + '''||||''' + gr + '''e ''' + Fore.YELLOW + '''||||''' + gr + '''s''' + Fore.YELLOW + ''' ||
||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\|

          --------------------------
          |  id  |  name  |  tel
          --------------------------
          |  01  |  Ivan  |  +7(915)

 © 2022   nikolaysmirnov86@gmail.com
 ''')

def main_menu():
    new = Back.YELLOW + Fore.BLACK + 'n' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'ew'
    open = Back.YELLOW + Fore.BLACK + 'o' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'pen'
    exit = Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'e' + Style.RESET_ALL + Back.YELLOW + Fore.BLACK + 'x' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'it'
    list = Back.YELLOW + Fore.BLACK + 'l' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'ist'
    delete = Back.YELLOW + Fore.BLACK + 'd' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'el'
    print('\n' + new, open, list, exit, delete + '\n')

def open_menu():
    add = Back.YELLOW + Fore.BLACK + 'a' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'dd'
    save = Back.YELLOW + Fore.BLACK + 's' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'ave'
    exit = Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'e' + Style.RESET_ALL + Back.YELLOW + Fore.BLACK + 'x' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'it'
    delete = Back.YELLOW + Fore.BLACK + 'd' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'el'
    edit = Back.YELLOW + Fore.BLACK + 'e' + Back.BLACK  + Fore.YELLOW+ Style.BRIGHT + 'dit'
    print('\n' + add, edit, delete, save, exit + '\n')

def ls():
    os.system('ls *.txt')

def new_table(name):
    if os.path.isfile(name) == True:
        while True:
            acept = input(name + ' already exists, want to overwrite? (y/n) ').strip()
            if acept.lower() == 'y':
                os.system('touch ' + name)
                break
            elif acept.lower() == 'n':
                return
            else:
                print(Fore.RED + 'command not found')
    else:
        if os.system('touch ' + name) != 0:
            return print(Fore.RED + 'invalid filename')
    while True:
        try:
            columns = int(input('columns: ').strip())
            if type(columns) == int:
                break
        except:
            print('enter digit')
    cnt = 1
    list = []
    while cnt <= columns:
        list.append(input('column #' + str(cnt) + ': ').strip())
        cnt += 1
    with open(name, 'a') as f:
        f.write(' '.join(list))

def file_to_list(name):
    file = open(name, 'r')
    flist = []
    for line in file:
        flist.append(line.split())
    return flist

def delete():
    os.system('ls *.txt')
    name = input('\ndelete file name (c - cancel): ').strip()
    if name == 'c':
    	return
    os.system('rm ' + name + '.txt')

def add_row(flist):
    row = []
    index = input('after row (enter for add row to end): ').strip()
    if index.isdigit() == False and index != '' or index.isdigit() == True and int(index) > len(flist) - 1:
        print('invalid value')
        input()
        return flist
    elif index == '':
        index = str(len(flist))
    for key in flist[0]:
        value = input(key + ': ')
        if value == '':
            row.append('None')
        else:
            row.append(value)
    flist.insert(int(index) + 1, row)
    return flist

def save_table(fname, flist):
    with open(fname, 'w') as f:
        cnt = 0
        for line in flist:
            if cnt == 0:
                f.write(' '.join(line))
                cnt += 1
            else:
                f.write('\n' + ' '.join(line))
            

def exit_table(fname, flist, name):
    while True:
        if flist != file_to_list(fname):
            item = input('table ' + name + ' not saved! save table? (y/n)').strip()
            if item.lower() == 'y':
                save_table(fname, flist)
                return True
            elif item.lower() == 'n':
                return False
            else:
                print(Fore.RED + 'command not found')
        else:
            return

def print_table(flist):
    max_lens=[]
    for key in flist[0]:
        max_lens.append(len(key))
    for line in flist:
        index = 0
        for items in line:
            if len(items) > max_lens[index]:
                max_lens[index] = len(items)
            index += 1
    cnt = 0
    for line in flist:
        index = 0
        if cnt == 1:
            print('-' * (sum(max_lens) + len(max_lens) + 2 + len(str(len(flist))) - 1))
        if cnt == 0:
            print('#  '.rjust(2 + len(str(len(flist))), ' '), end ='')
        else:
            print((str(cnt) + '| ').rjust(2 + len(str(len(flist))), ' '), end ='')
        for i in line:
            if i == 'None':
                i = ''
            print(i.ljust(max_lens[index], ' '), end = ' ')
            index += 1
        print()
        cnt += 1
    print('-' * (sum(max_lens) + len(max_lens) + 2 + len(str(len(flist))) - 1))

def delete_row(flist):
    del_row = input('delete row:').strip()
    if del_row.isdigit() == False or del_row.isdigit() == True and int(del_row) > len(flist) - 1:
        print('invalid input')
        input()
        return flist
    del flist[int(del_row)]
    return flist

def edit_row(flist):
    ed_row = input('edit row: ').strip()
    #ed_row = ed_row.strip()
    if ed_row.isdigit() == False or ed_row.isdigit() == True and int(ed_row) > len(flist) - 1:
        print('invalid input')
        input()
        return flist
    index = 0
    print('"-" empty value, "enter" dont edit')
    for key in flist[0]:
        edit_val = input(key + ' ' + flist[int(ed_row)][index] + ' edit to: ')
        if edit_val == '-':
            flist[int(ed_row)][index] = 'None'
        elif edit_val == '':
            flist[int(ed_row)][index] = flist[int(ed_row)][index]
        else:
            flist[int(ed_row)][index] = edit_val
        index += 1
    return flist
        
def open_table(name):
    fname = name + '.txt'
    if os.path.isfile(fname) == False:
        print('file not found')
        input()
        return
    flist = file_to_list(fname)
    print_logo()
    while True:
        print('\ntable: ' + name)
        print('-' * (7 + len(name)))
        print_table(flist)
        print('columns: ' + str(len(flist[0])) + '  rows: ' + str(len(flist) - 1))
        open_menu()
        item = input('>')
        if item.lower() == 'a':
            flist = add_row(flist)
            print_logo()
        elif item.lower() == 's':
            print_logo()
            save_table(fname, flist)
            print('table ' + name + ' saved')
        elif item.lower() == 'x':
            bool = exit_table(fname, flist, name)
            print_logo()
            if bool == True:
                print('table ' + name + ' saved')
            elif bool == False:
                print('table ' + name + ' not saved')
            return
        elif item.lower() == 'd':
            flist = delete_row(flist)
            print_logo()
        elif item.lower() == 'e':
            flist = edit_row(flist)
            print_logo()
        else:
            print_logo()
            print(Fore.RED + 'command not found')

def main():
    print_logo()
    while True:
        main_menu()
        go = input('>').strip()
        if go.lower() == 'l':
            print_logo()
            ls()
        elif go.lower() == 'n':
            print_logo()
            new_table_name = input('new file name: ').strip()
            new_table(new_table_name + '.txt')
        elif go.lower() == 'd':
            print_logo()
            delete()
        elif go.lower() == 'o':
            print_logo()
            os.system('ls *.txt')
            open_table(input('\nname: '))
        elif go.lower() == 'x':
            exit()
        else:
            print_logo()
            print(Fore.RED + 'command not found')

main()