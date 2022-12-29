import ipaddress
import string

# - v4.9
# - securely switching winbox on and off
# - different size p2p and site mask

mt_id="100.64.254.123"

mt_p2p_port="1"
mt_p2p_vlan="705"
mt_p2p_ip_full="100.64.245.180/29"

mt_site_port="1"
mt_site_vlan="1103"
mt_site_ip_full="100.64.245.153/29"

mt_customer_port="2"
mt_customer_ip_full="206.53.184.108/30"
mt_customer_region="COH"
mt_customer_name="RAB"
mt_customer_speed="30M/30M"

mt_source="WM"

mt_tunnel_source_port="2"
mt_tunnel_target_port="4"
mt_tunnel_target_id="100.64.254.104"
mt_target_name="Victoria"

mt_wifi_port="1"
mt_2000_port="3"
mt_3000_port="1"

ex_stage_0=1            # - This stage does nothing
ex_dia=1                # - Direct Internet Access
ex_iplc=0               # - Direct Internet Access
ex_site=0               # - Site
ex_bw=1                 # - bluewave local loop
ex_btc=0                # - btc local loop
ex_one=0                # - onecom local loop
ex_quantum=0            # - quantum local loop
ex_speed=0              # - Set customer speed
ex_routerboard=1        # - Mikrotik type
ex_stage_1=1            # - Base configuartion
ex_stage_2=1            # - Adds naming to Mikrotik
ex_stage_3=1            # - IP addressing, Bridges and VLANS, L2
ex_tagged=1             # - Tagged or untagged VLANs
ex_v2000=0              # - PPPoE VLAN
ex_v3000=0              # - Mimosa C5 management
ex_stage_4=1            # - MPLS for VPLS
ex_tunnel=0             # - VPLS tunnels
ex_stage_5=1            # - BGP for Internet
ex_wifi=0               # - WiDirect
ex_bta=0                # - WiDirect BTA
ex_secure=1             # - Switch off WinBox
ex_upstream=1           # - Scripts for upstream and core routers

ex_print=0              # - Print variables

if ex_bw:
    ex_tbi=0
else:
    ex_tbi=1

if ex_routerboard:
    ex_cloudrouter=0
else:
    ex_cloudrouter=1

if ex_dia or ex_wifi or ex_bta or ex_stage_4:
    ex_mpls=1
else:
    ex_mpls=0

if ex_tbi or ex_btc or ex_one or ex_quantum:
    ex_wifi=0
    ex_bta=0
    ex_v2000=0
    ex_v3000=0
    ex_bw=0

mt_p2p_mask=mt_p2p_ip_full.split("/")[1]
mt_p2p_network_ip=str(ipaddress.ip_interface(mt_p2p_ip_full).network.network_address)
mt_p2p_network_ip_full=str(ipaddress.ip_interface(mt_p2p_ip_full).network)
mt_p2p_network_ip3=str(ipaddress.ip_network(mt_p2p_network_ip_full)[4])
mt_p2p_network_ip_full3=str(ipaddress.ip_interface(mt_p2p_network_ip3+"/"+mt_p2p_mask))
mt_p2p_network_ip5=str(ipaddress.ip_network(mt_p2p_network_ip_full)[1])
mt_p2p_network_ip_full5=mt_p2p_network_ip5+"/"+mt_p2p_mask

mt_site_mask=mt_site_ip_full.split("/")[1]
mt_site_network_ip=str(ipaddress.ip_interface(mt_site_ip_full).network.network_address)
mt_site_network_ip_full=str(ipaddress.ip_interface(mt_site_ip_full).network)
mt_site_network_ip3=str(ipaddress.ip_network(mt_site_network_ip_full)[4])
mt_site_network_ip_full3=str(ipaddress.ip_interface(mt_site_network_ip3+"/"+mt_site_mask))
mt_site_network_ip5=str(ipaddress.ip_network(mt_site_network_ip_full)[1])
mt_site_network_ip_full5=mt_site_network_ip5+"/"+mt_site_mask

mt_public_network_ip=str(ipaddress.ip_interface(mt_customer_ip_full).network.network_address)
mt_public_network_ip_full=str(ipaddress.ip_interface(mt_customer_ip_full).network)

mt_oct4=mt_id.split('.')[4-1]
mt_target_oct4=mt_tunnel_target_id.split('.')[4-1]

