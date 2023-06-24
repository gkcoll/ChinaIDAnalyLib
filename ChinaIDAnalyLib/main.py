'''
@Time    :   2023/03/12 20:17:53
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   The core module of the project. Provided functions of *Random ID Generating*,
             *Computing Verification Code*, *Analysing ID Number*
             (Included basic informations querying and check legitimacy).
'''



try:
    from .data import getFull, data
    from .lunar import ZhDate, GanZhi
except:
    from data import getFull
    from lunar import ZhDate, GanZhi
from random import choice, randint
import time
from datetime import date, datetime


STR_CONST = {"male": "男", "female": "女"}
WEIGHTS = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
MOD_VERIFICATION_DICT = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
ZODIACS = [{'en': 'rat', 'zh': '鼠'}, {'en': 'ox', 'zh': '牛'}, {'en': 'tiger', 'zh': '虎'}, {'en': 'rabbit/hare', 'zh': '兔'}, {'en': 'dragon', 'zh': '龙'}, {'en': 'snake', 'zh': '蛇'},
           {'en': 'horse', 'zh': '马'}, {'en': 'sheep/goat', 'zh': '羊'}, {'en': 'monkey', 'zh': '猴'}, {'en': 'rooster', 'zh': '鸡'}, {'en': 'dog', 'zh': '狗'}, {'en': 'pig', 'zh': '猪'}]
SIGNS = [{'en': 'Aries', 'zh': '白羊座', 'd': 20}, {'en': 'Taurus', 'zh': '金牛座', 'd': 19}, {'en': 'Gemini', 'zh': '双子座', 'd': 21}, {'en': 'Cancer', 'zh': '巨蟹座', 'd': 20}, {'en': 'Leo', 'zh': '狮子座', 'd': 21}, {'en': 'Virgo', 'zh': '处女座', 'd': 22}, {
    'en': 'Libra', 'zh': '天秤座', 'd': 23}, {'en': 'Scorpio', 'zh': '天蝎座', 'd': 23}, {'en': 'Sagittarius', 'zh': '射手座', 'd': 23}, {'en': 'Capricorn', 'zh': '摩羯座', 'd': 24}, {'en': 'Aquarius', 'zh': '水瓶座', 'd': 23}, {'en': 'Pisces', 'zh': '双鱼座', 'd': 22}]


def verify(id17: str) -> int:
    '''Compute the last digit, the verfication code.'''
    weighted_sum = sum(int(id17[i]) * WEIGHTS[i] for i in range(17))
    mod = weighted_sum % 11
    return MOD_VERIFICATION_DICT[mod]


def id_gen(count: int = 1) -> list:
    result = []
    while len(result) < count:
        loc = choice(list(data.keys()))
        stamp = time.localtime(randint(0, int(time.time())))
        date = time.strftime('%Y%m%d', stamp)
        ordinal = str(randint(1, 99)).zfill(2)
        gender = str(randint(0, 9))
        id17 = loc + date + ordinal + gender
        v_code = str(verify(id17)) if verify(id17) != 10 else "X"
        ID = id17 + v_code
        if ID not in result:
            result.append(ID)
    return result


class IDError(Exception):
    def __init__(self, value: str=None, reason: str=None):
        self.value = value
        self.reason = reason

    def __str__(self):
        return f"You enterd a invalid and illegal ID: {str(self.value)}\nReason: {self.reason}"


