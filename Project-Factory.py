from tkinter import *
import csv
mywin = Tk()
mywin.title('Program for factory')
mywin.minsize(530,300)
list_cream_infer=[['Cetyl Alcohol',35],['Emulsifying Wax',40],['White Oil',50],['Polysorbate 20',10],['Stearic Acid',20],['Water',5],
                  ['Glycerin',35],['Kemaben 2',45],['Isopropyl Myristate',32],['Glyceryl Stearate',12],['Mineral Oil',34],['Ethylhexyl Methoxycinnamate',30],
                  ['Niacinamide',25],['Petrolatum',26],['Butyl Methoxycinnamate',29],['Tocopheryl Acetate',18],['Sodium Ascorbyl phosphate',40]]
list_cream_forloop=[['Cetyl Alcohol : 35 THB'],['Emulsifying Wax : 40 THB'],['White Oil : 50 THB'],['Polysorbate 20 : 10 THB'],['Stearic Acid : 20 THB'],['Water : 5 THB'],
                    ['Glycerin : 35'],['Kemaben 2 : 45 THB'],['Isopropyl Myristate : 32 THB'],['Glyceryl Stearate : 12 THB'],['Mineral Oil : 34 THB'],['Ethylhexyl Methoxycinnamate : 30 THB'],
                    ['Niacinamide : 25 THB'],['Petrolatum : 26 THB'],['Butyl Methoxycinnamate : 29 THB'],['Tocopheryl Acetate : 18 THB'],['Sodium Ascorbyl phosphate : 40 THB']]
bucket_name=[]
bucketinfercream=[]

def sel_2():
    bucketinfercream=[list_cream_infer[i] for i,chk in enumerate(chks) if chk.get()]
    try:
        filepath='Total Cream.csv'

        with open(filepath,'w',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(bucketinfercream)

    except Exception as infer_error:
        print('def infer | ',delete_error)
def infer():
    try:
        filepath='Total Cream.csv'

        with open(filepath,'w',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(bucketinfercream)
        mywin.destroy()
    except Exception as infer_error:
        print('def infer | ',delete_error)

lb=Label(mywin,text='[Select Cream List]',font='Tohoma 12 bold',fg='#FF6600').pack()

chks=[BooleanVar() for varchks in list_cream_forloop]
for i,label in enumerate(list_cream_forloop):
    radtk=Checkbutton(mywin,text=label,variable=chks[i],command=sel_2,font='Tohoma 10')
    radtk.pack(anchor=W,padx=5)

Button(mywin,text='Next',command=mywin.destroy,width=50,bg='#33FF33',font='Tohoma 10 bold').pack(pady=7)
mywin.mainloop()


mywin_2=Tk()
mywin_2.title('Program for factory')
mywin_2.minsize(530,300)

contrainer_no=[[1,'40x30'],[2,'25x35'],[3,'40x50'],[4,'80x50']]
ctn_infer=[['40x30',20],['25x35',15],['40x50',25],['80x50',40]]
ctn_list_price=[]

def sel():
    try:
        select_var=var_2.get()
        option=contrainer_no[select_var-1][1]
        price_ctn_var=ctn_infer[select_var-1][1]
        label.config(text='You selected the option : {} | Price : {} '.format(option,price_ctn_var))
    except Exception as sel_error:
        print('def sel(mywin 2) | ',sel_error)

def seld():
    try:
        select_var=var_2.get()
        i=(int(select_var))-1
        ctn_list_price.append(ctn_infer[i])

        filepath='Total Cream.csv'

        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(ctn_list_price)

        mywin_2.destroy()
    except Exception as seld_error:
        print('def seld(mywin 2) | ',seld_error)

var_2=IntVar()

lb=Label(mywin_2,text='[Select Contrainer]',font='Tohoma 12 bold',fg='#FF6600').pack()
for id,label in contrainer_no:
    radtk_2=Radiobutton(mywin_2,text=label,variable=var_2,value=id,command=sel,font='Tohoma 10')
    radtk_2.pack(anchor=W,padx=5)
    
label=Label(mywin_2,fg='#ff3300',font='Tohoma 10 bold')
label.pack()
Button(mywin_2,text='Select',command=seld,bg='#33FF33',font='Tohoma 10 bold',width=30).pack()

mywin_2.mainloop()



mywin_3=Tk()
mywin_3.title('Program for factory')
mywin_3.minsize(700,500)

try:
    filepath='Total Cream.csv'                                             #Process อ่านค่าจาก excel
    with open(filepath,'r',encoding='utf-8')as infile:
        read=csv.reader(infile)
        mylist=list(read)

    sum_total=0                                                                       #นำค่าที่เป็นตัวเลขมาบวกรวมกันเพื่อนำไปคำนวณต่อไป
    for loop in mylist:
        sum_total+=eval(loop[1])
    for loop in mylist:
        bucket_name.append(loop[0])
except Exception as readcsv_error:
    print('ream csv | ',readcsv_error)

def caltotal():
    try:
        def cal_total_def(definput_ans,definput_sum):
            thetotal=definput_ans*definput_sum
            return thetotal
        theinput=myinput.get()
        ans=int(theinput)
        if ans>0:
            all_total=cal_total_def(ans,sum_total)
            display3_2.set('List Your select : {}'.format(bucket_name))
            display3_3.set('T/P : {} THB x {} P.'.format(sum_total,ans))
            display3_4.set('Total : {} THB'.format(all_total))
            quantity.append(ans)
        else:
            display3_2.set('!!!!!!!!!!!!!!!!!!!!!!!')
            display3_3.set('Please Input Number > 0')
            display3_4.set('!!!!!!!!!!!!!!!!!!!!!!!')
        filepath='Quantity.csv'

        with open(filepath,'w',encoding='utf-8')as outfile:
            writer=csv.writer(outfile)
            writer.writerow(quantity)
            
    except Exception as caltotal_error:
        print('def caltotal | ',caltotal_error)


def calsell():
    try:
        def calsell_total(definput_total,definput_many,definput_sum):
            total=definput_total*definput_many
            all_total=definput_sum*definput_many
            sub_total=total-all_total
            price_add_bangle.append(sub_total)
            return sub_total

        filepath='Quantity.csv'                                             #Process อ่านค่าจาก excel

        with open(filepath,'r',encoding='utf-8')as infile:
            read=csv.reader(infile)
            mylist=list(read)
        
        theinput=myinput_2.get()
        input_total=float(theinput)
        many_part=int(mylist[0][1])
        net_total=calsell_total(input_total,many_part,sum_total)
        display3_7.set('If you can sell all.')
        display3_8.set('You will have bangle (-XXX = Loss) : {}'.format(net_total))
        display3_9.set('-----------------------------------------------')
        display3_10.set('Thank You for use my program')
        
    except Exception as caltotal_error:
        print('def caltotal | ',caltotal_error)

title=['List','Price']
quantity=['quantity']
space=['']
number_add_qua=[]
banglelist=['bangle']
price_add_bangle=[]
def close():
    try:
        quantity_infer=quantity+number_add_qua
        bangle_infer=banglelist+price_add_bangle
        
        filepath='Infer all Cream.csv'

        with open(filepath,'w',encoding='utf-8')as outfile:
            writer=csv.writer(outfile)
            writer.writerow(title)

        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(bucketinfercream)

        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(ctn_list_price)

        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile,lineterminator='\n')
            writer.writerows(space)
        
        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile)
            writer.writerow(quantity_infer)

        with open(filepath,'a',encoding='utf-8')as outfile:
            writer=csv.writer(outfile)
            writer.writerow(bangle_infer)

        mywin_3.destroy()

    except Exception as close_error:
        print('def close | ',close_error)
        
