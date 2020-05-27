import numpy as np
import pylab
import math
import wfdb
import logging


class HandlerECG:
    def __init__(self, N):
        self.N = N
        self.const_eight_counts = 1 / 8
        self.const = 'storage/ecgiddb/1.0.0/'
        self.const_rec = '/rec_1'
        self.const_atr = 'atr'
        self.mc = 1000

    def get_Inform_from_Person(self, person):
        way = self.const + person + self.const_rec
        record = wfdb.rdrecord(way, sampto=self.N)
        annotation = wfdb.rdann(way, self.const_atr, sampto=self.N)

        return record, annotation

    def filter_moving_average(self, x):
        f = np.zeros(self.N)
        for i in range(6):
            f[i] = self.const_eight_counts * x[i]
        i = 7
        while i < self.N:
            j = 0
            sum = 0
            while j <= 7:
                sum += x[i - j]
                j += 1
            f[i] = self.const_eight_counts * sum
            i += 1
        '''
        pylab.subplot(2, 1, 2)
        pylab.plot([k for k in range(1, self.N + 1)], f)
        pylab.title("filter moving average")
        for i in range(len(x)):
            f[i] = x[i]
        pylab.subplot(2, 1, 1)
        pylab.plot([k for k in range(1, self.N + 1)], f, color='green')
        pylab.title("ECG")
        pylab.show()
        '''

        return f

    def Pana_Tompkinsa(self, x, fs):
        function = np.zeros(self.N)

        p = np.zeros(self.N)
        der = np.zeros(self.N)
        f = np.zeros(self.N)
        fun = np.zeros(self.N)

        for i in range(len(x)):
            f[i] = x[i][0]
        self.filter_moving_average(f)

        def recursion_filter_down_frequency(filter_down):
            filter_down[0] = x[0][0] / 32
            filter_down[1] = 2 * filter_down[0] + x[1][0] / 32
            filter_down[2] = 2 * filter_down[1] \
                             - filter_down[0] \
                             + x[2][0] / 32
            i = 3
            while i < 6:
                filter_down[i] = 2 * filter_down[i - 1]\
                                 - filter_down[i - 2]\
                                 + x[i][0] / 32
                i += 1
            while i < 12:
                filter_down[i] = 2 * filter_down[i - 1]\
                                 - filter_down[i - 2] \
                                 + (x[i][0]
                                    - 2 * x[i - 6][0]) / 32
                i += 1
            while i < self.N:
                filter_down[i] = 2 * filter_down[i - 1] \
                                 - filter_down[i - 2] \
                                 + (x[i][0] - 2 * x[i - 6][0]
                                    + x[i - 12][0]) / 32
                i += 1
            return filter_down

        def filter_up_frequency(fulter_up, fun):
            fulter_up[0] = -fun[0] / 32
            i = 1
            while i < 16:
                fulter_up[i] = fulter_up[i - 1] \
                               - fun[i] / 32
                i += 1
            fulter_up[i] = fulter_up[i - 1] \
                           - (fun[i] / 32) \
                           + fun[i - 16]
            i += 1
            while i < 32:
                fulter_up[i] = fulter_up[i - 1] \
                               - (fun[i] / 32) \
                               + fun[i - 16] - fun[i - 17]
                i += 1
            while i < self.N:
                fulter_up[i] = fulter_up[i - 1] \
                               - (fun[i] / 32) \
                               + fun[i - 16] - fun[i - 17]\
                               + fun[i - 32] / 32
                i += 1
            return fulter_up

        def derivative(der, fun):
            der[0] = fun[0] / 4
            i = 1
            while i < 3:
                der[i] = (2 * fun[i]
                          + fun[i - 1]) / 8
                i += 1
            der[i] = (2 * fun[i]
                      + fun[i - 1]
                      - fun[i - 3]) / 8
            i += 1
            while i < self.N:
                der[i] = (2 * fun[i]
                          + fun[i - 1]
                          - fun[i - 3]
                          - 2 * fun[i - 4]) / 8
                i += 1
            return der

        def square(fun):
            for i in range(len(fun)):
                fun[i] = fun[i] ** 2
            return fun

        def integral(fun, x, fs):
            N_ = int(fs * 3 / 20)
            i = 0
            while i < 30:
                fun[i] = x[0] / N_
                i += 1
            while i < self.N:
                delta = N_
                sum = 0
                while delta != 0:
                    delta -= 1
                    sum += x[i - (delta)]

                fun[i] = sum / N_
                i += 1
            return 100 * fun

        function = recursion_filter_down_frequency(function)
        p = filter_up_frequency(p, function)
        '''
        pylab.subplot(6, 1, 1)
        pylab.plot([k for k in range(1, N + 1)], f)
        pylab.title("ECG")
        pylab.subplot(6, 1, 2)
        pylab.plot([k for k in range(1, N + 1)], function)
        pylab.title("recursion filter down frequency")
        pylab.subplot(6, 1, 3)
        pylab.plot([k for k in range(1, N + 1)], p)
        pylab.title("filter up frequency")
        pylab.subplot(6, 1, 4)
        '''
        der = derivative(der, p)
        '''
        pylab.plot([k for k in range(1, N + 1)], der)
        pylab.title("derivative")
        '''
        der = square(der)
        '''
        pylab.subplot(6, 1, 5)
        pylab.plot([k for k in range(1, N + 1)], der)
        pylab.title("square")
        pylab.subplot(6, 1, 6)
        '''
        fun = integral(fun, der, fs)
        '''
        pylab.plot([k for k in range(1, N + 1)], fun, color='green')
        pylab.title("Pana-Tompkinsa")
        pylab.show()
        '''
        return f, p, self.filter_moving_average(fun)

    def get_peaks_counts(self, x):
        eps = self.average(x) + self.average(x) / 5
        i = 0
        delta = 0
        peaks = 0
        while i < self.N:
            if x[i] > eps:
                if x[i] > delta:
                    delta = x[i]
                elif x[i] < delta:
                    peaks += 1
                    delta = eps
                    while delta < x[i]:
                        i += 1
                        if i == self.N:
                            break
            i += 1
        return peaks

    def beats_per_minute(self, M):
        const = 60 / M
        return const

    def average(self, a):
        s = 0
        for i in range(len(a)):
            s += a[i]
        return s / len(a)

    def find_peaks(self, x):
        i = 0
        eps = self.average(x) + self.average(x) / 5
        j = 0
        peaks_counts = self.get_peaks_counts(x)
        f = np.zeros(peaks_counts)
        while i < self.N - 1 and j < peaks_counts:
            if x[i] > eps:
                max = 0
                while x[i] > eps:
                    if x[max] < x[i]:
                        max = i
                    i += 1
                    if i >= self.N - 1:
                        break
                f[j] = max
                j += 1
            i += 1
        logging.info("peaks count = {}".format(f))
        return f

    def sco_math_expectation(self, peaks):
        sum_sco = 0.0
        M = self.math_expectation(peaks)

        for i in range(len(peaks) - 1):
            sum_sco += (((peaks[i + 1] - peaks[i]) / self.mc) - M) ** 2

        D = sum_sco / (len(peaks) - 2)
        sco = D ** 0.5
        return sco, D

    def coefficient_covariance(self, M, SCO):
        return 100 * SCO / M

    def math_expectation(self, peaks):
        delta = 0.0
        for i in range(len(peaks) - 1):
            delta += (peaks[i + 1] - peaks[i])

        M = delta / (len(peaks) - 1)
        return M / self.mc

    def moda_and_amplitude(self, peaks):
        delta = 0.0
        eps = 0.01
        f = np.zeros(len(peaks))
        count_mode = np.zeros(len(peaks))
        for i in range(len(peaks) - 1):
            delta += (peaks[i + 1] - peaks[i])
            f[i] = (peaks[i + 1] - peaks[i])
        for m in range(len(f)):
            count = 0
            for t in range(len(f) - 1):
                if math.fabs(f[t + 1] - f[m]) / self.mc < eps:
                    count += 1
            count_mode[m] = count
        max = len(peaks) - 1
        for m in range(len(count_mode)):
            if count_mode[max] < count_mode[m]:
                max = m

        def amplitude_mode():
            return 100 * max / len(peaks)

        return f[max] / self.mc, amplitude_mode()

    def variational_range(self, peaks):
        f = np.zeros(len(peaks))
        for i in range(len(peaks) - 2):
            f[i] = math.fabs((peaks[i + 1] - peaks[i])) / self.mc

        max_f = max(f)
        min = 0
        for m in range(len(f)):
            if f[min] > f[m] != 0:
                min = m

        delta_x = max_f - f[min]
        return delta_x

    def index_vegetative_balance(self, amplitude, delta_x):
        return amplitude / delta_x

    def vegetative_rhethm_indicator(self, mode, delta_x):
        return 1 / (mode * delta_x)

    def indicator_of_the_adequacy_of_the_regularity_process(self, amplitude, mode):
        return amplitude / mode

    def stress_index_Baevsky(self, amplitude, delta_x, mode):
        return amplitude / (2 * delta_x * mode)

    def static_analysis_ECG(self, record):
        function_, filter_function, sequence = self.Pana_Tompkinsa(record.p_signal, record.fs)
        peaks = self.find_peaks(self.filter_moving_average(sequence))
        correlation = self.correlation_coefficient(sequence)
        M = self.math_expectation(peaks)
        SCO, D = self.sco_math_expectation(peaks)
        coefficient_cov = self.coefficient_covariance(M, SCO)
        m, amplitude = self.moda_and_amplitude(peaks)
        delta_x = self.variational_range(peaks)
        index = self.index_vegetative_balance(amplitude, delta_x)
        vri = self.vegetative_rhethm_indicator(m, delta_x)
        iarp = self.indicator_of_the_adequacy_of_the_regularity_process(amplitude, m)
        sib = self.stress_index_Baevsky(amplitude, delta_x, m)
        logging.info("correlation = {}".format(correlation))
        logging.info("peaks = {}".format(peaks))
        logging.info("M = {}".format(M))
        logging.info("D = {}".format(D))
        logging.info("SCO = {}".format(SCO))
        logging.info("coefficient_cov = {} %".format(coefficient_cov))
        logging.info("Moda = {}".format(m))
        logging.info("amplitude = {} %".format(amplitude))
        logging.info("delta_x = {}".format(delta_x))
        logging.info("index vegetative balance = {}ед".format(index))
        logging.info("vri = {} %".format(vri))
        logging.info("iarp = {}".format(iarp))
        logging.info("sib  = {}".format(sib))
        return peaks, M, D, SCO, coefficient_cov, m, amplitude, delta_x, index, vri, iarp, sib

    def correlation_coefficient(self, sequence_2):
        record = wfdb.rdrecord('storage/ecgiddb/1.0.0/Person_01/rec_1', sampto=self.N)
        function_, filter_function, sequence = self.Pana_Tompkinsa(record.p_signal, record.fs)
        peaks = self.find_peaks(self.filter_moving_average(sequence_2))
        eps = self.average(sequence)
        eps_2 = self.average(sequence_2)
        i = 0
        sum_ = 0
        sum_1_square = 0
        sum_2_square = 0
        index_1 = 0
        index_2 = 0
        while i < peaks[len(peaks) - 1]:
            if sequence_2[i] > eps_2:
                index_1 = i
                break
            i += 1
        i = 0
        while i < peaks[len(peaks) - 1]:
            if sequence[i] > eps:
                index_2 = i
                break
            i += 1
        i = 0
        while i < peaks[2]:

            if sequence_2[i + index_1] > eps_2:
                sum_2_square += (sequence_2[i + index_1] ** 2)
                element_2 = sequence_2[i + index_1]
            else:
                element_2 = 0
            if sequence[i + index_2] > eps:
                sum_1_square += (sequence[i + index_2] ** 2)
                element_1 = sequence[i + index_2]
            else:
                element_1 = 0
            sum_ += (element_2*element_1)
            i += 1

        correlation = sum_/((sum_1_square * sum_2_square) ** 0.5)
        return correlation


