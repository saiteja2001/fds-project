class individuals:
    def __init__(self,name,category,mobile,pin):
        self.name=name
        self.category=category
        self.mobile=mobile
        self.pin=pin
    def display_individual(self):
        print("Name     : ",self.name)
        print("Category : ",self.category)
        print("MObile   : ",self.mobile)
        print("pin      : ",self.pin)
        return "added\n"

class spot_person:
    def __init__(self,name,mobile,spot,age,pay):
        self.name=name
        self.mobile=mobile
        self.spot=spot
        self.age=age
        self.pay=pay
    def display_position(self):
        if(self.spot=="Dr"):
            print("Name.......",self.name)
            print("MObile.....",self.mobile)
            print("spot.......",self.spot)
            print("age........",self.age)
            print("fee........",self.pay)
            return "added"
        else:
            print("Name.......",self.name)
            print("MObile.....",self.mobile)
            print("spot.......",self.spot)
            print("age........",self.age)
            print("Bill.......",self.pay)
            return "successful"

class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)
     def printStack(self):
         res=[]
         for i in range(len(self.items)):
             res.append(self.items[i])
         return res

class Node:
    def __init__(self,data):
        self.data=data
        self.next_val=None
class linked_list:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next_val
    def add_at_end(self,new_data):
        new_node=Node(new_data)
        if(self.head is None):
            self.head=new_node
            return
        last=self.head
        while(last.next_val):
            last=last.next_val
        last.next_val=new_node
          
def managing(ch):
    if(ch==1):
        for i in range(int(input("Enter the number of candidates : "))):
            n=input("Name..........")
            p=input("category......")
            m=int(input("mobile...."))
            s=int(input("pin......."))
            ind=individuals(n,p,m,s)
            store.append(ind)
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch==2):
        for i in range(len(store)):
            print(store[i].display_individual())
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch==3):
        pin_search=int(input("ENTER THE PIN TO BE SEARCHED : "))
        for i in range(len(store)):
            if(store[i].pin==pin_search):
                print(str(pin_search)+" is found at "+str(i))
                store[i].display_individual()
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch==4):
        pin_search=int(input("ENTER THE PIN TO BE DELETED : "))
        for i in range(len(store)):
            if(store[i].pin==pin_search):
                del store[i]
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch==5):
        init=int(input("ENTER THE PIN TO BE UPDATED : "))
        mob=int(input("ENTER THE NEW PIN TO BE UPDATED : "))
        for i in range(len(store)):
            if(store[i].pin==init):
                store[i].pin=mob
            print(store[i].display_individual())
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    else:
        print("Exit........")

def get_data(ch):
    if(ch=='a'):
        n=input("Name......")
        m=input("Mobile....")
        s=input("Spot......")
        a=int(input("age......"))
        p=int(input("Pay....."))
        var=spot_person(n,m,s,a,p)
        sheet.add_at_end(var)
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch=='b'):
        temp=sheet.head
        while(temp):
            print(temp.data.display_position())
            temp=temp.next_val
        nxt=int(input("Enter choice in order to do what To do next : "))
        managing(nxt)
    elif(ch=='c'):
        doc_name=input("ENTER THE NAME OF THE DOCTOR TO SEARCH FOR : ")
        temp=sheet.head
        while(temp!=None):
            if(temp.data.name==doc_name and temp.data.spot=="Dr"):
                print("Your doctor is available")
                return temp.data.display_position()
            temp=temp.next_val
        return "Not Found"
    elif(ch=='d'):
        patient_name=input("ENTER THE NAME OF THE PATIENT TO SEARCH FOR : ")
        temp=sheet.head
        while(temp!=None):
            if(temp.data.name==patient_name and temp.data.spot=="Pt"):
                print("Fetching patient details")
                return temp.data.display_position()
            temp=temp.next_val
        return "Not Found"
    elif(ch=='e'):
        search_name=input("ENTER THE NAME TO UPDATE PAY : ")
        update_pay=int(input("ENTER THE UPDATED PAY : "))
        temp=sheet.head
        while(temp!=None):
            if(temp.data.name==search_name):
                temp.data.pay=update_pay
                return temp.data.display_position()
            temp=temp.next_val
        return "Not found"
    else:
        return "Exit....."
    
def display_people(ch):
    if(ch=="D"):
        print("number of doctors available are ",docs.size())
        for i in range(len(docs_list)):
            docs_list[i].display_individual()
    elif(ch=="P"):
        print("The number of patients in the lobby are ",pats.size())
        for i in range(len(pati_list)):
            pati_list[i].display_individual()
    else:
        print("Exit.....")
    return "succesfull"

store=[]
one=individuals("A","P",21,3)
two=individuals("V","D",34,2)
store.append(one)
store.append(two)

print("\n\tOperations used, ") 
print("1.Accept details\n2.Display Details")
print("3.Search Details\n4.Delete Details")
print("5.Update Details\n6.Exit")

choice=int(input("ENTER THE CHOICE : ")) 
print(managing(choice))

docs=Stack()
pats=Stack()
docs_list=[]
pati_list=[]
for i in range(len(store)):
    if(store[i].category=="D"):
        docs.push(store[i].name)
        val=individuals(store[i].name,store[i].category,store[i].mobile,store[i].pin)
        docs_list.append(val)
    else:
        pats.push(store[i].name)
        val=individuals(store[i].name,store[i].category,store[i].mobile,store[i].pin)
        pati_list.append(val)

print(display_people(input("ENTER THE CHARACTER : ")))

print("\n\tOperations used, ") 
print("\na.entering details\nb.Display Details\n")
print("c.Search doctor\nd.search patient")
print("e.Update Details\nf.Exit")

sheet=linked_list()

one=spot_person("Abc",3456,"Dr",34,345)
two=spot_person("Xyz",2352,"Pt",27,765)

sheet.add_at_end(one)
sheet.add_at_end(two)

inp=input("enter your character : ")
print(get_data(inp))

