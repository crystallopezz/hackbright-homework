def sales_report(report):

    """Generate sales report showing total melons each salesperson sold."""

#create empty lists to store salespeople and melons sold
    salespeople = []
    melons_sold = []

#open up the sales report
    f = open('sales-report.txt')

#go through each line in the report
    for line in f:
    #strip any whitespace at the end of the line
        line = line.rstrip()
    #create a list of each item in the line separated by |
        entries = line.split('|')

    #find the salesperson and number of melons they sold
        salesperson = entries[0]
        melons = int(entries[2])

    #add up how many melons the person sold

    #if the person is in the salespeople list, find what position they are
    #in the list. That position should correspond with an item in the 
    #melons_sold list that is the total # of melons the person sold
    #add the number sold in the current line to the total number of melons sold
        if salesperson in salespeople:
            position = salespeople.index(salesperson)

            melons_sold[position] += melons
    

    #if this is the first line where we encountered the salesperson, then add
    #their name to the salespeople list and add the number of melons sold to the
    #melons_sold list
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)

#for each salespoerson print out "[salesperson] sold [number] melons"
    for i in range(len(salespeople)):
        print(f'{salespeople[i]} sold {melons_sold[i]} melons')



        # improvements:

        # make a dictionary of salespeople where the keys are the salespeople
        # and the values are another dictionary where key = melons_sold and 
        # value = the number of melons sold

        # on each line, find if the salesperson's name exists in the dictionary,
        # if it doesn't, create a key for the salesperson and make the value the 
        # number of melons sold from that line.

        # if the salesperson's name does exist, add the number of melons sold
        # on current line to total

        #tldr: use a dictionary instead of parallel lists