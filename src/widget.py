from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: int | bool | list | dict | None | str) -> str:
    """Принимает на вход строку с типом и номером карты / счета и возвращает строку с замаскированным номером"""
    if type(account_card) is not str or account_card == "":
        raise Exception("Неверное значение на входе функции!")
    else:
        full_number = account_card.split()[-1]
        group_of_number = account_card.split()[0]
        if len(full_number) == 16 and group_of_number in ["Maestro", "MasterCard", "Visa"]:
            masked_number = get_mask_card_number(int(full_number))
        elif len(full_number) == 20 and group_of_number == "Счет":
            masked_number = get_mask_account(int(full_number))
        else:
            raise Exception("Неверное значение на входе функции!")

        masked_account_card = account_card.replace(full_number, masked_number)
        return masked_account_card


def get_date(specified_format_date: int | bool | list | dict | None | str) -> str:
    """Принимает строку с датой в заданном формате, возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if type(specified_format_date) is not str or specified_format_date == "":
        raise Exception("Значение на входе не соответствует заданному формату даты!")
    else:
        if (
            len(specified_format_date) == 26
            and 0 < int(specified_format_date[5:7]) <= 12
            and 0 < int(specified_format_date[8:10]) <= 31
        ):
            simple_format_date = (
                specified_format_date[8:10] + "." + specified_format_date[5:7] + "." + specified_format_date[:4]
            )
            return simple_format_date
        else:
            raise Exception("Значение на входе не соответствует заданному формату даты!")
