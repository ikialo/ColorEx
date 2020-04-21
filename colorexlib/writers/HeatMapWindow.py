from tkinter import *
from tkinter import ttk
from ..common.datastructures import HeatMap, Tile
from ..common.styling import Themes, StyleSheet
import math



class HeatMapWindow(Frame):


    
    def __init__(self, parent, heatmap=None, 
        stylesheet=StyleSheet, **kwargs):
        
        # Determine the validity of all parameters passed.
        if(not isinstance(parent, Tk)):
            raise TypeError("argument 'parent' \
                must be of type 'Tk'")
        elif(not isinstance(heatmap, HeatMap)):
            raise TypeError("argument 'heatmap' \
                must be of type 'HeatMap'")
        elif(not isinstance(stylesheet, StyleSheet)):
            raise TypeError("argument 'stylesheet' \
                must be of type 'StyleSheet'")


        # call parent initialize
        Frame.__init__(self, parent, **kwargs)
        
        # declare some constants, styles for stylesheet
        styles = stylesheet.styles
        # tile styles and constants
        self.const = dict()
        self.const["TILESIZE"] = styles['tile_size']
        # plane styles and constants
        self.const["PLANE_TOP_MARGIN"] = styles['plane_top_margin']
        # canvas styles and constants
        self.const["CANVAS_SIZE_FACTOR"] = styles['canvas_size_factor']
        self.const["CANVAS_TOP_MARGIN"] = styles['canvas_top_margin']
        self.const["CANVAS_BOTTOM_MARGIN"] = styles['canvas_bottom_margin']
        # label styles and constants
        self.const["YLABEL_MARGIN"] = styles['ylabel_margin']
        self.const["XLABEL_MARGIN"] = styles['xlabel_margin']
        # axes styles and constants
        self.const['AXES_TITLE_FONT'] = styles['axes_title_font']
        self.const['AXES_TITLE_SIZE'] = styles['axes_title_size']
        self.const['AXES_TITLE_BOLD'] = styles['axes_title_bold']
        self.const["AXES_TICK_LENGTH"] = styles['axes_tick_length']
        self.const['AXES_LABEL_FONT'] = styles['axes_label_font']
        self.const['AXES_LABEL_SIZE'] = styles['axes_label_size']
        self.const['AXES_LABEL_BOLD'] = styles['axes_label_bold']
        # title styles and constants
        self.const['TITLE_FONT'] = styles['title_font']
        self.const['TITLE_SIZE'] = styles['title_size']
        self.const['TITLE_BOLD'] = styles['title_bold']
        self.const['TITLE_YCOORD'] = styles['title_ycoord']
        # subtitle styles and constants
        self.const['SUBTITLE_FONT'] = styles['subtitle_font']
        self.const['SUBTITLE_SIZE'] = styles['subtitle_size']
        self.const['SUBTITLE_BOLD'] = styles['subtitle_bold']
        self.const['SUBTITLE_YCOORD'] = styles['subtitle_ycoord']
        # determine and generate the font for all axes labels.
        self.axes_label_font = list()
        font_family = self.const["AXES_LABEL_FONT"]
        font_size = str(self.const["AXES_LABEL_SIZE"])
        bold = self.const["AXES_LABEL_BOLD"]
        self.axes_label_font.append(font_family)
        self.axes_label_font.append(font_size)
        if(bold):
            self.axes_label_font.append('bold')
        # set some heatmap properties
        self.heatmap = heatmap
        self.title = heatmap.title
        self.subtitle = heatmap.subtitle
        self.ncols = self.heatmap.cols
        self.nrows = self.heatmap.rows

        # determine which rows and columns are data, 
        # and which rows and columns are the axes
        # labels, and set accordingly.
        if(self.heatmap.rowcolheaders):
            # There are row and column headers
            # already specified in the HeatMap object.
            # decrease ncols and nrows
            self.ncols -= 1
            self.nrows -= 1
            # row and column headers have been set in data source.
            self.heatmap_data = list(map(lambda row: row[1:], 
                heatmap.grid[1:]))
            if(isinstance(heatmap.xaxislabels, list)):
                self.xaxis_labels = heatmap.xaxislabels
            else:
                self.xaxis_labels = heatmap.grid[0][1:]
            
            if(isinstance(heatmap.yaxislabels, list)):
                self.yaxis_labels = heatmap.yaxislabels
            else:
                self.yaxis_labels = list(map(lambda row: row[0], 
                    heatmap.grid[1:]))
        
        else:
            # There are NO row and column headers in
            # the HeatMap object, which means all the
            # items in HeatMap are essentially data
            # items to be plotted as a Tile.
            self.heatmap_data = self.heatmap.grid
            self.xaxis_labels = heatmap.xaxislabels
            self.yaxis_labels = heatmap.yaxislabels

        # set the axes title values
        self.xaxis_title = heatmap.xaxistitle
        self.yaxis_title = heatmap.yaxistitle

        # create layout frames
        self.bottom_frame = Frame(self)
        self.right_frame = Frame(self)
        self.left_frame = Frame(self)
        self.parent = parent
        
        # create a canvas object, and set window properties.
        self.canvas_width = int(
            self.const["CANVAS_SIZE_FACTOR"]*
            self.parent.winfo_screenwidth())
        self.canvas_height = int(
            self.const["CANVAS_SIZE_FACTOR"]*
            self.parent.winfo_screenheight())

        # set window minimum size.
        self.parent.minsize(width=400,
            height=300)

        # position the window
        self.parent.geometry(str(self.canvas_width)+
            "x"+str(self.canvas_height)+"+0+0")

        # initialize the canvas and render.
        self.canvas = Canvas(self.left_frame, bg="white",
            width=self.canvas_width, height=self.canvas_height)
        self.init_canvas()
        self.render()

        # bind some events to handlers
        self.left_frame.bind("<Configure>",self.on_configure)
        





    def onMouseEnterTile(self, event, tile_id):
        # restyle the tile item in canvas.
        self.canvas.itemconfigure(str(tile_id), 
            width=5, outline="black")
        # raise the tile above all other canvas items.
        self.canvas.tag_raise(str(tile_id),"heatmap")
        # change the mouse cursor in the heatmap
        self.canvas.config(cursor="crosshair")




    def onMouseLeaveTile(self, event, tile_id):
        # reset the tile's style in canvas.
        self.canvas.itemconfigure(str(tile_id), width=0)
        # hide the tile's balloon popup.
        self.hide_all_tile_balloons()
        # reset the cursor
        self.canvas.config(cursor="")
        # push the tiles to a lower layer in canvas, 
        # to allow axes lines to show.
        self.canvas.tag_lower("tiles",ALL)




    def onMouseClickTile(self, event, tile_id, tile_data):
        # restyle the tile that has been selected
        self.canvas.itemconfigure(str(tile_id), 
            width=11, outline="black")
        # Determine the coordinates of the tile.
        coords = self.canvas.coords(str(tile_id))
        x = coords[0]+self.const["TILESIZE"][0]
        y = coords[1]
        # show the current tile's popup balloon.
        self.show_current_tile_balloon(x, y, 
            tile_data.value)




    def show_current_tile_balloon(self, x, y, data):
        # Generate points for the balloon
        point1 = (x,y)
        point2 = (x+10, y-40)
        point3 = (x+80, y-40)
        point4 = (x+80, y-40+30)
        point5 = (x+10, y-40+30)
        # Draw the balloon polygon on the canvas.
        self.canvas.create_polygon(point1[0],point1[1],point2[0],
            point2[1],point3[0],point3[1],point4[0],point4[1],
            point5[0],point5[1],point1[0],point1[1],fill="black",
            tag="current_tile_popup")
        # Insert data into the balloon about the selected Tile.
        self.canvas.create_text(point2[0]+(point3[0]-point2[0])/2,
            ((point5[1]-point2[1])/2)+point2[1],text=data,
            font="Arial 11 bold",tag="current_tile_popup", 
            fill="white")




    def hide_all_tile_balloons(self):
        self.canvas.delete("current_tile_popup")




    def init_canvas(self):

        # set background color of canvas
        self.canvas.config(background=
            self.heatmap.theme.palette["background"])


        # draw the titles on the canvas.
        # title
        title_font = list()
        title_font.append(self.const["TITLE_FONT"])
        title_font.append(self.const["TITLE_SIZE"])
        if(self.const["TITLE_BOLD"]):
            title_font.append("bold")
        self.canvas.create_text(0,
        self.const["TITLE_YCOORD"],
        anchor="center", text=self.title,
        fill=self.heatmap.theme.palette["on-background"]
        , font=title_font, tag="header")


        # subtitle
        subtitle_font = list()
        subtitle_font.append(self.const["SUBTITLE_FONT"])
        subtitle_font.append(self.const["SUBTITLE_SIZE"])
        if(self.const["SUBTITLE_BOLD"]):
            subtitle_font.append("bold")
        self.canvas.create_text(0,
        self.const['SUBTITLE_YCOORD'],
        anchor="center", text=self.subtitle,
        fill=self.heatmap.theme.palette["on-background"], 
        font=subtitle_font, tag="header")        

        

        # draw the cartesian plane on the canvas at canvas 
        # origin first vertical axis
        yaxis_start = (0,0)
        yaxis_end =  (0,(self.const["TILESIZE"][1]*self.nrows))
        self.canvas.create_line(yaxis_start[0],yaxis_start[1],
            yaxis_end[0], yaxis_end[1], tag=("heatmap", 
                "cartesian"))
        for n in range(self.nrows):
            point = (yaxis_start[0], yaxis_start[1]+
                (self.const["TILESIZE"][1]*n))
            try:
                label = self.yaxis_labels[n]
            except:
                label = ""
            self.canvas_draw_yaxis_tick(point, label)
        



        # horizontal axis
        xaxis_start = yaxis_end
        xaxis_end = (xaxis_start[0]+(self.const["TILESIZE"][0]*
            self.ncols), xaxis_start[1])
        self.canvas.create_line(xaxis_start[0], xaxis_start[1],
            xaxis_end[0], xaxis_end[1], tag=("heatmap", 
                "cartesian"))
        for n in range(self.ncols):
            point = (xaxis_start[0]+(self.const["TILESIZE"][0]*
                (n+1)), xaxis_start[1])
            try:
                label = self.xaxis_labels[n]
            except:
                label = ""
            self.canvas_draw_xaxis_tick(point, label)


        

        # plot all tiles into the heat map cartesian plane
        plot_start = yaxis_start
        for i in range(self.ncols):
            for j in range(self.nrows):
                point = self.canvas_get_new_point(plot_start,
                    i*self.const["TILESIZE"][0],
                    j*self.const["TILESIZE"][1])
                self.canvas_draw_tile(point,self.heatmap_data[j][i].rgb,
                    self.heatmap_data[j][i], width=0, outline="white")
        
        # push the tiles to a lower layer in canvas, 
        # to allow axes lines to show.
        self.canvas.tag_lower("tiles",ALL)


        # draw the axes titles for xaxis, yaxis.
        if(self.xaxis_title != "" or self.yaxis_title != ""):
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

            if(self.xaxis_title != ""):
                axistitle_font = list()
                axistitle_font.append(self.const['AXES_TITLE_FONT'])
                axistitle_font.append(self.const['AXES_TITLE_SIZE'])
                if(self.const['AXES_TITLE_BOLD']):
                    axistitle_font.append("bold")

                self.canvas.create_text(xaxis_label_x, xaxis_label_y,
                    fill=self.heatmap.theme.palette["on-background"],
                    text=self.xaxis_title, font=axistitle_font, 
                    tag=("heatmap","cartesian"))
            if(self.yaxis_title != ""):
                self.canvas.create_text(yaxis_label_x, yaxis_label_y,
                    fill=self.heatmap.theme.palette["on-background"],
                    text=self.yaxis_title, font=axistitle_font, 
                    angle=90, tag=("heatmap","cartesian"))

        
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




    def canvas_center_heatmap(self,centerAlongX=True, 
        centerAlongY=True):
        ''' centers the cartesian plane illustrating 
        the heat map '''
        tag = "heatmap"
        # get the bounding box coordinates for heatmap
        # on the canvas.
        bbox = self.canvas.bbox(tag)
        bbox_x1 = bbox[0]
        bbox_x2 = bbox[2]
        bbox_y1 = bbox[1]
        bbox_width = bbox_x2 - bbox_x1
        canvas_width = self.canvas_width
        final_x = (canvas_width/2) - (bbox_width/2)
        dx = final_x - bbox_x1
        # center heatmap horizontally if
        # it was indicated.
        if(centerAlongX):
            for item in self.canvas.find_withtag(tag):
                self.canvas.move(item, dx, 0)
        # center heatmap vertically if
        # it was indicated.
        if(centerAlongY):
            for item in self.canvas.find_withtag(tag):
                self.canvas.move(item,0,
                    self.const["PLANE_TOP_MARGIN"])
        # update the scrollregion to access
        # any hidden parts of canvas not visible
        # on the screen.
        self.canvas_update_scrollregion()





    def canvas_center_header(self):
        ''' horizontally centers the header of the heatmap 
        containing title, subtitle. '''
        tag = "header"
        # Determine bounding box coordinates of header
        # on the canvas.
        bbox = self.canvas.bbox(tag)
        bbox_x1 = bbox[0]
        bbox_x2 = bbox[2]
        bbox_width = bbox_x2 - bbox_x1
        canvas_width = self.canvas_width
        final_x = (canvas_width/2) - (bbox_width/2)
        dx = final_x - bbox_x1
        # move the header accordingly to center
        # horizontally.
        self.canvas.move(tag, dx, 0)
        self.canvas_update_scrollregion()





    def canvas_get_new_point(self, old_point, dx, dy):
        old_x = old_point[0]
        old_y = old_point[1]
        new_x = old_x + dx
        new_y = old_y + dy
        return (new_x, new_y)




    def canvas_draw_tile(self, topleft_point, 
        fill_color, tile, 
        width=0, outline="black"):
        # determine dimensions of the tile
        xint = self.const["TILESIZE"][0]
        yint = self.const["TILESIZE"][1]
        # determine the coordinates of each
        # point of the tile.
        x1 = topleft_point[0]
        y1 = topleft_point[1]
        x2 = topleft_point[0]+xint
        y2 = topleft_point[1]+yint
        # Draw the tile on the canvas given
        # the determined points.
        tile_id = self.canvas.create_rectangle(x1,y1,x2,y2,
            fill=fill_color,width=width, outline=outline,
            tag=("heatmap", "tiles"))
        # Bind a handler when mouse cursor enters the Tile.
        self.canvas.tag_bind(str(tile_id),"<Enter>",
            lambda event, tile=tile_id: self.onMouseEnterTile(
                event, tile_id))
        # Bind a handler when mouse cursor leaves the Tile.
        self.canvas.tag_bind(str(tile_id),"<Leave>",
            lambda event, tile=tile_id: self.onMouseLeaveTile(
                event, tile_id))
        # Bind a handler when the Tile is clicked.
        self.canvas.tag_bind(str(tile_id),"<Button>",
            lambda event,tile=tile_id, tile_data=
            tile: self.onMouseClickTile(event, tile_id, 
                tile_data))




    def canvas_draw_yaxis_tick(self, point, label):
        # determine the coordinates
        x1 = point[0]
        y1 = point[1]
        end = (point[0]-self.const["AXES_TICK_LENGTH"],
            point[1])
        x2 = end[0]
        y2 = end[1]
        # draw the tick
        self.canvas.create_line(x1,y1,x2,y2, tag="heatmap")
        # label the tick
        label_point = list()
        label_point.append(point[0]-self.const["AXES_TICK_LENGTH"]
            -self.const["YLABEL_MARGIN"])
        label_point.append(point[1])


        self.canvas.create_text(label_point[0],
            label_point[1]+self.const["TILESIZE"][1]/2,
            fill=self.heatmap.theme.palette["on-background"],
            text=label, anchor="e", font=self.axes_label_font, 
            tag=("heatmap","cartesian"))




    def canvas_draw_xaxis_tick(self, point, label):
        # determine the coordinates
        x1 = point[0]
        y1 = point[1]
        end = (point[0],point[1]+self.const["AXES_TICK_LENGTH"])
        x2 = end[0]
        y2 = end[1]
        # draw the tick
        self.canvas.create_line(x1,y1,x2,y2, tag="heatmap")
        # Determine label point coordinates.
        label_point = list()
        label_point.append(point[0])
        label_point.append(point[1]+self.const["AXES_TICK_LENGTH"]
            +self.const["XLABEL_MARGIN"])
        # Label the tick drawn on the canvas.
        self.canvas.create_text(label_point[0]-
            self.const["TILESIZE"][0]/2,
            label_point[1],fill=self.heatmap.theme.palette[
            "on-background"],text=label, anchor="e", angle=90, 
            font=self.axes_label_font, tag=("heatmap",
                "cartesian"))






    def canvas_update_scrollregion(self):
        region = (0,0,self.canvas.bbox(ALL)[2],
        self.canvas.bbox(ALL)[3]+50)
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





