

# SECTION 1 ===================================================

##open file for reading
##create try-except fields to catch errors such as:
##file not present, wrong data format, file too big, etc.


def main():

    try:
        
        records_file = open('RECORD_NAME.TXT', 'r')
        file_contents = records_file.read()
        records_file.close()

    except IOError:
        print('An error occured trying to read the file.)
    except FileNotFoundError:
        print('The file was not found.)
    except:
        print('Error has occurred.')

# SECTION 2 ===================================================

##file will print statistics about the dataset including the amount, order ID, and index number or order date

##record with the highest total profit

##record with the lowest total profit

##list of 10 highest total profit orders 

##list of 10 lowest total profit orders 


# SECTION 3 ===================================================

##create a dictionary

##prompt user for Order ID (key) and if found print record (value)
##if record is not found provide default message: ORDER ID NOT FOUND

##create proper input validation loops to catch any errors


# SECTION 4 ===================================================

##creating objects from records, putting them into lists, and serializing them

##create a class with the following attributes: ORDER ID, SHIP DATE, TOTAL PROFIT

##object is read only and thus provides only accessor methods
##object provides __str__

##create 100 instances for the first 100 records

##add instances to a list and serialized to file “RECORD_OBJECTS.DAT”

##deserialize objects from file
##and display the 10th object
