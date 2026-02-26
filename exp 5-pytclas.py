#print each adjective for every fruit:
adj=["red","big","tastey"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

#ex: print all the words that have eeven no. of charecters from a scentence
st="My name's [name]\
I'm student of giet ,I developed my coding skills\
      which I think will apply well at my job."      
for word in st.split():
        if(len(word)%2==0):
                print(word)  