import re
import StringIO

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

with open('/home/farhad/Downloads/data.json') as f:
    content = f.readline()
#val = [['' for i in range(8)] for j in range(10)]
content = [x.strip() for x in content]
line=""
content=""
pos=1
for y in range(560):#no of items(561 items) 
	    line=""
	    content=""
	    with open('/home/farhad/Downloads/data.json') as f:   
		f.seek(pos) 	        
		while True:		
			content = content + f.readline().strip()
			pos =  f.tell()	
			#print content
    			#content = [x.strip() for x in content]
			if "height" in content:
			    break
	    
	    a = re.split(r'\W', content)
	    num = a.count('left')
	    print "\n\n\n"
	    print num
	    line = content
	    #print line
	    line = line.strip()
	    line = line.strip('\n')
	    line = line.strip('\t')
	    line = line.replace('\r\n','')
	    line = line.replace('\t','')
	    print line

	    result = re.search('/(.*)":{"s', line)
	    name = result.group(1)
	    res0 = re.findall('"left":(.\d*),"right', line)
	    res1 = re.findall('"right":(.\d+),"top"', line)
	    res2 = re.findall('"top":(.\d*),"bottom"', line)
	    res3 = re.findall('"bottom":(\d+)', line)
	    if res1==[]:
		res1=re.search('"bottom":(.*)', line).group(1)
			
	    res4 = re.search('"width":(.\d+),"height', line)
	    res5 = re.search('"height":(.\d+)', line)
	    width = res4.group(1)
	    height = res5.group(1)	    
	    print "\n"
	    for n in range(num):
		    #pos = find_nth(line,'left',n+1)
		
		    print res0
	 	    print res1
		    print res2
		    print res3
		    print res4.group(1)
		    print res5.group(1)
	    	    left = res0[n]
		    
		    right= res1[n]
		    
		    top = res2[n]
		    bottom = res3[n]
		    
		    #else: res2 = re.search('"bottom":(.\d+)}]}', line)		      
		    #print name+" Left:"+left+" Right:"+right+" Top:"+top+" Bottom:"+bottom+" Width:"+width+ " Height:" + height+"\n"

		    with open('train_labels.csv', 'a') as f:
			f.write(name+".jpg,"+width+","+height+",tennisball,"+left+","+top+","+right+","+bottom+"\n")
			f.close()

