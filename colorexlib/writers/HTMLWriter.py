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

from .FileOutputWriter import FileOutputWriter
from Cheetah.Template import Template
from ..common.datastructures import HeatMap
from ..common.styling import StyleSheet

class HTMLWriter(FileOutputWriter):

    ''' Class that handles writing to HTML output files '''

    def __init__(self, filepath=None, heatmap=None, 
        stylesheet=None):
        ''' Initialize HTMLWriter object '''


        # do validation
        # Determine the validity of all parameters passed.
        if(not isinstance(heatmap, HeatMap)):
            raise TypeError("argument 'heatmap' \
                must be of type 'HeatMap'")
        elif(not isinstance(stylesheet, StyleSheet)):
            raise TypeError("argument 'stylesheet' \
                must be of type 'StyleSheet'")




        
        FileOutputWriter.__init__(self, filepath=filepath, 
            heatmap=heatmap, stylesheet=stylesheet)
        
        self.dirs = dict()





        # set some heatmap properties
        self.heatmap = heatmap
        self.title = heatmap.title
        self.subtitle = heatmap.subtitle
        self.ncols = self.heatmap.cols
        self.nrows = self.heatmap.rows
        self.dataformatter = self.heatmap.dataformatter
        self.stylesheet = stylesheet

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
            }

            /* Tile settings for the HeatMap */
            .tile {
                width: $stylesheet.styles['tile_size'][0];
                height: $stylesheet.styles['tile_size'][1];
            }

            .heatmap {
                padding-top: $stylesheet.styles['plane_top_margin'] ;
            }


            /* Axes Title settings */
            .xaxis_title {
                font-family: $stylesheet.styles['axes_title_font'];
                font-size: #echo $stylesheet.styles['axes_title_size']#pt;
                #if $stylesheet.styles['axes_title_bold'] == True
                font-weight: bold;
                #end if
                text-align: center;             
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
            }

            .yaxis_label {
                font-family: $stylesheet.styles['axes_label_font'];
                font-size: #echo $stylesheet.styles['axes_label_size']#pt;
                #if $stylesheet.styles['axes_label_bold'] == True
                font-weight: bold;
                #end if
            }

            .xaxis_label_row {
                text-align: center;
                vertical-align: top;
                padding-top: #echo $stylesheet.styles['xlabel_margin']#px;
            }

            .yaxis_label_column {
                text-align: right;
                vertical-align: middle;
                padding-right: #echo $stylesheet.styles['ylabel_margin']#px;
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
                padding: 5px 0;

                position: absolute;
                z-index: 1;
            }

            .tile:hover .tileballoonpopup {
                visibility: visible;
            }





        </style>




        <script>


            function tile_mouseup(value, label, tile) {
                console.log(value,label,tile);
            }


        </script>



        
    </head>




    <body>


    <center>




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










        <table class="heatmap" border="0" cellspacing="0" cellpadding="0">


            #for $row in $data
            #set global row_n = 0



            <!-- HeatMap Tiles -->
            <tr>
                #if $row_n == 0
                #if $heatmap.rowcolheaders
                <!-- Y-Axis Title -->
                <td rowspan="#echo $heatmap.rows-1#">
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
                        <div class="tileballoonpopup">
                            #if $col.label is not None
                            #echo $col.label# <br/>
                            #end if
                            #echo $heatmap.dataformatter.format($col.value)#
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
                <td colspan="$heatmap.cols" class="xaxis_title">
                    $heatmap.xaxistitle
                </td>
                #else
                <td></td>
                <td></td>
                <td colspan="$heatmap.cols" class="xaxis_title">
                    $heatmap.xaxistitle
                </td>
                #end if
            </tr>
        </table>



        </center>
    </body>
</html>







        '''