# PornSites-FirewallTest
List of known porn sites and python code to test local firewall rules against known porn websites.


#How to use this script

Download this repository:
```
git clone https://github.com/buggtoaster/PornSites-FirewallTest.git
```
Change directory to the downlaoded repository:
```
cd PornSite-FirewallTest
```
Execute the python script:
```
python3 ./porn.py 
```

Any porn sites that allow a connection will be output to a file named "porn.out".

Sites that are blocked by the firewall or other reason will be printed to the teminal.

All other sites in the list have failed due to DNS resolution issues.
