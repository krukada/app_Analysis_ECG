def function_analysis(peaks, M, D, SCO, coefficient_cov, m, amplitude, delta_x, index, vri, iarp, sib, bpm):
    full_analysis = ''

    def analysis_mat_expectation():

        conclusion = ''
        if M < 0.5:
            conclusion = M_Expressed_Tachycardia
        elif 0.5 <= M < 0.66:
            conclusion = M_Tachycardia
        elif 0.66 <= M < 0.76:
            conclusion = M_Moderate_Tachycardia
        elif 0.75 <= M < 0.9:
            conclusion = M_Normal_heart_rate
        elif 0.9 <= M < 1.:
            conclusion = M_Moderate_Bradycardia
        elif 1. <= M < 1.2:
            conclusion = M_Bradycardia
        elif M > 1.2:
            conclusion = M_Expressed_Bradycardia
        return conclusion

    def analysis_SCO():

        conclusion = ''
        if 0.02 <= SCO <= 0.06:
            conclusion = SCO_normal_rhythm_veracity
        elif 0.06 < SCO < 0.1:
            conclusion = SCO_cardiac_arrhythmias
        elif SCO > 0.1:
            conclusion = SCO_Expressed_cardiac_arrhythmias
        elif SCO < 0.02:
            conclusion = SCO_rigid_rhythm
        return conclusion

    def analysis_coefficient_cov():

        conclusion = ''
        if 3 <= coefficient_cov <= 5:
            conclusion = coefficient_cov_normal_heart_rate
        elif coefficient_cov > 10:
            conclusion = coefficient_cov_heart_rhythm_disturbance
        elif coefficient_cov > 5:
            conclusion = coefficient_cov_increase_in_cardiac_arrhythmia
        elif 3 > coefficient_cov:
            conclusion = coefficient_cov_heart_rate_stabilization
        return conclusion

    def analysis_amplitude():

        if 20 <= amplitude < 50:
            conclusion = normal_amplitude
        else:
            conclusion = not_normal_amplitude
        return conclusion

    def analysis_delta_x():

        if 0.15 <= delta_x <= 0.3:
            conclusion = variation_range_of_normal
        else:
            conclusion = variation_range_of_not_normal
        return conclusion

    def analysis_IVR():
        conclusion = ''
        if 100 <= index <= 300:
            conclusion = ivr_normal
        elif index > 300:
            conclusion = ivr_upscale
        return conclusion

    def analysis_VPR():
        conclusion = ''
        if 7.1 <= vri <= 9.3:
            conclusion = vpi_normal
        elif vri < 7.1:
            conclusion = vpi_lowered
        elif vri > 9.3:
            conclusion = vpi_upscale
        return conclusion

    def analysis_PAPR():
        conclusion = ''
        if 35 <= iarp <= 70:
            conclusion = papr_normal
        elif iarp > 70:
            conclusion = papr_upscale
        elif iarp < 35:
            conclusion = papr_lowered
        return conclusion

    def analysis_index_Baevsky():

        conclusion = ''
        if 50 <= sib <= 200:
            conclusion = Baevsky_Stress_Index_state_of_rest
        elif 500 >= sib > 200:
            conclusion = Baevsky_Stress_Index_upscale
        elif sib >= 900:
            conclusion = Baevsky_Stress_Index_upscale_pre_infarction_condition
        elif sib >= 600:
            conclusion = Baevsky_Stress_Index_upscale_stenocardia
        elif sib < 50:
            conclusion = Baevsky_Stress_Index_lowered
        return conclusion

    full_analysis += '  ' + analysis_mat_expectation() + '\n\n'
    full_analysis += '  ' + analysis_SCO() + '\n\n'
    full_analysis += '  ' + analysis_amplitude() + '\n\n'
    full_analysis += '  ' + analysis_coefficient_cov() + '\n\n'
    full_analysis += '  ' + analysis_delta_x() + '\n\n'
    full_analysis += '  ' + analysis_IVR() + '\n\n'
    full_analysis += '  ' + analysis_VPR() + '\n\n'
    full_analysis += '  ' + analysis_PAPR() + '\n\n'
    full_analysis += '  ' + analysis_index_Baevsky() + '\n\n'

    return full_analysis


M_Expressed_Tachycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Выраженную ' \
                          'Тахикардию. '

M_Tachycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Тахикардию.'

M_Moderate_Tachycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Умеренную Тахикардию.'

M_Normal_heart_rate = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Нормальный пульс.'

M_Moderate_Bradycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Умеренную ' \
                         'Брадикардию.> '
M_Bradycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Брадикардию.'

M_Expressed_Bradycardia = 'Математическое ожидание по всему ряду пульсовых интервалов указывает на Выраженнаю. ' \
                          'Брадикардию. '

