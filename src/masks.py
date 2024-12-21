def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты в виде числа и возвращает ее маску"""
    adding_first = " "
    adding_second = "*"
    card_number_str = str(card_number)
    card_number_masked = (
        card_number_str[:4]
        + adding_first
        + card_number_str[4:6]
        + 2 * adding_second
        + adding_first
        + 4 * adding_second
        + adding_first
        + card_number_str[-4:]
    )
    return card_number_masked


def get_mask_account(account: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает его маску"""
    adding_second = "*"
    account_masked = 2 * adding_second + str(account)[-4:]
    return account_masked
