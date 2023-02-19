from pandas_datareader import data

from bokeh.plotting import figure,output_file,show

import datetime

start=datetime.datetime(2019,3,1)

end=datetime.datetime(2019,3,15)

df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

df

def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="equal"
    return value
        
df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]


df["Middle"]=(df.Close+df.Open)/2

df["Height"]=abs(df.Close-df.Open)


df

p=figure(x_axis_type='datetime',width=1000,height=700,tools='')

p.title.text="Finace Chart"
p.title.text_font_size="35px"
p.grid.grid_line_alpha=0.6

hours_12=12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,line_color="black")
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,df.Height[df.Status=="Increase"],fill_color="green",line_color="black")


p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,df.Height[df.Status=="Decrease"],fill_color="red",line_color="black")

output_file("cats.html")

show(p)
