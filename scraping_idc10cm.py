from bs4 import BeautifulSoup
import urllib3


A = ['A','B','C']
B = ['01', '02', '03']
code = []
C = ['0', '1', '2', '3','4']
D = ['.0', '.1', ]
dd = []
for i in A:
    for x in B:
        code.append(i+x)
def check_code(idc):
    url = "https://www.icd10data.com/search?s={}&codebook=icd10cm".format(idc)
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, "html.parser")
    container = soup.find('div', class_='container vp')
    row = container.find('div', class_='row')
    disease = row.find('div', class_='searchPadded').text
    print(idc,  disease)

for i in code:

    try:
        check_code(i)
        for l in D:
            dd.append(i+l)
            for q in dd:
                check_code(q)


    except AttributeError:
        print(i)