#Local loop 
n_port_1 = "ether1-BW" if ex_bw else "ether1-BTC" if ex_btc else "ether1-ONE" if ex_one else "ether1-QUANTUM" if ex_quantum else "ether1"
n_port_2 = "ether2-BW" if ex_bw else "ether2-BTC" if ex_btc else "ether2-ONE" if ex_one else "ether2-QUANTUM" if ex_quantum else "ether2"
n_port_3 = "ether3-BW" if ex_bw else "ether3-BTC" if ex_btc else "ether3-ONE" if ex_one else "ether3-QUANTUM" if ex_quantum else "ether3"
n_port_4 = "ether4-BW" if ex_bw else "ether4-BTC" if ex_btc else "ether4-ONE" if ex_one else "ether4-QUANTUM" if ex_quantum else "ether4"
n_port_5 = "ether5-BW" if ex_bw else "ether5-BTC" if ex_btc else "ether5-ONE" if ex_one else "ether5-QUANTUM" if ex_quantum else "ether5"
n_port_sfp = "etherSFP-BW" if ex_bw else "etherSFP-BTC" if ex_btc else "etherSFP-ONE" if ex_one else "etherSFP-QUANTUM" if ex_quantum else "sfp1"

#MTU 
n_mtu_1 = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""
n_mtu_2 = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""
n_mtu_3 = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""
n_mtu_4 = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""
n_mtu_5 = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""
n_mtu_sfp = "mtu=1600" if ex_bw else "mtu=1580" if ex_btc else "mtu=1580" if ex_one else "mtu=1580" if ex_quantum else ""

#Customer port
mt_port_name_1 = "ether1-Customer" if mt_customer_port =="1" else n_port_1 if mt_p2p_port == "1" else "ether1"
mt_port_name_2 = "ether2-Customer" if mt_customer_port =="2" else n_port_2 if mt_p2p_port == "2" else "ether2"
mt_port_name_3 = "ether3-Customer" if mt_customer_port =="3" else n_port_3 if mt_p2p_port == "3" else "ether3"
mt_port_name_4 = "ether4-Customer" if mt_customer_port =="4" else n_port_4 if mt_p2p_port == "4" else "ether4"
mt_port_name_5 = "ether5-Customer" if mt_customer_port =="5" else n_port_5 if mt_p2p_port == "5" else "ether5"
mt_port_name_sfp = "etherSFP-Customer" if mt_customer_port =="sfp" else n_port_sfp if mt_p2p_port == "sfp" else "sfp1"

#P2P
mt_p2p_local = "BW" if ex_bw else "BTC" if ex_btc else "ONE" if ex_one else "QUANTUM" if ex_quantum else ""

#Customer type
mt_customer_type = "BW" if ex_bw else "DIA" if ex_dia else "IPLC" if ex_iplc else ""

mt_public_range=str(ipaddress.ip_network(mt_public_network_ip_full)[2])+"-"+str(ipaddress.ip_network(mt_public_network_ip_full)[-2])

mt_p2p_upstream_port=mt_p2p_port

