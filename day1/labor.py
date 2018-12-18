import os

#print(os.listdir('.'))
#print(os.listdir('./List'))

#os.chdir(r'./List')
os.chdir(r'C:\Users\student\chatbot\day1\List')

#print(os.getcwd())
#print(os.listdir('.'))

for filename in os.listdir('.'):
    os.rename(filename, 'ssafy_'+filename)
    
    #if filename.find('_')==1:
    #    os.rename(filename,'ssafy_00'+filename)
    #elif filename.find('_')==2:
    #    os.rename(filename, 'ssafy_0'+filename)
    #else:
    #    os.rename(filename, 'ssafy_'+filename)
