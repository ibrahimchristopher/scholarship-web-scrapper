import json
#access last loaded page
try:
        file = 'last_seen.json'
        with open(file) as f:
                last_seen = json.load(f)

except:
        last_seen = [6,1]

last_page = last_seen[0]
last_article = last_seen[1]
#brings out the desried scholarship dictionary
try:
        file = 'desired_scholarship.json'
        with open(file) as f:
                desired_scholarship = json.load(f)
except:
        desired_scholarship = []

def save_scholarship():
        #saves desired scholarship to file

    file = 'desired_scholarship.json'
    with open(file,'w') as f:
        json.dump(desired_scholarship,f)

                
for i in range(last_page ,38):
        #saves page currently on as last page
    last_page = i
    flag = 'n'
    #print page number and access page file
    print(f'page {i}')
    file = f'scholarship_page_{i}.json'
    
    with open(file) as f:
        scholarships = json.load(f)
        for scholarship in scholarships:
                if last_article > (scholarships.index(scholarship) + 1):
                        continue

                last_seen = [last_page,(scholarships.index(scholarship) + 1)]
                last_article = last_seen[1]
                file = 'last_seen.json'
                with open(file,'w') as f:
                        json.dump(last_seen,f)

                print(scholarships.index(scholarship) + 1)
                print(scholarship[0][0])
                print(scholarship[0][1])
                pause = input('press enter to continue:')
                line = 0
                for text in scholarship[1]:
                        print(text)
                        line += 1
                        if line % 7 == 0:
                                pause = input(':')

                decide = input('input:\n s to select\n d to decline \n q to save and quit:')
                #decide = 'd'
                if decide == 's':
                        desired_scholarship.append(scholarship)
                        save_scholarship()
                
                elif decide == 'd':
                        pass
                elif decide == 'q':
                        flag = 'q'
                        break
        last_article =  1
        if flag == 'q':
                break
print('the end')
