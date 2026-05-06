# Climate Reference Data

Use this file as fallback when the Open-Meteo API is unreachable.
Data is from China Meteorological Administration (CMA) long-term averages
and published building climate zoning references.

## Building Climate Zones (China)

| Zone | Code | Cities | Key Characteristics |
|------|------|--------|---------------------|
| Severe Cold | 1A, 1B, 1C | Harbin, Changchun, Shenyang, Urumqi | HDD18 > 3800; extreme winter |
| Cold | 2A, 2B | Beijing, Tianjin, Xi'an, Jinan, Taiyuan | HDD18 2000-3800; district heating |
| Hot Summer / Cold Winter | 3A, 3B | Shanghai, Nanjing, Wuhan, Hangzhou, Chongqing, Changsha | HDD18 1200-2000; CDD26 300-900; humid year-round |
| Hot Summer / Warm Winter | 4A, 4B | Guangzhou, Shenzhen, Xiamen, Haikou, Nanning | HDD18 < 600; CDD26 1000+; cooling dominant |
| Temperate | 5A, 5B | Kunming, Guiyang, Lijiang | Mild year-round; small seasonal swing |

## Quick Lookup by City

### 华北 / North China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 北京 Beijing | 39.9 | 116.4 | 2B | 12.3 | -3.5 | 26.5 | 56 | 575 | NNW | SSE | 2450 | 250 |
| 天津 Tianjin | 39.1 | 117.2 | 2B | 12.5 | -3.0 | 26.8 | 62 | 545 | NNW | SSE | 2300 | 260 |
| 济南 Jinan | 36.7 | 117.0 | 2B | 14.5 | -0.4 | 27.6 | 58 | 680 | NNE | SSW | 1750 | 380 |
| 太原 Taiyuan | 37.9 | 112.5 | 2A | 10.0 | -5.0 | 23.5 | 58 | 430 | NW | SE | 2850 | 80 |
| 西安 Xi'an | 34.3 | 108.9 | 2B | 13.7 | -0.1 | 26.8 | 69 | 570 | NE | SW | 2050 | 350 |

### 华东 / East China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 上海 Shanghai | 31.2 | 121.5 | 3A | 16.5 | 4.5 | 28.2 | 75 | 1180 | NNW | SSE | 1480 | 420 |
| 南京 Nanjing | 32.1 | 118.8 | 3A | 15.5 | 2.5 | 28.2 | 76 | 1070 | NE | SE | 1780 | 430 |
| 杭州 Hangzhou | 30.3 | 120.2 | 3A | 17.0 | 4.8 | 29.0 | 77 | 1450 | N | SSE | 1540 | 500 |
| 苏州 Suzhou | 31.3 | 120.6 | 3A | 16.3 | 3.8 | 28.3 | 78 | 1100 | NNW | SE | 1600 | 450 |

### 华中 / Central China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 武汉 Wuhan | 30.6 | 114.3 | 3A | 16.6 | 3.8 | 29.0 | 78 | 1270 | NNE | SSE | 1550 | 560 |
| 长沙 Changsha | 28.2 | 113.0 | 3A | 17.2 | 4.9 | 29.0 | 80 | 1450 | NNW | S | 1520 | 570 |
| 郑州 Zhengzhou | 34.7 | 113.7 | 2B | 14.3 | 0.1 | 27.0 | 66 | 630 | NE | S | 2080 | 330 |
| 合肥 Hefei | 31.9 | 117.2 | 3A | 15.8 | 2.5 | 28.0 | 76 | 1000 | NE | SE | 1720 | 410 |

### 华南 / South China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 广州 Guangzhou | 23.1 | 113.3 | 4A | 22.0 | 13.5 | 28.5 | 78 | 1740 | N | SE | 300 | 980 |
| 深圳 Shenzhen | 22.5 | 114.1 | 4A | 22.5 | 14.8 | 28.6 | 78 | 1930 | NE | SE | 250 | 1050 |
| 厦门 Xiamen | 24.5 | 118.1 | 4A | 21.0 | 12.8 | 28.3 | 77 | 1350 | NE | SE | 340 | 720 |
| 海口 Haikou | 20.0 | 110.3 | 4B | 24.2 | 17.5 | 28.6 | 85 | 1650 | NE | SSE | 50 | 1320 |
| 南宁 Nanning | 22.8 | 108.3 | 4A | 21.6 | 12.8 | 28.3 | 79 | 1310 | NE | SE | 320 | 850 |

