# Homework 4




EXAMPLE
---
>>> henry = Customer('Henry', 'Male', 'HenryJJ@yo.com', '1990-07-23', '111-111-3344')
>>> print(henry)
Name: Henry
Gender: Male
Email: HenryJJ@yo.com
Birthday: 1990-07-23
Phone: 111-111-3344
Accounts: 0
>>>
>>> henry.get_account_balance_saving('0000')
None
>>>
>>>
>>> henry.create_account(100,300,'0000-0000-0000-0000')
>>> print(henry)
Name: Henry
Gender: Male
Email: HenryJJ@yo.com
Birthday: 1990-07-23
Phone: 111-111-3344
Accounts: 1
Account Number : XXXX-XXXX-XXXX-0000
>>> henry.get_account_balance_saving('0000')
100
>>> henry.get_account_balance_checking('0000')
300