import sys 
import os

def scan_file(directory):
    """Mengecek semua letak file di directory"""
    file_path_list = []
    if directory.endswith('.txt'):
        file_path_list.append(directory)
    for root,dirs,files in os.walk(directory, topdown = True):
        for file in files:
            file_path = f"{root}\{file}"
            file_path_list.append(file_path)
    return file_path_list

def print_file(file_path,line_num,line):
    """Untuk mencetak satu baris yang match dengan pola string"""
    print(f"{file_path:<40} line {line_num:<3} {line[0:40]:<40}")

def option_checker():
    """Untuk mengecek opsi argument yang digunakan ( tanpa argument / -w / -i )"""
    if len(sys.argv) == 3 :
        return 'none'
    if len(sys.argv) == 4 and (sys.argv[1] == '-w' or sys.argv[1] == '-i'):
        return sys.argv[1]
    return ''

def check_input(option):
    """Fungsi ini akan mengecek opsi argument dan input untuk wildcard"""
    return not (option == '' or sys.argv[-2].count('*') > 1)

def is_wildcard(str_pattern):
    """Untuk mengecek apakah pola string yang menggunakan sebuah karakter (*)"""
    return str_pattern.count('*') == 1

def wildcard(str_pattern,checked_sentence):
    """Pengecekan string memakai wildcard.Pola string X*Y akan match dengan baris yang mengandung X kemudian 
    diikuti oleh beberapa karakter (boleh juga string kosong) dan diikuti lagi dengan Y"""
    
    parts = str_pattern.split('*')
    if parts[0] in checked_sentence:
        parts_1_index = checked_sentence.index(parts[0]) + len(parts[0])
        return parts[1] in checked_sentence[ parts_1_index : ]

def none_argument(checked_sentence):
    """Program akan melakukan proses pencarian pola string secara
    case sensitive sebagai substring ke string yang ingin dicek""" 
    
    if is_wildcard(sys.argv[1]):
        return wildcard(sys.argv[1],checked_sentence)
    return sys.argv[1] in checked_sentence 

def w_argument(checked_sentence):
    """Program akan melakukan proses pencarian pola string secara case sensitive sebagai sebuah kata penuh 
    (whole word) ke string yang ingin dicek.whole word adalah sebuah substring yang berbatasan langsung 
    dengan whitespace termasuk substring paling kiri dan kanan"""
    
    if is_wildcard(sys.argv[2]):
        return wildcard(' ' + sys.argv[2] + ' ',' ' + checked_sentence + ' ')
    return (' ' + sys.argv[2] + ' ') in (' ' + checked_sentence + ' ')

def i_argument(checked_sentence):
    """Program akan melakukan proses pencarian pola string secara case
    insensitive sebagai substring ke string yang ingin dicek"""
    
    if is_wildcard(sys.argv[2]):
        return wildcard(sys.argv[2].lower(),checked_sentence.lower())
    return (sys.argv[2]).lower() in checked_sentence.lower() 

if __name__ == '__main__':
    list_file_path = scan_file(sys.argv[-1])
    arg_option = option_checker()
    if check_input(arg_option):
        print("\n")
        try:
            for file_path in list_file_path:
                with open(file_path,'r') as file:
                    line_num = 1
                    for line in file :
                        line = line.strip()
                        if arg_option == 'none':
                            if none_argument(line):
                                print_file(file_path,line_num,line)
                        elif arg_option == '-w':
                            if w_argument(line):
                                print_file(file_path,line_num,line)
                        else:
                            if i_argument(line):
                                print_file(file_path,line_num,line)
                        line_num += 1
            if not (os.path.exists(sys.argv[-1])):
                print(f"Path <{sys.argv[-1]}> tidak ditemukan")
        except FileNotFoundError :
            print(f"Path <{sys.argv[-1]}> tidak ditemukan")
    else:
        print("\nArgumen program tidak benar")