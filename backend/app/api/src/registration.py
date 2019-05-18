from app.api.sql.register_provider import Provider


def register(user_data):
    provider = Provider()
    check = provider.check_user(user_data)
    if not check:
        id_user = provider.register_user(user_data)
        if id_user:
            id_user = {'data': 'Пользователь добавлен'}
    else:
        id_user = {'data': 'Пользователь существует'}
    return id_user