SCO_normal_rhythm_veracity = 'Среднеквадратичное отклонение по всему ряду пульсовых интервалов в норме - нормальная ' \
                             'верабельность ритма. '

SCO_cardiac_arrhythmias = 'Среднеквадратичное отклонение по всему ряду пульсовых интервалов указывает на наличие ' \
                          'аритмии сердца. '

SCO_Expressed_cardiac_arrhythmias = 'Среднеквадратичное отклонение по всему ряду пульсовых интервалов указывает на ' \
                                    'выраженную ' \
                                    'аритмию сердца. '

SCO_rigid_rhythm = 'Среднеквадратичное отклонение по всему ряду пульсовых интервалов указывает на стабильный(' \
                   'ригидный) ритм. '

coefficient_cov_normal_heart_rate = 'Коэффициент вариации указывает на нормальный ритм сердца.'

coefficient_cov_heart_rhythm_disturbance = 'Коэффициент вариации указывает на нарушение ритмичности сердца.'

coefficient_cov_increase_in_cardiac_arrhythmia = 'Коэффициент вариации указывает о нарастании аритмичности сердца.'

coefficient_cov_heart_rate_stabilization = 'Коэффициент вариации указывает о стабилизации ритма сердца.'

normal_amplitude = 'Нормальное значение амплитуды - стабильное воздействие симпатического отдела нервной ' \
                   'системы '

not_normal_amplitude = 'Не нормальное значение амплитуды - не стабильное воздействие симпатического отдела нервной ' \
                       'системы '

variation_range_of_normal = 'Значение вариационного размаха (максимальный разброс значений межпульсовых ' \
                            'кардиоинтервалов) в норме - приводится в качестве оценки о фоновых аритмиях и о состоянии ' \
                            'вегетатичного гомеостаза '
variation_range_of_not_normal = 'Значение вариационного размаха (максимальный разброс значений межпульсовых ' \
                                'кардиоинтервалов) не в норме - приводится в качестве оценки о фоновых аритмиях и о ' \
                                'состоянии ' \
                                'вегетатичного гомеостаза '

ivr_normal = 'Индекс Вегетатичного равновесия в норме, из этого следует, что нет гипертонуса ' \
             'симпатического отдела '

ivr_upscale = 'Индекс Вегетатичного равновесия повышен, что свидетельствует о  гипертонуса ' \
              'симпатического отдела, снижению ваготании '

vpi_normal = 'Вегетативный показатель ритма в норме - вегетатичный баланс с точки зрения автономного ' \
             'контура '

vpi_lowered = 'Вегетативный показатель ритм не в норме - вегетатичный баланс смещен в сторону ' \
              'преобладания парасимпатического отдела '

vpi_upscale = 'Вегетативный показатель ритм не в норме'

papr_normal = 'Показатель адекватности процессов регуляции отражает соответствие между активностью ' \
              'симпатического отдела вегетатичной нервной системы и ведущим уровнем функционирования ' \
              'синусного узла. В данном случае показатель находится в норме - централизация управления ' \
              'ритмом '
papr_upscale = 'Показатель адекватности процессов регуляции отражает соответствие между активностью ' \
               'симпатического отдела вегетатичной нервной системы и ведущим уровнем функционирования ' \
               'синусного узла. В данном случае показатель находится выше нормы - недостаточная ' \
               'централизация управления ' \
               'ритмом '

papr_lowered = 'Показатель адекватности процессов регуляции отражает соответствие между активностью ' \
               'симпатического отдела вегетатичной нервной системы и ведущим уровнем функционирования ' \
               'синусного узла. В данном случае показатель находится ниже нормы - избыточная ' \
               'централизация управления ' \
               'ритмом '

Baevsky_Stress_Index_state_of_rest = 'Индекс напряджения Баевского в норме - характеризует степень централизации управления ' \
                                     'ритмом (состояние покоя) '

Baevsky_Stress_Index_upscale = 'Индекс напряджения Баевского увеличен (избыточная активность высших уровней центрального ' \
                               'контура) - характеризует степень централизации управления ритмом, данный показатель ' \
                               'показывает эмоциональный стресс или физическую работу у здоровых людей '

Baevsky_Stress_Index_upscale_pre_infarction_condition = 'Индекс напряджения Баевского увеличен (избыточная активность высших уровней центрального ' \
                                                        'контура) - характеризует степень централизации управления ритмом - прединфарктное состояние '

Baevsky_Stress_Index_upscale_stenocardia = 'Индекс напряджения Баевского увеличен (избыточная активность высших уровней центрального ' \
                                           'контура) - характеризует степень централизации управления ритмом - стенокардия '

Baevsky_Stress_Index_lowered = 'Индекс напряджения Баевского понижен (ваготония) - характеризует степень централизации ' \
                               'управления ритмом '
