#!/usr/bin/python
import pprint
# v1, no dicts
# with open("scores.txt", "r") as file:
#     filetext = file.readlines()
#     resultlist = []
#     for line in filetext:
#         resultlist.append(line.strip().split(":"))  # get rid of \n

#     sortedlist = sorted(resultlist)
#     for item in sortedlist:
#         print "Restaurant1 '%s' is rated at %s." % (item[0], item[1]) 


# # v2
# with open("scores.txt", "r") as file:
#     filetext = file.readlines()
#     resultlist = []
#     for line in filetext:
#         resultlist.append(line.strip().split(":"))  # get rid of \n

#     resultdict = {}
#     for item in resultlist:
#         #print "Restaurant '%s' is rated at %s" % (item[0], item[1]) 
#         resultdict[item[0]] = item[1] 

#     for item in resultdict:
#         print "Restaurant2 '%s' is rated at %s." % (item, resultdict[item])   

# v3

f = open("scores.txt")
text_list = f.read().strip().split("\n")
name_dict = {}

for item in sorted(text_list):
    name = item.split(":")[0]
    number = item.split(":")[1]
    name_dict[name] = number
    #print "Restaurant3 '%s' is rated %s." % (name, number)

#print name_dict


# extra cred, play with sorting the dict

value_dict = {}
for key, value in name_dict.items():
    value_dict[value] = []

#print value_dict

for key, value in name_dict.items():
    value_dict[value] += [key]


for key in sorted(value_dict, reverse=True):
    print (key, sorted(value_dict[key]))