if ex_print:
    print ("\r")
    print ("ex_dia "+str(ex_dia))
    print ("ex_site "+str(ex_site))
    print ("ex_bw "+str(ex_bw))
    print ("ex_btc "+str(ex_btc))
    print ("ex_one "+str(ex_one))
    print ("ex_quantum "+str(ex_quantum))
    print ("ex_routerboard "+str(ex_routerboard))
    print ("ex_cloudrouter "+str(ex_cloudrouter))
    print ("ex_tagged "+str(ex_tagged))
    print ("ex_stage_0 "+str(ex_stage_0))
    print ("ex_stage_1 "+str(ex_stage_1))
    print ("ex_stage_2 "+str(ex_stage_2))
    print ("ex_stage_3 "+str(ex_stage_3))
    print ("ex_v2000 "+str(ex_v2000))
    print ("ex_v3000 "+str(ex_v3000))
    print ("ex_stage_4 "+str(ex_stage_4))
    print ("ex_tunnel "+str(ex_tunnel))
    print ("ex_stage_5 "+str(ex_stage_5))
    print ("ex_ex_wifi "+str(ex_wifi))
    print ("ex_bta "+str(ex_bta))
    print ("ex_secure "+str(ex_secure))
    print ("ex_upstream "+str(ex_upstream))
    print ("\r")
    print ("mt_p2p_mask "+mt_p2p_mask)
    print ("mt_p2p_port "+mt_p2p_port)
    print ("mt_p2p_upstream_port "+mt_p2p_upstream_port)
    print ("mt_p2p_vlan "+mt_p2p_vlan)
    print ("mt_p2p_ip_full "+mt_p2p_ip_full)
    print ("mt_p2p_network_ip "+mt_p2p_network_ip)
    print ("mt_p2p_network_ip_full "+mt_p2p_network_ip_full)
    print ("mt_p2p_network_ip3 "+mt_p2p_network_ip3)
    print ("mt_p2p_network_ip_full3 "+mt_p2p_network_ip_full3)
    print ("mt_p2p_network_ip5 "+mt_p2p_network_ip5)
    print ("mt_p2p_network_ip_full5 "+mt_p2p_network_ip_full5)
    print ("\r")
    print ("mt_site_mask "+mt_site_mask)
    print ("mt_site_port "+mt_site_port)
    print ("mt_site_vlan "+mt_site_vlan)
    print ("mt_site_ip_full "+mt_site_ip_full)
    print ("mt_site_network_ip "+mt_site_network_ip)
    print ("mt_site_network_ip_full "+mt_site_network_ip_full)
    print ("mt_site_network_ip3 "+mt_site_network_ip3)
    print ("mt_site_network_ip_full3 "+mt_site_network_ip_full3)
    print ("mt_site_network_ip5 "+mt_site_network_ip5)
    print ("mt_site_network_ip_full5 "+mt_site_network_ip_full5)
    print ("\r")
    print ("n_port_1 "+n_port_1)
    print ("n_port_2 "+n_port_2)
    print ("n_port_3 "+n_port_3)
    print ("n_port_4 "+n_port_4)
    print ("n_port_5 "+n_port_5)
    print ("n_port_sfp "+n_port_sfp)
    print ("\r")
    print ("mt_port_name_1 "+mt_port_name_1)
    print ("mt_port_name_2 "+mt_port_name_2)
    print ("mt_port_name_3 "+mt_port_name_3)
    print ("mt_port_name_4 "+mt_port_name_4)
    print ("mt_port_name_5 "+mt_port_name_5)
    print ("mt_port_name_sfp "+mt_port_name_sfp)
    print ("\r")
    print ("mt_p2p_local "+mt_p2p_local)
    print ("mt_customer_type "+mt_customer_type)
    print ("\r")

# /interface bridge
if ex_stage_3:
    if ex_v2000 or ex_v3000 or ex_wifi or ex_bta or ex_tunnel or ex_dia or ex_iplc or ex_bw:
        print ("\r")
        print ("/interface bridge")
    if ex_dia:
        print ("add name=Bridge-DIA protocol-mode=none")
    if ex_v2000:
        print ("add name=Bridge-VPLS-VLAN2000 protocol-mode=none")
    if ex_v3000:
        print ("add name=Bridge-VPLS-VLAN3000 protocol-mode=none")
    if ex_wifi:
        print ("add name=Bridge-Wifizone120 protocol-mode=none")
        print ("add name=Bridge-Wifizone130 protocol-mode=none")
    if ex_bta:
        print ("add name=Bridge-Wifizone140 protocol-mode=none")
    if ex_tunnel:
        print ("add name=Bridge-"+mt_target_name+"-"+mt_customer_name+" protocol-mode=none")
    if ex_iplc:
        print ("add name=Bridge-IPLC protocol-mode=none")
    print ("add name=lobridge")

# /interface ethernet - add name & comments ***
if ex_stage_1:
    print ("\r")
    print ("/interface ethernet")
    if ex_cloudrouter:
        print ("set [ find default-name=combo1 ] disabled=yes")
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=ether1 ] name="+mt_port_name_1)
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=ether2 ] name="+mt_port_name_2)
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=ether3 ] name="+mt_port_name_3)
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=ether4 ] name="+mt_port_name_4)
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=ether5 ] name="+mt_port_name_5)
    if ex_routerboard or ex_cloudrouter:
        print ("set [ find default-name=sfp1 ] name="+mt_port_name_sfp)
    if ex_cloudrouter:
        print ("set [ find default-name=ether6 ] name="+mt_port_6)
    if ex_cloudrouter:
        print ("set [ find default-name=ether7 ] name="+mt_port_7)
    if ex_cloudrouter:
        print ("set [ find default-name=sfp-sfpplus1 ] advertise=10M-full,100M-full,1000M-full disabled=yes")

