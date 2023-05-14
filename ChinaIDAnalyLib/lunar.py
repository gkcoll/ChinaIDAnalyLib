'''
@File              :   lunar.py
@Time              :   2023/04/16 16:15:49
@Author            :   @灰尘疾客(gkcoll)
@Site              :   https://www.gkcoll.xyz
@Desc              :   A full-featured module of Chinese Lunar Calendar.
@Refer             :   https://github.com/CutePandaSh/zhdate
                       https://github.com/kiddx01/lunar
'''
from datetime import datetime, timedelta, date
from itertools import accumulate
import math


TIAN_GAN = "甲,乙,丙,丁,戊,己,庚,辛,壬,癸".split(",")
DI_ZHI = "子,丑,寅,卯,辰,巳,午,未,申,酉,戌,亥".split(",")
SHU_XIANG = "猪,鼠,牛,虎,兔,龙,蛇,马,羊,猴,鸡,狗".split(",")
JIA_ZHI60 = {
    1: "甲子", 2: "乙丑", 3: "丙寅", 4: "丁卯", 5: "戊辰", 6: "己巳", 7: "庚午", 8: "辛未", 9: "壬申", 10: "癸酉",
    11: "甲戌", 12: "乙亥", 13: "丙子", 14: "丁丑", 15: "戊寅", 16: "己卯", 17: "庚辰", 18: "辛巳", 19: "壬午", 20: "癸未",
    21: "甲申", 22: "乙酉", 23: "丙戌", 24: "丁亥", 25: "戊子", 26: "己丑", 27: "庚寅", 28: "辛卯", 29: "壬辰", 30: "癸巳",
    31: "甲午", 32: "乙未", 33: "丙申", 34: "丁酉", 35: "戊戌", 36: "己亥", 37: "庚子", 38: "辛丑", 39: "壬寅", 40: "癸卯",
    41: "甲辰", 42: "乙巳", 43: "丙午", 44: "丁未", 45: "戊申", 46: "己酉", 47: "庚戌", 48: "辛亥", 49: "壬子", 50: "癸丑",
    51: "甲寅", 52: "乙卯", 53: "丙辰", 54: "丁巳", 55: "戊午", 56: "己未", 57: "庚申", 58: "辛酉", 59: "壬戌", 60: "癸亥"
}