### 西南 / Southwest China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 成都 Chengdu | 30.6 | 104.0 | 3A | 16.2 | 5.6 | 25.5 | 81 | 920 | NE | NNE | 1520 | 130 |
| 重庆 Chongqing | 29.5 | 106.5 | 3A | 18.3 | 7.8 | 28.5 | 79 | 1130 | N | SE | 1150 | 540 |
| 昆明 Kunming | 25.0 | 102.7 | 5A | 15.5 | 8.5 | 20.0 | 72 | 1030 | SW | SW | 1200 | 0 |
| 贵阳 Guiyang | 26.6 | 106.7 | 5A | 15.3 | 5.0 | 24.0 | 77 | 1170 | NE | S | 1200 | 30 |

### 东北 / Northeast China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 沈阳 Shenyang | 41.8 | 123.4 | 1C | 8.5 | -11.5 | 24.8 | 62 | 720 | N | S | 3700 | 120 |
| 哈尔滨 Harbin | 45.8 | 126.5 | 1A | 4.3 | -18.0 | 23.0 | 65 | 525 | NW | SSE | 5100 | 60 |
| 长春 Changchun | 43.9 | 125.3 | 1C | 5.5 | -15.0 | 23.5 | 62 | 590 | SW | SW | 4450 | 50 |

### 西北 / Northwest China

| City | Lat | Lon | Zone | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Winter Wind | Summer Wind | HDD18 | CDD26 |
|------|-----|-----|------|---------------|-------|-------|---------------|-------------|-------------|-------------|-------|-------|
| 兰州 Lanzhou | 36.1 | 103.8 | 2A | 9.8 | -4.5 | 22.5 | 57 | 330 | NE | SE | 3100 | 40 |
| 乌鲁木齐 Urumqi | 43.8 | 87.6 | 1C | 7.5 | -13.0 | 24.0 | 58 | 280 | S | NW | 4200 | 100 |

### 国际城市 / International

| City | Lat | Lon | Climate (Köppen) | Annual T (°C) | Jan T | Jul T | Annual RH (%) | Precip (mm) | Dominant Wind | Sea Temp (°C) |
|------|-----|-----|-------------------|---------------|-------|-------|---------------|-------------|---------------|----------------|
| 仙本那 Semporna, MY | 4.5 | 118.6 | Af (Tropical Rainforest) | 26.6 | 26.1 | 26.7 | 84 | 2100 | NE(win)/S(sum) | 28–30 |
| 吉隆坡 Kuala Lumpur, MY | 3.1 | 101.7 | Af | 27.0 | 26.5 | 27.5 | 80 | 2500 | NE(win)/SW(sum) | — |
| 曼谷 Bangkok, TH | 13.8 | 100.5 | Aw (Tropical Savanna) | 28.5 | 26.5 | 29.5 | 73 | 1500 | NE(win)/SW(sum) | — |
| 新加坡 Singapore | 1.3 | 103.8 | Af | 27.5 | 26.5 | 28.0 | 83 | 2350 | NE(win)/SW(sum) | 27–30 |
| 马累 Malé, MV | 4.2 | 73.5 | Am (Tropical Monsoon) | 27.8 | 27.0 | 28.3 | 80 | 1900 | NE(win)/SW(sum) | 27–29 |
| 东京 Tokyo, JP | 35.7 | 139.7 | Cfa | 15.6 | 5.2 | 26.4 | 65 | 1530 | NNW(win)/S(sum) | — |
| 迪拜 Dubai, AE | 25.3 | 55.3 | BWh (Hot Desert) | 27.0 | 19.0 | 35.0 | 60 | 95 | NW | 22–33 |
| 悉尼 Sydney, AU | -33.9 | 151.2 | Cfa | 18.0 | 22.5 | 12.5 | 62 | 1215 | — | 18–23 |

## Usage When API Fails

1. Look up the project city in the table above
2. If found: use the row data directly; cite as "基于中国气象局多年平均数据（1991-2020）" or equivalent
3. If not found: use the closest city with similar latitude and climate zone; clearly note "气候数据基于[参考城市]多年平均值推断，建议人工核实"
4. For the wind rose: if the wind directions are listed above, generate a simple SVG wind rose from the given directions; if not, describe the wind pattern in text only

## Climate Zone Design Strategy Summary

| Zone | Key Challenge | Primary Passive Strategy | Orientation |
|------|--------------|-------------------------|-------------|
| Severe Cold (1) | Extreme winter, deep frost | Super-insulation + compact form + passive solar | S ± 15° |
| Cold (2) | Cold winter, hot summer | High thermal mass + solar gain + night vent | S ± 10° |
| Hot Summer / Cold Winter (3) | Humidity + heating + cooling | Cross-vent + solar shading + medium insulation | S ± 10°; avoid W |
| Hot Summer / Warm Winter (4) | Cooling dominant, typhoon | Max cross-vent + deep shading + lightweight envelope | S ± 5°; capture SE breeze |
| Temperate (5) | Mild, thin air at altitude | Passive solar + natural ventilation | S ± 15° |
