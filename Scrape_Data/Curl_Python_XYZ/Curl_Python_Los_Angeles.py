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
    'tracestate': '1190893@nr=0-1-1543670-910326579-35e580bb6a3c9c37----1644038112843',
    'traceparent': '00-e69b419b0152cda1a868d27874682550-35e580bb6a3c9c37-01',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDM2NzAiLCJhcCI6IjkxMDMyNjU3OSIsImlkIjoiMzVlNTgwYmI2YTNjOWMzNyIsInRyIjoiZTY5YjQxOWIwMTUyY2RhMWE4NjhkMjc4NzQ2ODI1NTAiLCJ0aSI6MTY0NDAzODExMjg0MywidGsiOiIxMTkwODkzIn19',
    'content-type': 'application/json',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.autotrader.com/cars-for-sale/all-cars/los-angeles-ca-90001?dma=&searchRadius=25&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=25&firstRecord=50',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'ATC_ID=38695c89-5d6a-4725-97de-9228bc997a23; bm_sz=72FBD16C468F46DB9CE7D8D44B18D10A~YAAQ3nMsMXq15bh+AQAAR/0QyA4r+sbU2Q8bmbyKbtPsEKhgTo057dKJrWG+jzM0XujvZyNQycXRhnmdvYwCOjtEE4qgJUOI4paDy7EwdvXmK+WgP2ctkQT2mhYf+ASNSToQLk06LNTPc9oKKnOyz3VQ/FluZ8kYsalyL+QXgEhuldKyqZxvVVAEXsiOy99a3vfaS++9XYK3LGFRDhQobOBkX3cEFlHwQW4btVb/j5IrZ5Cv927FRmdMTpmRV8LfTivnWHirERqEdR7lSfFq0W/pf7M1TlmziLhBi+DbXf3B4lP/0lwI~4338229~3618886; ak_bmsc=6D565FEED5CDFE57E3A11E1F6E523328~000000000000000000000000000000~YAAQ3nMsMZK15bh+AQAAdAcRyA6Gr34gmwCwQHxrSshczh3hNh+6Jst4Uq1y1/VJC75xOBJhyukwgOjLiD1ns6M5456TJej0Jtg8RkOEYgnlQZ0sAtglZte36rxkGzOaQsUXxtpdvNWkLcccSIaO3h6ZAPjmVAdWvB80Hc3/8rxk+ZfZWZJ06EA38YGiRvIDuvdgvnr6LFqlAo5ueeuybIK3Y4R9HBMfOBECsKHS4nZYqL+Y8Q9UW/Ml5kuImKwTcXPk5pU7jXK53KY06n82VeSZNY247XTWPYyrTZL4nPWx4yChLsWCPZl1QjohnQJCADHwaazoNVVuo89byWYEwOj98PVHgKBwcfXKDdKAOtKCZAAoK4YbpBvcNljTf3GUWJl5BEUC6GDPUY+jbULGiE65D43cr/2B1BH6eyfNtJRquFOUdMAoHOsogJIpE02bBEFwNJsqnyCoQ9dhfSeQNQYAJAZko/8xnmXc1RyMPqYS5NlZm8mUks+RELMMo8c=; pxa_id=7t581PLAbpLaknSIgjE0VqFX; _gcl_au=1.1.1264858426.1644034067; AMCVS_A9D33BC75245B2650A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C35082967246199125900669614635959067013; _scid=23f19ee6-af4c-47ec-8878-e7dcc34f80ef; _gid=GA1.2.1487812677.1644034069; _fbp=fb.1.1644034068989.861423825; abc=7t581PLAbpLaknSIgjE0VqFX; pxa_ipv4=157.40.232.61; pixall_cookie_sync=true; pxa_at=true; _cs_c=1; aam_aa=aamaa%3D96119%7C96152%7C96128; aamoptsegs=aam%3D92872; aam_uuid=35248076571290034830652927790183386576; _lr_geo_location=IN; _sctr=1|1643999400000; _clck=1qacwtq|1|eyq|0; __gads=ID=06f4fd1e98b26b76:T=1644034067:S=ALNI_Mb6QVVsdKMVHlKygEZUN4lZ3BGjfA; _4c_mc_=6a6b4313-eb24-4ed5-974d-1246fb786820; _aeaid=61ea0516-79a3-4ed3-aaaa-a5f29eaae3d6; aeatstartmessage=true; ATC_USER_RADIUS=25; pixall_abc=7t581PLAbpLaknSIgjE0VqFX; _pbjs_userid_consent_data=3524755945110770; abc_3rd_party=7t581PLAbpLaknSIgjE0VqFX; AMCV_A9D33BC75245B2650A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19029%7CMCMID%7C35082967246199125900669614635959067013%7CMCAAMLH-1644638985%7C12%7CMCAAMB-1644638985%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C-145948657%7CMCOPTOUT-1644041385s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19036%7CvVersion%7C4.4.1; _lr_env_src_ats=false; _pin_unauth=dWlkPU16QTNNV1ExTm1NdE0yTXpNeTAwWVdRM0xXSTJZakF0TnpGbE0ySmtaVFV5WmpFMA; dxatc=%3D6545; aam_tnt_vin=vin_seg%3Datc; pbjs-unifiedid=%7B%22TDID%22%3A%22d63f2eab-18bc-454f-b132-8fdab5236abc%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-05T04%3A09%3A46%22%7D; DCNAME=www-aws.autotrader.com; AWSELB=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90174FA3222DF3081BF07DA093D018B9AF7D0494BC38B53E2263DF7FF0B9DBE74F4CD1B1D885CECF20B78111FE3511BE96; AWSELBCORS=4F5B35E70EB661C4D1C098EABD38669F62BFA33A90174FA3222DF3081BF07DA093D018B9AF7D0494BC38B53E2263DF7FF0B9DBE74F4CD1B1D885CECF20B78111FE3511BE96; akaalb_at_alb=1644039842~op=AT_col_lb:AT_col_use1|~rv=49~m=AT_col_use1:0|~os=659c3ec2d171bf62456d07d58a4d53bf~id=99820d4c8e88a6e9345c34c875dbccea; _dpm_ses.070d=*; ATC_USER_ZIP=90001; _lr_retry_request=true; _uetsid=2e57d6b0863911ec82739f39dc6f3a18; _uetvid=2e58a4d0863911ec92df8b463a0acd32; _ga=GA1.2.66353926.1644034067; _dpm_id.070d=56c884d4-358d-42d0-8035-0b7cfc1dcb58.1644034071.2.1644038062.1644035440.bd190156-2d4e-4b1b-a188-c0ade7a0f000; _cs_id=d9f78b36-206e-a340-9c8a-ea5c6606d26d.1644034070.2.1644038063.1644037513.1.1678198070475; _cs_s=3.0.0.1644039863084; _td=e471282e-7c6d-4d3b-94a7-3b1744b8cf0e; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3Dfyc_srl%3B; JSESSIONID=P5vqo9zryuI7muYBDNxp9RJU3zLMVG8wJEshJhIL.90c072778f0d; _clsk=19edtzz|1644038101774|15|0|h.clarity.ms/collect; _ga_GRZKKR4C6W=GS1.1.1644034067.1.1.1644038102.60; s_pers=%20s_tbm23.6%3Dtrue%7C1646074907691%3B%20ev95gapv%3DTyped%252FBookmarked%7C1644039903261%3B%20ev97gapv%3Dundefined%7C1644039903284%3B%20ev98gapv%3Dundefined%7C1646072999294%3B%20s_tbm%3Dtrue%7C1644039903307%3B%20ev96gapv%3D%7C1646072999326%3B; akaalb_pixall_prod=1644039903~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-us-west-2|~rv=44~m=eng_ana_pixall_prod-us-west-2:0|~os=6aafa3aac97a52a58cd06655a170720e~id=4504264c8c9016492a13cc4cc4868941; bm_sv=B7293DA503E70662322EE43353D4144A~UMDL2SfqX9w2/t1joemoVHl0EOS+eXZc5wCWXEFHA/W7kLp8g4E85rSEMZoJGaO6aieEU+c87/8rDySWrnQWu+kdaRWEeYxsjsy1sFZffLp4bJ6P8lesplfEf2jLr+lJ19QOtDvijAp4t53reIjGNEfoaUlb48tvN0tPDPheS/4=; _gat_UA-182514997-17=1; s_sq=%5B%5BB%5D%5D; _abck=B48CA273DDEAFF3AFCCEDFFAA4F3E1FE~0~YAAQ3nMsMf4p5rh+AQAAdcNOyAfnDUbv0ZHqS18BNFxtj/bxfpZjS0HIyanuC3PGhRv6c2mgXJHyWZYn4w0RWQY4TQyy8mQzK4SEcUNxN7GLADaZvbwaRaRlbkjVndBbc0NrDbNLrm6qpkE926GBC1XNW/noGP13W4LtZ7TMxZj/IAtt/0MQVYvg+3VBxfolTf+X2PijhaqSlsxfU89oAmAtsUeTd7re0eCb0nHmRVhJrVozew5lb9rDPHjpUv3TRGBkv2Q20q+KCyKSIDb6guL3VTebUAwPrJosMoAaIcheMtUoygF5yy0LKpoUly/uglbJxKFRgeAnXbYqYDmTO4aTljCaJpX8ovrlyurcc603u1uBbj77Q+1gZqxrFez3BZTcgw3aoB8spQwr/FOlaA6z6DgzmTkXPA==~-1~||1-HvxSppqrVq-1-10-1000-2||~-1',
    }


    params = (
        ('allListingType', 'all-cars'),
        ('city', 'Los Angeles'),
        ('state', 'CA'),
        ('zip', '90001'),
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

