import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


def plot_bar(bars: list, items: dict):
    x = np.arange(len(bars))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0.5

    fig, ax = plt.subplots(layout='constrained')
    ax.grid(zorder=0)
    for attribute, measurement in items.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=0, rotation=20)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Messages Count')
    ax.set_title('')
    ax.set_xticks(x + width, bars)
    ax.legend(loc='upper left', ncols=2)
    ax.set_axisbelow(True)


    # ax.set_ylim(0, 250)
    plt.savefig('foo.pdf')
    plt.show()
    return 0


def main():
    df = pd.read_csv('telegram_data.csv')
    # print(df.head)
    # print(df.columns)
    # print(pd.unique(df.sender))
    # print(df.date[0])
    # print(df.msg_type.unique())
    df['date'] = pd.to_datetime(df['date'])
    # print(type(df.date[0]))
    # print(df.info(verbose=True))
    df.loc[df['sender'] == 'Vlad Yti', 'sender'] = 'PVA'
    df.loc[df['sender'] == 'Й', 'sender'] = 'AMI'
    ttt = df.where((df.date.dt.year == 2018) & (df.msg_type == 'text'))
    print(ttt.where(ttt.sender == 'AMI').count().msg_id)

    print(df.date.keys())
    print(type(df.date))
    print(type(df.date[0].year))

    PVA_mes_count = []
    AMI_mes_count = []
    for i in range(6):
        PVA_mes_count.append(df.where((df.date.dt.year == 2018 + i)
                                      & (df.msg_type == 'text')
                                      & (df.sender == 'PVA')).count().msg_id)
        AMI_mes_count.append(df.where((df.date.dt.year == 2018 + i)
                                      & (df.msg_type == 'text')
                                      & (df.sender == 'AMI')).count().msg_id)

    print(PVA_mes_count)
    print(AMI_mes_count)
    years = (2018, 2019, 2020, 2021, 2022, 2023)
    it = {'PVA': PVA_mes_count, 'AMI': AMI_mes_count}
    plot_bar(years, it)
    return 0


if __name__ == '__main__':
    main()