CHINESEYEARCODE = [
    19416,
    19168,  42352,  21717,  53856,  55632,  91476,  22176,  39632,
    21970,  19168,  42422,  42192,  53840, 119381,  46400,  54944,
    44450,  38320,  84343,  18800,  42160,  46261,  27216,  27968,
    109396,  11104,  38256,  21234,  18800,  25958,  54432,  59984,
    92821,  23248,  11104, 100067,  37600, 116951,  51536,  54432,
    120998,  46416,  22176, 107956,   9680,  37584,  53938,  43344,
    46423,  27808,  46416,  86869,  19872,  42416,  83315,  21168,
    43432,  59728,  27296,  44710,  43856,  19296,  43748,  42352,
    21088,  62051,  55632,  23383,  22176,  38608,  19925,  19152,
    42192,  54484,  53840,  54616,  46400,  46752, 103846,  38320,
    18864,  43380,  42160,  45690,  27216,  27968,  44870,  43872,
    38256,  19189,  18800,  25776,  29859,  59984,  27480,  23232,
    43872,  38613,  37600,  51552,  55636,  54432,  55888,  30034,
    22176,  43959,   9680,  37584,  51893,  43344,  46240,  47780,
    44368,  21977,  19360,  42416,  86390,  21168,  43312,  31060,
    27296,  44368,  23378,  19296,  42726,  42208,  53856,  60005,
    54576,  23200,  30371,  38608,  19195,  19152,  42192, 118966,
    53840,  54560,  56645,  46496,  22224,  21938,  18864,  42359,
    42160,  43600, 111189,  27936,  44448,  84835,  37744,  18936,
    18800,  25776,  92326,  59984,  27296, 108228,  43744,  37600,
    53987,  51552,  54615,  54432,  55888,  23893,  22176,  42704,
    21972,  21200,  43448,  43344,  46240,  46758,  44368,  21920,
    43940,  42416,  21168,  45683,  26928,  29495,  27296,  44368,
    84821,  19296,  42352,  21732,  53600,  59752,  54560,  55968,
    92838,  22224,  19168,  43476,  41680,  53584,  62034,  54560
]
CHINESENEWYEAR = [
    '19000131',
    '19010219', '19020208', '19030129', '19040216', '19050204',
    '19060125', '19070213', '19080202', '19090122', '19100210',
    '19110130', '19120218', '19130206', '19140126', '19150214',
    '19160203', '19170123', '19180211', '19190201', '19200220',
    '19210208', '19220128', '19230216', '19240205', '19250124',
    '19260213', '19270202', '19280123', '19290210', '19300130',
    '19310217', '19320206', '19330126', '19340214', '19350204',
    '19360124', '19370211', '19380131', '19390219', '19400208',
    '19410127', '19420215', '19430205', '19440125', '19450213',
    '19460202', '19470122', '19480210', '19490129', '19500217',
    '19510206', '19520127', '19530214', '19540203', '19550124',
    '19560212', '19570131', '19580218', '19590208', '19600128',
    '19610215', '19620205', '19630125', '19640213', '19650202',
    '19660121', '19670209', '19680130', '19690217', '19700206',
    '19710127', '19720215', '19730203', '19740123', '19750211',
    '19760131', '19770218', '19780207', '19790128', '19800216',
    '19810205', '19820125', '19830213', '19840202', '19850220',
    '19860209', '19870129', '19880217', '19890206', '19900127',
    '19910215', '19920204', '19930123', '19940210', '19950131',
    '19960219', '19970207', '19980128', '19990216', '20000205',
    '20010124', '20020212', '20030201', '20040122', '20050209',
    '20060129', '20070218', '20080207', '20090126', '20100214',
    '20110203', '20120123', '20130210', '20140131', '20150219',
    '20160208', '20170128', '20180216', '20190205', '20200125',
    '20210212', '20220201', '20230122', '20240210', '20250129',
    '20260217', '20270206', '20280126', '20290213', '20300203',
    '20310123', '20320211', '20330131', '20340219', '20350208',
    '20360128', '20370215', '20380204', '20390124', '20400212',
    '20410201', '20420122', '20430210', '20440130', '20450217',
    '20460206', '20470126', '20480214', '20490202', '20500123',
    '20510211', '20520201', '20530219', '20540208', '20550128',
    '20560215', '20570204', '20580124', '20590212', '20600202',
    '20610121', '20620209', '20630129', '20640217', '20650205',
    '20660126', '20670214', '20680203', '20690123', '20700211',
    '20710131', '20720219', '20730207', '20740127', '20750215',
    '20760205', '20770124', '20780212', '20790202', '20800122',
    '20810209', '20820129', '20830217', '20840206', '20850126',
    '20860214', '20870203', '20880124', '20890210', '20900130',
    '20910218', '20920207', '20930127', '20940215', '20950205',
    '20960125', '20970212', '20980201', '20990121', '21000209'
]
ZHNUMS = '〇一二三四五六七八九十'


