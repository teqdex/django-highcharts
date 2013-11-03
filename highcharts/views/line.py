from highcharts.views import HighChartsBasicView
from django.views.generic import View


class HighChartsLineView(HighChartsBasicView, View):
    chart = {}
    categories = []
    y_axis = {}
    y_axis_title = None

    def get_data(self):
        data = super(HighChartsLineView, self).get_data()
        data['chart'] = self.chart
        data['xAxis'] = {}
        data['xAxis']['categories'] = self.categories
        data['yAxis'] = self.y_axis
        data['yAxis']['title'] = {"text": self.y_axis_title}
        data['series'] = self.series
        return data

    @property
    def series(self):
        return []
