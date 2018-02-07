<<<<<<< HEAD
import csv
from io import StringIO
import glob

filename_list = []
team_name = ""
camel_count = 0
filename = ""

def main():
    collect_all_csv_filenames()

    write_file = open("everyone.csv","w")
    global filename

    for filename in filename_list:
        if filename != "mlp6.csv":
            csvfile = open(filename,"r")
            temp = list(csv.reader(csvfile,delimiter=","))
            global team_name
            team_name = temp[0][4]
            read_csv()
            write_file = open("everyone.csv","a")
            write_file.write(",".join(temp[0]))
            write_file.write("\n")
            write_file.close
            write_data()


    print(camel_count, "entries are in camel case!")

def collect_all_csv_filenames():
    global filename_list
    filename_list = glob.glob('*.csv')

def read_csv():
    global camel_count
    no_spaces = check_no_spaces()
    if no_spaces == False:
        print("Spaces in ", filename)
    camel_case = check_camel_case()
    if camel_case == True:
        print(filename, " did not use camel case.")
    else:    
        camel_count += 1


def write_data(type='json'):
    csvfile = open(filename,"r")
    temp = list(csv.reader(csvfile,delimiter=","))
    json_filename = filename.replace('.csv','.json')
    json_file = open(json_filename, "w")
    json_file.write(",".join(temp[0]))
    json_file.close

def check_no_spaces():
    no_spaces=True
    if " " in team_name:
        no_spaces=False
        if team_name[0] == " ":
            no_spaces=True    
    return no_spaces

def check_camel_case():
    return (team_name.islower() or team_name.isupper())
    

if __name__ == "__main__":
    main()

=======
def main():
    filenames = collect_csv_files()
    student_data = cat_data()
    write_data()

def collect_csv_files():
    pass

def cat_data():
    pass

def write_():
    # CSV or JSON
    pass

if __name__ == "__main__":
    main()
>>>>>>> dd610efb7fcafca5db60cd55f09fe3cda4a5ea87