# /interface vpls tunnel
if ex_stage_4:
    if ex_v2000 or ex_v3000 or ex_tunnel or ex_iplc:
        print ("\r")
        print ("/interface vpls")
    if ex_v2000:
        print ("add disabled=no l2mtu=1500 name=VPLS-Vlan2000-"+mt_oct4+"-1 remote-peer=100.64.254.1 vpls-id=200001:"+mt_oct4)
        print ("add disabled=no l2mtu=1500 name=VPLS-Vlan2000-"+mt_oct4+"-30 remote-peer=100.64.254.30 vpls-id=200030:"+mt_oct4)
    if ex_v3000:
        print ("add disabled=no l2mtu=1500 name=VPLS-Vlan3000-"+mt_oct4+"-1 remote-peer=100.64.254.1 vpls-id=300001:"+mt_oct4)
        print ("add disabled=no l2mtu=1500 name=VPLS-Vlan3000-"+mt_oct4+"-30 remote-peer=100.64.254.30 vpls-id=300030:"+mt_oct4)
    if ex_tunnel:
        print ("add disabled=no l2mtu=1500 name=VPLS-"+mt_target_name+"-"+mt_customer_name+" remote-peer="+mt_tunnel_target_id+" vpls-id="+mt_target_oct4+":"+mt_oct4)
    if ex_iplc:
        print ("add advertised-l2mtu=9178 cisco-style=yes cisco-style-id=3513 disabled=no l2mtu=9178 mtu=1530 name=VPLS-"+mt_customer_name+" remote-peer="+mt_tunnel_target_id)

# /interface vlan - ***work on bw vlan***
if ex_stage_3:
    if ex_bw or ex_wifi or ex_bta or ex_site or ex_v2000 or ex_v3000:
        print ("\r")
        print ("/interface vlan")
        if ex_bw:
            print ("add interface=ether"+mt_p2p_port+"-"+mt_p2p_local+" mtu=1560 name=Ether"+mt_p2p_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_source+" vlan-id="+mt_p2p_vlan)
        if ex_site:
            print ("add interface=ether"+mt_site_port+" name=Ether"+mt_site_port+"-Vlan"+mt_site_vlan+"-Site vlan-id="+mt_site_vlan)
        if ex_wifi:
            print ("add interface=ether"+mt_wifi_port+" name=Ether"+mt_wifi_port+"-Vlan2120-Wifizone vlan-id=2120")
            print ("add interface=ether"+mt_wifi_port+" name=Ether"+mt_wifi_port+"-Vlan2130-WifiDHCP vlan-id=2130")
        if ex_bta:
            print ("add interface=ether"+mt_wifi_port+" name=Ether"+mt_wifi_port+"-Vlan2140-WifiBTA vlan-id=2140")
        if ex_v2000 and ex_tagged:
            print ("add interface=ether"+mt_2000_port+" name=Ether"+mt_2000_port+"-Vlan2000-PPPoE vlan-id=2000")
        if ex_v3000:
            print ("add interface=ether"+mt_3000_port+" name=Ether"+mt_3000_port+"-Vlan3000-C5Manage vlan-id=3000")

# /ip pool
if ex_stage_3:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/ip pool")
    if ex_dia:
        print ("add name=dhcp_puplic ranges="+mt_public_range)
    if ex_wifi:
        print ("add name=wifi120pool ranges=10.120."+mt_oct4+".10-10.120."+mt_oct4+".250")
        print ("add name=wifi130pool ranges=10.130."+mt_oct4+".10-10.130."+mt_oct4+".250")
    if ex_bta:
        print ("add name=wifi140pool ranges=10.140."+mt_oct4+".10-10.140."+mt_oct4+".250")

# /ip dhcp-server
if ex_stage_3:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/ip dhcp-server")
    if ex_dia:
        print ("add address-pool=dhcp_puplic disabled=no interface=Bridge-DIA name=dhcp1")
    if ex_wifi:
        print ("add address-pool=wifi120pool disabled=no interface=Bridge-Wifizone120 name=wifi120dhcp")
        print ("add address-pool=wifi130pool disabled=no interface=Bridge-Wifizone130 name=wifi130dhcp")
    if ex_bta:
        print ("add address-pool=wifi140pool disabled=no interface=Bridge-Wifizone140 name=wifi140dhcp")

