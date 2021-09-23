
text = ",c="
c_alpha = {"c=","c-","dz=","d-","lj",'nj','s=','z='}

for i in c_alpha:
    if i in text:
        text = text.replace(i,",")
        print(text)