exec(open('C:/Users/gilbe/OneDrive/Bureau/MDSMS 2/Data Science sous Python et R/jinja-star-admin-master/app/metrics_df.py').read())
donnees = df
from highcharts_core.chart import Chart
from highcharts_core.global_options.shared_options import SharedOptions
from highcharts_core.options import HighchartsOptions
from highcharts_core.options.plot_options.bar import BarOptions
from highcharts_core.options.series.bar import BarSeries
from highcharts_core.options.title import Title
from highcharts_core.options.subtitle import Subtitle

from highcharts_core import highcharts

#hc1 = Chart(data = donnees.iloc[:-1,1].tolist(),
           # series_type = 'line')
hc1 = Chart.from_pandas(donnees.iloc[:-1,:],
                          property_map={
                                        'x': 'Names',
                                        'y': 'Metrics'
                                    },
                          series_type = 'line')


my_title = Title(text = 'Courbe des métriques',
                 align = 'center',
                 use_html = True)
my_subtitle = Subtitle(
        text = '<b><i>Source : Travaux sous Jupyter Notebook</i></b>')
xaxis = {'categories' : donnees.iloc[:-1,0].tolist()}
yaxis = {'title' :  {'text': 'Pourcentage (%)'},
         'labels': {format: '{value}'}
        }

hc1.options.title = my_title
hc1.options.subtitle = my_subtitle
hc1.options.x_axis = xaxis
hc1.options.y_axis = yaxis
