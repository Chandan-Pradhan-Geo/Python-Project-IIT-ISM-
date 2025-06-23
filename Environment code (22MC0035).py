#PREREQUISITE TO RUN THIS CODE
'''
As this is a 'graphical user interface(GUI)' through which any user can interact with it like a application to calculate answer based
on the given problem and it has been embeded with a graph(which is set to 3 year only as per the problem).


To do so, we need some additional Python modules to install into our system such as 1.tkinter(for building GUI),2.Matplotlib(to show graph),

*******for installation*********
open COMMAND PROMPT on your computer
type the following command and hit enter

pip install tk
pip install matplotlib
pip install pillow

if any problem during the installaion of these modules or pip recongnition then install the latest version of python IDLE and try again.


'''


from tkinter import *
from PIL import ImageTk,Image
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg,NavigationToolbar2Tk)
root=Tk()
root.title("ENVIRONMENTAL GEOLOGY (22MCOO35)")
root.config(bg="#F5F5DC",highlightthickness=4,highlightbackground="#B1FB17",highlightcolor="green")
#root.geometry("1920x1080")
#root.attributes("-fullscreen",True)
root.geometry("600x600")
#root.iconbitmap(r"ismlogo.ico")this will now be executed unless you don't have the logo icon in your system
'''
#this will also not be executed unless you don't have the image in your system to set 
img=Image.open("C:/Users/Lenovo/Downloads/ismlogo.ico")
resized_image=img.resize((65,65))
img=ImageTk.PhotoImage(resized_image)
img_label=Label(root,image=img)
img_label.place(x=4,y=4,anchor="nw")
'''




main_frame=Frame(root,bg="#00FFFF",highlightthickness=2,bd="2")
main_frame.config(highlightbackground="#0000FF",highlightcolor="green")
main_frame.place(x=80,y=40,anchor="nw")
graph_frame=Frame(root,bd="5",highlightthickness=2)
graph_frame.config(highlightbackground="#B1FB17",highlightcolor="green")

graph_frame.place(x=1100,y=700,anchor="s")

length_label=Label(main_frame,
                   text="What is length of the lake(in Km):",
                   bg="#00FFFF",
                   font=("calibre",10,"bold"))
length_label.grid(row="0",column="1",padx="5",pady="5",sticky="w")
breadth_label=Label(main_frame,
                    text="What is breadth of the lake(in Km):",
                    bg="#00FFFF",
                    font=("calibre",10,"bold"))
breadth_label.grid(row="1",column="1",padx="5",pady="5",sticky="w")
height_label=Label(main_frame,
                   text="What is height of the lake(in Km):",
                   bg="#00FFFF",
                   font=("calibre",10,"bold"))
height_label.grid(row="2",column="1",padx="5",pady="5",sticky="w")
initial_pb_conc_label=Label(main_frame,
                            text="What is initial concentration of Pb in the lake(in gram/litre):",
                            bg="#00FFFF",
                            font=("calibre",10,"bold"))
initial_pb_conc_label.grid(row="3",column="1",padx="5",pady="5",sticky="w")
affluent_rate_label=Label(main_frame,
                          text="What rate of affluent from smelters into the lake(in litres/day):",
                          bg="#00FFFF",
                          font=("calibre",10,"bold"))
affluent_rate_label.grid(row="4",column="1",padx="5",pady="5",sticky="w")
affluent_pb_conc_label=Label(main_frame,
                             text="What is the concentration of Pb in affluent(in gram/litre):",
                             bg="#00FFFF",
                             font=("calibre",10,"bold"))
affluent_pb_conc_label.grid(row="5",column="1",padx="5",pady="5",sticky="w")
time_of_flow_label=Label(main_frame,
                         text="The time of flow of affluent into the lake(in days) :",
                         bg="#00FFFF",
                         font=("calibre",10,"bold"))
time_of_flow_label.grid(row="6",column="1",padx="5",pady="5",sticky="w")

#defining the variable to use in entry widget
length_var=DoubleVar()
breadth_var=DoubleVar()
height_var=DoubleVar()
initial_pb_conc_var=DoubleVar()
affluent_rate_var=DoubleVar()
affluent_pb_conc_var=DoubleVar()
time_of_flow_var=DoubleVar()
remedial_pb_var=StringVar()



#creating entry widget to get value from user input
length_entry=Entry(main_frame,
                   textvariable=length_var,
                   bd="2",highlightthickness="2")