# /queue simple
if ex_stage_3:
    if ex_speed or ex_bw or ex_dia or ex_one or ex_quantum:
        print ("\r")
        print ("/queue simple")
        print ("add max-limit="+mt_customer_speed+" name="+mt_customer_name+" target=ether"+mt_customer_port)

# /routing bgp instance
if ex_stage_5:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/routing bgp instance")
    if ex_bw:
        print ("set default router-id="+mt_id)
    if ex_tbi:
        print ("set default as=65501 router-id="+mt_id)

# /routing ospf instance
if ex_stage_3:
    print ("\r")
    print ("/routing ospf instance")
    print ("set [ find default=yes ] router-id="+mt_id)

# /snmp community
if ex_stage_2:
    print ("\r")
    print ("/snmp community")
    print ("add addresses=100.64.0.0/16,172.31.0.0/16 name=bluewavesnmp")

# /interface bridge port
if ex_stage_3:
    if ex_dia or ex_wifi or ex_bta or ex_v2000 or ex_v3000 or ex_tunnel or ex_iplc:
        print ("\r")
        print ("/interface bridge port")
    if ex_dia:
        print ("add bridge=Bridge-DIA interface=ether"+mt_customer_port+"-Customer")
    if ex_wifi:
        print ("add bridge=Bridge-Wifizone130 interface=Ether"+mt_wifi_port+"-Vlan2130-WifiDHCP")
        print ("add bridge=Bridge-Wifizone120 interface=Ether"+mt_wifi_port+"-Vlan2120-Wifizone")
    if ex_bta:
        print ("add bridge=Bridge-Wifizone140 interface=Ether"+mt_wifi_port+"-Vlan2140-WifiBTA")
    if ex_v2000:
        if ex_tagged:
            print ("add bridge=Bridge-VPLS-VLAN2000 horizon=2000 interface=VPLS-Vlan2000-"+mt_oct4+"-1")
            print ("add bridge=Bridge-VPLS-VLAN2000 horizon=2000 interface=VPLS-Vlan2000-"+mt_oct4+"-30")
        else: 
            print ("add bridge=Bridge-VPLS-VLAN2000 interface=ether"+mt_2000_port)
    if ex_v3000:
        print ("add bridge=Bridge-VPLS-VLAN3000 horizon=3000 interface=VPLS-Vlan3000-"+mt_oct4+"-1")
        print ("add bridge=Bridge-VPLS-VLAN3000 horizon=3000 interface=VPLS-Vlan3000-"+mt_oct4+"-30")
    if ex_tunnel:
        print ("add bridge=Bridge-"+mt_target_name+"-"+mt_customer_name+" interface=VPLS-"+mt_target_name+"-"+mt_customer_name)
        print ("add bridge=Bridge-"+mt_target_name+"-"+mt_customer_name+" interface=ether"+mt_tunnel_source_port)
    if ex_iplc:
        print ("add bridge=Bridge-IPLC interface=VPLS-"+mt_customer_name)
        print ("add bridge=Bridge-IPLC interface=ether"+mt_customer_port+"-Customer")

# /ip neighbor discovery-settings
if ex_secure:
    print ("\r")
    print ("/ip neighbor discovery-settings")
    print ("set discover-interface-list=none")

# /ip address
if ex_stage_3:
    if ex_bw or ex_dia or ex_wifi or ex_bta or ex_site or ex_iplc:
        print ("\r")
        print ("/ip address")
        if ex_bw:
            print ("add address="+mt_p2p_network_ip_full3+" interface=ether"+mt_p2p_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_source+" network="+mt_p2p_network_ip)
        if ex_dia:
            print ("add address="+mt_customer_ip_full+" interface=Bridge-DIA network="+mt_public_network_ip)
        if ex_iplc:
            print ("add address="+mt_p2p_network_ip_full3+" interface=ether"+mt_p2p_port+"-"+mt_p2p_local+" network="+mt_p2p_network_ip)
        if ex_wifi:
            print ("add address=10.120."+mt_oct4+".1/24 interface=Bridge-Wifizone120 network=10.120."+mt_oct4+".0")
            print ("add address=10.130."+mt_oct4+".1/24 interface=Bridge-Wifizone130 network=10.130."+mt_oct4+".0")
        if ex_bta:
            print ("add address=10.140."+mt_oct4+".1/24 interface=Bridge-Wifizone140 network=10.140."+mt_oct4+".0")
        if ex_site:
            print ("add address="+mt_site_ip_full+" interface=ether"+mt_site_port+"-Vlan"+mt_site_vlan+"-Site network="+mt_site_network_ip)
        print ("add address="+mt_id+" interface=lobridge network="+mt_id)


