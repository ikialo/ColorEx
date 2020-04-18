from tkinter import *
from tkinter import ttk
from ..common.datastructures import HeatMap, Tile
from ..common.styling import Themes, StyleSheet
import math



class HeatMapWindow(Frame):


    
    def __init__(self, parent, heatmap=None, stylesheet=None, **kwargs):
        
        if(heatmap == None and stylesheet==None):
            raise Exception
        
        # call parent initialize
        Frame.__init__(self, parent, **kwargs)
        

        # declare some constants for stylesheet
        self.const = dict()
        self.const["TILESIZE"] = stylesheet.stylesheet['tile_size']
        self.const["CANVAS_SIZE_FACTOR"] = stylesheet.stylesheet['canvas_size_factor']
        self.const["CANVAS_TOP_MARGIN"] = stylesheet.stylesheet['canvas_top_margin']
        self.const["CANVAS_BOTTOM_MARGIN"] = stylesheet.stylesheet['canvas_bottom_margin']
        self.const["YLABEL_MARGIN"] = stylesheet.stylesheet['ylabel_margin']
        self.const["XLABEL_MARGIN"] = stylesheet.stylesheet['xlabel_margin']
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
        self.xaxis_label = heatmap.xaxislabel
        self.yaxis_label = heatmap.yaxislabel



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
        



    def onMouseEnterTile(self, event, tile_id):
        self.canvas.itemconfigure(str(tile_id), width=5, outline="black")
        self.canvas.tag_raise(str(tile_id),"heatmap")


    def onMouseLeaveTile(self, event, tile_id):
        self.canvas.itemconfigure(str(tile_id), width=0)
        self.canvas.delete("current_tile_popup")


    def onMouseClickTile(self, event, tile_id, tile_data):
        self.canvas.itemconfigure(str(tile_id), width=11, outline="black")
        coords = self.canvas.coords(str(tile_id))
        x = coords[0]+self.const["TILESIZE"][0]
        y = coords[1]

        point1 = (x,y)
        point2 = (x+10, y-40)
        point3 = (x+80, y-40)
        point4 = (x+80, y-40+30)
        point5 = (x+10, y-40+30)
        self.canvas.create_polygon(point1[0],point1[1],point2[0],
            point2[1],point3[0],point3[1],point4[0],point4[1],
            point5[0],point5[1],point1[0],point1[1],fill="black",
            tag="current_tile_popup")
        
        self.canvas.create_text(point2[0]+(point3[0]-point2[0])/2,
            ((point5[1]-point2[1])/2)+point2[1],text=tile_data.value,
            font="Arial 11 bold",tag="current_tile_popup", fill="white")


    def init_canvas(self):
        # draw the titles on the canvas.
        # title
        self.canvas.create_text(0,
        self.const["YCOORD_TITLE"],
        anchor="center", text=self.title,
        fill='black', font="Arial 22", tag="header")
        # subtitle
        self.canvas.create_text(0,
        self.const["YCOORD_SUBTITLE"],
        anchor="center", text=self.subtitle,
        fill='gray', font="Arial 13", tag="header")        

        

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
                point = self.canvas_get_new_point(plot_start,
                    i*self.const["TILESIZE"][0],
                    j*self.const["TILESIZE"][1])
                self.canvas_draw_tile(point,self.heatmap_data[j][i].rgb,
                    self.heatmap_data[j][i], width=0, outline="white")
                

        # draw the axis labels, xaxis, yaxis.
        if(self.xaxis_label != "" or self.yaxis_label != ""):
            hm_leftx = self.canvas.bbox("heatmap")[0]
            hm_lefty = self.canvas.bbox("heatmap")[1]
            hm_rightx = self.canvas.bbox("heatmap")[2]
            hm_righty = self.canvas.bbox("heatmap")[3]
            
            tiles_leftx = self.canvas.bbox("tiles")[0]
            tiles_lefty = self.canvas.bbox("tiles")[1]
            tiles_rightx = self.canvas.bbox("tiles")[2]
            tiles_righty = self.canvas.bbox("tiles")[3]
            
            xaxis_label_x = (tiles_rightx-tiles_leftx)/2 + tiles_leftx
            xaxis_label_y = (hm_righty) + 20
            yaxis_label_x = hm_leftx - 20
            yaxis_label_y = (tiles_righty - tiles_lefty)/2

            if(self.xaxis_label != ""):
                self.canvas.create_text(xaxis_label_x, xaxis_label_y,
                    text=self.xaxis_label, font="Arial 14 bold", 
                    tag="heatmap")
            if(self.yaxis_label != ""):
                self.canvas.create_text(yaxis_label_x, yaxis_label_y,
                    text=self.yaxis_label, font="Arial 14 bold", 
                    angle=90, tag="heatmap")

        
        # center the heatmap horizontally.
        self.canvas_center_header()
        self.canvas_center_heatmap(centerAlongX=True, 
            centerAlongY=True)

    
        # create some scrollbars
        self.scroll_y = Scrollbar(self.right_frame,
            command=self.canvas.yview, orient=VERTICAL)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x = Scrollbar(self.bottom_frame,
            command=self.canvas.xview, orient=HORIZONTAL)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)






    ################################################# Not using this as a legend may not be necessary due to heatmap interactivity.
    def canvas_draw_legend(self):
        # create the legend or key for the heatmap
        legendbox_x1 = 50
        legendbox_y1 = self.const["PLANE_TOP_MARGIN"]
        legendbox_x2 = 250
        legendbox_y2 = self.const["PLANE_TOP_MARGIN"]+300
        self.canvas.create_rectangle(legendbox_x1, legendbox_y1,
            legendbox_x2, legendbox_y2)
        self.canvas.create_text((legendbox_x1+legendbox_x2)/2,
            legendbox_y1+40,text="Legend")


        self.canvas.create_rectangle(legendbox_x1+15, legendbox_y1+60,
            legendbox_x1+30, legendbox_y1+75)
        self.canvas.create_text(legendbox_x1+45, legendbox_y1+60,text="20-30",
            anchor="w")
    ################################################# Not using this as a legend may not be necessary due to heatmap interactivity.




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




    def canvas_draw_tile(self, topleft_point, fill_color, tile, 
        width=0, outline="black"):
        xint = self.const["TILESIZE"][0]
        yint = self.const["TILESIZE"][1]
        x1 = topleft_point[0]
        y1 = topleft_point[1]
        x2 = topleft_point[0]+xint
        y2 = topleft_point[1]+yint
        tile_id = self.canvas.create_rectangle(x1,y1,x2,y2,
            fill=fill_color,width=width, outline=outline,
            tag=("heatmap", "tiles"))
        self.canvas.tag_bind(str(tile_id),"<Enter>",lambda event, 
            tile=tile_id: self.onMouseEnterTile(event, tile_id))
        self.canvas.tag_bind(str(tile_id),"<Leave>",lambda event, 
            tile=tile_id: self.onMouseLeaveTile(event, tile_id))
        self.canvas.tag_bind(str(tile_id),"<Button>",lambda event, 
            tile=tile_id, tile_data=tile: self.onMouseClickTile(event, 
                tile_id, tile_data))




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
            self.canvas_center_heatmap(centerAlongX=True, 
                centerAlongY=False)
        self.canvas_update_scrollregion()





    def render(self):
        self.pack(fill=BOTH, expand=True, side=TOP)
        self.bottom_frame.pack(fill=X, expand=False, side=BOTTOM)
        self.right_frame.pack(fill=Y, expand=False, side=RIGHT)
        self.left_frame.pack(fill=BOTH, expand=True, side=LEFT)
        self.canvas.pack(fill=BOTH, expand=True, padx=0, 
            pady=0, side=LEFT)
        self.scroll_y.pack(fill=Y, side=RIGHT)
        self.scroll_x.pack(fill=X, side=BOTTOM)