class CNID:
    """China Mainland Resident ID card number class."""

    def __init__(self, ID):
        self.id = str(ID)
        # Check legality of id(according to GB 11643-1999).
        if len(self.id) == 18:
            try:
                d = self.birthdate()['num']
                date(d[0], d[1], d[2])
            except:
                raise IDError(self.id, "Illegal birthdate.")
            else:
                ck = self.id[-1]
                ckn = 10 if ck == 'X' else int(ck)
                ckv = verify(self.id[0:17])

                if ckn != ckv:
                    raise IDError(self.id, "Verification error. Check the last digit, the verification code.")
        else:
            raise IDError(self.id, "ID less than 18 digits.")

    def loc(self) -> str:
        code = self.id[0:6]
        return getFull(code)

    def birthdate(self) -> dict:
        y = int(self.id[6:10])
        m = int(self.id[10:12])
        d = int(self.id[12:14])
        return {'num': (y, m, d),
                'gregorian': (str(y), str(m), str(d)),
                'lunar': ZhDate.from_datetime(datetime(y, m, d)).chinese(),
                'ganzhi': GanZhi(datetime(y, m, d)).tpl()}

    def age(self) -> int:
        # Birthdate tuple.
        bdt = self.birthdate().get('num')
        bddt = datetime(bdt[0], bdt[1], bdt[2])
        today = datetime.now()
        d_value = today - bddt
        return int(d_value.days // 365.25)

    def is_adult(self) -> bool:
        return self.age() >= 18

    def zodiac(self) -> str:
        '''Get the zodiac of the id owner.'''
        dt = self.birthdate().get('num')
        # Judge if date after the LiChun solar term of the year.
        birthdate = datetime(dt[0], dt[1], dt[2])
        lichun_date = datetime(dt[0], 2, GanZhi(
            datetime(dt[0], 1, 1)).lichun())
        if birthdate >= lichun_date:
            return ZODIACS[(dt[0] % 12 + 8) % 12]['zh']
        else:
            return ZODIACS[((dt[0] - 1) % 12 + 8) % 12]['zh']

    def star_sign(self) -> str:
        '''A method to get star sign.'''
        dt = self.birthdate().get('num')
        index = dt[1] - 3
        if dt[2] < SIGNS[index-1]['d']:
            return SIGNS[index-1]['zh']
        else:
            return SIGNS[index]['zh']

    def gender(self) -> str:
        '''A method to judge gender.'''
        key_num = int(self.id[-2])
        gndr_judge = key_num % 2
        if gndr_judge == 1:
            return STR_CONST["male"]
        if gndr_judge == 0:
            return STR_CONST["female"]

    def order(self) -> str:
        return self.id[-4:-1]

    def info(self) -> dict:
        return {'birthplace': self.loc(),
                'birthdate': self.birthdate(),
                'age': self.age(),
                'adult': self.is_adult(),
                'zodiac': self.zodiac(),
                'star_sign': self.star_sign(),
                'gender': self.gender(),
                'order': self.order()
                }

    def msg(self):
        info = self.info()
        msg = ''
        msg += '这位' + ('美女' if info['gender'] == '女' else '帅哥')
        msg += '是 ' + info['birthplace'] + ' 人，'
        msg += '出生日期 ' + '-'.join(info['birthdate']['gregorian'])
        msg += ' (农历 ' + ''.join(info['birthdate']['lunar']) + ')，'
        msg += '年龄 ' + str(info['age']) + ' 岁，'
        msg += '未成年'[info['adult']:] + '，'
        msg += '属' + info['zodiac'] + '，' + info['star_sign'] + '。'
        return msg

    def __str__(self) -> str:
        return 'CNID(\'' + str(self.id) + '\')'

    def __repr__(self) -> str:
        return self.__str__()


def _isCN(ch):
    """Judge if the incomed character is a Chinese character or not."""
    return '\u4e00' <= ch <= '\u9fff'


def _len(string):
    """Special length counting function. A CJK Character will regard as 2 times than a English letter."""
    return sum([2 if _isCN(i) else 1 for i in string])


def load(ID: CNID) -> dict:
    return ID.info()


def report(ID: CNID) -> str:
    print(ID.msg())


def table(ID: CNID) -> str:
    info = load(ID)
    keys = ['出生地', '出生日期(公历)', '出生日期(农历)', '出生日期(天干地支)',
            '年龄', '性别', '成年', '生肖', '星座', '顺序码']
    try:
        values = [info['birthplace'], '-'.join(info['birthdate']['gregorian']), ''.join(info['birthdate']['lunar']), ''.join(
                  info['birthdate']['ganzhi']), info['age'], info['gender'], '是' if info['adult'] else '否', info['zodiac'], info['star_sign'], info['order']]
    except:
        values = [info['birthplace'], '-'.join(info['birthdate']['gregorian']), ''.join(info['birthdate']['lunar']), '计算失败', info['age'], info['gender'], '是' if info['adult'] else '否', info['zodiac'], info['star_sign'], info['order']]
    
    values = [' ' + str(v) for v in values]
    keys = [k + ' ' * (max([_len(k) for k in keys]) -
                       _len(k) + 1) + '|' for k in keys]
    d = dict(zip(keys, values))
    header = '参数' + ' ' * (max([_len(k) for k in keys]) - 5) + \
        '| ' + '内容' + ' ' * (max([_len(v) for v in values]) - 4)
    split = '-' * (max([_len(k) for k in keys]) - 1) + \
        '+' + '-' * (max([_len(v) for v in values]) + 1)
    print(header)
    print(split.replace('-', '='))
    for k in keys:
        print(k + d[k])
        print(split)
