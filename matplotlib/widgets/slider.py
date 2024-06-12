import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

amp = 1.0
freq = 1.0

# fig-The top level container for all the plot elements
# ax-ax can be either a single Axes object, or an array of Axes objects if more than one subplot was created.
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35) #space from the bottom of the figure (ie from the top level container)

# x #linspace-evenly spaced numbers over a specified interval in the x axis.
t = np.linspace(0.0, 2.0 * np.pi, num=1000) 
# y
s = amp * np.sin(freq * t)
# plot a line along points x,y. lw -> line width (i.e. thickness of the plot line)
l, = ax.plot(t, s, lw=2)

# position of the slider, x, y, w, h - position of the slider in percentage of the figure
ax_slider = plt.axes(arg=[0.15, 0.1, 0.65, 0.02], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, label='f', valmin=0.1, valmax=5.0, valinit=freq)

def update(val):
    freq = val
    l.set_ydata(amp * np.sin(freq * t))
    fig.canvas.draw_idle()
    
    
slider.on_changed(update)

plt.show()




