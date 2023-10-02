import streamlit as st
import datetime
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("Currency Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

if currencies is None:
    st.error("Error fetching currency list from Frankfurter API.")
else:
    # Add input fields for capturing amount, from and to currencies
    amount = st.number_input("Enter Amount:", value=1.0)
    from_currency = st.selectbox("From Currency:", currencies)
    to_currency = st.selectbox("To Currency:", currencies)

    # Add a button to get and display the latest rate for selected currencies and amount
    if st.button("Get Latest Rate"):
        latest_rates = get_latest_rates(from_currency, to_currency)

        if latest_rates is not None:
            conversion_rate = latest_rates[to_currency]
            converted_amount = amount * conversion_rate
            st.success(f"1 {from_currency} = {conversion_rate} {to_currency}")
            st.success(f"Converted Amount: {round_rate(amount)} {from_currency} = {round_rate(converted_amount)} {to_currency}")
        else:
            st.error("Error fetching latest rates from Frankfurter API.")

    # Add a date selector (calendar)
    selected_date = st.date_input("Select Date:", datetime.date.today())

    # Add a button to get and display the historical rate for selected date, currencies, and amount
    if st.button("Get Historical Rate"):
        historical_rate = get_historical_rate(selected_date, from_currency, to_currency)

        if historical_rate is not None:
            converted_amount = amount * historical_rate
            st.success(f"1 {from_currency} = {historical_rate} {to_currency}")
            st.success(f"Converted Amount: {round_rate(amount)} {from_currency} = {round_rate(converted_amount)} {to_currency}")
        else:
            st.error("Error fetching historical rate from Frankfurter API.")





