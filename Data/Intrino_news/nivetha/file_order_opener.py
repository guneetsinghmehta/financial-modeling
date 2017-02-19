from __future__ import print_function
import os

files_list = []
def get_uniq_stock_names():
    global files_list
    files_list = os.listdir(".")
    files_list.sort()
    stock_names = [x.split("_")[0] for x in files_list]
    return set(stock_names)


def file_open_order():
    global files_list
    done_file_holder = open("done_files.txt", "r")
    done_files = [line.strip() for line in done_file_holder.readlines()]
    # return done_files
    # files_list = os.listdir(".").sort()
    stock_names = get_uniq_stock_names()
    stock_file_mapper = {}
    for file_name in files_list:
        stock_name = file_name.split("_")[0]
        # print(stock_file_mapper[stock_name])
        if not stock_file_mapper.has_key(stock_name):
            stock_file_mapper[stock_name] = []
        if file_name not in done_files:
            stock_file_mapper[stock_name].append(file_name)
    # for key,value in stock_file_mapper:
    with open("read_order", "w") as f:
        while True:
            changed = False
            for stock_name in stock_names:
                if len(stock_file_mapper[stock_name]) != 0:
                    # last_file = stock_file_mapper[stock_name].pop()
                    print(stock_file_mapper[stock_name].pop(), file=f)
                    changed = True
            # print("changed ", changed)
            if not changed:
                break

if __name__ == '__main__':
    file_open_order()
    # a = file_open_order()
    # print 'AAPL_16.txt' in a
