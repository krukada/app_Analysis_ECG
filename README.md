# Analysis ECG
В данной работе создана программа, которая на вход принимает значения биологических сигланов электрокардиограммы и далее выполняет поэтапно шаги:
1.	Фильтрация биологических сигналов с целью избавления от лишних шумов;
2.	Применение алгоритма Пана-Томкинса для поиска QRS - комплексов;
3.	Поиск R-R интервалов в электрокардиограмме;
4.	Вычисление функциональных показателей для анализа электрокардиограммы;
5.	Вынос заключения об электрокардиограмме посредством анализа функциональных показателей. 

Данная программа может быть использована для фукнционального анализа для биологических сигналов ЭКГ.

### Получение электрокардиограмм
-------------------------
Биологические сигналы получены с сайта [physionet](https://physionet.org):
>Гольдбергер А., Амарал Л., Гласс Л., Хаусдорф Ю., Иванов П.С., Марк Р., ... и Стэнли Х. ( 2000). PhysioBank, PhysioToolkit и PhysioNet: компоненты нового исследовательского ресурса для сложных физиологических сигналов. Тираж [Онлайн]. 101 (23), с. E215 – e220.

из [Базы Данных](https://physionet.org/content/ecgiddb/1.0.0/). Эта база данных была создана и предоставлена ​​Татьяной Луговой, которая использовала ее в своей магистерской работе:

>Луговая Т.С. Биометрическая идентификация человека на основе электрокардиограммы. [Магистерская работа] Факультет вычислительных технологий и информатики, Электротехнический университет "ЛЭТИ", Санкт-Петербург, Российская Федерация; Июнь 2005 г.

### Используемые библиотеки
-------------------------

+ [wfdb](https://wfdb.readthedocs.io/en/latest/wfdb.html#module-wfdb) - для получения биологических сигналов;
+ [PyQt5](https://doc.qt.io/qtforpython/#documentation) - для создания UI;
+ [pyqtgraph](https://pyqtgraph.readthedocs.io/en/latest/) - для добовления графиков в UI;
+ [pylab](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html) - для дебага программы;
+ [qdarkstyle](https://github.com/ColinDuquesnoy/QDarkStyleSheet) - для стилизирования UI.

### Инсталяция и запуск
-------------------------
Для инсталляции программы нужно склонировать себе локально проект –  в терминале ввести строку:
```
$ git clone https://github.com/krukada/app_Analysis_ECG.git 
```
Для воспроизведения программы понадобиться Python 3.6 или выше. Для запуска приложения нужно в корне проекта ввести строку в терминале:
```
$ python3 -m app
```
### Руководство пользователя
-------------------------
 
При запуске программы появится первое пользовательское окно – Analysis ECG , в котором нужно выбрать пациента для диагностики ЭКГ. Если выбор не будет совершен, по умолчанию, в программе выбирается первый пациент, он также всегда выбран при запуске программы. Чтобы выбрать другого пациента нужно нажать на виджет раскрывающегося списка и нажать в списке на  другого пациента. Следующим шагом следует нажать на кнопку – «Применить». 


После предыдущего нажатия произойдет открытие второго окна – Full Analysis ECG. Во втором окне приведен полный функциональный анализ ЭКГ выбранного пользователя. Второе пользовательское окно состоит из трех информативных блоков, в первом блоке располагается информация о пользователе (возраст, пол) и дата проведения ЭКГ, во втором блоке расположена полученная информация функциональных показателей для ЭКГ, во третьем блоке показаны графики: График входных биологических сигналов ЭКГ пациента, график значений сигналов после фильтрации – после избавления шумов на ЭКГ, график QRS - комплексов с выделенными «звездами» R - зубцами. Пользовательское окно дополняются кнопкой – «Получить заключение полного анализа ЭКГ». При нажатии на кнопку откроется третье окно – Total Full Analysis ECG.


Третье пользовательское окно – Total Full Analysis ECG, открытое после нажатия на кнопку – «Получить заключение полного анализа ЭКГ» во втором окне покажет заключение и возможные заболевания по найденным функциональным показателям. Заключение анализа ЭКГ можно проскроллить, чтобы увидеть оставшуюся информацию.
