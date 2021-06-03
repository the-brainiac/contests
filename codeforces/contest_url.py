import requests

url = 'https://codeforces.com/contest/'
contest = input('Enter contest number: ').strip()
url += contest + '/problem/'
folder = input('Enter folder name: ').strip()
for i in 'ABCDE':
    try:
        response = requests.get(url+i)

        s = response.text
        idx1 = s.index('class="input"')
        idx2 = s.index('class="output"')
        inp = s[idx1:idx2].split('\n')[1:-1]
        f = open(f'{folder}/input_{i}.txt', 'w')
        f.write('\n'.join(inp))
        f.close()        
    except:
        break
