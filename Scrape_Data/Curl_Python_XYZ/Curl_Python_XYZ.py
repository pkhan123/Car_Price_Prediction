from turtle import st
import requests

# Sometime headers and params changes
# if get error on response.json() please check that
# also replace ('firstRecord', '50') by ('firstRecord', str(firstRecord))

def Curl_Python(page_to_scroll = 1):
    firstRecord = 25 * page_to_scroll - 25



    headers = {
        'authority': 'www.autotrader.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'tracestate': '1190893@nr=0-1-1543670-910396692-0a9cf29844e0a19e----1643999324749',
        'traceparent': '00-6138bb9cb435641e6a0c9b53ec45dd40-0a9cf29844e0a19e-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDM5NjY5MiIsImlkIjoiMGE5Y2YyOTg0NGUwYTE5ZSIsInRyIjoiNjEzOGJiOWNiNDM1NjQxZTZhMGM5YjUzZWM0NWRkNDAiLCJ0aSI6MTY0Mzk5OTMyNDc0OSwidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/new-york-ny-10001?dma=&searchRadius=25&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=25',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=8524b16a-8436-4743-bd04-b1b024907d22; akaalb_at_alb=1644001074~op=AT_col_lb:AT_col_use1|~rv=10~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=85d4ecae4c22bbc1dbc6297b70c27b63; bm_sz=2140940D473EC52122F5C54CEA7F1F39~YAAQ3nMsMcfv4rh+AQAAEiT+xQ4drjlVipltnnrci0Etayo39bhwiw1STlhGFaWEPLsFYBk6lG8TvPgtRf2a6MW7GebOdwGoiXLcbEuFM6XsSlXvFIbwkLXPUNmhAvD0Xw3m+dJ40nn5vu4iqFSV6MFWspMYtgvzcflCXoALQeSdyx7/NAvzL1crRw8yrOFyvCrh9BQ7xr8i47B0ljWEdmjbVUdh5KpVbDDL39ZtQL5HsYUqpX/r6Fef45TUfRU5iwtS/Kgj1PFT0fXjKzKUmYckAnZi3DR2ZT5bRxpKMO1DDlZgboGU~4469314~3683141; ak_bmsc=BDABABE821AA177100393202D617711A~000000000000000000000000000000~YAAQ3nMsMczv4rh+AQAA/Sr+xQ4gKqTQdohnqtFiVimnDeCeCIsChQx+bkYpaJSk0JlV9soJXeGivq8AF/Jkkn6+PEk4fr1KpHvdrdFu6+YElUCdlYXDCHfEuKWoeIftu9O5JORRbeT0tHvT8BJYZc1SeyjTjpwtsyIR1WIjgyUAj66WK6cb4BG6vDV7JXJZl7KuPA+YXZhXLI1ur6tW0+cjep8EZ+wyxdAo2xo9B5xS4KoQyc8VEBN6lta9TYMV23nrNMzEIEjqccB212XjDD4DGSH46GixnqIfEHdm0wTEQlV/GjjrOgr1A0rQVtMWm3r99fwIJLcrOcPbIkwhgCRa6qG8TJ+wiAf9HQpvw6++wJWcVx4ezv6g4yTIKYHxy5v0Otax65gM2hsBZ0xjB/mx00sWKhK4MkoFinUHZiYmxeJ6H2W0JFxyKmvXeyqAJ916ftmChYNR7CZfncW2KdPcVp/oDFM4LDCFL79YUYgGPRwA9U13itVeU6SVFDWG; pxa_id=hhty1kBnm6KpAlcqcoDcdBkh; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; _gcl_au=1.1.1303058908.1643999278; s_ecid=MCMID%7C68926264149984461474286271448453121778; abc=hhty1kBnm6KpAlcqcoDcdBkh; pxa_ipv4=157.40.253.204; pixall_cookie_sync=true; pxa_at=true; _gid=GA1.2.1381135223.1643999280; _gat_UA-182514997-17=1; _scid=c36a6ffd-70e3-499b-9fd7-cf6add755bd4; _cs_c=1; _dpm_ses.070d=*; _fbp=fb.1.1643999282112.1226092207; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=69093306555216885984269057884891916967; _lr_geo_location=IN; _sctr=1|1643913000000; _4c_mc_=e1ff129c-eb1a-462d-a7c1-470d4ecc5f5c; _aeaid=bea4261c-c3bb-49be-bb6a-8e71b0c8bce1; ATC_USER_ZIP=10001; _clck=1vm4wpb|1|eyp|0; aeatstartmessage=true; ATC_USER_RADIUS=25; pixall_abc=hhty1kBnm6KpAlcqcoDcdBkh; _pbjs_userid_consent_data=3524755945110770; akaalb_pixall_prod=1644001091~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=75~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=a62ba985eae11b32aebc98f941a20bc7; abc_3rd_party=hhty1kBnm6KpAlcqcoDcdBkh; _uetsid=2ea14b8085e811ec9a8157edc59707fa; _uetvid=2ea2a06085e811ecb9806b95d43492d7; s_pers=%20s_tbm24%3Dtrue%7C1646074678123%3B%20ev95gapv%3DTyped%252FBookmarked%7C1644001092318%3B%20ev97gapv%3Dundefined%7C1644001092337%3B%20ev98gapv%3Dundefined%7C1646072999351%3B%20s_tbm%3Dtrue%7C1644001092365%3B%20ev96gapv%3D%7C1646072999377%3B; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19028%7CMCMID%7C68926264149984461474286271448453121778%7CMCAAMLH-1644604092%7C12%7CMCAAMB-1644604092%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-331640267%7CMCOPTOUT-1644006492s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19035%7CvVersion%7C4.4.1; _ga=GA1.2.899105102.1643999278; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; _lr_retry_request=true; _lr_env_src_ats=false; _pin_unauth=dWlkPVptUmlNbUU0TURRdE5XRmhNeTAwT1dVNExUZ3lZVEl0WWpaaE1qUTRaalE0T0RVeg; pbjs-unifiedid=%7B%22TDID%22%3A%221f819765-c0b2-4e98-8ef1-75458cc8c3f7%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-04T18%3A28%3A13%22%7D; __gads=ID=1cae8014815cbef3:T=1643999278:S=ALNI_MbCNmc3yhLuLpGEwwiT9IzFsWCuPA; _dpm_id.070d=469dc1cb-1692-402c-8bc3-19c03ac0859f.1643999282.1.1643999295.1643999282.32505e5a-c6f0-4818-a300-9c7e81479099; _cs_id=e325bef6-206e-a174-9152-a3b151069e8c.1643999281.1.1643999295.1643999281.1.1678163281302; _cs_s=2.0.0.1644001095200; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; _td=31e9c819-9cd6-4fdc-a721-d04fbb7d4982; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1643999278.1.1.1643999324.14; bm_sv=0054A7BCB87149D54FF8720F5D980C5D~UMDL2SfqX9w2/t1joemoVCqFF1OgNNLOfwEXugg/4JEBDk9nKTX4LlOf4ixHfOOYyZjx3DCo5sPmhB0WkY1v373NK3ueJUfyELm7Ik64APpXn7lj8VTPYUgUOe96/74vLgi+5f81DWcgSutFbI656GacJtvLvmTboSF0QIUF0tM=; _abck=0ADBA09D93F30B6E7A7F025AA79A089E~0~YAAQ3nMsMXXw4rh+AQAA1un+xQd+3PjuRSm2DT0S4vFnrl2hGHJj8V54BbR5U1SZwZd3cIhxlE5ak0xxIMJbAEMy9xqMc7x2FrikAIEXnmGhPAo1WdKVxgS5ki+pUvo3WDXA/2B+BUiEbYcWfwe9vJbgr6cf+PELEG51x44Qu69ohY/y5ZlIqbfDkAMGrXDqhjnBCSlKgJ+HMowf1UzP4Sw4boaOCu9SjJNvkuVKj5AOIIcjLlt5zv32cro5i+S7EMq9UJPz8cVulifYTiKIR1DiC+6LkzbsO3e0KDzKZjq/eUyvGkbmFyHKrOzAdtLfwFGYL29HznAJyEIlr521iv13EGUF76KOavCE1n/GiargeCkw2L0YbUajGOp24M6xrPimWsa1nuXu9/jiAbUt7oTbsSXfDgSuSA==~-1~-1~-1; _clsk=4iy2v1|1643999324662|3|0|f.clarity.ms/collect',
    }

    params = (
        ('allListingType', 'all-cars'),
        ('city', 'New York'),
        ('state', 'NY'),
        ('zip', '10001'),
        ('location', '[object Object]'),
        ('searchRadius', '25'),
        ('isNewSearch', 'false'),
        ('marketExtension', 'include'),
        ('showAccelerateBanner', 'false'),
        ('sortBy', 'relevance'),
        ('numRecords', '25'),
        ('firstRecord', str(firstRecord)),
        ('dma', '[object Object]'),
        ('channel', 'ATC'),
        ('relevanceConfig', 'relevance-v2'),
        ('searchByDma', 'false'),
    )

    response = requests.get('https://www.autotrader.com/rest/searchresults/base', headers=headers, params=params)
    return response