# /ip dhcp-server network
if ex_stage_3:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/ip dhcp-server network")
    if ex_dia:
        print ("add address="+mt_public_network_ip_full+" dns-server=206.53.177.3,206.53.177.2 gateway="+str(ipaddress.ip_interface(mt_customer_ip_full).ip))
    if ex_wifi:
        print ("add address=10.120."+mt_oct4+".0/24 dns-server=8.8.8.8 domain=bluewave.bm gateway=10.120."+mt_oct4+".1")
        print ("add address=10.130."+mt_oct4+".0/24 dns-server=8.8.8.8 domain=bluewave.bm gateway=10.130."+mt_oct4+".1")
    if ex_bta:
        print ("add address=10.140."+mt_oct4+".0/24 dns-server=8.8.8.8 domain=bluewave.bm gateway=10.140."+mt_oct4+".1")

# /ip dns
if ex_stage_1:
    print ("\r")
    print ("/ip dns")
    print ("set servers=8.8.8.8")

# /ip sock
if ex_stage_1:
    print ("\r")
    print ("/ip sock")
    print ("set enabled=no")

# /ip upnp
if ex_stage_1:
    print ("\r")
    print ("/ip upnp")
    print ("set enabled=no")

# /ip proxy
if ex_stage_1:
    print ("\r")
    print ("/ip proxy")
    print ("set enabled=no")

# /ip route vrf
if ex_stage_3:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/ip route vrf")
    if ex_dia:
        print ("add export-route-targets=65501:16413 import-route-targets=65501:16413 interfaces=Bridge-DIA route-distinguisher=65501:1641392 routing-mark=INTERNET")
    if ex_wifi:
        print ("add export-route-targets=16413:120 import-route-targets=16413:120 interfaces=Bridge-Wifizone120 route-distinguisher=16413:120 routing-mark=WIFI120")
        print ("add export-route-targets=16413:130 import-route-targets=16413:130 interfaces=Bridge-Wifizone130 route-distinguisher=16413:130 routing-mark=WIFI130")
    if ex_bta:
        print ("add export-route-targets=16413:140 import-route-targets=16413:140 interfaces=Bridge-Wifizone140 route-distinguisher=16413:140 routing-mark=WIFI140")

# /ip service
if ex_stage_1:
    print ("\r")
    print ("/ip service")
    print ("set telnet address=100.64.0.0/16,172.31.0.0/16 disabled=yes")
    print ("set ftp address=100.64.0.0/16,172.31.0.0/16 disabled=yes")
    print ("set www address=100.64.0.0/16,172.31.0.0/16")
    print ("set ssh address=100.64.0.0/16,172.31.0.0/16")
    print ("set api address=100.64.0.0/16,172.31.0.0/16 disabled=yes")
    print ("set api-ssl address=100.64.0.0/16,172.31.0.0/16 disabled=yes")
    if ex_secure:
        print ("set winbox address=100.64.0.0/16,172.31.0.0/16 disabled=yes")
    
# /lcd
if ex_stage_1:
    if ex_cloudrouter:
        print ("\r")
        print ("/lcd")
        print ("set enabled=no time-interval=daily")

# /mpls interface
if ex_stage_4:
    if ex_mpls:
        print ("\r")
        print ("/mpls interface")
        print ("set [ find default=yes ] mpls-mtu=1530")

# /mpls ldp
if ex_stage_4:
    if ex_mpls:
        print ("\r")
        print ("/mpls ldp")
        print ("set enabled=yes lsr-id="+mt_id+" transport-address="+mt_id)

# /mpls ldp interface
if ex_stage_4:
    if ex_mpls:
        print ("\r")
        print ("/mpls ldp interface")
        if ex_bw:
            print ("add interface=Ether"+mt_p2p_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_source)
        if ex_btc or ex_one or ex_quantum:
            print ("add interface="+mt_port_name_1)

