from c302.NeuroMLUtilities import ConnectionInfo
from c302.NeuroMLUtilities import analyse_connections

from xlrd import open_workbook
import os

spreadsheet_location = os.path.dirname(os.path.abspath(__file__))+"/data/"

from c302 import print_

def read_data(include_nonconnected_cells=False, neuron_connect=False):

    if neuron_connect:
        conns = []
        cells = []
        filename = "%s8_adult.xls"%spreadsheet_location
        rb = open_workbook(filename)
        print_("Opened the Excel file: " + filename)

        for row in range(1,rb.sheet_by_index(0).nrows):
            pre = str(rb.sheet_by_index(0).cell(row,0).value)
            post = str(rb.sheet_by_index(0).cell(row,1).value)
            syntype = rb.sheet_by_index(0).cell(row,2).value
            num = int(rb.sheet_by_index(0).cell(row,3).value)
            

            conns.append(ConnectionInfo(pre, post, num, syntype))
            if pre not in cells:
                cells.append(pre)
            if post not in cells:
                cells.append(post)

        return cells, conns

    else:
        conns = []
        cells = []
        filename = "%s8_adult.xls"%spreadsheet_location
        rb = open_workbook(filename)

        print_("Opened Excel file..: " + filename)

        known_nonconnected_cells = ['CANL', 'CANR', 'VC6']


        for row in range(1,rb.sheet_by_index(0).nrows):
            pre = str(rb.sheet_by_index(0).cell(row,0).value)
            post = str(rb.sheet_by_index(0).cell(row,1).value)
            syntype = rb.sheet_by_index(0).cell(row,2).value
            num = int(rb.sheet_by_index(0).cell(row,3).value)

            conns.append(ConnectionInfo(pre, post, num, syntype))
            if pre not in cells:
                cells.append(pre)
            if post not in cells:
                cells.append(post)

        if include_nonconnected_cells:
            for c in known_nonconnected_cells: cells.append(c)

        return cells, conns


def read_muscle_data():

    conns = []
    neurons = []
    muscles = []

    filename = "%s8_adult.xls"%spreadsheet_location
    rb = load_workbook(filename)

    print_("Opened Excel file: "+ filename)

    sheet = rb.sheet_by_index(1)

    for row in range(1,sheet.nrows):
        pre = str(sheet.cell(row,0).value)
        post = str(sheet.cell(row,1).value)
        syntype = 'Send'
        num = int(sheet.cell(row,2).value)

        conns.append(ConnectionInfo(pre, post, num, syntype))
        if pre not in neurons:
            neurons.append(pre)
        if post not in muscles:
            muscles.append(post)


    return neurons, muscles, conns



def main():

    cells, neuron_conns = read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

if __name__ == '__main__':

    main()

