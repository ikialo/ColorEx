from tkinter import *
from tkinter import ttk
from ..common.datastructures import HeatMap, Tile
from ..common.themes import Themes
import math



class HeatMapWindow(Frame):


    
    def __init__(self, parent,heatmap=None, **kwargs):

        if(heatmap == None):
            raise Exception
        
        # call parent initialize
        Frame.__init__(self, parent, **kwargs)
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
        canvas_width_factor = 0.9
        canvas_height_factor = 0.9
        self.canvas_width = int(
            canvas_width_factor*self.parent.winfo_screenwidth())
        self.canvas_height = int(
            canvas_height_factor*self.parent.winfo_screenheight())
        # set window minimum size.
        self.parent.minsize(width=self.canvas_width,
            height=self.canvas_height)
        # position the window
        self.parent.geometry("1x1+0+0")
        # initialize the canvas and render.
        self.canvas = Canvas(self.left_frame, bg="white",
            width=self.canvas_width, height=self.canvas_height)
        self.init_canvas()
        # center the heatmap in the canvas
        self.canvas_center_heatmap()
        self.render()
        # bind some events to handlers
        #self.left_frame.bind("<Configure>",self.on_configure)
        


    def init_canvas(self):
        # init the canvas
        margin_x = 0.15
        margin_y = 0.15
        # draw the title on the canvas.
        self.canvas.create_text(self.canvas_width/2,28,
            anchor="center", text=self.title,
            fill='black', font=('Tahoma',26))
        # draw the cartesian plane on the canvas.
        cartesian_points = self.canvas_draw_cartesian(
            len(self.xaxis_labels),len(self.yaxis_labels),
            self.xaxis_labels, self.yaxis_labels, margin_x, margin_y)
        # draw the tiles on the cartesian plane.
        xint = cartesian_points["xaxis"]["axis_interval"]
        yint = cartesian_points["yaxis"]["axis_interval"]
        for i in range(len(self.xaxis_labels)):
            for j in range(len(self.yaxis_labels)):
                '''                
                alpha_color = Themes().generate_alpha_rgbcolor(
                    self.heatmap_data[j][i].rgb,
                    self.heatmap_data[j][i].alpha)
                '''
                alpha_color = Themes().generate_alpha_rgb_bicolor(
                    (212,0,1),(255,204,0),self.heatmap_data[j][i].alpha)
                alpha_color_hex = Themes().decimal_to_rgb_hex(
                    alpha_color)
                self.canvas_draw_tile(self.canvas_get_new_point(
                    cartesian_points["origin"], i*xint, j*yint),xint,
                    yint, alpha_color_hex)      
        self.canvas.addtag_all("all")
        # create some scrollbars
        self.scroll_y = Scrollbar(self.right_frame,
            command=self.canvas.yview, orient=VERTICAL)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x = Scrollbar(self.bottom_frame,
            command=self.canvas.xview, orient=HORIZONTAL)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)


    def canvas_get_new_point(self, old_point, dx, dy):
        old_x = old_point[0]
        old_y = old_point[1]
        new_x = old_x + dx
        new_y = old_y - dy
        return (new_x, new_y)


    def canvas_draw_tile(self, bottom_left_xy, xint, yint, fill_color):
        self.canvas.create_rectangle(bottom_left_xy[0], bottom_left_xy[1],
            bottom_left_xy[0]+xint, bottom_left_xy[1]-yint, fill=fill_color, tag="heatmap")


    def canvas_draw_cartesian(self,n_xaxis_ticks, n_yaxis_ticks,
        xaxis_ticks_labels, yaxis_ticks_labels, margin_x, margin_y):
        # draw vertical axis
        v_start_point = (margin_x*self.canvas_width,70)
        v_end_point =  (margin_x*self.canvas_width,(1-margin_y)*self.canvas_height)
        self.canvas.create_line(v_start_point[0],v_start_point[1],
            v_end_point[0], v_end_point[1], tag="heatmap")
        # draw horizontal axis
        h_start_point = (margin_x*self.canvas_width,(1-margin_y)*self.canvas_height)
        h_end_point = (900,(1-margin_y)*self.canvas_height)
        self.canvas.create_line(h_start_point[0], h_start_point[1],
            h_end_point[0], h_end_point[1], tag="heatmap")
        # draw ticks on vertical axis
        yaxis_const = self.canvas_draw_yaxis_ticks(v_start_point,
            v_end_point,n_yaxis_ticks,yaxis_ticks_labels)
        xaxis_const = self.canvas_draw_xaxis_ticks(h_start_point,
            h_end_point,n_xaxis_ticks,xaxis_ticks_labels)
        points = dict()
        points["yaxis"] = yaxis_const
        points["xaxis"] = xaxis_const
        points["origin"] = v_end_point
        points["xmargin"] = margin_x
        points["ymargin"] = margin_y
        return points


    def canvas_draw_yaxis_ticks(self, start, end, n_ticks, tick_labels):
        y_axis_length = math.trunc(math.sqrt(
            (end[0]-start[0])**2+(end[1]-start[1])**2))
        y_axis_interval = math.trunc(y_axis_length / n_ticks)
        current_point = end
        for i in range(n_ticks):
            self.canvas_draw_axis_tick(current_point, "y")
            current_point = (current_point[0], current_point[1]-y_axis_interval)
            self.canvas_label_yaxis_tick(self.canvas_get_new_point(current_point,
                -20, -y_axis_interval/2), tick_labels[i])
        constants = dict()
        constants["axis_length"] = y_axis_length
        constants["axis_interval"] = y_axis_interval
        return constants



    def canvas_draw_xaxis_ticks(self, start, end, n_ticks, tick_labels):
        x_axis_length = math.trunc(math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2))
        x_axis_interval = math.trunc(x_axis_length / n_ticks)
        current_point = start
        for i in range(n_ticks):
            self.canvas_draw_axis_tick(current_point, "x")
            current_point = (current_point[0]+x_axis_interval, current_point[1])
            self.canvas_label_xaxis_tick(self.canvas_get_new_point(current_point,
                -x_axis_interval/2,-20), tick_labels[i])
        constants = dict()
        constants["axis_length"] = x_axis_length
        constants["axis_interval"] = x_axis_interval
        return constants




    def canvas_draw_axis_tick(self, point, axis):
        x = point[0]
        y = point[1]
        if(axis=="x"):
            self.canvas.create_line(x, y-10, x, y+10, tag="heatmap")
        elif(axis=="y"):
            self.canvas.create_line(x-10, y, x+10, y, tag="heatmap")
    


    def canvas_label_xaxis_tick(self, point, label):
        self.canvas.create_text(point[0], point[1], text=label, anchor="e", angle=90, tag="heatmap")
        

    def canvas_label_yaxis_tick(self, point, label):
        self.canvas.create_text(point[0], point[1], text=label, anchor="e", tag="heatmap")
    



    def on_configure(self,event):
        if(self.canvas.winfo_width()!=1):
            self.canvas_width = self.canvas.winfo_width()
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_position_item("all", self.canvas_width/2, 28)
        #self.canvas.scale("all",0,0,1.0001,1.001)
        self.canvas_update_scrollregion()
    



    def canvas_update_scrollregion(self):
        region = (0,0,self.canvas.bbox(ALL)[2],self.canvas.bbox(ALL)[3])
        self.canvas.configure(scrollregion=region)



    def canvas_move_all_items(self, x, y):
        self.canvas.move("all", x, y)
        self.canvas_update_scrollregion()



    def canvas_position_item(self, tag, x, y):
        self.canvas.coords(tag, x, y)
        self.canvas_update_scrollregion()



    def canvas_center_heatmap(self):
        ''' centers the cartesian plane illustrating the heat map '''
        tag = "heatmap"
        bbox_width = self.canvas.bbox(tag)[2] - self.canvas.bbox(tag)[0]
        print("bbox",self.canvas.bbox(tag))
        print("bbox_width",bbox_width)
        print("canvas_width",self.canvas_width)
        print("canvas_width/2",self.canvas_width/2)
        self.canvas.move(tag, ((self.canvas_width/2)-(bbox_width/2))/2,0)


    def render(self):
        self.pack(fill=BOTH, expand=True, side=TOP)
        self.bottom_frame.pack(fill=X, expand=False, side=BOTTOM)
        self.right_frame.pack(fill=Y, expand=False, side=RIGHT)
        self.left_frame.pack(fill=BOTH, expand=True, side=LEFT)
        self.canvas.pack(fill=BOTH, expand=True, padx=0, pady=0, side=LEFT)
        self.scroll_y.pack(fill=Y, side=RIGHT)
        self.scroll_x.pack(fill=X, side=BOTTOM)





