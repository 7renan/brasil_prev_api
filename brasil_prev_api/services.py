import pytz
from rest_framework import status
from rest_framework.exceptions import APIException
from datetime import datetime

utc = pytz.utc


def get_age(birthday):
    today = datetime.now()
    is_birthday = ((today.month, today.day) < (birthday.month, birthday.day))
    year_difference = today.year - birthday.year
    age = year_difference - is_birthday
    return age


def validate_date_contract(product_expirate_date, contract_date):
    if product_expirate_date.replace(tzinfo=utc) < contract_date.replace(tzinfo=utc):
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                           detail='Não é possível contratar um produto com prazo de venda expirado')


def validate_value_aport(aport, value_min_aport):
    if aport < value_min_aport:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                           detail='Valor de aporte não permitido')


def validate_minimal_age(birthday):
    age = get_age(birthday)
    if age < 18:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Idade mínima permitida é de 18 anos')


def validate_max_age(birthday):
    age = get_age(birthday)
    if age > 60:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Idade máxima permitida é de 60 anos')


#TODO criar metodo carencia

def validate_initial_care(contract_date, initial_care_rescue):
    today = datetime.now()
    diference_days = today.replace(tzinfo=utc) - contract_date.replace(tzinfo=utc)
    if diference_days.days > initial_care_rescue:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                           detail=f'Carência para primeiro resgate deve ser de {initial_care_rescue} dias')


def validate_minimal_value_aport_extra(aport, minimal_aport_extra):
    if aport < minimal_aport_extra:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'Valor minimo do aporte extra é de {minimal_aport_extra}')


def validate_value_rescue(aport, value_rescue):
    if aport < value_rescue:
        raise APIException(code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                           detail='Saldo do plano insuficiente')


