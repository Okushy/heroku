# -*- coding:utf-8 -*- 
#!/usr/bin/python

"""
subtitle.py
.txt形式の脚本をcsv形式のファイルに変換する
"""
import sys
import re

characters = ["ペンギン","パンダ","上司"]

def convert_txt_csv(filename, lines):
    f = open(filename + '.csv', 'w')
    
    #make 1st line
    header_columns = []
    header_columns.append("id")
    header_columns.append("text")
    header_columns.append("title")
    header_columns.append("subtitle")
    header_columns.append("penguin")
    header_columns.append("panda")
    header_columns.append("joushi")
    dict = {}
    for character in characters:
        dict[character] = "FALSE"
    f.write(",".join(header_columns) + "\n")
    
    #make 2nd~ line
    id = 0
    for line_index, line in enumerate(lines):
        print(line_index)
        if line == "":
            continue
        else:
            columns = []
            columns.append(str(id))
            id += 1
            
            #convert subtitle
            if line.find("##") != -1:
                columns.append(line)
                columns.append("FALSE")
                columns.append("TRUE")
                for index,character in enumerate(characters):
                    columns.append("FALSE")
                    dict[characters[index]] = "FALSE"
                f.write(",".join(columns) + "\n")
                continue
                    
            #convert title
            elif line.find("#") != -1:
                columns.append(line)
                columns.append("TRUE")
                columns.append("FALSE")
                for index,character in enumerate(characters):
                    columns.append("FALSE")
                    dict[characters[index]] = "FALSE"
                f.write(",".join(columns) + "\n")
                continue
                
            elif line.find("（") != -1 and line.find("）") != -1:
                continue

            else:
                for index,character in enumerate(characters):
                    if line.find(character) == 0:
                        words = re.split(" +", line)
                        columns.append(words[1])
                        columns.append("FALSE")
                        columns.append("FALSE")
                        for key, value in dict.items():
                            if key == character:
                                dict[key] = "TRUE"
                                columns.append("TRUE")
                            else:
                                dict[key] = "FALSE"
                                columns.append("FALSE")                        
                        f.write(",".join(columns) + "\n")
                        break
                else:
                    words = re.split(" +", line)
                    columns.append(words[1])
                    columns.append("FALSE")
                    columns.append("FALSE")
                    for value in dict.values():
                        columns.append(value)
                    f.write(",".join(columns) + "\n")
                    continue


if __name__ == '__main__':
    filename = sys.argv[1]

    lines = [line.rstrip('\n') for line in open(filename)]
    convert_txt_csv(filename, lines)
