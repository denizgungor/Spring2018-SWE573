import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from swe573 import settings

class Graph(object):
    def __init__(self, analyse_results):
        self.analyse_results = analyse_results

    def draw_graph(self):
        neg = []
        neu = []
        pos = []
        comp = []
        x = []
        y = []

        for result in self.analyse_results:
            print(result)
            print(type(result))
            r = list(result)
            print(list(result))
            neg.append(str(r[0])[8:-1])
            neu.append(str(r[1])[8:-1])
            pos.append(str(r[2])[8:-1])
            comp.append(str(r[3])[13:-1])
            print(str(r[3])[13:-1])
            print("-------------------------------------------------------------------------"
                  ""
                  ""
                  ""
                  ""
                  "---------------------------------------------------------------------")

        neg = self.string_to_float(neg)
        neu = self.string_to_float(neu)
        pos = self.string_to_float(pos)
        # comp = self.string_to_float(comp)

        # self.negative = self.column(self.analyse_results, 0)
        # self.nautral = self.column(self.analyse_results, 1)
        # self.positive = self.column(self.analyse_results, 2)
        #
        fig = plt.figure()
        plt.title('Sentiment Analysis')
        plt.xlabel('Number of Tweets')
        plt.ylabel('Values')
        print(type(neg))
        print(neg)

        x = range(len(neg))
        # plot the data itself
        #plt.plot(x, neg, 'o')
        #plt.plot(x, neu, 'o')
        #plt.plot(x, pos, 'o')
        # plt.plot(x, neg, 'o', c=neg)
        # plt.plot(x, neu, 'o', c=neg)
        # plt.plot(x, pos, 'o', c=neg)
        # plt.plot(x, neg,'o')

        # # calc the trendline (it is simply a linear fitting)
        # z = numpy.polyfit(x, y, 1)
        # p = numpy.poly1d(z)
        # plt.plot(x, p(x),"r--")
        # the line equation:

        #colors = [(1-n, 1-n, 1-n) for n in neg]

        stacked_neu = neg
        stacked_pos = neg + neu

        plt.bar(range(1, len(neg + 1)), neg, align="center", color='coral')
        plt.bar(range(1, len(neg + 1)), neu, bottom=stacked_neu, align="center", color='khaki')
        plt.bar(range(1, len(neg + 1)), pos, bottom=stacked_pos, align="center", color='forestgreen')
        # fig.savefig('denizgraph.png', dpi=fig.dpi)
        fig.savefig(settings.BASE_DIR + settings.STATIC_URL + 'deniz_graph.png')


        # plt.bar(range(len(neg)), neg, align="center")
        # plt.xticks(range(len(neg)), neg)
        # fig.savefig('denizgraph.png', dpi=fig.dpi)
        # fig.savefig(settings.BASE_DIR + settings.STATIC_URL + '/denizgraph.png')
        return plt


    def string_to_float(self, my_list):
        return np.array([float(i) for i in my_list])


