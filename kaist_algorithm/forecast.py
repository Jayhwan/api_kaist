import requests
import pandas as pd
# 필요한 기상 데이터 받아오는 작업
# 전후 24시간, 총 48시간 단기예보 데이터를 반환
# POP : 강수확률
# PCP : 1시간 강수량
# REH : 습도
# SKY : 하늘상태 (맑음(1), 구름많음(3), 흐림(4))
# WSD : 풍속
# TMP : 1시간 기온

def get_forecast_data_48h(ttime = None):
    '''
    주어진 ttime기준으로 전후 24시간, 총 48시간 단기예보 데이터를 반환
    기상청 open API에서 단기예보를 받아오고, 1시간 간격 데이터를 15분 간격으로 변환

    :return: (강수 확률, 구름 양, 기온, 풍속)를 15분 간격으로 반환

    # url : 기상청 단기예보 open API 주소
    # servicekey : 개인적으로 발급, 만료 예정일 2024-04-25 (이후 발급 필요) - 최대 연결 가능한 트래픽 문제 있을 수 있음
    # encoding/decoding : 2개의 key가 주어졌지만 url에 따라서 둘 중 하나만 유효 (단기예보의 경우 decoding service key)
    # parameter : (nx, ny) = (95, 76) : 부산 스마트시티의 지점 좌표
    '''

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    servicekey_encoding = 'ssqG9c911lmrEi%2F9oCTRBzXQSB1qzb2P2S8IF0vKTPplrNb5ux3KOHeHJDa04Z%2BvqAELQvcygV4SVTc8MNOLQw%3D%3D'
    servicekey_decoding = 'ssqG9c911lmrEi/9oCTRBzXQSB1qzb2P2S8IF0vKTPplrNb5ux3KOHeHJDa04Z+vqAELQvcygV4SVTc8MNOLQw=='
    params = {'serviceKey': servicekey_decoding, 'pageNo': '1', 'numOfRows': '50', 'dataType': 'JSON',
              'base_date': '20220602', 'base_time': '0600', 'nx': '95', 'ny': '76'}
    '''
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code != 200:
        pass
    주어진 지속적인 기상청 open API 오류로 우선 형식에 맞추어 특정 날짜 데이터를 사용
    '''

    f = pd.read_excel('./data/20220529_20220531_forecast.xlsx')
    print(f)


    return response

response = get_forecast_data_48h()
print(response.status_code)
print(response.content)
print(response.text)
print(response.json().get('response').get('body').get('items'))
