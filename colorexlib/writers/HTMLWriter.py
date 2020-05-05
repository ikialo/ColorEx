'''

Copyright 2019 Louis Ronald

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.


'''

# from .FileOutputWriter import FileOutputWriter
# from Cheetah.Template import Template
# from ..common.datastructures import HeatMap
# from ..common.styling import StyleSheet


from colorexlib.colorexlib.writers.FileOutputWriter import FileOutputWriter
from Cheetah.Template import Template
from colorexlib.colorexlib.common.datastructures import HeatMap
from colorexlib.colorexlib.common.styling import StyleSheet


class HTMLWriter(FileOutputWriter):

    ''' Class that handles writing to HTML output files '''

    def __init__(self, filepath=None, heatmap=None):
        ''' Initialize HTMLWriter object '''


        # do validation
        # Determine the validity of all parameters passed.
        if(not isinstance(heatmap, HeatMap)):
            raise TypeError("argument 'heatmap' \
                must be of type 'HeatMap'")




        
        FileOutputWriter.__init__(self, filepath=filepath, 
            heatmap=heatmap)
        
        self.dirs = dict()





        # set some heatmap properties
        self.heatmap = heatmap
        self.title = heatmap.title
        self.subtitle = heatmap.subtitle
        self.ncols = self.heatmap.cols
        self.nrows = self.heatmap.rows
        self.dataformatter = self.heatmap.dataformatter
        self.stylesheet = heatmap.stylesheet

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








    def write(self):
        ''' write the HeatMap to output HTML file '''
        filepath = self.filepath
        output_file = open(filepath, "w")
        #template_filename = options['template']
        #template_file = open(template_filename, 'r')
        #template_str = template_file.read()
        template_str = self.generate_html_template_str()
        template = Template(template_str,
            searchList=[{'heatmap': self.heatmap,
                         'data': self.heatmap_data,
                         'yaxis_labels': self.yaxis_labels,
                         'xaxis_labels': self.xaxis_labels,
                         'title': self.title,
                         'subtitle': self.subtitle,
                         'theme': self.heatmap.theme,
                         'stylesheet': self.stylesheet}])
        output_file.write(str(template))
        output_file.close()




    def generate_html_template_str(self):
        return '''


<html>
    <head>
        <title>
            $title
        </title>
        
        <style>
            /* body default settings */
            body {
                background-color: white;
            }


            /* Title settings */
            .title {
                font-family: $stylesheet.styles['title_font'];
                font-size: #echo $stylesheet.styles['title_size']#pt;
                #if $stylesheet.styles['title_bold'] == True
                font-weight: bold;
                #end if
                text-align: center;
                padding-top: #echo $stylesheet.styles['title_ycoord']#px;
                color: $heatmap.theme.palette['on-background'];
            }

            /* Subtitle settings */
            .subtitle {
                font-family: $stylesheet.styles['subtitle_font'];
                font-size: #echo $stylesheet.styles['subtitle_size']#pt;
                #if $stylesheet.styles['subtitle_bold'] == True
                font-weight: bold;
                #end if
                text-align: center;
                #set $subtitle_pad = $stylesheet.styles['subtitle_ycoord'] - $stylesheet.styles['title_ycoord']
                padding-top: #echo $subtitle_pad#px;
                color: $heatmap.theme.palette['on-background'];
            }

            /* Tile settings for the HeatMap */
            .tile {
                width: $stylesheet.styles['tile_size'][0];
                height: $stylesheet.styles['tile_size'][1];
            }

            .tile_selector {
                z-index: 40;
                height: 100%;                
            }

            .tile_selector:hover {
                border: 5px solid;
            }


            .heatmap {
                padding-top: $stylesheet.styles['plane_top_margin'];
                background-color: $heatmap.theme.palette['background'];
                color: $heatmap.theme.palette['on-background'];
            }


            .plane {
                padding-top: $stylesheet.styles['plane_top_margin'];
            }


            /* Axes Title settings */
            .xaxis_title {
                font-family: $stylesheet.styles['axes_title_font'];
                font-size: #echo $stylesheet.styles['axes_title_size']#pt;
                #if $stylesheet.styles['axes_title_bold'] == True
                font-weight: bold;
                #end if
                text-align: center;
                color: $heatmap.theme.palette['on-background'];
            }
            .yaxis_title {
                font-family: $stylesheet.styles['axes_title_font'];
                font-size: #echo $stylesheet.styles['axes_title_size']#pt;
                #if $stylesheet.styles['axes_title_bold'] == True
                font-weight: bold;
                #end if
                -ms-writing-mode: tbl-rl;
                -webkit-writing-mode: vertical-rl;
                writing-mode: vertical-rl;
                transform: rotate(180deg);
                white-space: nowrap;
                color: $heatmap.theme.palette['on-background'];
            }




            /* Axes Label settings */
            .xaxis_label {
                font-family: $stylesheet.styles['axes_label_font'];
                font-size: #echo $stylesheet.styles['axes_label_size']#pt;
                #if $stylesheet.styles['axes_label_bold'] == True
                font-weight: bold;
                #end if
                -ms-writing-mode: tbl-rl;
                -webkit-writing-mode: vertical-rl;
                writing-mode: vertical-rl;
                transform: rotate(180deg);
                white-space: nowrap;
                color: $heatmap.theme.palette['on-background'];
            }

            .yaxis_label {
                font-family: $stylesheet.styles['axes_label_font'];
                font-size: #echo $stylesheet.styles['axes_label_size']#pt;
                #if $stylesheet.styles['axes_label_bold'] == True
                font-weight: bold;
                #end if
                color: $heatmap.theme.palette['on-background'];
            }

            .xaxis_label_row {
                text-align: center;
                vertical-align: top;
                padding-top: #echo $stylesheet.styles['xlabel_margin']#px;
                color: $heatmap.theme.palette['on-background'];
            }

            .yaxis_label_column {
                text-align: right;
                vertical-align: middle;
                padding-right: #echo $stylesheet.styles['ylabel_margin']#px;
                color: $heatmap.theme.palette['on-background'];
            }
            






            .tileballoonpopup {
                visibility: hidden;
                width: 120px;
                background-color: black;
                color: #fff;
                font-size: 10pt;
                font-family: "Tahoma";
                text-align: center;
                border-radius: 6px;
                padding: 6px 0;

                position: absolute;
                z-index: 2;
            }

            .tile:hover .tileballoonpopup {
                visibility: visible;
            }










            /* balloon.css embedded */
            :root{--balloon-border-radius: 2px;--balloon-text-color: #fff;--balloon-color: rgba(16,16,16,0.95);--balloon-font-size: 12px;--balloon-move: 4px}button[aria-label][data-balloon-pos]{overflow:visible}[aria-label][data-balloon-pos]{position:relative;cursor:pointer}[aria-label][data-balloon-pos]:after{opacity:0;pointer-events:none;transition:all .18s ease-out .18s;text-indent:0;font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;font-weight:normal;font-style:normal;text-shadow:none;font-size:var(--balloon-font-size);background:var(--balloon-color);border-radius:var(--balloon-border-radius);color:var(--balloon-text-color);content:attr(aria-label);padding:.5em 1em;position:absolute;white-space:nowrap;z-index:10}[aria-label][data-balloon-pos]:before{width:0;height:0;border:5px solid transparent;border-top-color:var(--balloon-color);opacity:0;pointer-events:none;transition:all .18s ease-out .18s;content:"";position:absolute;z-index:10}[aria-label][data-balloon-pos]:hover:before,[aria-label][data-balloon-pos]:hover:after,[aria-label][data-balloon-pos][data-balloon-visible]:before,[aria-label][data-balloon-pos][data-balloon-visible]:after,[aria-label][data-balloon-pos]:not([data-balloon-nofocus]):focus:before,[aria-label][data-balloon-pos]:not([data-balloon-nofocus]):focus:after{opacity:1;pointer-events:none}[aria-label][data-balloon-pos].font-awesome:after{font-family:FontAwesome, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif}[aria-label][data-balloon-pos][data-balloon-break]:after{white-space:pre}[aria-label][data-balloon-pos][data-balloon-break][data-balloon-length]:after{white-space:pre-line;word-break:break-word}[aria-label][data-balloon-pos][data-balloon-blunt]:before,[aria-label][data-balloon-pos][data-balloon-blunt]:after{transition:none}[aria-label][data-balloon-pos][data-balloon-pos="up"]:after{bottom:100%;left:50%;margin-bottom:10px;transform:translate(-50%, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up"]:before{bottom:100%;left:50%;transform:translate(-50%, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="up"][data-balloon-visible]:after{transform:translate(-50%, 0)}[aria-label][data-balloon-pos][data-balloon-pos="up"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="up"][data-balloon-visible]:before{transform:translate(-50%, 0)}[aria-label][data-balloon-pos][data-balloon-pos="up-left"]:after{bottom:100%;left:0;margin-bottom:10px;transform:translate(0, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up-left"]:before{bottom:100%;left:5px;transform:translate(0, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up-left"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="up-left"][data-balloon-visible]:after{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="up-left"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="up-left"][data-balloon-visible]:before{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="up-right"]:after{bottom:100%;right:0;margin-bottom:10px;transform:translate(0, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up-right"]:before{bottom:100%;right:5px;transform:translate(0, var(--balloon-move));transform-origin:top}[aria-label][data-balloon-pos][data-balloon-pos="up-right"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="up-right"][data-balloon-visible]:after{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="up-right"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="up-right"][data-balloon-visible]:before{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down"]:after{left:50%;margin-top:10px;top:100%;transform:translate(-50%, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down"]:before{width:0;height:0;border:5px solid transparent;border-bottom-color:var(--balloon-color);left:50%;top:100%;transform:translate(-50%, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="down"][data-balloon-visible]:after{transform:translate(-50%, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="down"][data-balloon-visible]:before{transform:translate(-50%, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down-left"]:after{left:0;margin-top:10px;top:100%;transform:translate(0, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down-left"]:before{width:0;height:0;border:5px solid transparent;border-bottom-color:var(--balloon-color);left:5px;top:100%;transform:translate(0, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down-left"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="down-left"][data-balloon-visible]:after{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down-left"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="down-left"][data-balloon-visible]:before{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down-right"]:after{right:0;margin-top:10px;top:100%;transform:translate(0, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down-right"]:before{width:0;height:0;border:5px solid transparent;border-bottom-color:var(--balloon-color);right:5px;top:100%;transform:translate(0, calc(var(--balloon-move) * -1))}[aria-label][data-balloon-pos][data-balloon-pos="down-right"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="down-right"][data-balloon-visible]:after{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="down-right"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="down-right"][data-balloon-visible]:before{transform:translate(0, 0)}[aria-label][data-balloon-pos][data-balloon-pos="left"]:after{margin-right:10px;right:100%;top:50%;transform:translate(var(--balloon-move), -50%)}[aria-label][data-balloon-pos][data-balloon-pos="left"]:before{width:0;height:0;border:5px solid transparent;border-left-color:var(--balloon-color);right:100%;top:50%;transform:translate(var(--balloon-move), -50%)}[aria-label][data-balloon-pos][data-balloon-pos="left"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="left"][data-balloon-visible]:after{transform:translate(0, -50%)}[aria-label][data-balloon-pos][data-balloon-pos="left"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="left"][data-balloon-visible]:before{transform:translate(0, -50%)}[aria-label][data-balloon-pos][data-balloon-pos="right"]:after{left:100%;margin-left:10px;top:50%;transform:translate(calc(var(--balloon-move) * -1), -50%)}[aria-label][data-balloon-pos][data-balloon-pos="right"]:before{width:0;height:0;border:5px solid transparent;border-right-color:var(--balloon-color);left:100%;top:50%;transform:translate(calc(var(--balloon-move) * -1), -50%)}[aria-label][data-balloon-pos][data-balloon-pos="right"]:hover:after,[aria-label][data-balloon-pos][data-balloon-pos="right"][data-balloon-visible]:after{transform:translate(0, -50%)}[aria-label][data-balloon-pos][data-balloon-pos="right"]:hover:before,[aria-label][data-balloon-pos][data-balloon-pos="right"][data-balloon-visible]:before{transform:translate(0, -50%)}[aria-label][data-balloon-pos][data-balloon-length="small"]:after{white-space:normal;width:80px}[aria-label][data-balloon-pos][data-balloon-length="medium"]:after{white-space:normal;width:150px}[aria-label][data-balloon-pos][data-balloon-length="large"]:after{white-space:normal;width:260px}[aria-label][data-balloon-pos][data-balloon-length="xlarge"]:after{white-space:normal;width:380px}@media screen and (max-width: 768px){[aria-label][data-balloon-pos][data-balloon-length="xlarge"]:after{white-space:normal;width:90vw}}[aria-label][data-balloon-pos][data-balloon-length="fit"]:after{white-space:normal;width:100%}








            .tooltip-big-text {
                --balloon-font-size: 15px;
            }


        </style>




        <script>


            function tile_onmouseover(dom_tile) {
                document.getElementById("status").innerHTML = "hovering";
            }


        </script>



        
    </head>




    <body>


    <center>


        <br/>
        <div class="heatmap" style="border: 1px solid; display: inline-block; padding: 30px;">

        <table>

            <!-- Main Title -->
            <tr>
                <td colspan="#echo $heatmap.cols+2#" class="title">
                    $title
                </td>
            </tr>

            <!-- SubTitle -->
            <tr>
                <td colspan="#echo $heatmap.cols+2#" class="subtitle">
                    $subtitle
                </td>
            </tr>

        </table>










        <table class="plane" border="0" cellspacing="0" cellpadding="0">


            #for $row in $data
            #set global row_n = 0



            <!-- HeatMap Tiles -->
            <tr>
                #if $row_n == 0
                #if $heatmap.rowcolheaders
                <!-- Y-Axis Title -->
                <td rowspan="#echo $heatmap.rows-1#" style="padding-right: 23px;">
                    <div class="yaxis_title">$heatmap.yaxistitle</div>
                </td>
                #else
                <td rowspan="#echo $heatmap.rows#">
                    <div class="yaxis_title">$heatmap.yaxistitle</div>
                </td>
                #end if
                #end if
                <!-- Y-Axis Labels -->
                <td class="yaxis_label_column">
                    #try
                        <span class="yaxis_label">$yaxis_labels[$row_n]</span>
                    #except
                        <span class="yaxis_label"></span>
                    #end try
                </td>               
                #for $col in $row
                <td class="tile" style="background-color: $col.rgb;">
                        <div class="tile_selector tooltip-big-text" aria-label="#if $col.label is not None # #echo $col.label# &#10; #end if# #echo $heatmap.dataformatter.format($col.value)#
                        " data-balloon-break data-balloon-pos="up" data-balloon-length="medium">
                        </div>

                </td>
                #end for
            </tr>
            #set $row_n = $row_n + 1
            #end for



            <!-- Labels for the X-Axis -->
            <tr>
                <td></td><td></td>
                #try
                #for $label in $xaxis_labels
                <td class="xaxis_label_row">
                    <span class="xaxis_label">
                        $label
                    </span>
                </td>
                #end for
                #except
                #for $label in range($heatmap.cols)
                <td class="xaxis_label_row">
                    <span class="xaxis_label">
                    </span>
                </td>
                #end for
                #end try
            </tr>




            <!-- X-Axis Title -->
            <tr>
                #if $heatmap.rowcolheaders
                <td></td>
                <td style="padding-top: 23px;" colspan="$heatmap.cols" class="xaxis_title">
                    $heatmap.xaxistitle
                </td>
                #else
                <td></td>
                <td></td>
                <td style="padding-top: 23px;" colspan="$heatmap.cols" class="xaxis_title">
                    $heatmap.xaxistitle
                </td>
                #end if
            </tr>
        </table>



        </div>

        </center>
    </body>
</html>







        '''