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
        'tracestate': '1190893@nr=0-1-1543670-910308770-791a52f61af1199b----1645417843534',
        'traceparent': '00-84198919fdec928483fbec42a64a4800-791a52f61af1199b-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMwODc3MCIsImlkIjoiNzkxYTUyZjYxYWYxMTk5YiIsInRyIjoiODQxOTg5MTlmZGVjOTI4NDgzZmJlYzQyYTY0YTQ4MDAiLCJ0aSI6MTY0NTQxNzg0MzUzNCwidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/detroit-mi-48201?dma=&searchRadius=50&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=25',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=3b120f1a-ce5c-45d8-830b-18a7f32a7ede; akaalb_at_alb=1645417915~op=AT_col_lb:AT_col_use1|~rv=56~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=9f6ff27241f0835abf242c6940bdfae7; bm_sz=EC0CBDE0DC184C2636622CEEA079FC9D~YAAQ3nMsMf8LTw1/AQAAWm1xGg5LGGgfvka9jBNIGKYi4F/UwcOcjpMpdKToADYqNmHhh1CAdERc+5kCm67ZuhPHZXhdYQRIvVRNmWWqJsgWGG+BD3J03AICG6GryoDIIjRaGSYAviPfiTfn3NyUvhn0wAw2Dzh+KYuA/Y/U3AefO3M9drC+SroY4PthpwZuBwqzyq+75f4TjW/zEeKNST3Kpo3gfbItxx1p44EkFfUvHGFN8CUcfUz55F7sGnFfwNWEttpFAO/c3AOd98w1OT2WOSlJr+2AMq869awBMzAYLSIhtsMk~3225395~4605494; ak_bmsc=F5A3720AE1606231041503CD37DE4517~000000000000000000000000000000~YAAQ3nMsMS4MTw1/AQAA3HdxGg7PG7Je7rtu7qpPCM28pP2MfgSwcK2f4TyMx2UG1R0E1iVopwS0yXrrYBbFn7jKWR34fTU7nkMkDaEek8XNiDuM4pZNMCWAvgxM0CA/9hKfK5EwDPGUxlN7Lx+HSMx+n97O7UwIybY3mA79rWuqmUTcHXp0BRRvlcFzs/jAapnaMpKyKGwx2BXl/ojn6/s0XH7XK9A6u8f5VRU/dD6rWvvtIge5y0e6vd3fc0Gi8YuCU/97Q3xGG6yR/LLQHJBCGgIw82obnXDDhwpEWGeTwiRGfzDQbJ30jSgsJIPQo+TFr5eWvYZLXYMVLq8l1t6yOCTOGu8qWQQ+5CjOZwsRgutvBJiw5EmOz5/8swibDVZOytEWi67d18B751DxA72Nq/oHD57iLLWyRGun96T26jwHR06K8EBjWNOho6wi8Jv63rQwL1v0Ia4gwJQzo4v4Z64VZP/hK+ysBr7Q8q2sgao4X1AAejdo; pxa_id=1sNDsMcCgEis9aPZetEtsjRU; _gcl_au=1.1.1373177298.1645416120; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; _gid=GA1.2.1088278493.1645416120; _scid=51a0fc0a-51fd-4674-9fef-97345b4dc75f; abc=1sNDsMcCgEis9aPZetEtsjRU; pxa_ipv4=47.11.66.47; pixall_cookie_sync=true; pxa_at=true; _cs_c=1; _dpm_ses.070d=*; s_ecid=MCMID%7C10344760565941492642531822218980505842; _fbp=fb.1.1645416122353.1963265380; _lr_geo_location=IN; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=10173680291038012852551164187265242279; _clck=pek3gw|1|ez6|0; _sctr=1|1645381800000; _4c_mc_=4f6116c6-db89-4eb1-9967-9843d8c3382d; _aeaid=4014b22d-9a38-43db-a353-cca6b75f58d1; aeatstartmessage=true; pixall_abc=1sNDsMcCgEis9aPZetEtsjRU; _pbjs_userid_consent_data=3524755945110770; abc_3rd_party=1sNDsMcCgEis9aPZetEtsjRU; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19045%7CMCMID%7C10344760565941492642531822218980505842%7CMCAAMLH-1646021230%7C12%7CMCAAMB-1646021230%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C91770589%7CMCOPTOUT-1645423630s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19052%7CvVersion%7C4.4.1; _lr_retry_request=true; _lr_env_src_ats=false; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; pbjs-unifiedid=%7B%22TDID%22%3A%226da1c8b2-e856-439b-ba01-f986f12c9823%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-21T04%3A07%3A10%22%7D; _pin_unauth=dWlkPU5qRXlaREV5WTJVdE9UWmtZUzAwTW1JM0xUazROVFV0WmpKbE1EQXhNVEk0TUdaaw; __gads=ID=2ccbf5406df39395:T=1645416120:S=ALNI_MZV42SQYFybzUxt6oFaGNwgDXvC4A; DCNAME=www-aws.autotrader.com; AWSELB=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90D1A09B36C06CCE60F34F5F985A6EE37C7D0494BC38B53E2263DF7FF0B9DBE74FE4A248BFAC5BD81BFCBDDFD5DE6E25DC; AWSELBCORS=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90D1A09B36C06CCE60F34F5F985A6EE37C7D0494BC38B53E2263DF7FF0B9DBE74FE4A248BFAC5BD81BFCBDDFD5DE6E25DC; ATC_USER_RADIUS=50; _gat_UA-182514997-17=1; JSESSIONID=2923DAC49EFB2BAB6519F6D74A030F80; ATC_USER_ZIP=48201; akaalb_pixall_prod=1645419609~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=21~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=e19a555ca449462668aa2e4fb2423516; _ga=GA1.2.2066409207.1645416120; _uetsid=05880f3092cb11ec9af87185faa99494; _uetvid=05886af092cb11eca79295b21b24b05f; s_pers=%20s_tbm7.6%3Dtrue%7C1646074559580%3B%20ev95gapv%3DTyped%252FBookmarked%7C1645419610104%3B%20ev97gapv%3Dundefined%7C1645419610117%3B%20ev98gapv%3Dundefined%7C1646072999128%3B%20s_tbm%3Dtrue%7C1645419610135%3B%20ev96gapv%3D%7C1646072999143%3B; _dpm_id.070d=6922f3ed-c927-47b7-b188-4f9bb79015a6.1645416122.1.1645417813.1645416122.d062d5b3-60f1-403a-bfa6-2cf165dc329f; _cs_id=e8c3fed2-2181-a60f-e2b0-f5ebfb905ec0.1645416121.1.1645417813.1645416121.1.1679580121467; _cs_s=7.0.0.1645419613425; _td=0a409213-2ecf-4129-974a-2958341170d9; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1645416119.1.1.1645417843.60; _clsk=yg2eks|1645417843380|12|0|k.clarity.ms/collect; bm_sv=8E50ABB0A80EF82EA90EFE247890E18F~x+75+OY4KFhAEvqTavG7SR55/hE6oJkHGnLQsGh/HS2jH9Licxh6N8syqsryrfpS8tmhfi64+uD+/sqayfgA1sqalXzEWvHk3oahJbfSa1SLrjSuFJWq1L70g02WMHGgL9tNzXgSB4yM2+A/bdagSDvMSb1Zpg8KE25tWx+BEfc=; _abck=74DA0356410F7AE4375414A3314EC8CA~0~YAAQ3nMsMXlzTw1/AQAAs8qLGgeFTho5qI+ux3u0zLqrn6TJKJiS0xkgEz1Yv5s7gpPcX8YimDA/wrkO+T+rPDUUc/vx8fuMD7j01wmMwLWjvG8c/fU/zHQX1bJnndVertSGsmyTkVfXG+royZx/W31Ruvrs3q4ekwpqHGAL6zmbSFK7kXs2rWDFlOOhZPsWFesrK8V+GBSWy5p+YzmCNcbU0vpR0ca3OcUEqWZ36/TxNuInxIVemXFW5J+x9Nk2Oi2JYqxiydEMvFYybwWAfIvmh7GsMkkpGOnmEusNjbaeI4t/T9hUmZcR8BSluACdWMsxQ1CxLC5AFZqprcIp1EmFWKGxe6dzbBDA/J8nmu44QUGShSJqj0ykc0i+BTYdF9Ke7gLeSXxHXAm4XN9eOc8ndvegqFUzOr1I4w==~-1~-1~-1',
    }

    params = (
        ('allListingType', 'all-cars'),
        ('city', 'Detroit'),
        ('state', 'MI'),
        ('zip', '48201'),
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