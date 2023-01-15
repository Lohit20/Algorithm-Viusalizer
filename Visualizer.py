from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from PIL import ImageTk, Image
import random
from graph_plot import graph
from bubbleSort import bubble_sort
from bucketsort import bucketSort
from quicksort import quick_sort
from mergesort import merge_sort
from insertionsort import insertionSort
from countsort import countingSort
from radixsort import radixSort
from heapifysort import heapSort
from problem_a import hybrid_quick_sort
from problem_b import problem



root= Tk()
root.title('Sorting Algorithm Project')
image_O = Image.open('data.jpg')
bck_end = ImageTk.PhotoImage(image_O)
root.geometry('900x600+200+80')
lbl = Label(root,image=bck_end)
lbl.place(x=0,y=0)
root.config(bg='#082A46') 

# Heading Algorithms
mainlabel = Label(root,text="Algorithms: ", font=("new roman",16,"italic bold"),bg="#E5A5FF",width=10,fg="black",relief=GROOVE,bd=5)
mainlabel.place(x=0,y=0)

# Showing Algorithm options such as Bubble Sort 
select_algorithm= StringVar()
algo_menu= ttk.Combobox(root,width=15,font=("new roman",19,"italic bold"),textvariable=select_algorithm,
                        values=['Bubble Sort','Merge Sort','Quick Sort','Insertion Sort','Count Sort','Radix Sort','Heap Sort','Bucket Sort','Hybrid Quick Sort','Problem 8.2.4'])
algo_menu.place(x=145,y=0)
algo_menu.current(0)  #by default bubble sort


# showing data in form of bars in canvas(Black BOX)
def drawData(data,colorArray,mssg=None):
    canvas.delete("all") # it will delete previous data( Data Bars) if this function is  previously run
    if (mssg!= None):
        canvas.create_text(len(mssg)+250,15,text=mssg,font=("new roman",15,"italic bold"),fill="orange")
    canvas_height=450
    canvas_width=870
    x_width= canvas_width / (len(data)+1)
    # spacing between the bars
    offset=10
    spacing_bet_rect=10
    normalised_data=[(i)/max(data) for i in data]  # in order to avoid the small bars
    #creating bar with respect to the number 
    for i , height in enumerate(normalised_data):
        x0=i*x_width + offset + spacing_bet_rect
        y0= canvas_height - height * 400  # we have multiplied 400 because we will normalised our values with one
                                        #one formula so that our data won't exceed our canvas 
        x1= (i+1)* x_width
        y1= canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("new roman",15,"italic bold"),fill="orange")

    root.update_idletasks() # it will show every step of algorithm for e.g comparision between number in bubble sort

#start button for running the  algorithm 
def StartAlgorithm():
    global data
    # if not data: return

    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedscale.get())
    
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Bucket Sort':
        bucketSort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Insertion Sort':
        insertionSort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Count Sort':
        countingSort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Radix Sort':
        radixSort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Heap Sort':
        heapSort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Hybrid Quick Sort':
        hybrid_quick_sort(data, drawData, speedscale.get())
    elif algo_menu.get() == 'Problem 8.2.4':
        start = simpledialog.askinteger("Input","Starting Point",parent=root)
        end = simpledialog.askinteger("Input","Ending Point",parent=root)
        problem(data, start,end, drawData, speedscale.get())
    # drawData(data, ['green' for x in range(len(data))])
#it will generate the bars according to the number given
def Generate():
    global data
    print('Select Algorithm'+select_algorithm.get())
    # min value
    minivalue=int(minvalue.get())
    maxivalue=int(maxvalue.get())
    sizeevalue=int(sizevalue.get())
    data=[]
    if(algo_menu.get() == 'Bucket Sort'):
		    for _ in range(sizeevalue):
		        data.append(round(random.uniform(0, 1), 2))
    
    else:
        for _ in range(sizeevalue):
            data.append(random.randrange(minivalue,maxivalue+1))

	
    drawData(data,["#A90042" for x in range (len(data))])

random_generate = Button(root,text="Generate",bg="#F7A4A4",font=("arial",12,"italic bold"),relief=SUNKEN,
                        activebackground="#05945B",activeforeground="white",bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)

#Defines the tag of size of array that should be generated
sizevaluelabel=Label(root,text ="Size: ", font=("new roman",12,"italic bold"),bg="#EEF1FF",
                    width=10,fg="black",height=2,relief=GROOVE,bd=5)
sizevaluelabel.place(x=0,y=60)

#Defines the size of array that should be generated
sizevalue= Scale(root,from_=0,to=30,resolution=1,bg="#B1AFFF",orient=HORIZONTAL,font=("arial",14,"italic bold"),
                    relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=60)

#Defines the tag of size of array that should be generated
minvaluelabel=Label(root,text ="Min Value: ", font=("new roman",12,"italic bold"),bg="#EEF1FF",
                    width=10,fg="black",height=2,relief=GROOVE,bd=5)
minvaluelabel.place(x=250,y=60)

#Defines the size of array that should be generated
minvalue= Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,bg="#B1AFFF",font=("arial",14,"italic bold"),
                    relief=GROOVE,bd=2,width=10)
minvalue.place(x=370,y=60)

#Defines the tag of size of array that should be generated
maxvaluelabel=Label(root,text ="Max Value: " ,font=("new roman",12,"italic bold"),bg="#EEF1FF",
                    width=10,fg="black",height=2,relief=GROOVE,bd=5)
maxvaluelabel.place(x=500,y=60)

#Defines the size of array that should be generated
maxvalue= Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,bg="#B1AFFF",font=("arial",14,"italic bold"),
                    relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=60)

# start the algorithm
start= Button(root,text="Start",bg="#BDBDD7",font=("arial",12,"italic bold"),relief=SUNKEN,
                        activebackground="#05945B",activeforeground="white",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)

#speed of the algorithm
speedlabel=Label(root,text ="Speed: ", font=("new roman",12,"italic bold"),bg="#EEF1FF",
                    width=10,fg="black",height=2,relief=GROOVE,bd=5)
speedlabel.place(x=400,y=0)

speedscale= Scale(root,from_=0.1,to=5.0,resolution=0.2,length=200,digits=2,bg="#B1AFFF",orient=HORIZONTAL,font=("arial",14,"italic bold"),
                    relief=GROOVE,bd=2,width=10)
speedscale.place(x=520,y=0)

graph_label=Button(root,text="Graphical Reprsentation",bg="#F7A4A4",font=("arial",12,"italic bold"),relief=SUNKEN,
                        activebackground="#05945B",activeforeground="white",bd=5,width=20,command=graph)
graph_label.place(x=350,y=120)


#define the box in which whole algorithm will be visualize 
canvas=Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=180)

root.mainloop() # main driver which will run whole Gui
