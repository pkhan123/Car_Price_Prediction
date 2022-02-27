from turtle import st
import requests

# Sometime headers and params changes
# if get error on response.json() please check that
# also replace ('firstRecord', '50') by ('firstRecord', str(firstRecord))

def Curl_Python(page_to_scroll = 1):
    firstRecord = 25 * page_to_scroll - 25

### change the part below




    headers = {
        'authority': 'www.autotrader.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'tracestate': '1190893@nr=0-1-1543670-910308770-eceba94f5858f0a9----1645453765238',
        'traceparent': '00-cfe6d9e401a9beecb4e1ccd354432170-eceba94f5858f0a9-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMwODc3MCIsImlkIjoiZWNlYmE5NGY1ODU4ZjBhOSIsInRyIjoiY2ZlNmQ5ZTQwMWE5YmVlY2I0ZTFjY2QzNTQ0MzIxNzAiLCJ0aSI6MTY0NTQ1Mzc2NTIzOCwidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/nashville-tn-37201?dma=&searchRadius=50&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=25',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=d2b17d08-3641-4ff1-99d2-ed1467604577; akaalb_at_alb=1645455405~op=AT_col_lb:AT_col_use1|~rv=48~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=26efad2642534d0d4f289a4486bde8cf; bm_sz=77A431B1012130E10FB044AC0B568F99~YAAQ3nMsMdHaVw1/AQAAmXutHA6eDb8paKGkyJCUUUpdfMgjwSVyTre9y/LErWodq42itnPXQVCGHdnY1kOs1xyEmVHLtXpA69YNciJJ4pzI6PYYc5YqG4+ZRcOB/JwmTSpsJnSIu2gDkZR9mm75n5pz9Z+CeSrN4aN5ce6BLSwD/TgQoYln4xgSmegxg0pi14LMz1G4cmMsVoVCDDJYWlCMSaCZ7hoeiJmu8LHdLPMmy6e1jwKZ2rWNWAG9tzfX4AJfi5lOW2PIn3jgj8JQrf6HIPmXCNhUXzjgwt8dYPiuXqyzg1ti~4408889~3224902; ak_bmsc=CF6EB1C116476FA5F607E42C4EEA3687~000000000000000000000000000000~YAAQ3nMsMefaVw1/AQAAB4KtHA7KUSGJ2lK3PyQ5+CLKDEIvEp7Y6IDNDb8wD4tszk1TjWJK4LTdHsocB99cPfdvxlMdma9Jp+C+kx2FQy6x1xvNla+ztlxxt3altaUVWKX7KZ8aF5xUnW6wMzWlt750bUhvC67yfb35vQYImJazP2OiXD3eJyAsxK7Rlf3O1yRjVwNFYUEajuuPJd4tmDViA3gOFf0xs8sw/asYdue8rF0XP+TLR3IhNZt3tZP5ToTZRLpH8IDnrSDGpKdCiZVivJ/iKCYxFfYoYk83An518/as64yA2w+ppikfAOM56mPkikfGigAoW7CR7FdZa3yUUf2Vu+g8qo98JNzsVwvoQli59jQ5aCHI8VLVUikqhvt3ILdxtUpdUCeiEhG6ZF8D8/7vmY+j7P7xycSv7zRo5teLqHs+/z/S2Ma3GjxKNupyiAUW7nQaXqRDhei1Hqlbg8YqOyM3JuuDbhV3pJcYlOswER5/wzOw; pxa_id=9Sz2VsbGzAoFgvKiJvnBj5oJ; _gcl_au=1.1.759738032.1645453609; __gads=ID=0a70b0e92edccca9:T=1645453609:S=ALNI_Mb7gH679PoVWRDOcaH36VG91BOybA; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; _gid=GA1.2.778434356.1645453610; s_ecid=MCMID%7C42468521777295442684459117286069802107; _scid=b9db7362-f25a-4497-b5fb-0786e996e83d; abc=9Sz2VsbGzAoFgvKiJvnBj5oJ; pxa_ipv4=47.11.75.42; pixall_cookie_sync=true; pxa_at=true; _fbp=fb.1.1645453611228.1906976784; _cs_c=1; _dpm_ses.070d=*; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=42273331966626560254441867687732983854; _lr_geo_location=IN; _clck=9sea88|1|ez6|0; _sctr=1|1645381800000; _4c_mc_=ebcdfd8f-0189-4988-a95f-b87a78868191; _aeaid=9a624de9-29cc-4a07-b8a0-248efc278ffd; ATC_USER_ZIP=37201; aeatstartmessage=true; DCNAME=www-aws.autotrader.com; AWSELB=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90174FA3222DF3081BF07DA093D018B9AF3C840A81B845BE01060EE9E009F4C3204FFD70B6892F6FCA576E3534C089D79E; AWSELBCORS=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90174FA3222DF3081BF07DA093D018B9AF3C840A81B845BE01060EE9E009F4C3204FFD70B6892F6FCA576E3534C089D79E; ATC_USER_RADIUS=50; pixall_abc=9Sz2VsbGzAoFgvKiJvnBj5oJ; _pbjs_userid_consent_data=3524755945110770; akaalb_pixall_prod=1645455426~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=36~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=e186036eedbd8783a8da249214a8353b; abc_3rd_party=9Sz2VsbGzAoFgvKiJvnBj5oJ; s_pers=%20s_tbm7.17%3Dtrue%7C1646074897711%3B%20ev95gapv%3DTyped%252FBookmarked%7C1645455427293%3B%20ev97gapv%3Dundefined%7C1645455427312%3B%20ev98gapv%3Dundefined%7C1646072999322%3B%20s_tbm%3Dtrue%7C1645455427331%3B%20ev96gapv%3D%7C1646072999346%3B; _uetsid=4f397710932211ecb13ca35ff73d501c; _uetvid=4f3d1f30932211ecae88098deffd09de; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19045%7CMCMID%7C42468521777295442684459117286069802107%7CMCAAMLH-1646058427%7C12%7CMCAAMB-1646058427%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-1542788837%7CMCOPTOUT-1645460827s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19052%7CvVersion%7C4.4.1; _ga=GA1.2.1010498699.1645453609; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; _lr_retry_request=true; _lr_env_src_ats=false; _pin_unauth=dWlkPVpqRTJPRGxpTldNdE56VTNPUzAwTlRFMkxXSXdOR0l0TlRVNVlXWmhNVFF5TmpSaQ; pbjs-unifiedid=%7B%22TDID%22%3A%22355ce488-dbaa-4121-88aa-a22bbfdf847f%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-21T14%3A27%3A08%22%7D; _dpm_id.070d=ab4cfcf6-ed0e-446c-b9c1-f39dc7b1b7eb.1645453613.1.1645453629.1645453613.c19aca9b-85a5-480c-8837-c60009b8201f; _cs_id=f5bc3761-2181-adcd-ad04-57aa7db33682.1645453612.1.1645453628.1645453612.1.1679617612193; _cs_s=2.5.0.1645455428963; _td=055ffcc3-2f8e-48c8-9c7e-9dce5d0228be; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; _clsk=1j8p5w|1645453641641|2|1|e.clarity.ms/collect; _gat_UA-182514997-17=1; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1645453609.1.1.1645453764.45; bm_sv=776E143B08DC5AFEC502C4A4AC62DCB2~x+75+OY4KFhAEvqTavG7SfGkkSzel2L73YJnSbxDy38VpGD1VQClsFJjMFO1JnY6s2mH4WhF8TwyUAtVJFbte1EvRaVqsrnQJB6KTJFuiydheYseIzYrzhrDm0JnnRpEQZD8FGv+21avpIU2OAzrqr/1dZskB8qDSGmlVZ76LGE=; _abck=184F261FFAC5A6C9950E6608FEB94804~0~YAAQ3nMsMTvgVw1/AQAA8umvHAcxF9ycAaHpYgFqYTZr1qPoRdgl31El8kZ1lNyvPMrzLB+zB/2lElvjcLqIstDuBLdxKXKBYh/B9Un4yTcS1OwjjYZUej862nX1bTqlYaJqQ5j2RE2JRrgMR+yrJb6Io345HaBbNN7pYro67PNfxkfyswZUqJneDxuF8ALtesNlmP6yYzNt93OYbKuDCxjGQEN0MnPzUdLbRZYwm+3nlJc8bs7hteW3f0pFBXlCHQ9EiSV+jgRbE/1lOW779H4vOBxUlTwUKsQh92jSXUh1wu952ujN7wUPRgsFxuaKOXIivfvYEKe9lxJfarsUYJLg1K6lVp13r6ECsGU+VbU+oo5Ws+MxNrUFXOYwQlkotdO0wqqzVgLn3N+O9nmNf9t9j2mfWMX9dS740g==~-1~-1~-1',
    }

    params = (
        ('allListingType', 'all-cars'),
        ('city', 'Nashville'),
        ('state', 'TN'),
        ('zip', '37201'),
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
  
    
    
    
    
    
### change the above part   
    
    return response