# /routing bgp instance vrf
if ex_stage_5:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/routing bgp instance vrf")
    if ex_dia:
        print ("add in-filter=BGP-IN out-filter=BGP-OUT redistribute-connected=yes routing-mark=INTERNET")
    if ex_wifi:
        print ("add redistribute-connected=yes routing-mark=WIFI120")
        print ("add redistribute-connected=yes routing-mark=WIFI130")
    if ex_bta:
        print ("add redistribute-connected=yes routing-mark=WIFI140")

# /routing bgp peer
if ex_stage_5:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/routing bgp peer")
        if ex_bw:
            print ("add address-families=ip,vpnv4 name=BW-BM-Site1-CR-1 remote-address=100.64.254.1 remote-as=65530 ttl=default update-source=lobridge")
            print ("add address-families=ip,vpnv4 name=BW-BM-TBI-CR-1 remote-address=100.64.254.30 remote-as=65530 ttl=default update-source=lobridge")
        if ex_tbi:
            print ("add address-families=ip,vpnv4 name=TBI-RR-1 remote-address=10.248.0.25 remote-as=65501 ttl=default update-source=lobridge")
            print ("add address-families=ip,vpnv4 name=TBI-RR-2 remote-address=10.248.0.26 remote-as=65501 ttl=default update-source=lobridge")

# /routing filter
if ex_stage_5:
    if ex_dia or ex_wifi or ex_bta:
        print ("\r")
        print ("/routing filter")
        print ("add action=discard chain=BGP-IN prefix-length=24-32 protocol=bgp")
        print ("add action=accept chain=BGP-IN protocol="+chr(34)+chr(34))
        if  ex_dia:
            print ("add action=accept chain=BGP-OUT prefix="+mt_public_network_ip_full)
        print ("add action=discard chain=BGP-OUT")

# /routing ospf network
if ex_stage_3:
    print ("\r")
    print ("/routing ospf network")
    print ("add area=backbone network="+mt_id+"/32")
    print ("add area=backbone network="+mt_p2p_network_ip_full)
    if ex_site:     
        print ("add area=backbone network="+mt_site_network_ip_full)

# /snmp
if ex_stage_2:
    print ("\r")
    print ("/snmp")
    print ("set contact=info@bluewave.bm enabled=yes location="+chr(34)+"BM;"+mt_customer_region+";"+mt_customer_name.upper()+chr(34)+" trap-community=bluewavesnmp")

# /system clock
if ex_stage_1:
    print ("\r")
    print ("/system clock")
    print ("set time-zone-autodetect=no time-zone-name=Atlantic/Bermuda")

# /system identity
if ex_stage_2:
    print ("\r")
    print ("/system identity")
    print ("set name=BW-BM-"+mt_customer_region+"-"+mt_customer_name.upper()+"-PE-1")

# /tool mac-server
if ex_secure:
    print ("\r")
    print ("/tool mac-server")
    print ("set allowed-interface-list=none")

# /tool mac-server mac-winbox
if ex_secure:
    print ("\r")
    print ("/tool mac-server mac-winbox")
    print ("set allowed-interface-list=none")

# /tool mac-server ping
if ex_secure:
    print ("\r")
    print ("/tool mac-server ping")
    print ("set enabled=no")

# /tool romon
if ex_stage_1:
    print ("\r")
    print ("/tool romon")
    print ("set enabled=yes")

# /user backup
if ex_stage_1:
    print ("\r")
    print ("/user")
    print ("add name=backupuser password=kmnr742apfAR group=full\n")



# Tunnel Target router

if ex_tunnel:
    if ex_stage_3 or ex_tunnel:
        print ("\r")
        print ("\r")
        print ("Tunnel\r")
        print ("\r")

        print ("\r")
        print ("\r")
        print ("/interface bridge")
        print ("add name=Bridge-"+mt_target_name+"-"+mt_customer_name+" protocol-mode=none")

        print ("\r")
        print ("\r")
        print ("/interface vpls")
        print ("add disabled=no l2mtu=1500 name=VPLS-"+mt_target_name+"-"+mt_customer_name+" remote-peer="+mt_id+" vpls-id="+mt_target_oct4+":"+mt_oct4)

        print ("\r")
        print ("\r")
        print ("/interface bridge port")
        print ("add bridge=Bridge-"+mt_target_name+"-"+mt_customer_name+" interface=ether"+mt_tunnel_target_port)
        print ("add bridge=Bridge-"+mt_target_name+"-"+mt_customer_name+" interface=VPLS-"+mt_target_name+"-"+mt_customer_name)
           


