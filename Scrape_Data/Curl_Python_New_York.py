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
        'tracestate': '1190893@nr=0-1-1543670-910326579-4fa665af5a839139----1645724326230',
        'traceparent': '00-ad88395ffeeab16f2d65bd5dccec6290-4fa665af5a839139-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMyNjU3OSIsImlkIjoiNGZhNjY1YWY1YTgzOTEzOSIsInRyIjoiYWQ4ODM5NWZmZWVhYjE2ZjJkNjViZDVkY2NlYzYyOTAiLCJ0aSI6MTY0NTcyNDMyNjIzMCwidGsiOiIxMTkwODkzIn19',
        'content-type': 'application/json',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/new-york-ny-10001?dma=&searchRadius=25&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=75',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'ATC_ID=6531d272-cabe-4b6d-9e75-624137eec5c8; akaalb_at_alb=1645726072~op=AT_col_lb:AT_col_use1|~rv=63~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=4281dde3519140eb2be21f9f2767ad8b; bm_sz=6BA0723236D02B6872632A534DE06B8E~YAAQRUo5FxZOFSV/AQAAL4nPLA7aqHCA0lXqv1l+/t80KDXBhlvsEjvCW7dtd23eb/0Eeyr6I0LXIGpG6z82MJ/VIBmfGgT9XhXqorP27P4mniJQ6FKhSoYiIJikW2zAvGobxL1LI+KSacP7IkmY1QiCyfvW1CzGmEsxoDMQmAiw1RF+mUG1A2Y3dNqdTO6TqI801XwleZfSFG0f1Mm0A1f9mBLus7TuXtJ/PwpbO54NBK2Jd4YHca6lLfDmPQQZMZJ13LFmSJkl8G8CxZfb8FNm6hp9QiSPyy2W9MxjQQewpAbdw/ob~4601905~4534833; ak_bmsc=A9B89523E45A85EA34BBB1537C84340C~000000000000000000000000000000~YAAQRUo5F0lOFSV/AQAAEY/PLA4CbwmjMhlRhRjpV1+j3R1YQM0NEl8VQm5iQi0DhLwj93NVDU8QCPOoii/6MRUVZZxRVEe0gg8DCExYQ9HypZhjlUlVU0UZsoXd6rd0ps8+xSDXDl6L1+OTpoYDswJ7zdc0xsO5EiYMp4q0CQA81EItCRGCB/ac4BfA6cPA9F9V03K/n0k3qJu4OAXiUSoqSsqLqQVwHTEwtDorua4eS415JEpHuQT/g153KKIQnWrDZ77BM5fvu8T9T3ugiFsNcylf/BP9YJrfGzlddMiifSpEiMoZ6KADz8rjwOFFxg5aecH9iAWJSV3FFZdvTaVOHwrqFpS5YH6sAHHwS1KuVVOGwqynNO2Ss26pN41+28ABtdwc1qAAIbnKwnT8k4rXUxCU9ViPMNQtFTPVM7GR4XQEQ/CUvkcbdNwliuOHSsVUVRMJBUE7bjp/X6SV9iGK6MdFF3Kff3Ah2h8Z7cKRM76c+auU25S03OLo; pxa_id=bCYd41aQB9z0y1A0rV11B0YF; __gads=ID=41295cb1d43e6c1a:T=1645724275:S=ALNI_MaUeHDiXVHDDMqND8ZXAep4jmIQsQ; _gcl_au=1.1.1863187294.1645724276; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; abc=bCYd41aQB9z0y1A0rV11B0YF; pxa_ipv4=103.59.73.204; pixall_cookie_sync=true; pxa_at=true; _gid=GA1.2.709950459.1645724277; _gat_UA-182514997-17=1; s_ecid=MCMID%7C00947717856574758911149873068546324427; _scid=99faea70-e638-4034-828a-0e162c08274e; _fbp=fb.1.1645724278251.253012424; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=00782266995681073661130530902684687262; _cs_c=1; _dpm_ses.070d=*; ATC_USER_ZIP=10001; _sctr=1|1645641000000; _clck=xfiki4|1|ez9|0; _lr_geo_location=IN; _aeaid=5c18802c-3f8a-4921-96d6-2913b5111039; aeatstartmessage=true; _4c_mc_=27ba2664-9907-47be-8673-a58a8d5c2008; ATC_USER_RADIUS=25; pixall_abc=bCYd41aQB9z0y1A0rV11B0YF; akaalb_pixall_prod=1645726093~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-pico-us-west-2|~rv=89~m=eng_ana_pixall_prod-pico-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=a8810273ec4241b611123833a7ad1e14; _pbjs_userid_consent_data=3524755945110770; abc_3rd_party=bCYd41aQB9z0y1A0rV11B0YF; _ga=GA1.2.1246903089.1645724276; s_pers=%20s_tbm4.04%3Dtrue%7C1646075132643%3B%20ev95gapv%3DTyped%252FBookmarked%7C1645726094727%3B%20ev97gapv%3Dundefined%7C1645726094742%3B%20ev98gapv%3Dundefined%7C1646072999755%3B%20s_tbm%3Dtrue%7C1645726094762%3B%20ev96gapv%3D%7C1646072999769%3B; _uetsid=81093f40959811ecbd2a79dd35d2eb73; _uetvid=8109ea60959811ec850313cc0c3916f6; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19048%7CMCMID%7C00947717856574758911149873068546324427%7CMCAAMLH-1646329095%7C12%7CMCAAMB-1646329095%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-472391603%7CMCOPTOUT-1645731495s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; _pin_unauth=dWlkPVlUQmtaR1EyTWpZdFl6WXpZUzAwTkdGbUxUa3daakl0WW1Vd016STRORGhrTnpCaw; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%2248ba2542-2fda-457d-ba4f-ee1e5032d0f5%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-24T17%3A38%3A15%22%7D; _dpm_id.070d=d1f3a629-97d0-4413-8068-555b3d2669fd.1645724280.1.1645724296.1645724280.00e19b83-7d53-4e41-93d9-740825e8b185; _td=6d6a113f-bb7f-41f4-98aa-998a22376c7f; _cs_id=1fdf98fe-c0ba-aa70-bcf3-e6b9be106a44.1645724279.1.1645724296.1645724279.1.1679888279970; _cs_s=2.0.0.1645726096046; DCNAME=www-aws.autotrader.com; AWSELB=63D17F8D0A6A31FD1A70DEEAE0035E96AA49FCE54DF7E58C2A1574D271CBD40164BAFD378E05C50B3490D3F7D77D63186541683A594F4DD59C26F1E666B9556B6C225100B5; AWSELBCORS=63D17F8D0A6A31FD1A70DEEAE0035E96AA49FCE54DF7E58C2A1574D271CBD40164BAFD378E05C50B3490D3F7D77D63186541683A594F4DD59C26F1E666B9556B6C225100B5; s_sq=%5B%5BB%5D%5D; _ga_GRZKKR4C6W=GS1.1.1645724276.1.1.1645724325.11; _clsk=10gho5o|1645724326081|3|0|l.clarity.ms/collect; bm_sv=1DF478C03C772E7FD150189AAA6116CF~gZ/ZmJWx1dWUssfuwtMtDgmSvxMazjrnXQZPKjD0mPuOT6vRD9C9S2u+jSRZpOF/OlUYIAqrO591we/gkimAsFMyUzf7D1STziaeQFycl5KQ2dnZdnhaXA+uu6rLCja1hYF9nFjvIdWpYrf2fP17RxTwwNibgdMrXlnklP5w1II=; _abck=05AAD10B3017B9E5DCFE49DFBE95ADCF~0~YAAQRUo5F5tRFSV/AQAA3ljQLAewOVJMVxxg6HErLjapYQ1lxajnFuLlIInO1Rt0mwkHY5pwI+0P3FGdrBCGs0+i5CjgOgk2TYm1VobQvPOFevpvfqqKvL4nHi2Sd5kIeIW16BNyfl7hupflL5e2IwRGU/Pvd5jHy9UTV7dMerEMrZSeHeTGRBdhI1CgGQNzpoaZWgHntgrL3ZexAQNpcWGhdW5zIrzlSVSdRu6jhnwQPTOELDx31f6Vq7a7cKvl/6204pw8cVYU1ch9KZnMN51HbaR1mRclzgpuMpJnpo1VTa411Xx24w4QflHhN1PfbyD76ya7l9CQRRuSwsO+tSFOPQpkMmSBkCoSqxfIwPsOdzrGGbo9t8XRn37EiQwkQ28x5DwdQb2NVPru7lH+Wr7CtDTGNrXqEYD3Uw==~-1~-1~-1',
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









### change the above part
    return response

