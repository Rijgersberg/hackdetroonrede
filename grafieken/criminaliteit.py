import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


def main():
    df = pd.read_csv('criminaliteit_schoon.csv', index_col='jaar')
    politie = pd.read_csv('uitgavenpolitie_schoon.csv', index_col='jaar')
    df['uitgaven'] = politie['politieuitgaven']
    print df

    trace1 = go.Bar(
        x=df.index,
        y=df['uitgaven'],
        name='Politieuitgaven (Mln)',
    )

    trace2 = go.Scatter(
        x=df.index,
        y=df['criminaliteit'],
        name='Misdrijven per 1000 inwoners',
        yaxis='y2'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title='Overheidsuitgaven aan politie en misdrijven per 1000 inwoners',
        showlegend=False,
        yaxis=dict(
            title='Uitgaven politie (x 1,000,000 euro)',
        ),
        yaxis2=dict(
            title='Misdrijven per 1000 inwoners',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right',
            range=[0, 100]
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='multiple-axes-double')
    print plot_url


if __name__ == '__main__':
    main()
