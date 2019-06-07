# CSFE-Scripts
Mostly Web Scraping for information from CSFE.

## Basic Usage
### acctinfo 
Provides Name, Security question (also answer), Email, Hosting Plan, Account Creation Date
Usage: acctinfo ipg.testmhancockgaillard
```
mhancock-gaillard$ acctinfo ipw.testmmstech
Cookie has expired! Provide password.
Password: 
Successfully logged in!
Name: Marcus Hancock-Gaillard
Security Question: What was your dream job as a child? Programmer/Hacker
Email: marcus.hancock-gaillard@endurance.com
Hosting Plan: Managed VPS Optimum (VPS - Unix)
Account Creation: 06/04/2018
```

### billsnap
Provides the billing snapshot from CSFE for an account.
Usage: billsnap ipg.testmhancockgaillard
```
mhancock-gaillard$ billsnap ipw.testmmstech
Bill Date: 2018-07-31	Product: .space register - 1 year                Amount: $2.99     Status: $2.99
Bill Date: 2018-07-31	Product: Domain Privacy                          Amount: $9.99     Status: $9.99
Bill Date: 2019-07-16	Product: Domain Privacy - 1 Year                 Amount: $12.99    Status: $13.80
Bill Date: 2020-05-20	Product: Managed VPS Optimum                     Amount: $2039.76  Status: $2039.76
```

### domhistory
Provides the history of the domain's ownership.
Usage: domhistory markanthony36.com
```
mhancock-gaillard$ domhistory munix.tech
2018 04 Jun - ipw.testmmstech
```

### findip
Provides the IP address for the VPS/Dedi server for an account.
Usage: findip ipg.testtempeproserve
```
mhancock-gaillard$ findip ipw.testmmstech
VPS IP: 192.163.208.126```
	
tickets -
	Provides all tickets associated with an account.
	Usage: tickets ipg.testmhancockgaillard
	```mhancock-gaillard$ tickets ipw.testmmstech
************************************************************
RESOLVED : 06/21/2018 - 16585596 - this is a test *ignore*
************************************************************
RESOLVED : 06/21/2018 - 16585572 - EXAMPLE
```

### csfepass
Updates the encrypted pass file to check for valid password.
Usage: csfepass
*Asks for new password and saves it.*
```
mhancock-gaillard$ csfepass 
CSFE Password: 
Saved encrypted pass to ~/passwd/
```

### billinfo
Provides the billing information we have on file.
Usage: billinfo [domain/IP/username]
```
mhancock-gaillard$ billinfo ipw.testmmstech
Billing Address:
	10 Corporate Dr.
	Burlington, MA 01803
	USA
	41XXXXXXXXXX1111
Company Address:
	10 Corporate Dr.
	Burlington, MA 01803
	USA
```
	
