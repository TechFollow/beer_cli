# !/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import sys
from data_beer import Data_Beer as DB


def load_csv(file):
    """
    load a csv file as a list of data_beer objects
    :param file: input csv file
    :return: list of data_beer
    """
    beer_list = []
    dic = {}  # dictionary of the label index
    initialised = False
    with open(file, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for line in reader:
            if not initialised:
                "fill the dictionary with label and corresponding index"
                for i in range(len(line)):
                    if i == 0:  # the string of the first cell of the csv file is buggy
                        dic["Name"] = 0
                    else:
                        dic[line[i]] = i

                if True:  # TODO : test the presence of each used label in the dictionnary dic
                    initialised = True
                else:
                    print("Error, ___ is not labelled in this csv file)")
                    sys.exit(1)
            else:
                new_beer = DB(name=line[dic["Name"]],
                              percentage=line[dic["Alcohol By Volume"]],
                              bitterness=line[dic["International Bitterness Units"]],
                              reference=line[dic["Standard Reference Method"]],
                              description=line[dic["Description"]],
                              style=line[dic["Style"]],
                              brewer=line[dic["Brewer"]],
                              country=line[dic["Country"]],
                              website=line[dic["Website"]])
                beer_list.append(new_beer)
    return beer_list


def display(tab):
    for i in range(len(tab)):
        #print(str(i)+":\t"+tab[i][0])
        print(str(i)+": \t"+tab[i][0]+"\t\t\t(score of " + str(tab[i][1])+")")


def bitterest_beer(data_base):
    """
    :param data_base:
    :return: string
    """
    max=0
    name=""
    for i in range(len(data_base)):
        if data_base[i].percentage > max:
            name = data_base[i].name
    return name


def country_ranking_on_breweries_number(data_base):
    """
    make a ranking of countries based on their number of breweries
    :param data_base:
    :return: list of string
    """
    list_of_countries = []
    dic={}  # index are countries and values are set of breweries
    for beer in data_base:
        if beer.country not in dic.keys():
            dic[beer.country] = set()
        dic[beer.country].add(beer.brewer)

    # translate dictionary into a tuple (country,size of the set of brweries)
    for country in dic.keys():
        tup = (country, len(dic[country]))
        list_of_countries.append(tup)

    return sorted(list_of_countries, key=lambda elem: elem[1], reverse=True)



def style_ranking_on_references_number(data_base):
    """
    make a ranking of style based on their number of references
    :param data_base:
    :return: list of string
    """
    list_of_styles = []
    dic={}  # index are styles and values is the sum of references
    for beer in data_base:
        if beer.style not in dic.keys():
            dic[beer.style] = 0
        dic[beer.style] += beer.reference

    # translate dictionary into a tuple (style, number of references)
    for style in dic.keys():
        tup = (style, dic[style])
        list_of_styles.append(tup)

    return sorted(list_of_styles, key=lambda elem: elem[1], reverse=True)


def beer_ranking_on_alcohol(data_base):
    """
    make a ranking of beers based on their percentage of alcohol
    :param data_base:
    :return: list of string
    """
    list_of_beers = []
    for beer in data_base:
        tup = (beer.name, beer.percentage)
        list_of_beers.append(tup)

    return sorted(list_of_beers, key=lambda elem: elem[1], reverse=True)


def generate_csv(new_name, data_base):
    """
    generate a new csv file based of the old one,
    including : Name,Style,Brewery,Alcohol,IBU,Description,Country,Website
    :param new_name: name of the new file
    :param data_base:
    :return: void
    """
    file = open(new_name+'.csv', 'w')
    with file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Style', 'Brewery', 'Alcohol', 'IBU', 'Description', 'Country', 'Website'])
        for beer in data_base:
            try:
                writer.writerow([beer.name,
                                 beer.style,
                                 beer.brewer,
                                 beer.percentage,
                                 beer.bitterness,
                                 beer.description,
                                 beer.country,
                                 beer.website])
            except UnicodeEncodeError:
                print("Error : beer '"+beer.name+"' has non acceptable characters, so it was not retranscribed in the new database")
                # TODO : throw away only the corrupted parameter instead of the whole beer.


if len(sys.argv) != 2:
    print("Error, 1 argument expected (the name of the csv file)")
    sys.exit(1)

file_name = sys.argv[1]
if file_name[(len(file_name) - 4):] == ".csv":
    data_base = load_csv(file_name)

    print("\n\n The bitterest beer is " + bitterest_beer(data_base))

    print("\n\n Country ranking on breweries number :")
    display(country_ranking_on_breweries_number(data_base))

    print("\n\n Style ranking on references number :")
    display(style_ranking_on_references_number(data_base))

    print("\n\n Beer ranking on alcohol percentage :")
    display(beer_ranking_on_alcohol(data_base))

    generate_csv("nouvelle_BDD", data_base)

    sys.exit(0)


else:
    print("Error : the input file is not a CSV file")
    sys.exit(1)

