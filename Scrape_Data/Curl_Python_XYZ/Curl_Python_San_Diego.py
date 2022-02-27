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
        'tracestate': '1190893@nr=0-1-1543670-910308770-026194398bbcfe64----1644067712982',
        'traceparent': '00-78b53ec33d2b28ece2b182717d421560-026194398bbcfe64-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMwODc3MCIsImlkIjoiMDI2MTk0Mzk4YmJjZmU2NCIsInRyIjoiNzhiNTNlYzMzZDJiMjhlY2UyYjE4MjcxN2Q0MjE1NjAiLCJ0aSI6MTY0NDA2NzcxMjk4MiwidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/san-diego-ca-92101?dma=&searchRadius=50&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=25',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=38695c89-5d6a-4725-97de-9228bc997a23; pxa_id=7t581PLAbpLaknSIgjE0VqFX; _gcl_au=1.1.1264858426.1644034067; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C35082967246199125900669614635959067013; _scid=23f19ee6-af4c-47ec-8878-e7dcc34f80ef; _gid=GA1.2.1487812677.1644034069; _fbp=fb.1.1644034068989.861423825; abc=7t581PLAbpLaknSIgjE0VqFX; pixall_cookie_sync=true; pxa_at=true; _cs_c=1; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=35248076571290034830652927790183386576; _lr_geo_location=IN; _sctr=1|1643999400000; _clck=1qacwtq|1|eyq|0; __gads=ID=06f4fd1e98b26b76:T=1644034067:S=ALNI_Mb6QVVsdKMVHlKygEZUN4lZ3BGjfA; _4c_mc_=6a6b4313-eb24-4ed5-974d-1246fb786820; _aeaid=61ea0516-79a3-4ed3-aaaa-a5f29eaae3d6; aeatstartmessage=true; pixall_abc=7t581PLAbpLaknSIgjE0VqFX; _pbjs_userid_consent_data=3524755945110770; abc_3rd_party=7t581PLAbpLaknSIgjE0VqFX; _lr_env_src_ats=false; _pin_unauth=dWlkPU16QTNNV1ExTm1NdE0yTXpNeTAwWVdRM0xXSTJZakF0TnpGbE0ySmtaVFV5WmpFMA; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; pbjs-unifiedid=%7B%22TDID%22%3A%22d63f2eab-18bc-454f-b132-8fdab5236abc%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-05T04%3A09%3A46%22%7D; DCNAME=www-aws.autotrader.com; SSM_GFU=eyJ2ZXJzaW9uIjoyLCJndWlkIjoiNjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwIiwic2lkIjoiUzIwMjIwMjA1MDUxODAxMElzS3R0SXBxQ3B3RyIsImxhc3Rfc2VlbiI6MTY0NDAzODMzMn0=; SSM_UTC=Z3VpZDo6NjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwfHx8c291cmNlOjpnZnU=; SSM_UTC_LS=Z3VpZDo6NjFmZTA4YmMyMTRhYjE3ZmJlMDAwMTgwfHx8c291cmNlOjpnZnU=; bm_sz=9DA27C8A4F9049CAB27CD43FB9EC7DA4~YAAQRUo5F65Qc4F+AQAAM63DyQ5p3/4Ms6Iu7ioHictNN5z46y0P0VphAojB1GdI20rzFQcdEdORHDC4bd+qCn8ZGNrejoPQjJwZ+d2yejsYjr7pl8jPSyaCDpBwfy2bpe7bOYrGmx9m9Lstdi7I/cgTIFqPEcKiRIvbmUJGhVoUV6zEgPz8W8DPc6NdovG+7+ayR3MIBkFayNi5bZ043MJTWgV6FARbx7mVygjI/3dDmwSMWSxZ5UH2GkQHHCfIPLJEirWEc8UX2hkCUGIduU8of+NMvTZ51qwrh35x7r1vX3NwMzHI~3162693~4470341; ak_bmsc=20718B7E2715E08D59D2993DA1A965F5~000000000000000000000000000000~YAAQRUo5FwhRc4F+AQAAILjDyQ7M3zfQHzBILndTXgBh0EFVEP05Ha4YU9RsWfPmqWtqFT9iOzmBmu6jEyu4hr0qQthBRyE7nXwX0wyB8Om9VEEv/IwQQU7Em3JsgMYSsTvJBebV4XffLcV3oCS4lwwDPEp6xBhnyHrEWuB5XvLrdRWlBrpXX5tOtONbC5yKVBDqk1TaGZ45+ANHWJ4i5roqgSw9nngSB0cP3SXu6l2PNrqkm9nZnJgK8I1yagoLdLdbn7ELpeY47t8IN8juv+9IhwDrl624d9GObjTGAEkgXzSRD1+bnAcTEcRTISKBoPUfFAQ3u03kRD+IhvOsvqb61RKOVDnmZMvPGI4DHRDK05621PiZHkylBjERLgQTrRQiZXPG0hJJRenz8QYEt4qO3GPNuO2H+lHkKYuske8bPLozP5T/F680hVVlJxxBTTXv1xDL8ENlk401phDhkQPqSeOy5lmjqq/sL1vyuukhrzXZeoPneFFudCXzgPCy; AWSELB=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90F2253C6BE3D923146E37BE76D25B6FB8549D736AE6046FECBF85DD2416AA6A66A29F91541FFD852096A98BD6F1C1DCC4; AWSELBCORS=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90F2253C6BE3D923146E37BE76D25B6FB8549D736AE6046FECBF85DD2416AA6A66A29F91541FFD852096A98BD6F1C1DCC4; pxa_ipv4=42.110.137.163; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19029%7CMCMID%7C35082967246199125900669614635959067013%7CMCAAMLH-1644667377%7C12%7CMCAAMB-1644667377%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-145948657%7CMCOPTOUT-1644069778s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19036%7CvVersion%7C4.4.1; akaalb_at_alb=1644068363~op=AT_col_lb:AT_col_use1|~rv=65~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=1e33c858d726b8b386014c17b734cec8; ATC_USER_RADIUS=50; _lr_retry_request=true; _dpm_ses.070d=*; JSESSIONID=AEF4EADF89311AF018B7D752C083EADA; _gat_UA-182514997-17=1; ATC_USER_ZIP=92101; akaalb_pixall_prod=1644069482~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=77~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=addaa05586db5fdb681fb674364598c5; s_pers=%20s_tbm23.6%3Dtrue%7C1646074907691%3B%20s_tbm23.5%3Dtrue%7C1646074774547%3B%20s_tbm23.27%3Dtrue%7C1646074897005%3B%20s_tbm23.22%3Dtrue%7C1646074581282%3B%20ev96gapv%3DUnknown%7C1646073000018%3B%20ev97gapv%3Dundefined%7C1644069484029%3B%20ev98gapv%3Dundefined%7C1646073000053%3B%20s_tbm%3Dtrue%7C1644069484071%3B%20ev95gapv%3D%7C1644069484081%3B; _uetsid=2e57d6b0863911ec82739f39dc6f3a18; _uetvid=2e58a4d0863911ec92df8b463a0acd32; _ga=GA1.2.66353926.1644034067; _dpm_id.070d=56c884d4-358d-42d0-8035-0b7cfc1dcb58.1644034071.5.1644067689.1644062583.f6bac8b4-e066-41e1-9ab1-718964622ddc; _cs_id=d9f78b36-206e-a340-9c8a-ea5c6606d26d.1644034070.6.1644067689.1644066438.1.1678198070475; _cs_s=8.0.0.1644069489544; _td=e471282e-7c6d-4d3b-94a7-3b1744b8cf0e; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1644066563.4.1.1644067712.60; _clsk=h8q9ro|1644067712810|12|0|f.clarity.ms/collect; bm_sv=F649C4CF0FE14E4A08839208937AD22B~B/0sgwOUn10rEOKxsGcRwpE3Znmkv6Vy/H06EFt0RW7BiSrk7edqjeAg+0Ue7bl0W/in+YyYv6bSb3QGcfb7OGQIcnp/3xWVkSc6Pr+bu+7rzgmGEMSpWQNtSJZavpJ1ivYMTngAcakx04UTvdw+9yPD+0NCJqNbZkqdhTv/EKI=; _abck=B48CA273DDEAFF3AFCCEDFFAA4F3E1FE~0~YAAQNzZ8aCgCU8V+AQAAUm8SygdcJlZlQFYpMDp9R90OG0tCdxYj0RYQIkC3WCX2NNOF9dEdIzLBfJVLuIb18xzRJeOsUhv2FzYjGHNO0cKIm+3eD2ds5epQkuo0XFwHnGHVnYMbOgKmxtVYanD9X61/aCkKA14PMvqPPzM11olp+7iuVzdboV9wIQtm3A0osYHBtowM7MSEHcNEFd11ayuaNfO8scdPX8bR2hp2pPOS/aBd+LfpGJ+9GKPKY5J/GHfrdM5YUKUtshtlnNBMXCs6yfIQWL+lhxVqbLAOBHsVqd7KskYqGV6PVN0U4ogKUooVyYnvB0oTBR4w2Idafzedz+wWsKVovh2iaWltwDjzLmnR2g+MgY6S3vZj/kcRWRDQ4nBw7hLOip4ifdlhAiVLTk+aqgD38w==~-1~-1~-1',
    }

    params = (
        ('allListingType', 'all-cars'),
        ('city', 'San Diego'),
        ('state', 'CA'),
        ('zip', '92101'),
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