import matplotlib.pyplot as plt
import matplotlib.patches as patches
import japanize_matplotlib
import pandas as pd


def main():
    filename = 'datas.csv'
    df = pd.read_csv(filename)
    size_df = len(df['title'])

    for i in range(size_df):
        title = df['title'][i]
        m_list = [
            df['固定資産'][i],
            df['流動資産'][i],
            df['純資産'][i],
            df['固定負債'][i],
            df['流動負債'][i]
        ]

        b2s = BS2Square()
        b2s.plot(title, m_list)
        b2s.save(df['title'][i] + '.png')


class BS2Square:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.texts = ['固定資産', '流動資産', '純資産', '固定負債', '流動負債']

    def plot(self, title, m_list):
        colors = ['#4472C5', '#599AD5', '#70AC46', '#FEC002', '#EC7D31']
        rate = [m_list[0] / (m_list[0] + m_list[1]),
                m_list[1] / (m_list[0] + m_list[1]),
                m_list[2] / (m_list[2] + m_list[3] + m_list[4]),
                m_list[3] / (m_list[2] + m_list[3] + m_list[4]),
                m_list[4] / (m_list[2] + m_list[3] + m_list[4])]
        _x = [0, 0, 0.5, 0.5, 0.5]
        _y = [0, rate[0], 0, rate[2], rate[2] + rate[3]]

        list_of_rectangle = []
        for i in range(5):
            list_of_rectangle.append(
                patches.Rectangle(
                    xy=(_x[i], _y[i]), width=0.5, height=rate[i],
                    fc=colors[i], ec='b'))
            cx = _x[i] + list_of_rectangle[i].get_width() / 2.
            cy = _y[i] + list_of_rectangle[i].get_height() / 2.

            self.ax.annotate(self.texts[i] + '\n（{:,}）'.format(m_list[i]),
                             (cx, cy), color='black', weight='bold',
                             fontsize=14, ha='center', va='center')

        for e in list_of_rectangle:
            self.ax.add_patch(e)

        plt.axis('scaled')
        self.ax.set_ylabel('{:,}'.format(m_list[0] + m_list[1]),
                           weight='bold', fontsize=16)
        self.ax.set_title(title, weight='bold', fontsize=16)
        self.ax.set_aspect('equal')

    def save(self, file_name='a.png'):
        plt.savefig(file_name, transparent=True)


if __name__ == '__main__':
    main()
