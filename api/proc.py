from datetime import datetime, timedelta

def get_previous_24h():
    '''
    :return: 현 시간 기준 24시간 전 (15분 단위 내림) 시간 반환
    '''
    start = datetime.now()
    start = start - timedelta(hours=24)
    minute = int(start.minute / 15) * 15
    start = start.replace(minute=minute, second=0, microsecond=0)
    return start


def call_predict(gwid: int, dt: str) -> pd.DataFrame:
    start_time: datetime = datetime.fromisoformat(dt)
    end_time: datetime = start_time + timedelta(days=1)

    params = {
        'gwid': gwid,
        'limit': 96,
        'url': '/ports/heatpump/1/meter',
        'starttime': start_time.isoformat(),
        'endtime': end_time.isoformat()
    }

    # print('%s %s' % (start_time.isoformat(), end_time.isoformat()))
    eparams = urllib.parse.urlencode(params)
    u = '%s/api/v1/history/energy/table?%s' % (ebrain_prefix, eparams)
    logger.info('url = %s', u)
    resp = requests.get(u, headers)
    if not resp.json():
        raise APIException('Empty response for %s' % u)
    df = pd.DataFrame.from_records(resp.json())
    df['ttime'] = pd.to_datetime(df['ttime'])
    df = df.rename(columns={'energy': 'pc', 'energyExport': 'pg', 'heatEnergy': 'hc'})
    df['hg'] = pd.Series(0, index=df.index)
    df.drop('gasVolume', inplace=True, axis=1)
    df.drop('waterVolume', inplace=True, axis=1)
    df.drop('hotwaterVolume', inplace=True, axis=1)
    df.drop('reactiveEnergyExportLag', inplace=True, axis=1)
    df.drop('reactiveEnergyExportLead', inplace=True, axis=1)
    df.drop('reactiveEnergyLag', inplace=True, axis=1)
    df.drop('reactiveEnergyLead', inplace=True, axis=1)

    logger.info(df.head())

    out_df = predict(df)
    return out_df.to_dict(orient='records')