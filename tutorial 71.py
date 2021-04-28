# Date 16-4-2021

# Create a libarary class add the following functions to it :-
# 1.) display all books
# 2.) lend book (who had taken this book if it is not avaliable)
# 3.) add books
# 4.) return books (i.e. the person who had taken the book is returning it back to the libarary)
# 5.) Dictionary which shows who all are the person who had taken books from libarary with their name and date and time of book takened
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
# this project is not completed by me 
import calendar
import datetime
import time


def gettime():
    """This function will help you to get date and time
    by using this syntax -
    file1.write("["+str(gettime())+"]: "+lock+"\n")
    """
    return datetime.datetime.now()


def maintime():
    maintime_date = str(gettime())[0:10]  # This is current date
    maintime_time = str(gettime())[11:19]  # This is current time
    maintime_x = str(gettime())[0:10].split("-")
    # print(maintime_x[0])
    date = f"{maintime_x[2]} {maintime_x[1]} {maintime_x[0]}"
    # print(maintime_date)
    main_day = day(date)  # This is current day
    # print(main_day)
    return f"{maintime_date} {maintime_time} {main_day}"
    # return f"\u276EDate\u27F9  {maintime_date}\u276F \t\u276ETime\u27F9  {maintime_time}\u276F \t\u276EDay\u27F9  {main_day}\u276F"


def day(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


def choice():
    person_choice = str(input("What's your choice\u21B4\nPress \'B\' to know what all books we can give to someone.\nPress \'L\' to lend a book to someone.\nPress \'R\' if someone return you his lended book.\nPress \'D\' to know which book is taken by whom.\nPress \'A\' to add new books to our library.\n")).upper()
    if(person_choice == "B" or person_choice == "L" or person_choice == "R" or person_choice == "D" or person_choice == "A"):
        return person_choice
    else:
        print("\nPlease enter values in only \'B\', \'L\', \'R\', \'D\', \'A\'.\n")
        time.sleep(5)
        exit()


def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return line number of the given string"""
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    list_of_results_2 = str(list_of_results).split(",")
    list_of_results_3 = str(list_of_results_2[0])
    return list_of_results_3[2:]


cho = choice()
maintime_date_time = str(gettime())[0:19]

if(cho == "A"):
    with open("tutorial 71(all books).txt", "a") as bi:
        bi_1 = input("Please type the name of the book\u21B4\n").upper()
        bi_2 = f"\n{bi_1}\t We got book named {bi_1} on---> {maintime_date_time}"
        # print(bi_2)
        bi.write(bi_2)

if(cho == "B"):
    with open("tutorial 71(all books).txt", "r") as bo:
        print(f"\nOur library books are\u21B4\n{bo.read()}")


if(cho == "L"):
    with open("tutorial 71(lending).txt", "r") as bo:
        # print(f"\nOur library books are\u21B4\n{bo.read()}")
        bo_o = bo.read()
        book_name = input(
            "Please enter the name of the book you want to lend\u21B4\n").upper()

        with open("tutorial 71(all books).txt", "r") as file1:
            readfile = file1.read()

            if (book_name in readfile) and (book_name not in bo_o):
                # print("it s there 1")
                print(
                    f"Ok! you can take {book_name}\nThanks for choosing our library")
                with open("tutorial 71(lending).txt", "a") as bo_2:
                    bo_2_1 = input("Please enter your name\u21B4")
                    bo_2.write(
                        f"{book_name} is with {bo_2_1} taken on {maintime_date_time}\n")
            elif (book_name in readfile) and (book_name in bo_o):

                # print("it s there 2")
                bo_4 = search_string_in_file(
                    "tutorial 71(lending).txt", "book_name")
                with open("tutorial 71(lending).txt", "r") as bo_f1:
                    bo_f1_line = bo_f1.readlines()
                    # bo_f1_line=bo_f1_line[bo_4]
                    print(
                        f"The information about this book is\u21B4\n{bo_f1_line[bo_4]}")
            else:
                # print("it s there 3")
                print("Soory! but we does not own this book")