length_entry.config(highlightbackground="yellow",highlightcolor="yellow")
length_entry.grid(row="0",column="2",padx="5",pady="5")
breadth_entry=Entry(main_frame,
                    textvariable=breadth_var,
                    bd="2",highlightthickness="2")
breadth_entry.config(highlightbackground="yellow",highlightcolor="yellow")
breadth_entry.grid(row="1",column="2",padx="5",pady="5")
height_entry=Entry(main_frame,
                   textvariable=height_var,
                   bd="2",highlightthickness="2")
height_entry.config(highlightbackground="yellow",highlightcolor="yellow")
height_entry.grid(row="2",column="2",padx="5",pady="5")
initial_pb_conc_entry=Entry(main_frame,
                            textvariable=initial_pb_conc_var,
                            bd="2",highlightthickness="2")
initial_pb_conc_entry.config(highlightbackground="yellow",highlightcolor="yellow")
initial_pb_conc_entry.grid(row="3",column="2",padx="5",pady="5")
affluent_rate_entry=Entry(main_frame,
                          textvariable=affluent_rate_var,
                          bd="2",highlightthickness="2")
affluent_rate_entry.config(highlightbackground="yellow",highlightcolor="yellow")
affluent_rate_entry.grid(row="4",column="2",padx="5",pady="5")
affluent_pb_conc_entry=Entry(main_frame,
                             textvariable=affluent_pb_conc_var,
                             bd="2",highlightthickness="2")
affluent_pb_conc_entry.config(highlightbackground="yellow",highlightcolor="yellow")
affluent_pb_conc_entry.grid(row="5",column="2",padx="5",pady="5")
time_of_flow_entry=Entry(main_frame,
                         textvariable=time_of_flow_var,
                         bd="2",highlightthickness="2")
time_of_flow_entry.config(highlightbackground="yellow",highlightcolor="yellow")
time_of_flow_entry.grid(row="6",column="2",padx="5",pady="5")


#updating some varible ,
#using get funtion to get value for easy configuration


x=length_var.get()
y=breadth_var.get()
z=height_var.get()
volume_of_lake=(x*y*z*1E12)
p=initial_pb_conc_var.get()
q=affluent_rate_var.get()
r=affluent_pb_conc_var.get()
s=time_of_flow_var.get()
print(x,y,z,p,q,r,s)


   
#Creating a function that we will use in output button

def calculate():
    global volume_of_lake
    global initial_pb_conc
    global initial_pb_amnt_in_lake
    global time_of_affluent_flow
    global total_pb_concentration_in_lake
    global r
    global l
    global m
    global n
    global o
    global p
    

    volume_of_lake=(length_var.get()*breadth_var.get()*height_var.get()*1E12)
    j=float(volume_of_lake)
    op=print("The total vloume of water in the lake is ",j,"Litre")
    
    initial_pb_conc=initial_pb_conc_var.get()
    k=float(initial_pb_conc)
    print("The initial concentration of pb in lake water is ",k,"mg/litre")
    
    initial_pb_amnt_in_lake=(volume_of_lake*initial_pb_conc)
    l=float(initial_pb_amnt_in_lake)
    print("The inital amount of pb in the lake water is",l,"mg")
    
    rate_of_affluent=affluent_rate_var.get()
    m=float(rate_of_affluent)
    print("The rate of affluent of pb from smelter is ",m,"litres/day")
    
    amnt_of_affluent_from_smelters=affluent_pb_conc_var.get()
    n=float(amnt_of_affluent_from_smelters)
    print("The the concentration of pb in the affluent is ",n,"gram/litres")
    
    time_of_affluent_flow=time_of_flow_var.get()
    o=float(time_of_affluent_flow)
    print("The total time duration of effluent flow is ",o,"days")
    
    total_pb_from_smelters=(amnt_of_affluent_from_smelters*rate_of_affluent*time_of_affluent_flow)
    p=float(total_pb_from_smelters)
    print("The amount of pb accumulated from smelters is ",p,"gram")
    
    total_pb_accumulation_in_lake_in_3years=(initial_pb_amnt_in_lake+total_pb_from_smelters)
    q=float(total_pb_accumulation_in_lake_in_3years)
    print("The total amount of pb accumulated in the lake is ",q,"grams")

    if volume_of_lake==0:
        r=0
    else:
        r=(total_pb_accumulation_in_lake_in_3years/volume_of_lake)
    
    #print(r)

    if total_pb_accumulation_in_lake_in_3years !=0:
        global total_pb_concentration_in_lake
        
    
        total_pb_concentration_in_lake=(total_pb_accumulation_in_lake_in_3years/volume_of_lake)
        r=float(total_pb_concentration_in_lake*1E9)
        print("The overall concentration of pb in the lake is ",r,"ngm/litres")
        print("refreshed",end="\n")
    else:
            
            
        r=0
        #print(r)
    
    #print(r)

    #setting the values/results into the label
    #inputs
    length_var.set(2)
    
    breadth_var.set(1)
    height_var.set(8)
    initial_pb_conc_var.set(4E-9)
    
    affluent_rate_var.set(2500)
    affluent_pb_conc_var.set(29E-3)
    time_of_flow_var.set(1095)
    
    #result
    
    info_box_var.set("The features of your calculation are shown below !!")
    info1_box_var.set("Results !!!")

    volume_var.set(f"The total volume of water in the lake is {j} litre. ")
    initial_pb_lake_var.set(f"The initial amount of pb in the like water is {l} gram.")
    total_pb_smelters_var.set(f"The total amount of Pb accumulated from smelters is {p} gram.")
    total_pb_lake_var.set(f"Overall accumulation of Pb in the lake water is {q} gram.")
    total_pb_conc_lake_var.set(F"Overall concentraion of Pb in the lake is {r*1E-9} gram/liter.")
    
    #print("test:",r)

    if r ==0:
        remedial_pb_var.set(f"The lake is quite safe with {r}ng/L of lead concentration")
        
    elif 0<r<15:
        
        remedial_pb_var.set(f"The lake is considered safe beacause our \n calculation yielded a total lead concentration of {r}ng/L ,\n which is well below the acceptable limit of 15ng/L")

    else:
        
        remedial_pb_var.set(f"The lake is considered unsafe as  our \n claculation indicate a total lead concentration of {r}ng/L ,\n slightly exceeding the acceptable limit of 15ng/L")
    

    

   
