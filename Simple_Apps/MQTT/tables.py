# places data into table form
# must use pretty-tables from https://pypi.org/project/pretty-tables/

from prettytable import PrettyTable


def add_to_table(average_list):
    table = PrettyTable()
    table.add_column("Time Amount", ["one minute", "five minute", "thirty minute"])
    table.add_column("Average", [average_list[0], average_list[1], average_list[2]])
    return table
