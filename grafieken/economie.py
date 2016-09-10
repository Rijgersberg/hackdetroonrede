import pandas as pd
from matplotlib import pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

plt.style.use('ggplot')


def main():
    df = pd.read_excel('economie_schoon.xls', index_col='jaar')
    print df

    nl = go.Scatter(
        x=df.index,
        y=df['Nederland'],
        name='Nederland',
        line={'color': 'orange'}
    )
    de = go.Scatter(
        x=df.index,
        y=df['Duitsland'],
        name='Duitsland',
        line={'color': 'black'}
    )
    be = go.Scatter(
        x=df.index,
        y=df['Belgie'],
        name='België',
        line={'color': 'red'}
    )
    eu = go.Scatter(
        x=df.index,
        y=df['EU'],
        name='EU',
        line={'color': 'blue'}
    )

    layout = go.Layout(
        title='Bruto Binnenlands Product per capita (euro)',
        showlegend=True,
        yaxis=dict(
            title='BBP per capita (euro)',
        )
    )

    data = [nl, de, be, eu]
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='economie')
    print plot_url


if __name__ == '__main__':
    main()