# Upstream router

mt_network_ip=str(ipaddress.ip_interface(mt_p2p_ip_full).network.network_address)
mt_ospf_network_ip=str(ipaddress.ip_interface(mt_p2p_ip_full).network)

if ex_upstream:

    if ex_stage_3 or ex_stage_4:
        print ("\r")
        print ("\r")
        print ("Upstream Router\r")

        if ex_stage_3:
            print ("\r")
            print ("/interface vlan")
            print ("add interface=ether"+mt_p2p_upstream_port+" mtu=1560 name=Ether"+mt_p2p_upstream_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_customer_name+" vlan-id="+mt_p2p_vlan)

        if ex_stage_3:
            print ("\r")
            print ("/ip address")
            print ("add address="+mt_p2p_network_ip_full5+" interface=Ether"+mt_p2p_upstream_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_customer_name+" network="+mt_network_ip)

        if ex_stage_4:
            print ("\r")
            print ("/mpls ldp interface")
            print ("add interface=Ether"+mt_p2p_upstream_port+"-Vlan"+mt_p2p_vlan+"-P2P_"+mt_customer_name)

        if ex_stage_3:
            print ("\r")
            print ("/routing ospf network")
            print ("add area=backbone network="+mt_ospf_network_ip+"\n")


    # Site1 

    if ex_v2000 or ex_v3000 or ex_stage_5:
        print ("\r")
        print ("\r")
        print ("Site1\r")
        print ("\r")

        if ex_v2000 or ex_v3000:
            print ("\r")
            print ("/interface vpls")
            if ex_v2000:
                print ("add disabled=no l2mtu=1500 name=VPLS-Vlan2000-"+mt_oct4+"-1 remote-peer="+mt_id+" vpls-id=200001:"+mt_oct4)
            if ex_v3000:
                print ("add disabled=no l2mtu=1500 name=VPLS-Vlan3000-"+mt_oct4+"-1 remote-peer="+mt_id+" vpls-id=300001:"+mt_oct4)

        if ex_v2000 or ex_v3000:
            print ("\r")
            print ("/interface bridge port")
            if ex_v2000:
                print ("add bridge=VPLS-VLAN2000 horizon=2000 interface=VPLS-Vlan2000-"+mt_oct4+"-1")
            if ex_v3000:
                print ("add bridge=VPLS-VLAN3000 horizon=3000 interface=VPLS-Vlan3000-"+mt_oct4+"-1")

        if ex_stage_5:
            print ("\r")
            print ("/routing bgp peer")
            print ("add address-families=ip,vpnv4 name=BW-BM-"+mt_customer_region+"-"+mt_customer_name.upper()+"-PE-1 remote-address="+mt_id+" remote-as=65530 route-reflect=yes ttl=default update-source=loopback")

    # TBi

    if ex_v2000 or ex_v3000 or ex_stage_5:
        print ("\r")
        print ("\r")
        print ("TBi Script")
        print ("\r")
        if ex_v2000 or ex_v3000:
            print ("/interface vpls")
            if ex_v2000:
                print ("add disabled=no l2mtu=1500 name=VPLS-Vlan2000-"+mt_oct4+"-30 remote-peer="+mt_id+" vpls-id=200030:"+mt_oct4)
            if ex_v3000:
                print ("add disabled=no l2mtu=1500 name=VPLS-Vlan3000-"+mt_oct4+"-30 remote-peer="+mt_id+" vpls-id=300030:"+mt_oct4)

        print ("\r")
        if ex_v2000 or ex_v3000:
            print ("/interface bridge port")
            if ex_v2000:
                print ("add bridge=VPLS-VLAN2000 horizon=2000 interface=VPLS-Vlan2000-"+mt_oct4+"-30")
            if ex_v3000:
                print ("add bridge=VPLS-VLAN3000 horizon=3000 interface=VPLS-Vlan3000-"+mt_oct4+"-30")

        if ex_stage_5:
            print ("\r")
            print ("/routing bgp peer")
            print ("add address-families=ip,vpnv4 name=BW-BM-"+mt_customer_region+"-"+mt_customer_name.upper()+"-PE-1 remote-address="+mt_id+" remote-as=65530 route-reflect=yes ttl=default update-source=loopback")
            print ("\r")
            
