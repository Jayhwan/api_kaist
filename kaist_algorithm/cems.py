# 필요한 CEMS 데이터 받아오는 작업
# 개별 가구 발전량, 사용 패턴(gwid, url) 커뮤니티 전체 발전량
from datetime import datetime, timedelta


def get_data_24h(gwid=None, url=None, ttime=None):
    '''
    주어진 ttime기준 주어진 gwid, url 정보로 이전 24시간 CEMS에서 측정된 값을 반환
    기상청 open API에서 단기예보를 받아오고, 1시간 간격 데이터를 15분 간격으로 변환

    :return: (강수 확률, 구름 양, 기온, 풍속)를 15분 간격으로 반환
    '''

    start_time: datetime