#The individual total pb from smetlers in each years
'''
    
total_pb_from_smelters_in_1year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*1*1E9)
total_pb_from_smelters_in_2year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*2*1E9)
total_pb_from_smelters_in_3year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*3*1E9)
total_pb_from_smelters_in_4year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*4*1E9)
total_pb_from_smelters_in_5year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*5*1E9)
a=total_pb_from_smelters_in_1year*1E9
print(a)
b=total_pb_from_smelters_in_2year*1E9
print(b)
c=total_pb_from_smelters_in_3year*1E9
print(c)
d=total_pb_from_smelters_in_4year*1E9
print(d)
e=total_pb_from_smelters_in_5year*1E9
print(e)
'''

#the following button will execute the  calculate function that we have created just now

answer=Button(main_frame,text="Answer",command=calculate)
answer.grid(row="7",column="2")


#creating another secondary frame to fit result and fit the frame into the main frame
secondary_frame=Frame(root,bg="#F5F5DC",highlightthickness=2)
secondary_frame.config(highlightbackground="green",highlightcolor="green")
secondary_frame.place(x=80,y=520,anchor="sw")
#creating third frame to show the remedial
remedial_frame=Frame(root,bg="#F5F5DC",highlightthickness=2)
remedial_frame.config(highlightbackground="green",highlightcolor="green")
remedial_frame.place(x=80,y=630,anchor="sw")
#defining variabe to use in output
info_box_var=StringVar()#for information
info1_box_var=StringVar()#for information
volume_var=StringVar()
initial_pb_lake_var=StringVar()
total_pb_smelters_var=StringVar()
total_pb_lake_var=StringVar()
total_pb_conc_lake_var=StringVar()
#information box
info_box=Label(root,textvariable=info_box_var,
               text="The features of your calculation are shown below !! ",font=("calibre",10,"bold"))
info_box.config(bg="#F5F5DC",fg="green")
info_box.place(x=80,y=330)
#infomation !!!!!
info1_box=Label(root,textvariable=info1_box_var,
               text="Results!! ",font=("calibre",10,"bold"))
info1_box.config(bg="#F5F5DC",fg="green")
info1_box.place(x=80,y=530,)

#creating the result section to show the calculted answers

volume_of_lake_r=Label(secondary_frame,
                       textvariable=volume_var,
                       text="Volume of the lake is :",
                       font=("calibre",10,"bold"))
volume_of_lake_r.grid(row="8",column="1",padx="5",pady="5",sticky="w")
initial_pb_in_lake_r=Label(secondary_frame,
                       textvariable=initial_pb_lake_var,
                       text="Initial pb amount in the lake is :",
                       font=("calibre",10,"bold"))
