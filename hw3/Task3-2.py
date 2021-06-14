def userdata (surname, name, was_born, town, email, tel):
    return dict(surname=surname, name=name, was_born=was_born, town=town, email=email, tel=tel)

print(userdata(town='Зюзюкино', name='Иван', was_born='2020', tel='+12345678901', email='ivanov@email.ru', surname='Иванов',))
