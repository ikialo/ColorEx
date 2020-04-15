from tkinter import *
from tkinter import ttk
from ..common.datastructures import HeatMap, Tile
from ..common.themes import Themes
import math



class HeatMapWindow(Frame):


    
    def __init__(self, parent, heatmap=None, tile_size=(60,60),
                 canvas_size_factor=0.9, canvas_top_margin=20,
                 canvas_bottom_margin=20, ylabel_margin=10,
                 xlabel_margin=2, **kwargs):

        if(heatmap == None):
            raise Exception
        
        # call parent initialize
        Frame.__init__(self, parent, **kwargs)


        # declare some constants.
        self.const = dict()
        self.const["TILESIZE"] = tile_size
        self.const["CANVAS_SIZE_FACTOR"] = canvas_size_factor
        self.const["CANVAS_TOP_MARGIN"] = canvas_top_margin
        self.const["CANVAS_BOTTOM_MARGIN"] = canvas_bottom_margin
        self.const["YLABEL_MARGIN"] = ylabel_margin
        self.const["XLABEL_MARGIN"] = xlabel_margin
        self.const["YCOORD_TITLE"] = 30
        self.const["YCOORD_SUBTITLE"] = 70
        self.const["PLANE_TOP_MARGIN"] = 110
        self.const["AXIS_TICK_LENGTH"] = 10

    

        # set some heat map properties
        self.title = heatmap.title
        self.subtitle = heatmap.subtitle
        self.xaxis_labels = heatmap.grid[0][1:]
        self.yaxis_labels = list(map(lambda row: row[0], heatmap.grid[1:]))
        self.heatmap = heatmap
        self.heatmap_data = list(map(lambda row: row[1:], heatmap.grid[1:]))


        # create layout frames
        self.bottom_frame = Frame(self)
        self.right_frame = Frame(self)
        self.left_frame = Frame(self)
        self.parent = parent
        
        # create a canvas object, and set window properties.
        self.canvas_width = int(
            self.const["CANVAS_SIZE_FACTOR"]*self.parent.winfo_screenwidth())
        self.canvas_height = int(
            self.const["CANVAS_SIZE_FACTOR"]*self.parent.winfo_screenheight())

        # set window minimum size.
        self.parent.minsize(width=400,
            height=300)


        # position the window
        self.parent.geometry(str(self.canvas_width)+"x"+str(self.canvas_height)+"+0+0")
        
        # initialize the canvas and render.
        self.canvas = Canvas(self.left_frame, bg="white",
            width=self.canvas_width, height=self.canvas_height)
        self.init_canvas()
        self.render()
        
        # bind some events to handlers
        self.left_frame.bind("<Configure>",self.on_configure)
        


    def init_canvas(self):
        # draw the titles on the canvas.
        # title
        self.canvas.create_text(0,
        self.const["YCOORD_TITLE"],
        anchor="center", text=self.title,
        fill='black', font=('Tahoma',26), tag="header")
        # subtitle
        self.canvas.create_text(0,
        self.const["YCOORD_SUBTITLE"],
        anchor="center", text=self.subtitle,
        fill='gray', font=('Tahoma',15), tag="header")        

        

        # draw the cartesian plane on the canvas at canvas origin first.
        # vertical axis
        yaxis_start = (0,0)
        yaxis_end =  (0,(self.const["TILESIZE"][1]*len(self.yaxis_labels)))
        self.canvas.create_line(yaxis_start[0],yaxis_start[1],
            yaxis_end[0], yaxis_end[1], tag="heatmap")
        for n in range(len(self.yaxis_labels)):
            point = (yaxis_start[0], yaxis_start[1]+(self.const["TILESIZE"][1]*n))
            label = self.yaxis_labels[n]
            self.canvas_draw_yaxis_tick(point, label)
        
        # horizontal axis
        xaxis_start = yaxis_end
        xaxis_end = (xaxis_start[0]+self.const["TILESIZE"][1]*len(self.xaxis_labels),
            xaxis_start[1])
        self.canvas.create_line(xaxis_start[0], xaxis_start[1],
            xaxis_end[0], xaxis_end[1], tag="heatmap")
        for n in range(len(self.xaxis_labels)):
            point = (xaxis_start[0]+(self.const["TILESIZE"][0]*(n+1)), xaxis_start[1])
            label = self.xaxis_labels[n]
            self.canvas_draw_xaxis_tick(point, label)


        plot_start = yaxis_start

        # plot all tiles into the heat map cartesian plane
        for i in range(len(self.xaxis_labels)):
            for j in range(len(self.yaxis_labels)):
                '''                
                alpha_color = Themes().generate_alpha_rgbcolor(
                    self.heatmap_data[j][i].rgb,
                    self.heatmap_data[j][i].alpha)
                '''
                alpha_color = Themes().generate_alpha_rgb_bicolor(
                    (128,0,51),(255,213,229),self.heatmap_data[j][i].alpha)
                alpha_color_hex = Themes().decimal_to_rgb_hex(
                    alpha_color)
                point = self.canvas_get_new_point(plot_start,
                    i*self.const["TILESIZE"][0],
                    j*self.const["TILESIZE"][1])
                self.canvas_draw_tile(point,alpha_color_hex,
                    self.heatmap_data[j][i], width=0, outline="white")
                
        
        # center the heatmap horizontally.
        self.canvas_center_header()
        self.canvas_center_heatmap(centerAlongX=True, centerAlongY=True)



        # create some scrollbars
        self.scroll_y = Scrollbar(self.right_frame,
            command=self.canvas.yview, orient=VERTICAL)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x = Scrollbar(self.bottom_frame,
            command=self.canvas.xview, orient=HORIZONTAL)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)





    def canvas_center_heatmap(self,centerAlongX=True, centerAlongY=True):
        ''' centers the cartesian plane illustrating the heat map '''
        tag = "heatmap"
        bbox = self.canvas.bbox(tag)
        bbox_x1 = bbox[0]
        bbox_x2 = bbox[2]
        bbox_y1 = bbox[1]
        bbox_width = bbox_x2 - bbox_x1
        canvas_width = self.canvas_width
        final_x = (canvas_width/2) - (bbox_width/2)
        dx = final_x - bbox_x1
        #self.canvas.move(tag, dx,0)
        if(centerAlongX):
            for item in self.canvas.find_withtag(tag):
                self.canvas.move(item, dx, 0)
        if(centerAlongY):
            for item in self.canvas.find_withtag(tag):
                self.canvas.move(item,0,self.const["PLANE_TOP_MARGIN"])
        self.canvas_update_scrollregion()


    def canvas_center_header(self):
        ''' centers the header of the heatmap containing title, subtitle. '''
        tag = "header"
        bbox = self.canvas.bbox(tag)
        bbox_x1 = bbox[0]
        bbox_x2 = bbox[2]
        bbox_width = bbox_x2 - bbox_x1
        canvas_width = self.canvas_width
        final_x = (canvas_width/2) - (bbox_width/2)
        dx = final_x - bbox_x1
        self.canvas.move(tag, dx, 0)
        self.canvas_update_scrollregion()








    def canvas_get_new_point(self, old_point, dx, dy):
        old_x = old_point[0]
        old_y = old_point[1]
        new_x = old_x + dx
        new_y = old_y + dy
        return (new_x, new_y)




    def canvas_draw_tile(self, topleft_point, fill_color, tile, width=0, outline="black"):
        xint = self.const["TILESIZE"][0]
        yint = self.const["TILESIZE"][1]
        x1 = topleft_point[0]
        y1 = topleft_point[1]
        x2 = topleft_point[0]+xint
        y2 = topleft_point[1]+yint
        self.canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color,
            width=width, outline=outline,tag="heatmap")
        #self.canvas.create_text(x1, y1,
        #    text=tile.value, tag="heatmap")






    def canvas_draw_yaxis_tick(self, point, label):
        # determine the coordinates
        x1 = point[0]
        y1 = point[1]
        end = (point[0]-self.const["AXIS_TICK_LENGTH"],point[1])
        x2 = end[0]
        y2 = end[1]
        # draw the tick
        self.canvas.create_line(x1,y1,x2,y2, tag="heatmap")
        # label the tick
        label_point = list()
        label_point.append(point[0]-self.const["AXIS_TICK_LENGTH"]
            -self.const["YLABEL_MARGIN"])
        label_point.append(point[1])
        self.canvas.create_text(label_point[0],
            label_point[1]+self.const["TILESIZE"][1]/2,
            text=label, anchor="e", tag="heatmap")



    def canvas_draw_xaxis_tick(self, point, label):
        # determine the coordinates
        x1 = point[0]
        y1 = point[1]
        end = (point[0],point[1]+self.const["AXIS_TICK_LENGTH"])
        x2 = end[0]
        y2 = end[1]
        # draw the tick
        self.canvas.create_line(x1,y1,x2,y2, tag="heatmap")
        # label the tick
        label_point = list()
        label_point.append(point[0])
        label_point.append(point[1]+self.const["AXIS_TICK_LENGTH"]
            +self.const["XLABEL_MARGIN"])
        self.canvas.create_text(label_point[0]-self.const["TILESIZE"][0]/2,
            label_point[1],
            text=label, anchor="e", angle=90, tag="heatmap")







    def canvas_update_scrollregion(self):
        region = (0,0,self.canvas.bbox(ALL)[2],self.canvas.bbox(ALL)[3])
        self.canvas.configure(scrollregion=region)




    def on_configure(self,event):
        if(self.canvas.winfo_width()!=1):
            self.canvas_width = self.canvas.winfo_width()
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_center_header()
            self.canvas_center_heatmap(centerAlongX=True, centerAlongY=False)
        self.canvas_update_scrollregion()





    def render(self):
        self.pack(fill=BOTH, expand=True, side=TOP)
        self.bottom_frame.pack(fill=X, expand=False, side=BOTTOM)
        self.right_frame.pack(fill=Y, expand=False, side=RIGHT)
        self.left_frame.pack(fill=BOTH, expand=True, side=LEFT)
        self.canvas.pack(fill=BOTH, expand=True, padx=0, pady=0, side=LEFT)
        self.scroll_y.pack(fill=Y, side=RIGHT)
        self.scroll_x.pack(fill=X, side=BOTTOM)





