import csv
categoryMap = {'Mortgage and Loans': 'Mortgage Payment', 'Rent': 'Rents'}
print(categoryMap.keys())
print(categoryMap.get('Mortgage and Loans'))
with open('C:/Users/mohan/OneDrive/Documents/Real Estate/Rentals/Property Docs/Stessa/Oct2021/TC-Sep-Oct-2021-4.csv', newline='') as csvfile:
    with open('C:/Users/mohan/OneDrive/Documents/Real Estate/Rentals/Property Docs/Stessa/Oct2021/StessUploadFile-1.csv', 'w', newline='') as writeFile:
        outputCsvWriter = csv.writer(writeFile, delimiter=',', quoting=csv.QUOTE_NONE)
        #csvReader = csv.reader(csvfile, delimiter='\t')
        csvReader = csv.reader(csvfile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                print(f'Column names are {", ".join(row)}')
                lineCount += 1
                outputCsvWriter.writerow(['Date','Amount','Payee','Description','Category','Property','Unit'])
            else:
                if len(row) == 15 and row[13] == 'paid':
                    category = row[3] if row[4] == '-' else row[4]
                    category = categoryMap.get(category) if category in categoryMap.keys() else category
                    lineCount += 1
                    amount = '-'+row[9] if row[11] == 'Expense' else row[9]
                    address = row[6] + ' #' + row[7] if row[7] != '-' else row[6]
                    address = 'AALM''s Porfolio' if address == '-' else address
#                    print(f'{row[2].split()[0]},{amount},{row[5]},{row[14]},{category},{row[6]},{row[7]}')
                    fields = [row[2].split()[0], amount, row[5].replace(',', ''), row[14].replace(',', '').replace('\n',''), category,
                              address, row[7]]
                    print(fields)
                    outputCsvWriter.writerow(fields)
                else:
                    print(row[13])
                    print(f'error line - handle manually {row}')
print(f'Processed {lineCount} lines.');

#Change to Mortgage Payment