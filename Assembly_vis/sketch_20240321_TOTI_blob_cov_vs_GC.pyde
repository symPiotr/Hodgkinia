""" INTRO:
This script, written for Processing v. 3.5.4 (Python mode), visualizes bacterial contigs present in the individual host in GC% vs coverage space.

It reads in "All_contig_stats.txt" file, with information on bacterial contigs as below:
Host  Contig_name  Len  GC  Cov  Dens  Complete
ERG26  ERG26_43_length_34163  34163  38.1  56.5932  0.637970904  0
ERG26  ERG26_48_length_28020  28020  30.26  59.2233  0.425017844  0

... with Length (int), GC contents (percentage - range 0-100), Read coverage (float), 
    Coding density (percentage) and Completeness (0 or 1) provided in columns 3-7.
    
Then, it takes some of the host names from "Assembly_list" (see the editable list - the first portions of the script),
and for each of them, draws a plot in the output directory.

"All_contig_stats.txt" table was generated through merging the output of: 
small custom script "GC_stats.py" - computes length and GC% for input fasta files;
and "gffs_to_coding_density_table.py" - computes coding density;
and Qualimap run on a bam file as a means of reconstructing read coverage.
"""

add_library('pdf')

### Providing sample name
work_dir = "/Users/piotrlukasik/bioinfo/TOTI_Processing/Fig3_Blobs"

#Assembly_list = ['DB114','DB118','TETULN','TETUND','TETLIM','TETAUR','MUDKUR','PLAKAE','KOSYEZ','MAGTRE','TETCRI', 'I9980','ERG44','ERG26','ERG27','ERG28','MOCK']
Assembly_list = ['DB114', 'DB118']

Assembly_names = {'I9980':'I9980','ERG44':'ERG44','ERG26':'ERG26','ERG27':'ERG27','ERG28':'ERG28',
"PLAKAE": "Platypleura kaempferi",
"MUDKUR": "Muda kuroiwae",
"KOSYEZ": "Kosemia yezoensis",
"MAGTRE": "Magicicada tredecim",
'DB114': "Okanagana oregona",
'DB118': "Okanagana bella",
'TETULN': "Tettigades ulnaria",
'TETUND': "Tettigades undata",
'TETLIM': "Tettigades limbata",
'TETAUR': "Tettigades auropilosa",
'TETCRI': "Tettigarcta crinita",
"JAP06": "Auritibicen japonicus",
"JAP10": "Auritibicen bihamatus",
"JAP22": "Vagitanus terminalis",
"MOCK": "Made up data"}

### Specifying plot location and size
### You need to plan those before starting the work. I have decided that for this specific dataset, I want 
### to show coverage from 10^0 to 10^4, 300 pixels per 10x increase (900 total)
### and GC contents from 0.15 to 0.7, 200 pixels per 0.1 increase (900 total) 
plot_x_start = 200
plot_x_size = 1100
plot_x_end = plot_x_start + plot_x_size
plot_y_start = 200
plot_y_size = 1200
plot_y_end = plot_y_start + plot_y_size


### Function for setting fill color, of contigs or legend
def SelectColor(Dens, Complete): ### coding_density as a fraction in the range <0,1>. complete as 0 or 1.
    I = Dens
    if I <= 0.50:
        R = 255
        G = I*2*255
        B = 0
        Op = int((0.5+I/2)*255)
    else:
        R = int((1-I)*2*255)
        G = int((1-I)*2*255)
        B = int((I-0.5)*2*255)
        Op = int((0.75-(I-0.5)/2)*255)
    fill(R, G, B, Op)
    
    strokeWeight(2*Complete)
    if Complete == 0:
        stroke(R, G, B, Op)
    else:
        stroke(0)
    
    return("")


### Need to define log10 for plotting coverage!
def log10(x):
    return(log(x)/log(10))

### Function that calculates contig or line position on x scale
def CalculateX(x):
    return(plot_x_start + (x-15)*20)

### Function that calculates contig or line position on y scale
def CalculateY(y):
    return(plot_y_end - (log10(y)*300))

### Function that calculates the size of contig to be drawn
def CalculateDiameter(x):
    return(2 * sqrt(x/60) - 1)


### Reading in tab-separated file with data
Contig_stats = loadTable("%s/All_contig_stats.txt" % work_dir, "tsv")
### Defining the size of figure
size(1600, 1600)

for assembly in Assembly_list:
    ### Specifying the location and name of the output pdf file, beginning recording
    beginRecord(PDF, "%s/%s.pdf" % (work_dir, assembly))
    textMode(SHAPE)
    f = createFont("Arial", 16)
    textFont(f,16)
    
    ### Background fill color - white
    background(255)



    ### Drawing grid. First, title:
    textSize(60)
    textAlign(CENTER)
    strokeWeight(2)
    fill(0)
    text("%s" % (Assembly_names[assembly]), (plot_x_end + 200)/2, 190)    
    
    ### Now, defining general parameters for everything else
    textSize(40)
    textAlign(RIGHT)
    strokeWeight(2)
    stroke(150)
    fill(0)
    
    ### Then, drawing x grid lines
    for Cov in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]:
        ypos = CalculateY(Cov)
        line(plot_x_start-20,ypos,plot_x_end,ypos)
        textSize(40)
        if Cov < 1:
            text("%.1f" % Cov, plot_x_start-30, ypos+12)
        else:
            text(Cov, plot_x_start-30, ypos+12)
    
    ### Then, drawing y grid lines
    for GC in [0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7]:
        xpos = CalculateX(GC*100)
        print(GC, xpos)
        line(xpos,plot_y_start,xpos,plot_y_end+20)
        textSize(40)
        textAlign(CENTER)
        text("%.2f" % GC, xpos, plot_y_end+50)
    
    ### Then, drawing outside frame
    stroke(0)
    strokeWeight(3)
    fill(255,0)
    rect(plot_x_start,plot_y_start,plot_x_size,plot_y_size)
    
    ### Finally, axis legends
    # x axis
    fill(0)
    textAlign(CENTER)
    textSize(40)
    text("GC contents", (plot_x_start+plot_x_end)/2, plot_y_end+110)
    # y axis... rotating cavas is such a pain, please add that one using graphic software!
   
    
    print("Grid drawn successfully!")
    

    ###########################
    ############## Plotting contigs!
    ######### Reading values for each contig from Stats_Table, calculating parameters, drawing ellipse!
    for i in range(Contig_stats.getRowCount()-1,0,-1):
        Row = Contig_stats.getRow(i)
        ID = Row.getString(0)
        Len = Row.getInt(2)
        GC = Row.getFloat(3)
        Cov = Row.getFloat(4)
        Dens = Row.getFloat(5)
        Complete = Row.getInt(6)
                
        ypos = CalculateY(Cov)
        xpos = CalculateX(GC)
        diameter = CalculateDiameter(Len)
        
        if ID == assembly and Cov > 1:
            SelectColor(Dens, Complete)
            ellipse(xpos, ypos, diameter, diameter)


    ########## Drawing legend
    fill(0)
    textSize(40)
    ypos = plot_y_start + 100
    xpos = plot_x_end + 40
    textAlign(LEFT)
    

    textSize(40)
    text("Contig size", xpos, ypos)
    ypos += 60

    stroke(0)
    textSize(30)
    for k in [500, 1000, 5000, 10000, 50000, 100000]:
        diameter = CalculateDiameter(k)
        ellipse(xpos+20, ypos, diameter, diameter)
        text("%d bp" % k, xpos+70, ypos+10)
        ypos += 70
    
        

    ### Finish making figure
    println("Finished drawing plot for assembly %s" % assembly)
    endRecord()
