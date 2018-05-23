# CSFE-Scripts
Mostly Web Scraping for information from CSFE.

## Basic Usage
acctinfo -
	Provides Name, Security question (also answer), Email, Hosting Plan, Account Creation Date
	Usage: acctinfo ipg.testmhancockgaillard

billsnap -
	Provides the billing snapshot from CSFE for an account.
	Usage: billsnap ipg.testmhancockgaillard


domhistory -
	Provides the history of the domain's ownership.
	Usage: domhistory markanthony36.com

findip -
	Provides the IP address for the VPS/Dedi server for an account.
	Usage: findip ipg.testtempeproserve
	
tickets -
	Provides all tickets associated with an account.
	Usage: tickets ipg.testmhancockgaillard

csfepass -
	Updates the encrypted pass file to check for valid password.
	Usage: csfepass
		*Asks for new password and saves it.*
