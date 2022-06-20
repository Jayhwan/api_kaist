# 미래 24시간 예측 데이터 반환

def predict_data_24h(gwid=None, url=None, ttime = None):
    '''
    주어진 ttime기준으로 이후 24시간의 예측 데이터를 반환
    기상청 단기예보 데이터 및 CEMS 데이터를 REST API 형태로 받아옴
    학습된 모델을 이용해서 예측 데이터 획득

    :return: 7개 열펌프에 대한 24시간 동작을 15분 간격으로 반환
    '''