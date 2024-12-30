# pandas mine
import pandas as pd

def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions = sessions.sort_values(by=['user_id', 'session_start'])
    # print(sessions)
    sessions = sessions.groupby(['user_id', 'session_type'],sort=False).size().reset_index(name='count')

    # print(sessions)
    id_done = set()
    result = []
    for i in range(len(sessions)-1):
        # print(i)
        row = sessions.iloc[i]
        if row['user_id'] in id_done:
            continue
        row_1 = sessions.iloc[i+1]
        if row['user_id'] == row_1['user_id'] and row['session_type'].lower()=='viewer':
            result.append((row_1['user_id'],row_1['count']))
            id_done.add(row_1['user_id'])
        else:
            id_done.add(row['user_id'])
    # print(result)

    result = sorted(result,reverse=True,key= lambda x : (x[1],x[0]))
    return pd.DataFrame(data=result,columns=['user_id','sessions_count'])

# pandas submitted go through rank fn.
import pandas as pd

def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
    # 1. rank sessions partition by user_id
    sessions['rnk'] = sessions.groupby('user_id')['session_start'].rank(method = 'dense', ascending = True)
    print('rnk',sessions)
    # 2. filter user_id whose rnk == 1 and session_type == 'viewer' 
    users = sessions[(sessions['rnk'] == 1) & (sessions['session_type'] == 'Viewer')][['user_id']].drop_duplicates()
    print('users',users)
    # 3. get user_id whose count(streamer session) >= 1
    streamer_session_count = sessions[sessions['session_type'] == 'Streamer'].groupby('user_id').agg(
        sessions_count = ('session_id', 'count')
        ).reset_index()
    print('session',streamer_session_count)
    # 4. merge users with streamer_session_count and sort and return
    df = users.merge(streamer_session_count, how = 'inner', on = 'user_id')
    print('df',df)
    return df.sort_values(by = ['sessions_count', 'user_id'], ascending = [False, False])


## SQL me 