initial_pb_in_lake_r.grid(row="9",column="1",padx="5",pady="5",sticky="w")
total_pb_from_smelters_r=Label(secondary_frame,
                               textvariable=total_pb_smelters_var,
                               text="Total amount of Pb from the smelters:",
                               font=("calibre",10,"bold"))
total_pb_from_smelters_r.grid(row="10",column="1",padx="5",pady="5",sticky="w")
total_pb_in_lake_r=Label(secondary_frame,
                         textvariable=total_pb_lake_var,
                         text="Total amount of Pb in the lake:",
                         font=("calibre",10,"bold"))
total_pb_in_lake_r.grid(row="11",column="1",padx="5",pady="5",sticky="w")
total_pb_conc_in_lake_r=Label(secondary_frame,
                              textvariable=total_pb_conc_lake_var,
                              text="Total Pb concentration in the lake:",
                              font=("calibre",10,"bold"))
total_pb_conc_in_lake_r.grid(row="12",column="1",padx="5",pady="5",sticky="w")


#creating label to show the remedials in thrid frame
remedial_r=Label(remedial_frame,textvariable=remedial_pb_var,
                 text="Remedial",
                 font=("calibre",10,"bold"))

remedial_r.grid(row="13",column="1",padx="5",pady="5",sticky="w")
#defing some varible for plot value



def plot():
    if volume_of_lake==0:
        print("Graph can't be shown with zero values")
    else:
        
        '''
        volume_of_lake=(length_var.get()*breadth_var.get()*height_var.get()*1E12)
        initial_pb_conc=initial_pb_conc_var.get()
        initial_pb_amnt_in_lake=(volume_of_lake*initial_pb_conc)
        '''
    
        total_pb_from_smelters_in_1year=(n*m*1*365)
        toatl_pb_conc_in_the_lake_in_1year=((total_pb_from_smelters_in_1year+l)/volume_of_lake)
        total_pb_from_smelters_in_2year=(n*m*2*365)
        toatl_pb_conc_in_the_lake_in_2year=((total_pb_from_smelters_in_2year+l)/volume_of_lake)
        total_pb_from_smelters_in_3year=(n*m*3*365)
        toatl_pb_conc_in_the_lake_in_3year=((total_pb_from_smelters_in_3year+l)/volume_of_lake)
        total_pb_from_smelters_in_4year=(n*m*4*365)
        toatl_pb_conc_in_the_lake_in_4year=((total_pb_from_smelters_in_4year+initial_pb_amnt_in_lake)/volume_of_lake)
        total_pb_from_smelters_in_5year=(affluent_pb_conc_var.get()*affluent_rate_var.get()*5*365)
        toatl_pb_conc_in_the_lake_in_5year=((total_pb_from_smelters_in_5year+initial_pb_amnt_in_lake)/volume_of_lake)
    
        a=toatl_pb_conc_in_the_lake_in_1year*1E9
        print("a:",a)
        b=toatl_pb_conc_in_the_lake_in_2year*1E9#to make it gm  to ng 
        print("b:",b)
        c=toatl_pb_conc_in_the_lake_in_3year*1E9
        print("c:",c)
        '''
        d=toatl_pb_conc_in_the_lake_in_4year*1E9
        print(d)
        e=toatl_pb_conc_in_the_lake_in_5year*1E9
        print(e)
        '''

        fig=Figure(figsize=(3.9,3.9),dpi=99)
        x=[1,2,3]
        y=[a,b,c]
        plot1=fig.add_subplot(111)
        plot1.set_title("Pb contamination",weight="bold")
        plot1.set_xlabel("Time in year",fontsize=7,weight="bold")
        plot1.set_ylabel("Concentration in ngm/litre",fontsize=7,weight="bold")
    
    
    
        plot1.bar(x,y)
    
        canvas=FigureCanvasTkAgg(fig,graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()#place(rely=0.5,relx=0.5,anchor="s")
        toolbar=NavigationToolbar2Tk(canvas,graph_frame)
        #toolbar.update()
        canvas.get_tk_widget().pack(padx="5",pady="5")#place(x=600,y=700,anchor="s")
#This button will draw our graph by executin the above plot function        
plot_button=Button(root,text="PLOT the graph",bd="2",command=plot,highlightthickness=3)
plot_button.config(highlightbackground="pink",highlightcolor="green")
plot_button.place(x=600,y=700,anchor="s")

patent=Label(root,text="CHANDAN PRADHAN (22MCOO35)",font=("calibre",8,"bold"))
patent.place(x=880,y=700,anchor="s")


root.mainloop()