class GanZhi():
    '''A class about Tian Gan Di Zhi(天干地支, also 8 Char(八字)).'''

    def __init__(self, dt: datetime = datetime.now()):
        if dt:
            if isinstance(dt, datetime):
                self.dt = dt
            else:
                raise TypeError('Please pass in a parameter of datetime type.')
        else:
            self.dt = datetime.now()

    def __getSolar(self, x=3) -> datetime:
        '''Get solar date.
        :param x: The order of the solar in the designated Gregorian year. Default value 3 is the order of LiChun(立春).'''
        if x not in range(1, 25):
            return None
        try:
            year = int(self.dt.year)
            x = int(x)
        except:
            return None
        if year < 1900:
            return None
        x -= 1
        startDT = datetime(1899, 12, 31)
        days = 365.242*(year - 1900) + 6.2 + 15.22*x - 1.9*math.sin(0.262*x)
        delta = timedelta(days=days)
        return startDT+delta

    def __getSolarTerms_byYear(self, jie_only: bool = False, qi_only: bool = False, addNum=False):
        '''Get all dates of solar terms in the designated year(Gregorian).
        :param jie_only: Only view 节 part.
        :param qi_only: Only view 气 part.
        :param addNum: Add orders of solar terms or not.'''
        res = []
        if jie_only and qi_only:
            raise KeyError(
                'Ensure that at least one of the 2 parameters(jie_only & qi_only) is False.')
        if jie_only:
            for i in range(1, 25, 2):
                if addNum:
                    res.append((self.__getSolar(x=i), i))
                else:
                    res.append(self.__getSolar(x=i))
        elif qi_only:
            for i in range(2, 25, 2):
                if addNum:
                    res.append((self.__getSolar(x=i), i))
                else:
                    res.append(self.__getSolar(x=i))
        else:
            for i in range(1, 25):
                if addNum:
                    res.append((self.__getSolar(x=i), i))
                else:
                    res.append(self.__getSolar(x=i))
        return res

    def lichun(self):
        '''Get LiChun(立春)\'day of the year(Gregorian).'''
        return self.__getSolar().day

    def getHourZhi(self, num=False):
        '''Get Di Zhi(地支) of the hour in designated date.'''
        try:
            n = int(self.dt.hour)
            cnt = int((n + 1) / 2)
            if cnt == 12:
                cnt = 0
            if num:
                return cnt + 1
            return DI_ZHI[cnt]
        except:
            return ""

    def getHourGanzhi(self, num=False):
        '''Get full Tian Gan Di Zhi(天干地支) of the hour in designated date.'''
        startDT = datetime(year=1901, month=1, day=1, hour=1)
        startGanzhi = 1

        delta = self.dt - startDT
        if delta.seconds < 0:
            return ""

        hours = delta.days*24 + delta.seconds/3600
        ganNum = int((startGanzhi + hours/2) % 10)
        if num:
            return (ganNum+1, self.getHourZhi(self.dt.hour, num=True))
        return ''.join([TIAN_GAN[ganNum], self.getHourZhi(), '时'])

    def getYearGanzhi(self, num=False):
        '''Get full Tian Gan Di Zhi(天干地支) of the year in designated date.'''
        if self.dt.year < 1900:
            return ""
        springDt = self.__getSolar(x=3)
        y = self.dt.year
        if self.dt < springDt:
            y -= 1
        ganNum = (y-4) % 10
        zhiNum = (y-4) % 12
        if num:
            return (ganNum+1, zhiNum+1)
        return ''.join([TIAN_GAN[ganNum], DI_ZHI[zhiNum], '年'])

    def getMonthGanzhi(self, num=False):
        '''Get full Tian Gan Di Zhi(天干地支) of the month in designated date.'''
        if self.dt.year < 1900:
            return ""
        jieqiDtList = self.__getSolarTerms_byYear(jie_only=True)
        startzhi = 1
        zhiNum = 0
        for jieqiDT, index in zip(jieqiDtList, range(12)):
            if self.dt >= jieqiDT:
                zhiNum = startzhi + index
        ganList = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
                   8: 7, 9: 8, 10: 9, 11: 10, 0: 11, 1: 12}
        yg = self.getYearGanzhi(num=True)[0]
        ganNum = (yg*2 + ganList[zhiNum]) % 10
        if ganNum == 0:
            ganNum = 10
        ganNum -= 1
        if num:
            return (ganNum+1, zhiNum+1)
        return ''.join([TIAN_GAN[ganNum], DI_ZHI[zhiNum], '月'])

    def getDayGanzhi(self, num=False):
        '''Get full Tian Gan Di Zhi(天干地支) of the day in designated date.'''
        dt = self.dt.date()
        startdate = date(1901, 1, 1)
        startganzhi = 16
        delta = dt - startdate
        if delta.days + delta.seconds < 0:
            return ""
        res = (startganzhi+delta.days) % 60
        if res == 0:
            res = 60
        ganNum = (res-1) % 10
        zhiNum = (res-1) % 12
        if num:
            return (ganNum+1, zhiNum+1)
        return ''.join([TIAN_GAN[ganNum], DI_ZHI[zhiNum], '日'])

    def __str__(self, without_hour: bool = True):
        year = self.getYearGanzhi()
        month = self.getMonthGanzhi()
        day = self.getDayGanzhi()
        if not without_hour:
            hour = self.getHourGanzhi()
            return str((year, month, day, hour))
        else:
            return str((year, month, day))

    def __repr__(self, without_hour: bool = True) -> str:
        return self.__str__(without_hour)

    def tpl(self, without_hour: bool = True) -> tuple:
        year = self.getYearGanzhi()
        month = self.getMonthGanzhi()
        day = self.getDayGanzhi()
        if not without_hour:
            hour = self.getHourGanzhi()
            return (year, month, day, hour)
        else:
            return (year, month, day)