lb=Label(mywin_3,text=': How many do you want to manufacture :',font='Tohoma 12 bold',fg='#FF6600')
lb.pack()

myinput=IntVar()
myinput_2=IntVar()

ent3_1=Entry(mywin_3,textvariable=myinput,width=30)
ent3_1.pack()
ent3_1.focus()
btsl3=Button(mywin_3,text='Select',command=caltotal,width=20,bg='#33FF33')
btsl3.pack(pady=7)


display3_1=StringVar()
display3_2=StringVar()
display3_3=StringVar()
display3_4=StringVar()


lb3_1=Label(mywin_3,text='-----------------------------------------------',font='Tohoma 10 bold',fg='#FF0000').pack()
lbdp3_2=Label(mywin_3,textvariable=display3_2,fg='#006600').pack()
lbdp3_3=Label(mywin_3,textvariable=display3_3,font='Tohoma 10 bold',fg='#FF0000').pack()
lbdp3_4=Label(mywin_3,textvariable=display3_4,font='Tohoma 10 bold',fg='#FF0000').pack()
lb3_6=Label(mywin_3,text='-----------------------------------------------',font='Tohoma 10 bold',fg='#FF0000').pack()

lb=Label(mywin_3,text='Input Price To Sell (Per part)',font='Tohoma 12 bold',fg='#FF6600').pack()
lb=Label(mywin_3,text='You should to input upper first',font='Tohoma 12 bold',fg='#FF6600').pack()

ent3_2=Entry(mywin_3,textvariable=myinput_2)
ent3_2.pack()
ent3_2.focus()
btsl3=Button(mywin_3,text='Select',command=calsell,width=20,bg='#33FF33').pack(pady=7)
btc=Button(mywin_3,text='Close',command=close,width=20,bg='#FF3300').pack(pady=3)

display3_6=StringVar()
display3_7=StringVar()
display3_8=StringVar()
display3_9=StringVar()
display3_10=StringVar()
lb3_7=Label(mywin_3,text='-----------------------------------------------',font='Tohoma 10 bold',fg='#FF0000').pack()
lbdp3_8=Label(mywin_3,textvariable=display3_8,font='Tohoma 10 bold',fg='#006600').pack()
lbdp3_9=Label(mywin_3,textvariable=display3_9,font='Tohoma 10 bold',fg='#FF0000').pack()
lbdp3_10=Label(mywin_3,textvariable=display3_10,font='Tohoma 10 bold',fg='#006600').pack()


mywin_3.mainloop()



