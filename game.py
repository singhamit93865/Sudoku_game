from tkinter import *
class game:
    def __init__(self,root):
        self.sudoku_values = [[0,0,0,0,0,0,0,0,0,0] for i in range(9)]
        #initializing the 81 values which will need for end calcaulations
        self.entry_in_index01 = IntVar()
        self.entry_in_index02 = IntVar()
        self.entry_in_index03 = IntVar()
        self.entry_in_index04 = IntVar()
        self.entry_in_index05 = IntVar()
        self.entry_in_index06 = IntVar()
        self.entry_in_index07 = IntVar()
        self.entry_in_index08 = IntVar()
        self.entry_in_index09 = IntVar()
                
        self.entry_in_index11 = IntVar()
        self.entry_in_index12 = IntVar()
        self.entry_in_index13 = IntVar()
        self.entry_in_index14 = IntVar()
        self.entry_in_index15 = IntVar()
        self.entry_in_index16 = IntVar()
        self.entry_in_index17 = IntVar()
        self.entry_in_index18 = IntVar()
        self.entry_in_index19 = IntVar()
                
        self.entry_in_index21 = IntVar()
        self.entry_in_index22 = IntVar()
        self.entry_in_index23 = IntVar()
        self.entry_in_index24 = IntVar()
        self.entry_in_index25 = IntVar()
        self.entry_in_index26 = IntVar()
        self.entry_in_index27 = IntVar()
        self.entry_in_index28 = IntVar()
        self.entry_in_index29 = IntVar()
                
        self.entry_in_index31 = IntVar()
        self.entry_in_index32 = IntVar()
        self.entry_in_index33 = IntVar()
        self.entry_in_index34 = IntVar()
        self.entry_in_index35 = IntVar()
        self.entry_in_index36 = IntVar()
        self.entry_in_index37 = IntVar()
        self.entry_in_index38 = IntVar()
        self.entry_in_index39 = IntVar()
                
        self.entry_in_index41 = IntVar()
        self.entry_in_index42 = IntVar()
        self.entry_in_index43 = IntVar()
        self.entry_in_index44 = IntVar()
        self.entry_in_index45 = IntVar()
        self.entry_in_index46 = IntVar()
        self.entry_in_index47 = IntVar()
        self.entry_in_index48 = IntVar()
        self.entry_in_index49 = IntVar()
                
        self.entry_in_index51 = IntVar()
        self.entry_in_index52 = IntVar()
        self.entry_in_index53 = IntVar()
        self.entry_in_index54 = IntVar()
        self.entry_in_index55 = IntVar()
        self.entry_in_index56 = IntVar()
        self.entry_in_index57 = IntVar()
        self.entry_in_index58 = IntVar()
        self.entry_in_index59 = IntVar()
                
        self.entry_in_index61 = IntVar()
        self.entry_in_index62 = IntVar()
        self.entry_in_index63 = IntVar()
        self.entry_in_index64 = IntVar()
        self.entry_in_index65 = IntVar()
        self.entry_in_index66 = IntVar()
        self.entry_in_index67 = IntVar()
        self.entry_in_index68 = IntVar()
        self.entry_in_index69 = IntVar()
                
        self.entry_in_index71 = IntVar()
        self.entry_in_index72 = IntVar()
        self.entry_in_index73 = IntVar()
        self.entry_in_index74 = IntVar()
        self.entry_in_index75 = IntVar()
        self.entry_in_index76 = IntVar()
        self.entry_in_index77 = IntVar()
        self.entry_in_index78 = IntVar()
        self.entry_in_index79 = IntVar()
                
        self.entry_in_index81 = IntVar()
        self.entry_in_index82 = IntVar()
        self.entry_in_index83 = IntVar()
        self.entry_in_index84 = IntVar()
        self.entry_in_index85 = IntVar()
        self.entry_in_index86 = IntVar()
        self.entry_in_index87 = IntVar()
        self.entry_in_index88 = IntVar()
        self.entry_in_index89 = IntVar()

    	#Making Main Frame in which whole page will ccome in existence
        self.base=Frame(root,width =1400, height = 50, bg = 'grey',padx=10,pady=10)
        self.base.propagate(0)

        time = Label(self.base,text="Time",bg='grey',font=("Verdana",15),fg='orange',padx = 300)
        control = Label(self.base,text="Controls",bg='grey',font=("Verdana",15),fg='orange',padx = 300)
        time.pack(side = 'left')
        control.pack(side = 'right')
        self.base.pack(fill=X)

        #Make gap between top label and sudoku grid or we can use place instead of this 
        self.gap = Frame(root,height=100)
        self.gap.pack()

        #this is fra pattern for the canvas so the grid can exit on canvas
        self.for_grid_frame = Frame(root,width = 50, height = 800 )
            
        def checkered(canvas, line_distance):
           # vertical lines at an interval of "line_distance" pixel
            for x in range(line_distance,440,line_distance):
                canvas.create_line(x+40, 80, x+40, 440, fill="#476042")
           # horizontal lines at an interval of "line_distance" pixel
            for y in range(line_distance,440,line_distance):
                canvas.create_line(80, y+40, 440, y+40, fill="#476042")
            #rectangle
            canvas.create_rectangle(80,80,440,440)
            canvas.create_rectangle(79,79,441,441)
            canvas.create_rectangle(78,78,442,442)
            #1st line
            canvas.create_line(199,80,199,440)
            canvas.create_line(200,80,200,440)
            canvas.create_line(201,80,201,440)
            #2nd line
            canvas.create_line(319,80,319,440)
            canvas.create_line(320,80,320,440)
            canvas.create_line(321,80,321,440)
            #3rd line
            canvas.create_line(80,199,440,199)
            canvas.create_line(80,200,440,200)
            canvas.create_line(80,201,440,201)
            #4th line
            canvas.create_line(80,319,440,319)
            canvas.create_line(80,320,440,320)
            canvas.create_line(80,321,440,321)
            # this is the row no 0
            self.entry_in_index01 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index02 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index03 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index04 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index05 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index06 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index07 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index08 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index09 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            # this is the row no 1
            self.entry_in_index11 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index12 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index13 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index14 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index15 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index16 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index17 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index18 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index19 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            # this is the row no 2
            self.entry_in_index21 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index22 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index23 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index24 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index25 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index26 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index27 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index28 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index29 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 3
            self.entry_in_index31 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index32 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index33 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index34 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index35 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index36 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index37 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index38 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index39 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 4
            self.entry_in_index41 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index42 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index43 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index44 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index45 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index46 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index47 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index48 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index49 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 5
            self.entry_in_index51 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index52 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index53 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index54 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index55 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index56 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index57 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index58 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index59 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 6
            self.entry_in_index61 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index62 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index63 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index64 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index65 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index66 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index67 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index68 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index69 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 7
            self.entry_in_index71 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index72 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index73 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index74 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index75 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index76 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index77 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index78 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index79 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			# this is the row no 8
            self.entry_in_index81 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= 'blue',height = 1)
            self.entry_in_index82 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index83 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index84 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index85 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index86 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index87 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index88 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
            self.entry_in_index89 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= 'blue',height = 1)
			
			#placing the entring boxex
            self.entry_in_index01.place(x=82,y=82)
            self.entry_in_index02.place(x=122,y=82)
            self.entry_in_index03.place(x=162,y=82)
            self.entry_in_index04.place(x=203,y=82)
            self.entry_in_index05.place(x=242,y=82)
            self.entry_in_index06.place(x=282,y=82)
            self.entry_in_index07.place(x=323,y=82)
            self.entry_in_index08.place(x=362,y=82)
            self.entry_in_index09.place(x=402,y=82)

            self.entry_in_index11.place(x=82,y=122)
            self.entry_in_index12.place(x=122,y=122)
            self.entry_in_index13.place(x=162,y=122)
            self.entry_in_index14.place(x=203,y=122)
            self.entry_in_index15.place(x=242,y=122)
            self.entry_in_index16.place(x=282,y=122)
            self.entry_in_index17.place(x=323,y=122)
            self.entry_in_index18.place(x=362,y=122)
            self.entry_in_index19.place(x=402,y=122)

            self.entry_in_index21.place(x=82,y=162)
            self.entry_in_index22.place(x=122,y=162)
            self.entry_in_index23.place(x=162,y=162)
            self.entry_in_index24.place(x=203,y=162)
            self.entry_in_index25.place(x=242,y=162)
            self.entry_in_index26.place(x=282,y=162)
            self.entry_in_index27.place(x=323,y=162)
            self.entry_in_index28.place(x=362,y=162)
            self.entry_in_index29.place(x=402,y=162)

            self.entry_in_index31.place(x=82,y=203)
            self.entry_in_index32.place(x=122,y=203)
            self.entry_in_index33.place(x=162,y=203)
            self.entry_in_index34.place(x=203,y=203)
            self.entry_in_index35.place(x=242,y=203)
            self.entry_in_index36.place(x=282,y=203)
            self.entry_in_index37.place(x=323,y=203)
            self.entry_in_index38.place(x=362,y=203)
            self.entry_in_index39.place(x=402,y=203)

            self.entry_in_index41.place(x=82,y=242)
            self.entry_in_index42.place(x=122,y=242)
            self.entry_in_index43.place(x=162,y=242)
            self.entry_in_index44.place(x=203,y=242)
            self.entry_in_index45.place(x=242,y=242)
            self.entry_in_index46.place(x=282,y=242)
            self.entry_in_index47.place(x=323,y=242)
            self.entry_in_index48.place(x=362,y=242)
            self.entry_in_index49.place(x=402,y=242)
            
            self.entry_in_index51.place(x=82,y=282)
            self.entry_in_index52.place(x=122,y=282)
            self.entry_in_index53.place(x=162,y=282)
            self.entry_in_index54.place(x=203,y=282)
            self.entry_in_index55.place(x=242,y=282)
            self.entry_in_index56.place(x=282,y=282)
            self.entry_in_index57.place(x=323,y=282)
            self.entry_in_index58.place(x=362,y=282)
            self.entry_in_index59.place(x=402,y=282)

            self.entry_in_index61.place(x=82,y=323)
            self.entry_in_index62.place(x=122,y=322)
            self.entry_in_index63.place(x=162,y=323)
            self.entry_in_index64.place(x=203,y=323)
            self.entry_in_index65.place(x=242,y=323)
            self.entry_in_index66.place(x=282,y=323)
            self.entry_in_index67.place(x=323,y=323)
            self.entry_in_index68.place(x=362,y=323)
            self.entry_in_index69.place(x=402,y=323)

            self.entry_in_index71.place(x=82,y=362)
            self.entry_in_index72.place(x=122,y=362)
            self.entry_in_index73.place(x=162,y=362)
            self.entry_in_index74.place(x=203,y=362)
            self.entry_in_index75.place(x=242,y=362)
            self.entry_in_index76.place(x=282,y=362)
            self.entry_in_index77.place(x=323,y=362)
            self.entry_in_index78.place(x=362,y=362)
            self.entry_in_index79.place(x=402,y=362)

            self.entry_in_index81.place(x=82,y=402)
            self.entry_in_index82.place(x=122,y=402)
            self.entry_in_index83.place(x=162,y=402)
            self.entry_in_index84.place(x=203,y=402)
            self.entry_in_index85.place(x=242,y=402)
            self.entry_in_index86.place(x=282,y=402)
            self.entry_in_index87.place(x=323,y=402)
            self.entry_in_index88.place(x=362,y=402)
            self.entry_in_index89.place(x=402,y=402)
                     
        #Making Canvas for the grid pattern
        canvas_width = 500
        canvas_height =500
        w = Canvas(root,width=canvas_width,height=canvas_height,highlightthickness=0)
        w.place(x=150,y=100)
        #Calling function grid pattern 
        checkered(w,40)
 
        self.for_grid_frame.pack(after = self.gap,anchor = 'w',padx='300')


        #command for button
        def cm_normal():
            no1.config(text="1")
            no2.config(text="2")
            no3.config(text="3")
            no4.config(text="4")
            no5.config(text="5")
            no6.config(text="6")
            no7.config(text="7")
            no8.config(text="8")
            no9.config(text="9")

            lab1.config(text="")
            lab2.config(text="")
            lab3.config(text="")
            lab4.config(text="")
            lab5.config(text="")
            lab6.config(text="")
            lab7.config(text="")
            lab8.config(text="")
            lab9.config(text="")

            lab1.place(x=1001,y=201)
            lab2.place(x=1061,y=201)
            lab3.place(x=1121,y=201)
            lab4.place(x=1001,y=251)
            lab5.place(x=1061,y=251)
            lab6.place(x=1121,y=251)
            lab7.place(x=1001,y=301)
            lab8.place(x=1061,y=301)
            lab9.place(x=1121,y=301)
            
            normal.config(bg='purple',fg='white')
            corner.config(fg='purple',bg='white')
            center.config(fg='purple',bg='white')

        def cm_corner():
            no1.config(text="")
            no2.config(text="")
            no3.config(text="")
            no4.config(text="")
            no5.config(text="")
            no6.config(text="")
            no7.config(text="")
            no8.config(text="")
            no9.config(text="")

            lab1.config(text='1')
            lab2.config(text='2')
            lab3.config(text='3')
            lab4.config(text='4')
            lab5.config(text='5')
            lab6.config(text='6')
            lab7.config(text='7')
            lab8.config(text='8')
            lab9.config(text='9')
            lab1.place(x=1001,y=201)
            lab2.place(x=1078,y=201)
            lab3.place(x=1149,y=201)
            lab4.place(x=1001,y=251)
            lab5.place(x=1078,y=251)
            lab6.place(x=1149,y=251)
            lab7.place(x=1001,y=301)
            lab8.place(x=1078,y=301)
            lab9.place(x=1149,y=301)

            corner.config(bg='purple',fg='white')
            normal.config(fg='purple',bg='white')
            center.config(fg='purple',bg='white')

        def cm_center():
            no1.config(text="")
            no2.config(text="")
            no3.config(text="")
            no4.config(text="")
            no5.config(text="")
            no6.config(text="")
            no7.config(text="")
            no8.config(text="")
            no9.config(text="")

            lab1.config(text='1')
            lab1.place(x=1018,y=210)
            lab2.config(text='2')
            lab2.place(x=1077,y=210)
            lab3.config(text='3')
            lab3.place(x=1137,y=210)
            lab4.config(text='4')
            lab4.place(x=1018,y=260)
            lab5.config(text='5')
            lab5.place(x=1077,y=260)
            lab6.config(text='6')
            lab6.place(x=1137,y=260)
            lab7.config(text='7')
            lab7.place(x=1018,y=310)
            lab8.config(text='8')
            lab8.place(x=1077,y=310)
            lab9.config(text='9')
            lab9.place(x=1137,y=310)
            center.config(bg='purple',fg='white')
            corner.config(fg='purple',bg='white')
            normal.config(fg='purple',bg='white')
        
        #here the big buttons came with their placement
        normal = Button(text = "Normal" , fg='purple' , font=("Verdana",14,'bold'),width = 7,command=cm_normal)
        corner = Button(text = "Corner" , fg='purple' , font=("Verdana",14,'bold'),width = 7,command=cm_corner) 
        center = Button(text = "Center" , fg='purple' , font=("Verdana",14,'bold'),width = 7,command=cm_center)
        colour = Button(text = "Colour" , fg='purple' , font=("Verdana",14,'bold'),width = 7)
        delete = Button(text = "Delete" , fg='purple' , font=("Verdana",14,'bold'),width = 12)
        undo = Button(text = "Undo" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        redo = Button(text = "Redo" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        restart = Button(text = "Restart" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        check = Button(text = "Check" , fg='purple' , font=("Verdana",14,'bold'),width = 10,command = self.checker)

        normal.place(x=875,y=200)
        corner.place(x=875,y=250)
        center.place(x=875,y=300)
        colour.place(x=875,y=350)
        delete.place(x=1002,y=350)
        undo.place(x=875,y=400)
        redo.place(x=1025,y=400)
        restart.place(x=875,y=450)
        check.place(x=1025,y=450)

        #here no and their placement are their.  
        no1 = Button(text = "1" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no2 = Button(text = "2" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no3 = Button(text = "3" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no4 = Button(text = "4" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no5 = Button(text = "5" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no6 = Button(text = "6" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no7 = Button(text = "7" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no8 = Button(text = "8" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no9 = Button(text = "9" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no1.place(x=1000,y=200)
        no2.place(x=1060,y=200)
        no3.place(x=1120,y=200)
        no4.place(x=1000,y=250)
        no5.place(x=1060,y=250)
        no6.place(x=1120,y=250)
        no7.place(x=1000,y=300)
        no8.place(x=1060,y=300)
        no9.place(x=1120,y=300)
        
        #labels of nos
        lab1=Label(root,text='1',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab2=Label(root,text='2',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab3=Label(root,text='3',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab4=Label(root,text='4',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab5=Label(root,text='5',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab6=Label(root,text='6',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab7=Label(root,text='7',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab8=Label(root,text='8',font=("Verdana",9,'bold'),bg='purple',fg='white')
        lab9=Label(root,text='9',font=("Verdana",9,'bold'),bg='purple',fg='white')
        
        # to give the frame some weight to look better
        self.gap = Frame(root,height=200)
        self.gap.pack()

        # other functions or topics to do
        def get_entries_from_user():
            pass
        def ans_valiadtor():
            pass
        def others():
            pass
    # string values in computer memory to calculate end result
    def checker (self):
        
        self.sudoku_values[0][0]= self.entry_in_index01.get("1.0",'end-1c')
        self.sudoku_values[0][1]= self.entry_in_index02.get("1.0",'end-1c')
        self.sudoku_values[0][2]= self.entry_in_index03.get("1.0",'end-1c')
        self.sudoku_values[0][3]= self.entry_in_index04.get("1.0",'end-1c')
        self.sudoku_values[0][4]= self.entry_in_index05.get("1.0",'end-1c')
        self.sudoku_values[0][5]= self.entry_in_index06.get("1.0",'end-1c')
        self.sudoku_values[0][6]= self.entry_in_index07.get("1.0",'end-1c')
        self.sudoku_values[0][7]= self.entry_in_index08.get("1.0",'end-1c')
        self.sudoku_values[0][8]= self.entry_in_index09.get("1.0",'end-1c')
        
        self.sudoku_values[1][0]= self.entry_in_index11.get("1.0",'end-1c')
        self.sudoku_values[1][1]= self.entry_in_index12.get("1.0",'end-1c')
        self.sudoku_values[1][2]= self.entry_in_index13.get("1.0",'end-1c')
        self.sudoku_values[1][3]= self.entry_in_index14.get("1.0",'end-1c')
        self.sudoku_values[1][4]= self.entry_in_index15.get("1.0",'end-1c')
        self.sudoku_values[1][5]= self.entry_in_index16.get("1.0",'end-1c')
        self.sudoku_values[1][6]= self.entry_in_index17.get("1.0",'end-1c')
        self.sudoku_values[1][7]= self.entry_in_index18.get("1.0",'end-1c')
        self.sudoku_values[1][8]= self.entry_in_index19.get("1.0",'end-1c')
        
        self.sudoku_values[2][0]= self.entry_in_index21.get("1.0",'end-1c')
        self.sudoku_values[2][1]= self.entry_in_index22.get("1.0",'end-1c')
        self.sudoku_values[2][2]= self.entry_in_index23.get("1.0",'end-1c')
        self.sudoku_values[2][3]= self.entry_in_index24.get("1.0",'end-1c')
        self.sudoku_values[2][4]= self.entry_in_index25.get("1.0",'end-1c')
        self.sudoku_values[2][5]= self.entry_in_index26.get("1.0",'end-1c')
        self.sudoku_values[2][6]= self.entry_in_index27.get("1.0",'end-1c')
        self.sudoku_values[2][7]= self.entry_in_index28.get("1.0",'end-1c')
        self.sudoku_values[2][8]= self.entry_in_index29.get("1.0",'end-1c')
        
        self.sudoku_values[3][0]= self.entry_in_index31.get("1.0",'end-1c')
        self.sudoku_values[3][1]= self.entry_in_index32.get("1.0",'end-1c')
        self.sudoku_values[3][2]= self.entry_in_index33.get("1.0",'end-1c')
        self.sudoku_values[3][3]= self.entry_in_index34.get("1.0",'end-1c')
        self.sudoku_values[3][4]= self.entry_in_index35.get("1.0",'end-1c')
        self.sudoku_values[3][5]= self.entry_in_index36.get("1.0",'end-1c')
        self.sudoku_values[3][6]= self.entry_in_index37.get("1.0",'end-1c')
        self.sudoku_values[3][7]= self.entry_in_index38.get("1.0",'end-1c')
        self.sudoku_values[3][8]= self.entry_in_index39.get("1.0",'end-1c')
        
        self.sudoku_values[4][0]= self.entry_in_index41.get("1.0",'end-1c')
        self.sudoku_values[4][1]= self.entry_in_index42.get("1.0",'end-1c')
        self.sudoku_values[4][2]= self.entry_in_index43.get("1.0",'end-1c')
        self.sudoku_values[4][3]= self.entry_in_index44.get("1.0",'end-1c')
        self.sudoku_values[4][4]= self.entry_in_index45.get("1.0",'end-1c')
        self.sudoku_values[4][5]= self.entry_in_index46.get("1.0",'end-1c')
        self.sudoku_values[4][6]= self.entry_in_index47.get("1.0",'end-1c')
        self.sudoku_values[4][7]= self.entry_in_index48.get("1.0",'end-1c')
        self.sudoku_values[4][8]= self.entry_in_index49.get("1.0",'end-1c')
        
        self.sudoku_values[5][0]= self.entry_in_index51.get("1.0",'end-1c')
        self.sudoku_values[5][1]= self.entry_in_index52.get("1.0",'end-1c')
        self.sudoku_values[5][2]= self.entry_in_index53.get("1.0",'end-1c')
        self.sudoku_values[5][3]= self.entry_in_index54.get("1.0",'end-1c')
        self.sudoku_values[5][4]= self.entry_in_index55.get("1.0",'end-1c')
        self.sudoku_values[5][5]= self.entry_in_index56.get("1.0",'end-1c')
        self.sudoku_values[5][6]= self.entry_in_index57.get("1.0",'end-1c')
        self.sudoku_values[5][7]= self.entry_in_index58.get("1.0",'end-1c')
        self.sudoku_values[5][8]= self.entry_in_index59.get("1.0",'end-1c')
        
        self.sudoku_values[6][0]= self.entry_in_index61.get("1.0",'end-1c')
        self.sudoku_values[6][1]= self.entry_in_index62.get("1.0",'end-1c')
        self.sudoku_values[6][2]= self.entry_in_index63.get("1.0",'end-1c')
        self.sudoku_values[6][3]= self.entry_in_index64.get("1.0",'end-1c')
        self.sudoku_values[6][4]= self.entry_in_index65.get("1.0",'end-1c')
        self.sudoku_values[6][5]= self.entry_in_index66.get("1.0",'end-1c')
        self.sudoku_values[6][6]= self.entry_in_index67.get("1.0",'end-1c')
        self.sudoku_values[6][7]= self.entry_in_index68.get("1.0",'end-1c')
        self.sudoku_values[6][8]= self.entry_in_index69.get("1.0",'end-1c')
        
        self.sudoku_values[7][0]= self.entry_in_index71.get("1.0",'end-1c')
        self.sudoku_values[7][1]= self.entry_in_index72.get("1.0",'end-1c')
        self.sudoku_values[7][2]= self.entry_in_index73.get("1.0",'end-1c')
        self.sudoku_values[7][3]= self.entry_in_index74.get("1.0",'end-1c')
        self.sudoku_values[7][4]= self.entry_in_index75.get("1.0",'end-1c')
        self.sudoku_values[7][5]= self.entry_in_index76.get("1.0",'end-1c')
        self.sudoku_values[7][6]= self.entry_in_index77.get("1.0",'end-1c')
        self.sudoku_values[7][7]= self.entry_in_index78.get("1.0",'end-1c')
        self.sudoku_values[7][8]= self.entry_in_index79.get("1.0",'end-1c')
        
        self.sudoku_values[8][0]= self.entry_in_index81.get("1.0",'end-1c')
        self.sudoku_values[8][1]= self.entry_in_index82.get("1.0",'end-1c')
        self.sudoku_values[8][2]= self.entry_in_index83.get("1.0",'end-1c')
        self.sudoku_values[8][3]= self.entry_in_index84.get("1.0",'end-1c')
        self.sudoku_values[8][4]= self.entry_in_index85.get("1.0",'end-1c')
        self.sudoku_values[8][5]= self.entry_in_index86.get("1.0",'end-1c')
        self.sudoku_values[8][6]= self.entry_in_index87.get("1.0",'end-1c')
        self.sudoku_values[8][7]= self.entry_in_index88.get("1.0",'end-1c')
        self.sudoku_values[8][8]= self.entry_in_index89.get("1.0",'end-1c')
        for i in range(9):
            for j in range(9):
                print(self.sudoku_values[i][j], end = ' ')
            print()            

#starting of tkinter
root = Tk()
obj = game(root)
root.title("Sudoku! Lets Play ")
root.mainloop()
