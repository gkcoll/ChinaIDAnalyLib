# ChinaIDAnalyLib

## Introduction

China Mainland (the Peoples Republic of China) resident identity card number analysis lib.

## Usage

Out-of-the-box, you can run `GUI.exe` directly. If you want to use it in your own project, please see details in `demo.py`.


## Functions

Query: BirthPlace/BirthDate/Gender

Calculate: Verification Code (The last digit, for check legality)

Generate: Randomly generate a specified number of legal ID number numbers according to the composition rule (not guaranteed to be valid)

## Features

1. The program returned included three types of birthdate, (for Chinese, ) you don't need to ask your mom: *When I born?*

   It supply: Gregorian + (Chinese) Lunar/ 8-Char(八字, also 天干地支), type is `set`.

2. The program also supply the information of Chinese Zodiac Sign (生肖) and Star Sign. It designed for help you to know yourself (your basic information).

## NOTE

* The lib can only precess China mainland resident identity card number(18 digits).
* Area code date are from China MCA.
* The lib have not ability to query real name or other sensitive information. If you have require, please ask for police.

### Insufficience

Now, ID of too old men entered will cause a IDError. In the GUI program, it told us "Illegal birthdate.", but here's nothing wrong about the date. In fact, it caused by the insufficience of calculation section of 天干地支(TianGanDiZhi). But my abilities are limited, so the trouble leaves here and waiting for someone niubility to repair it.

## FAQ

> ***Why I can't query out the birthplace of the ID?***
>
> That because some of *regionalism code* **have changed** or the original issuing place **has been merged** and the code **has been revoked**. You can search it on Internet.
>
> Recommendation: [行政区划代码_中华人民共和国民政部](https://www.mca.gov.cn/article/sj/xzqh/1980/)。
>
> ***Is it safe?***
>
> Sure! This project can only query out information like birthplace/birthdate/gender/legality. All of these are can be read from the ID number and the lib needn't connect to net. So you needn't worried about it will disclose your name and privacy information.


## License

> ### ChinaIDAnalyLib
>
> #### A Python lib for analyses China mainland resident identity card numbers
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