### container_status
Provides the container status for unmanaged servers.
Usage: container_status [domain/IP/username]
```
mhancock-gaillard$ container_status spr.s******
<response><status>finished</status><content><![CDATA[ Container 'spr.s******' is running on 209.40.192.11 at Fri Jun  7 16:45:25 2019
Running processes:
USER	PID	%CPU	%MEM	VSZ	RSS	TTY	STAT	START	TIME	COMMAND
root	1	0.0	0.1	2172	668	?	Ss	May31	0:09	init [3]      
root	2	0.0	0.0	0	0	?	S	May31	0:00	[kthreadd/89415]
root	3	0.0	0.0	0	0	?	S	May31	0:00	[khelper/89415]
root	402	0.0	0.1	1828	588	?	Ss	May31	0:08	syslogd -m 0
root	405	0.0	0.0	1776	400	?	Ss	May31	0:00	klogd -x
dbus	441	0.0	0.1	2864	648	?	Ss	May31	0:00	dbus-daemon --system
root	463	0.0	0.2	7256	1040	?	Ss	May31	0:11	/usr/sbin/sshd
root	474	0.0	0.1	2848	880	?	Ss	May31	0:00	xinetd -stayalive -pidfile /var/run/xinetd.pid
root	510	0.0	0.2	2564	1164	?	S	May31	0:00	/bin/sh /usr/bin/mysqld_safe --datadir=/var/lib/mysql --socket=/var/lib/mysql/mysql.sock --pid-file=/var/run/mysqld/mysqld.pid --basedir=/usr --user=mysql
mysql	586	0.0	3.7	130536	18968	?	Sl	May31	3:28	/usr/libexec/mysqld --basedir=/usr --datadir=/var/lib/mysql --user=mysql --pid-file=/var/run/mysqld/mysqld.pid --skip-external-locking --log-error=/var/lib/mysql/stagevision.spry.com.err --socket=/var/lib/mysql/mysql.sock --port=3306
root	618	0.0	0.3	9408	1892	?	Ss	May31	0:17	sendmail: accepting connections
smmsp	626	0.0	0.2	8284	1496	?	Ss	May31	0:00	sendmail: Queue runner@01:00:00 for /var/spool/clientmqueue
root	636	0.0	1.6	24644	8456	?	Ss	May31	0:21	/usr/sbin/httpd
root	646	0.0	0.2	3344	1100	?	Ss	May31	0:01	crond
root	652	0.0	0.0	1760	468	?	Ss+	May31	0:00	/sbin/mingetty console
root	653	0.0	0.0	1760	472	tty2	Ss+	May31	0:00	/sbin/mingetty tty2
apache	23881	0.1	5.3	43624	27140	?	S	11:26	0:10	/usr/sbin/httpd
apache	24166	0.2	4.6	40284	23732	?	S	12:56	0:07	/usr/sbin/httpd
apache	24213	0.3	4.5	40452	23276	?	S	13:08	0:07	/usr/sbin/httpd
root	24434	0.0	0.1	2284	840	?	Rs	13:45	0:00	ps aux
Network connections:
PROTO	RECV_Q	SEND_Q	LOCAL_ADDR	REMOTE_ADDR	PID/PROGRAM	STATE
tcp	0	0	0.0.0.0:22	0.0.0.0:*	463/sshd            	LISTEN
tcp	0	0	127.0.0.1:25	0.0.0.0:*	618/sendmail        	LISTEN
tcp	0	0	0.0.0.0:3306	0.0.0.0:*	586/mysqld          	LISTEN
tcp	0	0	:::80	:::*	636/httpd           	LISTEN
tcp	0	0	:::22	:::*	463/sshd            	LISTENdf -h :
Filesystem            Size  Used Avail Use% Mounted on
/dev/simfs             19G  1.4G   18G   8% /

df -ih :
Filesystem            Inodes   IUsed   IFree IUse% Mounted on
/dev/simfs              2.2M     52K    2.2M    3% /

free -m :
             total       used       free     shared    buffers     cached
Mem:           500        189        310          0          0        125
-/+ buffers/cache:         63        436
Swap:            0          0          0

ifconfig :
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:4423 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4423 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:1830872 (1.7 MiB)  TX bytes:1830872 (1.7 MiB)

venet0    Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
          inet addr:127.0.0.1  P-t-P:127.0.0.1  Bcast:0.0.0.0  Mask:255.255.255.255
          UP BROADCAST POINTOPOINT RUNNING NOARP  MTU:1500  Metric:1
          RX packets:473370 errors:0 dropped:0 overruns:0 frame:0
          TX packets:539291 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:54162508 (51.6 MiB)  TX bytes:122916141 (117.2 MiB)

venet0:0  Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
          inet addr:ADDRESS  P-t-P:ADDRESS  Bcast:ADDRESS  Mask:ADDRESS
          UP BROADCAST POINTOPOINT RUNNING NOARP  MTU:1500  Metric:1


iptables -vnL :
Chain INPUT (policy ACCEPT 477K packets, 56M bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 543K packets, 125M bytes)
 pkts bytes target     prot opt in     out     source               destination         

bean counter :
       uid  resource                     held              maxheld              barrier                limit              failcnt
    89415:  kmemsize                 26165416             28897280            104506470            114957117                    0
            lockedpages                     0                 3066                 5102                 5102                    2
            privvmpages                 48413                67553               128000               131072                    0
            shmpages                       43                 1723                45445                45445                    0
            dummy                           0                    0  9223372036854775807  9223372036854775807                    0
            numproc                        28                   84                 2550                 2550                    0
            physpages                   57781                71935                    0  9223372036854775807                    0
            vmguarpages                     0                    0               131072  9223372036854775807                    0
            oomguarpages                19173                28786                75742  9223372036854775807                    0
            numtcpsock                      7                   16                 2550                 2550                    0
            numflock                        6                   10                 1000                 1100                    0
            numpty                          0                    0                  255                  255                    0
            numsiginfo                      0                   48                 1024                 1024                    0
            tcpsndbuf                  122080              1611680             24390690             34835490                    0
            tcprcvbuf                  114688               268544             24390690             34835490                    0
            othersockbuf                 6936               485648             12195345             22640145                    0
            dgramrcvbuf                     0                 4360             12195345             12195345                    0
            numothersock                   11                   32                 2550                 2550                    0
            dcachesize               23499564             23500800             22816310             23500800                    0
            numfile                       369                  665                40800                40800                    0
            dummy                           0                    0  9223372036854775807  9223372036854775807                    0
            dummy                           0                    0  9223372036854775807  9223372036854775807                    0
            dummy                           0                    0  9223372036854775807  9223372036854775807                    0
            numiptent                      27                   27                 1536                 1536                    0
 ]]></content></response>
 ```
	
### rpass
Generates a new root password for server.
Usage: rpass [domain/IP/username]
	
### getuser
Finds the username from IP address or domain name.
Usage: getuser [domain/IP/username]
```
mhancock-gaillard$ getuser munix.tech
Username: ipw.testmmstech
```
	
### createticket
Creates a Polaris ticket for customer's account and drops it in the VPS/Dedi pool.
Usage: createticket [username] [subject] [details]
