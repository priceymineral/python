import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Button

df = pd.read_excel('../data/chart_data.ods', index_col='Issue Period')
labels = df.columns
record = df.loc[df.index[0]]
position = range(len(record))

print(labels) # Index(['Issued', 'Denied', 'Pending'], dtype='object')
print(record) 
# Issued     45999
# Denied     14644
# Pending     3243
# Name: 2020, dtype: int64
print(position) # range(0, 3)

class IndexTracker:
    idx = 0
    def previous(self, event):
        self.idx -= 1
        row_index = self.idx % len(record)
        # print(row_index)
        # print(df.index[row_index])
        # print(df.loc[df.index[row_index]])
        rec = df.loc[df.index[row_index]]

        for i, bar in enumerate(bars):
            # bar.set_height(rec[i]) => gives following warning: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
            bar.set_height(rec.iloc[i])

        ax.set_title(rec.name)
        fig.canvas.draw()


    def next(self, event):
        self.idx += 1
        row_index = self.idx % len(record)
        # print(row_index)
        # print(df.index[row_index])
        # print(df.loc[df.index[row_index]])
        rec = df.loc[df.index[row_index]]

        for i, bar in enumerate(bars):
            bar.set_height(rec.iloc[i])

        ax.set_title(rec.name)
        fig.canvas.draw()


fig, ax = plt.subplots(figsize=(7, 6))
bars = ax.bar(position, record)
plt.xticks(position, labels)
ax.set_title(record.name)

plt.subplots_adjust(bottom = 0.2)

current_index = IndexTracker()

# create buttons area
ax_prev = plt.axes([0.58, 0.05, 0.15, 0.07])
ax_next = plt.axes([0.75, 0.05, 0.15, 0.07])

# create buttons
button_prev = Button(ax_prev, 'previous', color='green', hovercolor='blue')
button_next = Button(ax_next, 'next', color='orange', hovercolor='red')

button_prev.on_clicked(current_index.previous)
button_next.on_clicked(current_index.next)

plt.show()


