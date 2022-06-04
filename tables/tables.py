from colorama import init, Fore, Back, Style
import os

init(autoreset=True)


def print_logo():
    os.system('clear')
    print(Fore.YELLOW + Style.BRIGHT + '''\n ____  ____  ____  ____  ____  ____ 
||t ||||a ||||b ||||l ||||e ||||s ||
||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\|

          --------------------------
          |  id  |  name  |  tel
          --------------------------
          |  01  |  Ivan  |  +7(915)

(c) 2022  nikolaysmirnov86@gmail.com
 ''')


def main_menu():
    byl = Back.YELLOW
    sra = Style.RESET_ALL
    fbc = Fore.BLACK
    fyl = Fore.YELLOW
    sbr = Style.BRIGHT
    new_t = byl + fbc + 'n' + sra + fyl + sbr + 'ew'
    open_t = byl + fbc + 'o' + sra + fyl + sbr + 'pen'
    exit_p = fyl + sbr + 'e' + sra + byl + fbc + 'x' + sra + fyl + sbr + 'it'
    list_t = byl + fbc + 'l' + sra + fyl + sbr + 'ist'
    delete_t = byl + fbc + 'd' + sra + fyl + sbr + 'el'
    print('\n' + new_t, open_t, list_t, exit_p, delete_t + Style.RESET_ALL + '\n')


def open_menu():
    byl = Back.YELLOW
    sra = Style.RESET_ALL
    fbc = Fore.BLACK
    fyl = Fore.YELLOW
    sbr = Style.BRIGHT
    add_row_t = byl + fbc + 'a' + sra + fyl + sbr + 'dd' + sra + byl + fbc + 'r' + sra + fyl + sbr + 'ow'
    add_col = byl + fbc + 'a' + sra + fyl + sbr + 'dd' + sra + byl + fbc + 'c' + sra + fyl + sbr + 'ol'
    save = byl + fbc + 's' + sra + fyl + sbr + 'ave'
    exit_t = fyl + sbr + 'e' + sra + byl + fbc + 'x' + sra + fyl + sbr + 'it'
    del_row = byl + fbc + 'd' + sra + fyl + sbr + 'el' + sra + byl + fbc + 'r' + sra + fyl + sbr + 'ow'
    del_col = byl + fbc + 'd' + sra + fyl + sbr + 'el' + sra + byl + fbc + 'c' + sra + fyl + sbr + 'ol'
    edit = byl + fbc + 'e' + sra + fyl + sbr + 'dit'
    help_m = byl + fbc + 'h' + sra + fyl + sbr + 'elp' + sra
    print('\n' + add_row_t, add_col, edit, help_m + '\n\n' + del_row, del_col, save, exit_t + '\n')


def ls():
    os.system('ls *.txt')


def new_table(name):
    if os.path.isfile(name):
        while True:
            accept = input(name + ' already exists, want to overwrite? (y/n) ').strip()
            if accept.lower() == 'y':
                os.system('touch ' + name)
                break
            elif accept.lower() == 'n':
                return
            else:
                print(Fore.RED + 'command not found')
    else:
        if os.system('touch ' + name) != 0:
            return print(Fore.RED + 'invalid filename')
    while True:
        try:
            columns = int(input('columns: ').strip())
            if columns == 0:
                print(Fore.RED + 'invalid value')
                continue
            if type(columns) == int:
                break
        except:
            print(Fore.RED + 'enter digit')
    cnt = 1
    list_columns = []
    while cnt <= columns:
        name_column = input('column #' + str(cnt) + ': ').strip()
        if name_column == '':
            print(Fore.RED + 'empty value')
            continue
        if name_column in list_columns:
            print(Fore.RED + 'column name already exists')
            continue
        list_columns.append(name_column)
        cnt += 1
    with open(name, 'a') as f:
        f.write(' '.join(list_columns))
    open_table(name[:-4])


def file_to_list(name):
    f = open(name, 'r')
    flist = []
    for line in f:
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
    if not index.isdigit() and index != '' or index.isdigit() and int(index) > len(flist) - 1:
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


def add_column(flist):
    pass


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
    max_lens = []
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
            print('#  '.rjust(2 + len(str(len(flist))), ' '), end='')
        else:
            print((str(cnt) + '| ').rjust(2 + len(str(len(flist))), ' '), end='')
        for i in line:
            if i == 'None':
                i = ''
            print(i.ljust(max_lens[index], ' '), end=' ')
            index += 1
        print()
        cnt += 1
    print('-' * (sum(max_lens) + len(max_lens) + 2 + len(str(len(flist))) - 1))


def delete_row(flist):
    del_row = input('delete row:').strip()
    if not del_row.isdigit() or del_row.isdigit() and int(del_row) > len(flist) - 1:
        print('invalid input')
        input()
        return flist
    del flist[int(del_row)]
    return flist


def delete_col(flist):
    while True:
        d_col = input('name column: ').strip()
        if d_col not in flist[0]:
            print(Fore.RED + 'column not found')
            continue
        ind = flist[0].index(d_col)
        break
    for line in flist:
        del line[ind]
    return flist


def edit_row(flist):
    ed_row = input('edit row: ').strip()
    if not ed_row.isdigit() or ed_row.isdigit() and int(ed_row) > len(flist) - 1:
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


def help_table():
    print('''ar - add row
ac - add column
e - edit row
dr - delete row
dc -delete column
s - save changes
x - exit''')
    input()


def open_table(name):
    fname = name + '.txt'
    if not os.path.isfile(fname):
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
        item = input('>').strip()
        if item.lower() == 'ar':
            flist = add_row(flist)
            print_logo()
        elif item.lower() == 'ac':
            flist = add_column(flist)
            print_logo()
        elif item.lower() == 's':
            print_logo()
            save_table(fname, flist)
            print('table ' + name + ' saved')
        elif item.lower() == 'x':
            choice = exit_table(fname, flist, name)
            print_logo()
            if choice:
                print('table ' + name + ' saved')
            elif not choice:
                print('table ' + name + ' not saved')
            return
        elif item.lower() == 'dr':
            flist = delete_row(flist)
            print_logo()
        elif item.lower() == 'dc':
            flist = delete_col(flist)
            print_logo()
        elif item.lower() == 'e':
            flist = edit_row(flist)
            print_logo()
        elif item.lower() == 'h':
            help_table()
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
