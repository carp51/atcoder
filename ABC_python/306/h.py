import sys, csv
from collections import defaultdict

def main(lines):
    branches = defaultdict(list)
    prefectures_list = []
    branches_money = defaultdict(int)
    prefectures_money = defaultdict(int)
    Nationwide_money = 0
    
    for line in enumerate(lines):
        line = line[1]
        
        if not line[0] in prefectures_list:
            prefectures_list.append(line[0])
        
        if not line[1] in branches[line[0]]:
            branches[line[0]].append(line[1])
        
        branches_money[(line[0], line[1])] += int(line[2])
        prefectures_money[line[0]] += int(line[2])
        
    for prefecture in prefectures_list:
        if prefectures_money[prefecture] == 0:
            continue
        
        print("*", prefecture)
        
        for branch in branches[prefecture]:
            print(branch, branches_money[(prefecture, branch)])
            
        Nationwide_money += prefectures_money[prefecture]
        
        print(f'{prefecture}合計 {prefectures_money[prefecture]}')
        
    print(f'全国合計 {Nationwide_money}')

if __name__ == '__main__':
    lines = []
    with open('01.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            lines.append(row)
    main(lines)