from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
# 조회 했을 때는 userId로 분류
class MyAnimals(Resource):
    # 로그인한 상태에서만 구매 및 조회 가능
    @jwt_required()
    def get(self):
        # 유저가 동물을 구매했을 때, 코인 차감, 보관함에 동물 추가
# 조회에 적용할 쿼리문
# select u.name as 'user_name', p.name as 'pet_name'
# from user u
# join userPet up
# on u.id = up.userId
# join pet p
# on up.petId = p.id
# where up.userId = 3;
        offset = request.args['offset']
        limit = request.args['limit']
        user_id = get_jwt_identity()
        try:
            connection = get_connection()
            query = ''' select u.name as 'user_name', p.name as 'pet_name'
                    from user u
                    join userPet up
                    on u.id = up.userId
                    join pet p
                    on up.petId = p.id
                    where up.userId = %s
                    limit '''+offset+''' , '''+limit+'''; '''
            record = (user_id,)
            # select 문은 , dictionary = True를 해준다.
            cursor = connection.cursor(dictionary = True)
            cursor.execute(query, record)
            # select 문은, 아래 함수를 이용해서, 데이터를 가져온다.
            result_list = cursor.fetchall()
            print(result_list)
            # created_at과 updated_at이 필요할까???
            # 중요! 디비에서 가져온 timestamp 는
            # 파이썬의 datetime 으로 자동 변경된다.
            # 문제는! 이데이터를 json 으로 바로 보낼수 없으므로,
            # 문자열로 바꿔서 다시 저장해서 보낸다.
            # i = 0
            # for record in result_list :
            #     result_list[i]['date'] = record['date'].isoformat()
            #     result_list[i]['created_at'] = record['created_at'].isoformat()
            #     result_list[i]['updated_at'] = record['updated_at'].isoformat()
            #     i = i + 1
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503
        return {'result': 'success',
                'count': len(result_list),
                'pets': result_list },200