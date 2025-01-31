from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Принимает на вход строку с типом и номером карты / счета и возвращает строку с замаскированным номером"""
    full_number = account_card.split()[-1]
    masked_number = ""
    if len(full_number) == 16:
        masked_number = get_mask_card_number(int(full_number))
    elif len(full_number) == 20:
        masked_number = get_mask_account(int(full_number))

    masked_account_card = account_card.replace(full_number, masked_number)
    return masked_account_card


def get_date(complex_format_date: str) -> str:
    """Принимает строку с датой в длинной форме, возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    simple_format_date = complex_format_date[8:10] + "." + complex_format_date[5:7] + "." + complex_format_date[:4]
    return simple_format_date
