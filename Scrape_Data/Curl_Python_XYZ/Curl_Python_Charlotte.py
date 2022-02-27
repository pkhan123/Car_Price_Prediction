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
        'tracestate': '1190893@nr=0-1-1543670-910326579-de18df014b4413c8----1644071714743',
        'traceparent': '00-e52ac20a181b1676be2e3964779afb70-de18df014b4413c8-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMyNjU3OSIsImlkIjoiZGUxOGRmMDE0YjQ0MTNjOCIsInRyIjoiZTUyYWMyMGExODFiMTY3NmJlMmUzOTY0Nzc5YWZiNzAiLCJ0aSI6MTY0NDA3MTcxNDc0MywidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/charlotte-nc-28201?dma=&searchRadius=50&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=25',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=38695c89-5d6a-4725-97de-9228bc997a23; pxa_id=7t581PLAbpLaknSIgjE0VqFX; _gcl_au=1.1.1264858426.1644034067; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C35082967246199125900669614635959067013; _scid=23f19ee6-af4c-47ec-8878-e7dcc34f80ef; _gid=GA1.2.1487812677.1644034069; _fbp=fb.1.1644034068989.861423825; abc=7t581PLAbpLaknSIgjE0VqFX; pxa_at=true; _cs_c=1; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=35248076571290034830652927790183386576; _lr_geo_location=IN; _sctr=1|1643999400000; _clck=1qacwtq|1|eyq|0; __gads=ID=06f4fd1e98b26b76:T=1644034067:S=ALNI_Mb6QVVsdKMVHlKygEZUN4lZ3BGjfA; _4c_mc_=6a6b4313-eb24-4ed5-974d-1246fb786820; _aeaid=61ea0516-79a3-4ed3-aaaa-a5f29eaae3d6; aeatstartmessage=true; pixall_abc=7t581PLAbpLaknSIgjE0VqFX; _pbjs_userid_consent_data=3524755945110770; abc_3rd_party=7t581PLAbpLaknSIgjE0VqFX; _lr_env_src_ats=false; _pin_unauth=dWlkPU16QTNNV1ExTm1NdE0yTXpNeTAwWVdRM0xXSTJZakF0TnpGbE0ySmtaVFV5WmpFMA; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; pbjs-unifiedid=%7B%22TDID%22%3A%22d63f2eab-18bc-454f-b132-8fdab5236abc%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-05T04%3A09%3A46%22%7D; DCNAME=www-aws.autotrader.com; SSM_GFU=eyJ2ZXJzaW9uIjoyLCJndWlkIjoiNjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwIiwic2lkIjoiUzIwMjIwMjA1MDUxODAxMElzS3R0SXBxQ3B3RyIsImxhc3Rfc2VlbiI6MTY0NDAzODMzMn0=; SSM_UTC=Z3VpZDo6NjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwfHx8c291cmNlOjpnZnU=; SSM_UTC_LS=Z3VpZDo6NjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwfHx8c291cmNlOjpnZnU=; bm_sz=9DA27C8A4F9049CAB27CD43FB9EC7DA4~YAAQRUo5F65Qc4F+AQAAM63DyQ5p3/4Ms6Iu7ioHictNN5z46y0P0VphAojB1GdI20rzFQcdEdORHDC4bd+qCn8ZGNrejoPQjJwZ+d2yejsYjr7pl8jPSyaCDpBwfy2bpe7bOYrGmx9m9Lstdi7I/cgTIFqPEcKiRIvbmUJGhVoUV6zEgPz8W8DPc6NdovG+7+ayR3MIBkFayNi5bZ043MJTWgV6FARbx7mVygjI/3dDmwSMWSxZ5UH2GkQHHCfIPLJEirWEc8UX2hkCUGIduU8of+NMvTZ51qwrh35x7r1vX3NwMzHI~3162693~4470341; AWSELB=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90F2253C6BE3D923146E37BE76D25B6FB8549D736AE6046FECBF85DD2416AA6A66A29F91541FFD852096A98BD6F1C1DCC4; AWSELBCORS=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90F2253C6BE3D923146E37BE76D25B6FB8549D736AE6046FECBF85DD2416AA6A66A29F91541FFD852096A98BD6F1C1DCC4; _dpm_ses.070d=*; pxa_ipv4=157.40.241.53; pixall_cookie_sync=true; bm_mi=A98E643E968FD56A4C113A0FF8928F30~E9fypX4PQTBaf2a0YRWujr/lhIAvdKWU3KQIAgzN/oOXfJRpju/NgaQiOeSnIVuBmxZUZr58AL+y6Ydu2KYhZaslQw/DsB92urPFKuJEw97ohI6aP4vsX2EuRaTLcqrho382hpZcGTscEAcNRpAY2WNxSULNxSyf46suqtfIN22rPrbY6muf9jQG2kImefPSYUY9UJU11SIaxavD/XFPrDpu+AMJ3HRGbX4q/incyl+m59OEYxjW9payxPa4qaafYNP3/D7n5f4mLYP2ivUyrpIxX2ul4ZcYrvZQGXFbCZg=; ak_bmsc=71DBA696111A9669B6EBBC9B0C0A4E35~000000000000000000000000000000~YAAQ3nMsMadL67h+AQAAgB4yyg65cVq+H4MN6iGnh0H8vmUmN1SsgeRk3Y3V92MSW0tRC8pShvCcrd+KnYHW/lMUiJk22W7JvigM/6eoTcVZHGDyjtdfINU7CHxByDpfddoLGRnPTge6Mv3BCsDL7pnwzBo8+SRMkmGpSplJ04Z3sehrm+F2GqWwCSaGe6/F3kg26Z8CVXAVN+55yTof6o5ag8X5U52rPKYhpjQOLYXxjBwSux2ZmxSnm5vb9ZJfRkrd8+1nD7EorE01g0V/1bea6pBjT2NtrKh0p0gWsiCjU26sIaH7ric7xBgT8ZZ9pBCWudN6NajNrX73jdaYj69pEQcT5FkVpA0LuqVNDWtTKd/zVyzzwfTS3CvWvo4RPr1RHO90YK8NaxxldG9vKkMTc4/D0Gldt3zOB0w/6+iJg0C2giqpJtFCRZVx9GCKKSU4xHpUSQNWEkYFJrO8Ch1zBKVRJrm1LCSSsHDMtox2L64YGMx2GZZkDGw3SnUiGFodDN5JBTzRM4XIE4rheu5ZeogZC9BvgUX9U4iOiaNR4YmvrtcJBAxsUd1CgMpGo72cJw==; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19029%7CMCMID%7C35082967246199125900669614635959067013%7CMCAAMLH-1644674592%7C12%7CMCAAMB-1644674592%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-145948657%7CMCOPTOUT-1644076993s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19036%7CvVersion%7C4.4.1; akaalb_at_alb=1644071967~op=AT_col_lb:AT_col_use1|~rv=38~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=d1becf02c63d4d6f5aa3f3df5e0953a8; _lr_retry_request=true; ATC_USER_RADIUS=50; JSESSIONID=97F4EB5592E3285B957727F29042530A; ATC_USER_ZIP=28201; akaalb_pixall_prod=1644073463~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=77~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=2a33472c578cbc2eb21c805c520bbf73; _ga=GA1.2.66353926.1644034067; s_pers=%20s_tbm23.6%3Dtrue%7C1646074907691%3B%20s_tbm23.5%3Dtrue%7C1646074774547%3B%20s_tbm23.27%3Dtrue%7C1646074897005%3B%20s_tbm23.22%3Dtrue%7C1646074581282%3B%20ev96gapv%3DUnknown%7C1646072999183%3B%20ev97gapv%3Dundefined%7C1644073465194%3B%20ev98gapv%3Dundefined%7C1646072999217%3B%20s_tbm%3Dtrue%7C1644073465228%3B%20ev95gapv%3D%7C1644073465234%3B; _uetsid=2e57d6b0863911ec82739f39dc6f3a18; _uetvid=2e58a4d0863911ec92df8b463a0acd32; _dpm_id.070d=56c884d4-358d-42d0-8035-0b7cfc1dcb58.1644034071.5.1644071668.1644062583.f6bac8b4-e066-41e1-9ab1-718964622ddc; _cs_id=d9f78b36-206e-a340-9c8a-ea5c6606d26d.1644034070.6.1644071668.1644066438.1.1678198070475; _cs_s=30.0.0.1644073468935; _td=e471282e-7c6d-4d3b-94a7-3b1744b8cf0e; _clsk=h8q9ro|1644071682395|43|0|www.clarity.ms/eus-d/collect; _gat_UA-182514997-17=1; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1644066563.4.1.1644071714.4; bm_sv=852F80CDDEACB43C58244B78D0B345F4~UMDL2SfqX9w2/t1joemoVFOfVwHpdJ+L5nYTDGJnCRe1OD1sqk/6QZLEQ0AjZ5x19Fi/OAFFJc1hRZBjPWloTa6yS1VUiamEl80K4jvbmEJMhafk+v0tRUn+Ipio0Wbh1Of5eF2iIEH1AtykBpBt4b0ZdHzvPrVvcKJNKSykhTI=; _abck=B48CA273DDEAFF3AFCCEDFFAA4F3E1FE~0~YAAQ3nMsMR7N67h+AQAATn9PygeQmHFU38/zqG1p2NQ7rd7HzWqeMMmDMU2NCSR8cwzpzwE+tolQ7tYdMyf39W99LwPixufY1xoLzWYfYnZqlTQOmbf0BBA3P0AOnJXk0ydoWK/pYHwi/sadY5IovusIUTJ7aWN/FVQpvUpzeVZhKWC1Sj+kWHaC4ZGHtX0wq5aWfyajNIJ9DOSh+lgk/lMnugwlx0P8Vr+LBm6fu1MGkr1XJzz6ZxTAvEKbf9nau3ixM1YIRjyhloI9CtGrkFi1v33Yor6KnRNyS/mexHd95SKCbiOeVu4FzZG5ZGfVnyhgaJtjLcLf2wb4WS33hzEi81TWcDAVDyWHmhM6FHiNxPc9ZD7OCUlJCe3ZSibQ/qxgDB2PpBbjkDNECEx9t5UgYCn5VH+plA==~-1~-1~-1',
    }

    params = (
        ('allListingType', 'all-cars'),
        ('city', 'Charlotte'),
        ('state', 'NC'),
        ('zip', '28201'),
        ('location', '[object Object]'),
        ('searchRadius', '50'),
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