import pandas as pd

def challenge1():
    dataFrame = pd.read_csv('2006_-_2011_NYS_Math_Test_Results_by_Grade_-_Citywide_-_by_Race-Ethnicity.csv')

    scores = dataFrame['Mean Scale Score'].get_values()
    tested = dataFrame['Number Tested'].get_values()
    dataFrame['Number Tested + Mean Scale Score'] = scores + tested

    dataFrame = dataFrame.sort_index(axis=1)
    columnNames = dataFrame.columns.get_values()
    print('Alphabetically Sorted Column Names:\n')

    for name in columnNames:
        print(name)

    numRows = dataFrame.shape[0]
    rowString = '\nNumber of rows in csv file = '
    print rowString, numRows

    dataFrame.to_csv('newFile.csv', index=False)
    print('New data file has been written')
