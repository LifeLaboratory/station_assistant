from app.api.sql.auth_provider import Provider


def auth(user_data):
    provider = Provider()
    answer = provider.auth_user(user_data)
    if isinstance(answer, list):
        answer = answer[0]
    return answer
