import os
o=os.geteuid()
# os.system('trap "kalitorify -c ; exit" 2 3 8 9')
if o!=0:
    print(f'Error run with sudo !!')
    exit()

k=input('enter username : ').strip()

passf=input('enter pass file : ')
a=os.system(f"sed -i '/^[[:space:]]*$/d' {passf} ")

if a!=0:
    print('error occured')
    exit 

o=open(passf ,'r')
ip=''
while ip.isdigit()!=True:
    ip=input('change ip limit (default = 18)')
    if ip.isspace()==True or ip=='':
        ip=18
    
        break
  
print(ip)

f=o.readlines()

c=0
for i in f:
    
    if c >ip:
        c=0
        os.system('kalitorify -r')
    os.system(f'bash main.sh {k} {i}')
    c+=1