class ZhDate():
    def __init__(self, lunar_year: int, lunar_month: int, lunar_day: int, leap_month: bool = False):
        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day
        self.leap_month = leap_month
        self.year_code = CHINESEYEARCODE[self.lunar_year - 1900]
        self.newyear = datetime.strptime(
            CHINESENEWYEAR[self.lunar_year - 1900], '%Y%m%d')

        if not ZhDate.validate(lunar_year, lunar_month, lunar_day, leap_month):
            raise TypeError(
                'Lunar date do not support “{}”, out of range from lunar 1900/01/01 to 2100/12/29, or the date is not existing.'.format(self))

    def to_datetime(self) -> datetime:
        return self.newyear + timedelta(days=self.__days_passed())

    @staticmethod
    def from_datetime(dt: datetime):
        lunar_year = dt.year
        lunar_year -= (datetime.strptime(
            CHINESENEWYEAR[lunar_year-1900], '%Y%m%d') - dt).total_seconds() > 0
        newyear_dt = datetime.strptime(
            CHINESENEWYEAR[lunar_year-1900], '%Y%m%d')
        days_passed = (dt - newyear_dt).days
        year_code = CHINESEYEARCODE[lunar_year - 1900]

        month_days = ZhDate.decode(year_code)
        for pos, days in enumerate(accumulate(month_days)):
            if days_passed + 1 <= days:
                month = pos + 1
                lunar_day = month_days[pos] - (days - days_passed) + 1
                break

        leap_month = False
        if (year_code & 0xf) == 0 or month <= (year_code & 0xf):
            lunar_month = month
        else:
            lunar_month = month - 1
        if (year_code & 0xf) != 0 and month == (year_code & 0xf) + 1:
            leap_month = True

        return ZhDate(lunar_year, lunar_month, lunar_day, leap_month)

    @staticmethod
    def today():
        return ZhDate.from_datetime(datetime.now())

    def __days_passed(self) -> int:
        month_days = ZhDate.decode(self.year_code)

        month_leap = self.year_code & 0xf

        if (month_leap == 0) or (self.lunar_month < month_leap):
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        elif (not self.leap_month) and (self.lunar_month == month_leap):
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        else:
            days_passed_month = sum(month_days[:self.lunar_month])

        return days_passed_month + self.lunar_day - 1

    def chinese(self):
        zh_year = ''
        for i in range(0, 4):
            zh_year += ZHNUMS[int(str(self.lunar_year)[i])]
        if self.leap_month:
            zh_month = '闰'
        else:
            zh_month = ''

        if self.lunar_month == 1:
            zh_month += '正'
        elif self.lunar_month == 12:
            zh_month += '腊'
        elif self.lunar_month <= 10:
            zh_month += ZHNUMS[self.lunar_month]
        else:
            zh_month += "十{}".format(ZHNUMS[self.lunar_month - 10])

        if self.lunar_day <= 10:
            zh_day = '初{}'.format(ZHNUMS[self.lunar_day])
        elif self.lunar_day < 20:
            zh_day = '十{}'.format(ZHNUMS[self.lunar_day - 10])
        elif self.lunar_day == 20:
            zh_day = '二十'
        elif self.lunar_day < 30:
            zh_day = '廿{}'.format(ZHNUMS[self.lunar_day - 20])
        else:
            zh_day = '三十'

        return (zh_year + '年', zh_month + '月', zh_day + '日')

    def ganzhi(self):
        return GanZhi(self.to_datetime())

    def __str__(self):
        return "{}年{}{}月{}日".format(self.lunar_year, "闰" if self.leap_month else "", self.lunar_month, self.lunar_day)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, another):
        if not isinstance(another, ZhDate):
            raise TypeError('Required all in ZhDate type.')
        cond1 = self.lunar_year == another.lunar_year
        cond2 = self.lunar_month == another.lunar_month
        cond3 = self.lunar_day == another.lunar_day
        cond4 = self.leap_month == another.leap_month
        return cond1 and cond2 and cond3 and cond4

    def __add__(self, another):
        if not isinstance(another, int):
            raise TypeError(
                'Addition only supports the addition of integer days.')

        return ZhDate.from_datetime(self.to_datetime() + timedelta(days=another))

    def __sub__(self, another):
        if isinstance(another, int):
            return ZhDate.from_datetime(self.to_datetime() - timedelta(days=another))
        elif isinstance(another, ZhDate):
            return (self.to_datetime() - another.to_datetime()).days
        elif isinstance(another, datetime):
            return (self.to_datetime() - another).days
        else:
            raise TypeError(
                'Subtraction only supports integers, ZhDate, Datetime types.')

    # These are supplemented by Albert Lin
    def __gt__(self, another):
        return self.__sub__(another) > 0

    def __lt__(self, another):
        return self.__sub__(another) < 0

    def __ge__(self, another):
        return self.__sub__(another) >= 0

    def __le__(self, another):
        return self.__sub__(another) <= 0

    def __eq__(self, another):
        return self.__sub__(another) == 0

    @staticmethod
    def validate(year, month, day, leap):

        if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 30):
            return False
        year_code = CHINESEYEARCODE[year - 1900]

        if leap:
            if (year_code & 0xf) != month:
                return False
            elif day == 30:
                return (year_code >> 16) == 1
            else:
                return True
        elif day <= 29:
            return True
        else:
            return ((year_code >> (12 - month) + 4) & 1) == 1

    @staticmethod
    def decode(year_code):
        month_days = []
        for i in range(4, 16):
            month_days.insert(0, 30 if (year_code >> i) & 1 else 29)
        if year_code & 0xf:
            month_days.insert((year_code & 0xf), 30 if year_code >> 16 else 29)

        return month_days
