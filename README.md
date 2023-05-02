# CAnalyLib

## Introduction

中国大陆居民身份证号分析库。

China Mainland (the Peoples Republic of China) resident identity card number analysis lib.

## Usage

开箱即用，具体请详情 `demo.py`。

Out-of-the-box, see details in `demo.py`.


## Functions

查询：出生地/生日/性别

Query: BirthPlace/BirthDate/Gender

计算：校验码（末位验证码，依此判断身份证号码合法性）

Calculate: Verification Code (The last digit, for check legality)

生成：依据组成规律随机生成指定数量的合法身份证号（不保证有效）

Generate: Randomly generate a specified number of legal ID number numbers according to the composition rule (not guaranteed to be valid)

## Features

1. 三种生日格式一起给，再也无须问 *When I born*！

   The program returnd included three types of birthdate, (for Chinese, ) you don't need to ask your mom: *When I born?*

   提供的格式：公历 + 农历 + 八字（天干地支），类型为 `set`。

   It supply: Gregorian + (Chinese) Lunar/ 8Char(TianGanDiZhi), type is `set`.

2. 生肖星座也跟上，让你更全面了解你自己（的基本信息）。

   The program also supply the information of Chinese Zodiac Sign (ShengXiao) and Star Sign. It designed for help you to know yourself (your basic information).

## NOTE

* 本库只能处理中国大陆的居民身份证号码（18位）。
* The lib can only precess China mainland resident identity card number(18 digits).
* 地区编码数据来自民政部。
* Area code date are from China MCA.
* 本分析库不具备任何查询姓名等敏感信息的能力，如有相关需求请找警察蜀黍。
* The lib have not ability to query real name or other sensitive information. If you have require, please ask for police.

## FAQ

> *我要查的身份证查不到出生地怎么办？*
>
> *Why I can't query out the birthplace of the ID?*
>
> 这是因为有些原有的身份证号码所在地的行政区划代码有过变化或者原先的发证地已撤并并且行政区代码已撤销，可以上网查。
>
> That because some of *regionalism code* **have changed** or the original issuing place **has been merged** and the code **has been revoked**. You can search it on Internet.
>
> Recommandation: [行政区划代码_中华人民共和国民政部](https://www.mca.gov.cn/article/sj/xzqh/1980/)。

> *这个项目安全吗？*
>
> *Is it safe?*
>
> 绝对安全，因为通过身份证号只能查到以下信息：出生地、生日、性别、身份有效性。这些信息都是可以从身份证号直接识别出来的，并且无需联网，**无需**担心姓名等隐私泄露。
>
> Sure! This project can only query out information like birthplace/birthdate/gender/legality. All of these are can be read from the ID number and the lib needn't connect to net. So you needn't worried about it will disclose your name and privicy information.


## Licence

> ### ChinaIDAnalyLib
>
> #### A Python lib to annlyse China mainland resident identity card numbers
>
> Copyright (C) 2023 Albert Lin
>
> This program is free software: you can redistribute it and/or modify it under the terms of the QUICKOR OPEN WORKS LICENSE as published by the author Albert Lin.
>
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the QUICKOR OPEN WORKS LICENSE for more details.
>
> You should have received a copy of the QUICKOR OPEN WORKS LICENSE along with this program. If not, see
>
> <center>&lt;https://lab.gkcoll.xyz/license&gt;<center>

