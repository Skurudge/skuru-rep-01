import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("E:/PythonProject/logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | bool | list | dict | None | str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает ее маску"""
    if type(card_number) is not int or len(str(card_number)) != 16 or card_number <= 0:
        logger.error('Run program "get_mask_card_number": Invalid card_number value at program input')
        raise Exception("Неверное значение card_number!")
    else:
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
        logger.info('Run program "get_mask_card_number": returns a mask by card number')
        return card_number_masked


def get_mask_account(account: int | bool | list | dict | None | str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает его маску"""
    if type(account) is not int or len(str(account)) != 20 or account <= 0:
        logger.error('Run program "get_mask_account": Invalid account value at program input')
        raise Exception("Неверное значение account!")
    else:
        adding_second = "*"
        account_masked = 2 * adding_second + str(account)[-4:]
        logger.info('Run program "get_mask_account": returns a mask by account')
        return account_masked
