from bokeh.plotting import Figure, output_file, show
import math
import scipy
import numpy as np
from bokeh.layouts import widgetbox, row, column
from bokeh.models import CustomJS, ColumnDataSource, Slider, Button, PreText, TextInput

def avg(s):
    #не используется
    s1 = s.split(' ')
    a = 0
    for i in range(0,len(s1)):
        a += float(s1[i])
    a /= len(s1)
    return a;
        

Cas1 = 5 #(мкмоль/л) - концентрация dCas9_1
Cas2 = 5 #(мкмоль/л) - концентрация dCas9_2
SO = 40 #(мкмоль/л) - концентрация субстрата
Cas1DNAO = 0
Cas2DNAO = 0
CpO = 0
k1 = 
k2 = 
DNA = 100 #(мкмоль/л) - концентрация ДНК
CEBL = 0
Km = 50.5
Vmax =  342.6 #(1/с) - константа катализа для бета-лактамазы TEM-1
kcatEBL = 0.0038
dt1=[dt*0.1 for dt in range(0, 20)]
C = [0]*20
a = 0

fig = Figure(plot_width=700, plot_height=500, title="Зависимость концентрации продукта расщепления нитроцефина бета-лактамазой TEM-1 от времени",x_axis_label='Время, с', y_axis_label='Концентрация продукта, мкмоль/л')
for i in range(0,20):
    if (i == 0):
        Cas1DNA = Cas1DNAO
        Cas2DNA = Cas2DNAO
        Cp = CpO
    else:  
        Cas1DNA =  Cas1DNA*(1 - k1*(dt1[i] - dt1[i-1])) + k1*Cas1*DNA*(dt1[i] - dt1[i-1])
        Cas2DNA =  Cas2DNA*(1 - k2*(dt1[i] - dt1[i-1])) + k2*Cas2*DNA*(dt1[i] - dt1[i-1])
        if (Cas1DNA + Cas2DNA > DNA):
            a = i-1
            break
        CEBL = (Cas1DNA*Cas2DNA)/DNA
        Cp = Cp + ((Vmax*(SO - Cp))*(dt1[i] - dt1[i-1])/(Km + (SO - Cp)))
        if (Cp > SO):
            a = i-1
            break;
    C[i] = Cp

y1 = list(C[0:a])
x1 = list(dt1[0:a])
source = ColumnDataSource(data=dict(x1=x1, y1=y1))

fig.circle('x1','y1', source=source, size = 1.5, color = 'red')

show(fig)
