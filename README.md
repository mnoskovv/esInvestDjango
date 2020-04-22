# esInvestDjango

This is a demo of multiuser web application for a small investment company that specializes in hedging, consulting, brokerage and investment banking.

Main project requirements were: 
1. multiuser support: Registration and Authorization, Personal user account 
User must be able: 
- donate money via BTC or Interkassa and see his current balance (in progress)
- open deals created by admin
- to see actual Exchange Rates
- have an opportunity to reset password (in progress)
- opened deals must be closed in period given by deal. User's balance must be updated after deal closed 

2. Top 5 recent deals must be displayed at the index page

3. Website must contain calculators of profit of deals 

2. Administrators always alerted by email/telegram about new users and their activities.
Administrator page allows to add/modify deals, users etc.


At first solution was implemented on wordpress and rewritten on Django. 
Project design was given by client. 

The project is deployed on heroku and available [here](https://es-invest.herokuapp.com)

