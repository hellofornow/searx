"""
 No Agenda Show Search

 @website       http://www.noagendashow.com/
 @provide-api   yes (https://search.nashownotes.com/search),
                unlimited
 @using-api     yes
 @results       python dictionary (from json)
 @stable        yes
 @parse         url, title, content
"""

from json import loads
from flask_babel import gettext
from searx.url_utils import urlencode

categories = ['news']
paging = True

url = 'https://search.nashownotes.com/search'

def request(query, params):
    params['url'] = url
    params['method'] = 'POST'
    params['headers']['Cookie'] = '_search_na_session=OEtCNGltSTgxcFlIREF0SGU2Z045R3BodHJ4SGo5QnBaa2NJdXN5bzVqOXRjbHNEQmpSSGk1SzR1MVdiSVZobHluRDMxVXM1OFU3Q3hwUDZDVGx3MW9RZ3pSM05VNStINkI0UGVFY2NPeDFUVmRCSTg3azZ2a2VPR2FxZlNHSXh5SmordkRyVHpQLzhTUDhnVU9nWnNnPT0tLVMzOThLeXVMdWNtTWxvVWxRRUxHMEE9PQ%3D%3D--3bd37e0bbb8c7e938b0f3ba41295ff624c9bb879'
    params['headers']['X-CSRF-Token'] = '3hc8WXeILLCdkw0DvUU7VZBGs4D6F+N54qBvtK/RcwUNAJiYan8v5THN09TGBb14T/ukSzC6Rgwgdlnkci3xQw=='
    params['headers']['Host'] = 'search.nashownotes.com'
    params['headers']['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    params['data'] = urlencode({'string': query, 'page': params['pageno'], 'min_show': '', 'max_show': ''})
    return params


def response(resp):
    search_results = loads(resp.text)

    results = []
    if not search_results['count'] or search_results['count'] == 0:
        return results

    # parse results
    for result in search_results['results']:
        results.append({
            'url': 'http://%s.noagendanotes.com/' % result['show_id'],
            'title': result['title'],
            'content': result['text'],
            # 'img_src': 'TODO'
        })

    return results
