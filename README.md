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

billinfo -
	Provides the billing information we have on file.
	Usage: billinfo [domain/IP/username]
	
container_status -
	Provides the container status for unmanaged servers.
	Usage: container_status [domain/IP/username]
	
rpass -
	Generates a new root password for server.
	Usage: rpass [domain/IP/username]
	
getuser -
	Finds the username from IP address or domain name.
	Usage: getuser [domain/IP/username]
	
createticket -
	Creates a Polaris ticket for customer's account and drops it in the VPS/Dedi pool.
	Usage: createticket [username] [subject] [details]
