# !/usr/bin/python3
# -*- coding: utf-8 -*

class Data_Beer(object):
    """
    contains all the necessary data of a beer
    """
    name = ""
    percentage = 0
    bitterness = 0
    reference = 0
    description = ""
    style = ""
    brewer = ""
    country = ""
    website = ""

    def __init__(self, name, percentage, bitterness, reference, description, style, brewer, country, website):
        self.name = name

        # percentage
        val = str(percentage).encode('utf-8')
        try:
            self.percentage = float(val)
        except ValueError:
            print("Error : No value found for the 'Alcohol By Volume' of '"+name+"' in the csv file, 0.0 was put as default")
            self.percentage = 0.0

        # bitterness
        val = str(bitterness).encode('utf-8')
        try:
            self.bitterness = int(val)
        except ValueError:
            print("Error : No value found for the 'International Bitterness Units' of '"+name+"' in the csv file, 0 was put as default")
            self.bitterness = 0

        # reference
        val = str(reference).encode('utf-8')
        try:
            self.reference = int(val)
        except ValueError:
            print("Error : No value found for the 'Standard Reference Method' of '"+name+"' in the csv file, 0 was put as default")
            self.reference = 0

        self.description = description
        self.style = style
        self.brewer = brewer
        self.country = country
        self.website = website
