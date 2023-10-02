def round_rate(rate):
    """
    Function that will round an input float to 4 decimal places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, 4)

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it's not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise, it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        inverse_rate = 1 / rate
        return round(inverse_rate, 4)
    else:
        return 0.0

def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that formats the output message with date, currencies, rate, and converted amount.

    Parameters
    ----------
    date: str
        Date of the FX conversion rate
    from_currency: str
        Origin currency code
    to_currency: str
        Destination currency code
    rate: float
        FX conversion rate
    amount: float
        Amount in the origin currency

    Returns
    -------
    str
        Formatted output message
    """
    formatted_message = f"Date: {date}\n"
    formatted_message += f"From Currency: {from_currency}\n"
    formatted_message += f"To Currency: {to_currency}\n"
    formatted_message += f"Conversion Rate: 1 {from_currency} = {rate} {to_currency}\n"
    formatted_message += f"Converted Amount: {round_rate(amount)} {from_currency} = {round_rate(amount * rate)} {to_currency}"
    return formatted_message
