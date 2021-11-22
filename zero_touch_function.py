#!/usr/bin/env python3
#####################################################
# Developed by Diego Escobar Arevalillo
# version 1.0alpha Webinar ZeroTouch Check Point 2022
#####################################################

import requests
import sys
import shutil
import json
import getpass
import time
from simple_term_menu import TerminalMenu

login_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/login"
show_all_accounts_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-accounts"
show_all_gaia_versions_ids_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-gaia-versions-ids"
show_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-template"
show_gaia_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-gaia-template"
show_all_templates_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-templates"
show_all_gaia_templates_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-gaia-templates"
show_claimed_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-claimed-gateway"
show_gaia_claimed_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-gaia-claimed-gateway"
show_claimed_gateway_configuration_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-claimed-gateway-configuration"
show_gaia_claimed_gateway_configuration_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-gaia-claimed-gateway-configuration"
show_all_claimed_gateways_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-claimed-gateways"
show_all_gaia_claimed_gateways_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-all-gaia-claimed-gateways"
show_claimed_gateway_status_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-claimed-gateway-status"
show_gaia_claimed_gateway_status_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/show-gaia-claimed-gateway-status"
add_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/add-template"
add_gaia_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/add-gaia-template"
set_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/set-template"
set_gaia_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/set-gaia-template"
clone_gaia_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/clone-gaia-templates"
set_claimed_gateway_configuration_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/set-claimed-gateway-configuration"
set_gaia_claimed_gateway_configuration_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/set-gaia-claimed-gateway-configuration"
claim_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/claim-gateway"
claim_gaia_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/claim-gaia-gateway"
unclaim_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/unclaim-gateway"
unclaim_gaia_gateway_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/unclaim-gaia-gateway"
delete_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/delete-template"
delete_gaia_template_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/delete-gaia-template"
logout_url = "https://zerotouch.checkpoint.com/ZeroTouch/web_api/v2/logout"
sid = ""
status_code = None

def banner():
    print("##########################################################################################\n")
    print("##########################################################################################")
    print("               d8888888P                                                                  ")
    print("                    .d8'                                                                  ")
    print("                   .d8'   .d8888b. 88d888b. .d8888b.                                      ")
    print("                 .d8'     88ooood8 88'  `88 88'  `88                                      ")
    print("                d8'       88.  ... 88       88.  .88                                      ")
    print("                Y8888888P `88888P' dP       `88888P'                                      ")
    print("")
    print("               d888888P                            dP                                     ")
    print("                  88                               88                                     ")
    print("                  88    .d8888b. dP    dP .d8888b. 88d888b.                               ")
    print("                  88    88'  `88 88    88 88'      88'  `88                               ")
    print("                  88    88.  .88 88.  .88 88.      88    88                               ")
    print("                  dP    `88888P' `88888P' `88888P' dP    dP   V1.0alpha                   ")
    print("")
    print("                      Develop by Diego Escobar Arevalillo                                 ")
    print("                       Channel & Telco Security Engineer                                  ")    
    print("                             diegoe@checkpoint.com                                        ")
    print("##########################################################################################")

def login():
    banner()
    print("                                   LOGIN                                                  ")	
    print("Enter your UC Check Point Username: ")
    username = input()
    password = getpass.getpass("Enter your UC Check Point password : ")
    payload = {			
        "user": username,
        "password": password			
    }
    with requests.Session() as session:
        response = session.post(login_url, json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json;charset=UTF-8"
            })
    status_code = response.status_code
    print(response.json())
    if status_code == 200:   
        print("\n\nLogin Success::..STATUS 200 OK..::")
        responsejson = response.json()
        sid = responsejson["sid"]
        print("\nYour session ID TOKEN (sid) is ::.."+ sid +"..::")
        time.sleep(2)   
    elif status_code == 500:
        print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
        time.sleep(2)
    elif status_code == 400:
        print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
        time.sleep(2)
    elif status_code == 401:
        print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
        time.sleep(2)
    time.sleep(2)
    return sid, status_code;

def logout(status_code, sid):
    banner()
    print("                                  LOGOUT                                                  ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            with requests.Session() as session:
                response_logout = session.post(logout_url,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })                  
            status_code_logout = response_logout.status_code
            if status_code_logout == 200:   
                print("\n\nLogout Succeeded::..STATUS 200 OK..::")
                sid = ""
                time.sleep(2)  
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                    
    status_code = None
    return sid, status_code;

def show_all_accounts(status_code, sid):
    banner()
    print("                             SHOW ALL ACCOUNTS                                            ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            with requests.Session() as session:
                response_all_accounts = session.post(show_all_accounts_url,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            response_all_accounts_json = response_all_accounts.json()
            print(json.dumps(response_all_accounts_json, indent=4, sort_keys=True))
            all_accounts = json.dumps(response_all_accounts_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                List_of_all_accounts = "List_of_all_accounts.json"
                f = open(List_of_all_accounts, 'w' )
                f.write(str(all_accounts))
                f.close()
                print ("Congratulations you can take the file " + List_of_all_accounts + " from path \n")
                time.sleep(2)
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
        time.sleep(2)

def add_template(status_code,sid):
    banner()
    print("                                ADD TEMPLATE                                              ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Press [[I]] to import a json file or Press [[M]] to type manually : ")
            option = input()
            if option == 'I':
                print("\nEnter the path with the json name [/mnt/c/Python34/name_of_file.json] ")
                filename = input()
                f = open(filename)
                payload = json.load(f)
                with requests.Session() as session:
                    response = session.post(add_template_url, json=payload,
                        headers={
                            "Content-Type": "application/json;charset=UTF-8",
                            "X-chkp-sid": sid
                        })    
                status_add_template_code = response.status_code
                print(response.json())
                if status_add_template_code == 200:   
                    print("\n\nImported Template Successfully::..STATUS 200 OK..::")
                    time.sleep(2)   
                f.close()
            elif option == 'M':
                print("Enter the name of template ...:::REQUIRED:::...: ")
                nameoftemplate = input()
                print("Enter the time-zone \"GMT+01:00(Brussels/Copenhagen/Madrid/Paris)\"...:::REQUIRED:::...: ")
                timezone = input()
                print("Enter wireless-country \"ES\"...:::REQUIRED:::...: ")
                wirelesscountry = input()
                print("Enter the admin-password...:::REQUIRED:::...: ")
                adminpassword = input()
                print("Enter the account-id...:::REQUIRED:::...: ")
                accountid = input()
                print("Enter the admin-access 'Network and IP address from which an administrator can acces the gateway [empty string means any IP address]'...:::REQUIRED:::...:")
                adminaccess = input()                               
                print("Enter the limit-source-ip-mode[If admin-access is an empty string, use:\"LIMIT_SRC_IP_MODE.NO_LIMIT\", If admin-access is an IPv4 address, or a network and a subnet, use:\"LIMIT_SRC_IP_MODE.ALL_INTERFACES\"]...:::REQUIRED:::...: ")
                limitsourceipmode = input()
                print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]: ")
                underconstruction = input()
                print("Enter template-id [integer value ::..unique identifier..::]: ")                                
                templateid = input()
                print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
                userscript = input()
                print("Enter accept-lan [Administrator has access to the gateway from a LAN, if true ..::Default value: true::..]: ")
                acceptlan = input()
                print("Enter accept-wifi [Administrator has access to the gateway from a trusted WIFI, if true ..::Default value: true::..]: ")
                acceptwifi = input()                                
                print("Enter accept-vpn [Administrator has access to the gateway from a VPN, if true ..::Default value: true::..]: ")
                acceptvpn = input()                                
                print("Enter accept-lan [Administrator has access to the gateway from the Internet, if true ..::Default value: true::..]")
                acceptwan = input()                                
                print("Enter upload-info [If true, improves product experience by sending data to Check Point]: ")
                uploadinfo = input()
                print("Enter service-center [ IP address or the DNS of the SMP server]: ")
                servicecenter = input()
                print("Enter registration-key [Key obtained from the gateway page in the SMP server]: ")
                registrationkey = input()                                                                                                                                                                                                
                print("Enter ignore-cert-verification [If true, ignores certificate \(if your SMP has a certificate from a CA that is not known to the gateway\)..::Default value: false::..]: ")
                ignorecertverification = input()                                
                print("Enter use-cpn-tp-server [Use Check Point NTP servers False indicates not using them ..::Default value: true::..]: ")
                usecpntpserver = input()                                                                
                print("Enter auto-gateway-creation [ To automatically create the gateway in the SMP, set to true If true, these fields are required: plan, service-center, registration-key, portal If false, plan must be empty ..::Default value: false::..]: ")
                autogatewaycreation = input()                                                                
                print("Enter activate-rmd [If true, then the gateway uses \"Reach My Device\" to be accessible while using NAT \(Network Address Translation\) within an organization]: ")
                activatermd = input()                                                                
                print("Enter comments: ")
                comments = input()                                  
                print("Enter portal [Service domain name for the gateway To manage your gateway from SMP, fill these fields: service-center, registration-key, portal \(Used by the gateway for cloud activation\)]: ")
                portal = input()                                                                                                                                                                
                print("Enter plan [ Plan name from the SMP If you fill this field, these fields are required: auto-gateway-creation, service-center, registration-key and portal If auto-gateway-creation is false, plan must be empty]: ")
                plan = input()                                       
                payload = {			
                    "time-zone": timezone,
                    "account-id": accountid,
                    "template-id": templateid,
                    "user-script": userscript,
                    "accept-lan": acceptlan,
                    "accept-wifi": acceptwifi,
                    "accept-vpn": acceptvpn,
                    "accept-wan": acceptwan,
                    "upload-info": uploadinfo,
                    "service-center": servicecenter,
                    "registration-key": registrationkey,
                    "wireless-country": wirelesscountry,
                    "admin-password": adminpassword,
                    "admin-access": adminaccess,
                    "limit-source-ip-mode": limitsourceipmode,
                    "ignore-cert-verification": ignorecertverification,
                    "use-cpn-tp-server": usecpntpserver,
                    "auto-gateway-creation": autogatewaycreation,
                    "under-construction": underconstruction,
                    "activate-rmd": activatermd,
                    "name": nameoftemplate,
                    "comments": comments,
                    "portal": portal,
                    "plan": plan                                    
                }
                with requests.Session() as session:
                    response = session.post(add_template_url, json=payload,
                        headers={
                            "Content-Type": "application/json;charset=UTF-8",
                            "X-chkp-sid": sid
                        })    
                status_add_template_code = response.status_code
                print(response.json())
                if status_add_template_code == 200:   
                    print("\n\nManually Template Added Successfully::..STATUS 200 OK..::")
                    time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)
    time.sleep(2)

def show_template(status_code,sid):
    banner()
    print("                               SHOW TEMPLATE                                              ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter Template id: ")
            templateid = input()        
            print("Enter Account id: ")
            accountid = input()                                                                                                          
            payload = {			
                "account-id": accountid,
                "template-id": templateid
            }
            with requests.Session() as session:
                response = session.post(show_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_template_code = response.status_code
            response_show_template_json = response.json()
            print(json.dumps(response_show_template_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_template_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_template = "show_template.json"
                f = open(show_template, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_template + " from path \n")
                time.sleep(2)
            if status_show_template_code == 200:   
                print("\n\nShow Template Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def show_all_templates(status_code,sid):
    banner()
    print("                              SHOW ALL TEMPLATES                                          ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter Account ids: 'Example [8044839, 8044339, 8043339]': ")
            accountids = input()                                                                                                          
            payload = {			
                "account-id": [accountids]
            }
            with requests.Session() as session:
                response = session.post(show_all_templates_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_all_templates_code = response.status_code
            response_show_all_templates_json = response.json()
            print(json.dumps(response_show_all_templates_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_all_templates_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_all_template = "show_all_template.json"
                f = open(show_all_template, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_all_templates + " from path \n")
                time.sleep(2)
            if status_show_all_templates_code == 200:   
                print("\n\nShow All Templates Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)    
def show_claimed_gateway(status_code,sid):
    banner()
    print("                            SHOW CLAIMED GATEWAY                                          ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_claimed_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_claimed_gateway_code = response.status_code
            response_show_claimed_gateway_json = response.json()
            print(json.dumps(response_show_claimed_gateway_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_claimed_gateway_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_claimed_gateway = "show_claimed_gateway.json"
                f = open(show_claimed_gateway, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_claimed_gateway + " from path \n")
                time.sleep(2)
            if status_show_claimed_gateway_code == 200:   
                print("\n\nShow Claimed Gateway Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)                            

def show_claimed_gateway_configuration(status_code,sid):
    banner()
    print("                       SHOW CLAIMED GATEWAY CONFIGURATION                                 ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_claimed_gateway_configuration_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_claimed_gateway_configuration_code = response.status_code
            response_show_claimed_gateway_configuration_json = response.json()
            print(json.dumps(response_show_claimed_gateway_configuration_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_claimed_gateway_configuration_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_claimed_gateway_configuration = "show_claimed_gateway_configuration.json"
                f = open(show_claimed_gateway_configuration, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_claimed_gateway_configuration + " from path \n")
                time.sleep(2)
            if status_show_claimed_gateway_configuration_code == 200:   
                print("\n\nShow Claimed Gateway Configuration Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)  

def show_all_claimed_gateways(status_code,sid):
    banner()
    print("                          SHOW ALL CLAIMED GATEWAYS                                       ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:     
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_all_claimed_gateways_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_all_claimed_gateways_code = response.status_code
            response_show_all_claimed_gateways_json = response.json()
            print(json.dumps(response_show_all_claimed_gateways_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_all_claimed_gateways_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_all_claimed_gateways = "show_all_claimed_gateways.json"
                f = open(show_all_claimed_gateways, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_all_claimed_gateways + " from path \n")
                time.sleep(2)
            if status_show_all_claimed_gateways_code == 200:   
                print("\n\nShow All Claimed Gateways Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)      

def show_claimed_gateway_status(status_code,sid):
    banner()
    print("                         SHOW CLAIMED GATEWAY STATUS                                      ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_claimed_gateway_status_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_claimed_gateway_status_code = response.status_code
            response_show_claimed_gateway_status_json = response.json()
            print(json.dumps(response_show_claimed_gateway_status_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_claimed_gateway_status_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_claimed_gateway_status = "show_claimed_gateway_status.json"
                f = open(show_claimed_gateway_status, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_claimed_gateway_status + " from path \n")
                time.sleep(2)
            if status_show_claimed_gateway_status_code == 200:   
                print("\n\nShow Claimed Gateway Status Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)  

def show_options_quantum_spark(status_code, sid,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu):
    banner()
    print("                               SHOW OPTIONS                                               ")
    while not show_options_quamtum_spark_menu_back:
        show_options_quamtum_spark_sel = show_options_quamtum_spark_menu.show()
        if show_options_quamtum_spark_sel == 0:
            show_template(status_code,sid)
        elif show_options_quamtum_spark_sel == 1:
            show_all_templates(status_code,sid)
        elif show_options_quamtum_spark_sel == 2:
            show_claimed_gateway(status_code,sid)
        elif show_options_quamtum_spark_sel == 3:
            show_claimed_gateway_configuration(status_code,sid)
        elif show_options_quamtum_spark_sel == 4:
            show_all_claimed_gateways(status_code,sid)
        elif show_options_quamtum_spark_sel == 5:
            show_claimed_gateway_status(status_code,sid)
        elif show_options_quamtum_spark_sel == 6:
            show_options_quamtum_spark_menu_back = True
    show_options_quamtum_spark_menu_back = False
    time.sleep(5)

def set_template(status_code,sid):
    banner()
    print("                                SET TEMPLATE                                              ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the name of template ...:::REQUIRED:::...: ")
            nameoftemplate = input()
            print("Enter the time-zone \"GMT+01:00(Brussels/Copenhagen/Madrid/Paris)\"...:::REQUIRED:::...: ")
            timezone = input()
            print("Enter wireless-country \"ES\"...:::REQUIRED:::...: ")
            wirelesscountry = input()
            print("Enter the admin-password...:::REQUIRED:::...: ")
            adminpassword = input()
            print("Enter the account-id...:::REQUIRED:::...: ")
            accountid = input()
            print("Enter the admin-access 'Network and IP address from which an administrator can acces the gateway [empty string means any IP address]'...:::REQUIRED:::...:")
            adminaccess = input()                               
            print("Enter the limit-source-ip-mode[If admin-access is an empty string, use:\"LIMIT_SRC_IP_MODE.NO_LIMIT\", If admin-access is an IPv4 address, or a network and a subnet, use:\"LIMIT_SRC_IP_MODE.ALL_INTERFACES\"]...:::REQUIRED:::...: ")
            limitsourceipmode = input()
            print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]: ")
            underconstruction = input()
            print("Enter template-id [integer value ::..unique identifier..::]: ")                                
            templateid = input()
            print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
            userscript = input()
            print("Enter accept-lan [Administrator has access to the gateway from a LAN, if true ..::Default value: true::..]: ")
            acceptlan = input()
            print("Enter accept-wifi [Administrator has access to the gateway from a trusted WIFI, if true ..::Default value: true::..]: ")
            acceptwifi = input()                                
            print("Enter accept-vpn [Administrator has access to the gateway from a VPN, if true ..::Default value: true::..]: ")
            acceptvpn = input()                                
            print("Enter accept-lan [Administrator has access to the gateway from the Internet, if true ..::Default value: true::..]")
            acceptwan = input()                                
            print("Enter upload-info [If true, improves product experience by sending data to Check Point]: ")
            uploadinfo = input()
            print("Enter service-center [ IP address or the DNS of the SMP server]: ")
            servicecenter = input()
            print("Enter registration-key [Key obtained from the gateway page in the SMP server]: ")
            registrationkey = input()                                                                                                                                                                                                
            print("Enter ignore-cert-verification [If true, ignores certificate \(if your SMP has a certificate from a CA that is not known to the gateway\)..::Default value: false::..]: ")
            ignorecertverification = input()                                
            print("Enter use-cpn-tp-server [Use Check Point NTP servers False indicates not using them ..::Default value: true::..]: ")
            usecpntpserver = input()                                                                
            print("Enter auto-gateway-creation [ To automatically create the gateway in the SMP, set to true If true, these fields are required: plan, service-center, registration-key, portal If false, plan must be empty ..::Default value: false::..]: ")
            autogatewaycreation = input()                                                                
            print("Enter activate-rmd [If true, then the gateway uses \"Reach My Device\" to be accessible while using NAT \(Network Address Translation\) within an organization]: ")
            activatermd = input()                                                                
            print("Enter comments: ")
            comments = input()                                  
            print("Enter portal [Service domain name for the gateway To manage your gateway from SMP, fill these fields: service-center, registration-key, portal \(Used by the gateway for cloud activation\)]: ")
            portal = input()                                                                                                                                                                
            print("Enter plan [ Plan name from the SMP If you fill this field, these fields are required: auto-gateway-creation, service-center, registration-key and portal If auto-gateway-creation is false, plan must be empty]: ")
            plan = input()                                       
            payload = {			
                "time-zone": timezone,
                "account-id": accountid,
                "template-id": templateid,
                "user-script": userscript,
                "accept-lan": acceptlan,
                "accept-wifi": acceptwifi,
                "accept-vpn": acceptvpn,
                "accept-wan": acceptwan,
                "upload-info": uploadinfo,
                "service-center": servicecenter,
                "registration-key": registrationkey,
                "wireless-country": wirelesscountry,
                "admin-password": adminpassword,
                "admin-access": adminaccess,
                "limit-source-ip-mode": limitsourceipmode,
                "ignore-cert-verification": ignorecertverification,
                "use-cpn-tp-server": usecpntpserver,
                "auto-gateway-creation": autogatewaycreation,
                "under-construction": underconstruction,
                "activate-rmd": activatermd,
                "name": nameoftemplate,
                "comments": comments,
                "portal": portal,
                "plan": plan                                    
            }
            with requests.Session() as session:
                response = session.post(set_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_set_template_code = response.status_code
            print(response.json())
            time.sleep(2)
            if status_set_template_code == 200:   
                print("\n\nManually Template Setted Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                    
    time.sleep(2)


def set_claimed_gateway_configuration(status_code,sid):
    banner()
    print("                       SET CLAIMED GATEWAY CONFIGURATION                                  ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the account-id...:::REQUIRED:::...: ")
            accountid = input()
            print("Enter the mac...:::REQUIRED:::...: ")
            mac = input()
            print("Enter the time-zone \"GMT+01:00(Brussels/Copenhagen/Madrid/Paris)\": ")
            timezone = input()
            print("Enter the gateway's name: ")
            objetname = input()                                                                        
            print("Enter the creation date the gateway was calimed in milisecons: ")
            creationdate = input()                                    
            print("Enter template-id [integer value ::..unique identifier..::]: ")                                
            templateid = input()  
            print("Enter the name of template: ")
            templatename = input()                                  
            print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
            userscript = input()
            print("Enter accept-lan [Administrator has access to the gateway from a LAN, if true ..::Default value: true::..]: ")
            acceptlan = input()
            print("Enter accept-wifi [Administrator has access to the gateway from a trusted WIFI, if true ..::Default value: true::..]: ")
            acceptwifi = input()                                
            print("Enter accept-vpn [Administrator has access to the gateway from a VPN, if true ..::Default value: true::..]: ")
            acceptvpn = input()                                
            print("Enter accept-lan [Administrator has access to the gateway from the Internet, if true ..::Default value: true::..]")
            acceptwan = input()  
            print("Enter Link for \"Reach My Device\" Web Access: ")
            rmdweburl = input()
            print("Enter upload-info [If true, improves product experience by sending data to Check Point]: ")
            uploadinfo = input()     
            print("Enter the date the gateway was last modified in miliseconds: ")
            lastmodifydate = input() 
            print("Enter the user who claims a gateway: ")
            creatinguser = input() 
            print("Enter the user who last modified a gateway: ")
            lastmodifyinguser = input()                                     
            print("Enter service-center [ IP address or the DNS of the SMP server]: ")
            servicecenter = input()
            print("Enter registration-key [Key obtained from the gateway page in the SMP server]: ")
            registrationkey = input()                                                                                                        
            print("Enter wireless-country \"ES\": ")
            wirelesscountry = input()                                    
            print("Enter the admin-password: ")
            adminpassword = input()
            print("Enter the admin-access 'Network and IP address from which an administrator can acces the gateway [empty string means any IP address]':")
            adminaccess = input()                               
            print("Enter the limit-source-ip-mode[If admin-access is an empty string, use:\"LIMIT_SRC_IP_MODE.NO_LIMIT\", If admin-access is an IPv4 address, or a network and a subnet, use:\"LIMIT_SRC_IP_MODE.ALL_INTERFACES\"]: ")
            limitsourceipmode = input()
            print("Enter ignore-cert-verification [If true, ignores certificate \(if your SMP has a certificate from a CA that is not known to the gateway\)..::Default value: false::..]: ")
            ignorecertverification = input()  
            print("Enter use-cpn-tp-server [Use Check Point NTP servers False indicates not using them ..::Default value: true::..]: ")
            usecpntpserver = input()   
            print("Enter auto-gateway-creation [ To automatically create the gateway in the SMP, set to true If true, these fields are required: plan, service-center, registration-key, portal If false, plan must be empty ..::Default value: false::..]: ")
            autogatewaycreation = input()  
            print("Enter Link for \"Reach My Device\" SSH Access: ")
            rmdshellurl = input()
            print("Enter activate-rmd [If true, then the gateway uses \"Reach My Device\" to be accessible while using NAT \(Network Address Translation\) within an organization]: ")
            activatermd = input()
            print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]: ")
            underconstruction = input()                                                           
            print("Enter comments: ")
            comments = input()                                  
            print("Enter portal [Service domain name for the gateway To manage your gateway from SMP, fill these fields: service-center, registration-key, portal \(Used by the gateway for cloud activation\)]: ")
            portal = input()                                                                                                                                                                
            print("Enter plan [ Plan name from the SMP If you fill this field, these fields are required: auto-gateway-creation, service-center, registration-key and portal If auto-gateway-creation is false, plan must be empty]: ")
            plan = input()    
            print("Enter sku: ")
            sku = input()                                                                        
            payload = {			
                "time-zone": timezone,
                "object-name": objectname,
                "creation-date": creationdate,
                "account-id": accountid,
                "template-id": templateid,
                "template-name": templatename,
                "user-script": userscript,
                "accept-lan": acceptlan,
                "accept-wifi": acceptwifi,
                "accept-vpn": acceptvpn,
                "accept-wan": acceptwan,
                "rmd-web-url": rmdweburl,
                "upload-info": uploadinfo,
                "last-modify-date": lastmodifydate,
                "creating-user": creatinguser,
                "last-modifying-user": lastmodifyinguser,
                "service-center": servicecenter,
                "registration-key": registrationkey,
                "wireless-country": wirelesscountry,
                "admin-password": adminpassword,
                "admin-access": adminaccess,
                "limit-source-ip-mode": limitsourceipmode,
                "ignore-cert-verification": ignorecertverification,
                "use-cpn-tp-server": usecpntpserver,
                "auto-gateway-creation": autogatewaycreation,
                "rmd-shell-url": rmdshellurl,
                "activate-rmd": activatermd,
                "under-construction": underconstruction,
                "mac": mac,
                "comments": comments,
                "portal": portal,
                "plan": plan,
                "sku": sku
            }
            with requests.Session() as session:
                response = session.post(set_claimed_gateway_configuration_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_set_claimed_gateway_configuration_code = response.status_code
            print(response.json())
            if status_set_claimed_gateway_configuration_code == 200:   
                print("\n\nGateway Claimed modified Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)
    time.sleep(2)


def set_options(status_code, sid,set_menu_title,set_menu_items,set_menu_back,set_menu):
    banner()            
    print("                                SET OPTIONS                                               ")
    while not set_menu_back:
        set_sel = set_menu.show()
        if set_sel == 0:
            set_template(status_code,sid)
        elif set_sel == 1:
            set_claimed_gateway_configuration(status_code,sid)
        elif set_sel == 2:
            set_menu_back = True
    set_menu_back = False
    time.sleep(2)

def claim_gateway(status_code,sid):
    banner()
    print("                                CLAIM GATEWAY                                             ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the gateway's sname : ")
            objectname = input()
            print("\nEnter the account-id : ")
            accountid = input()               
            print("\nEnter the template-id : ")
            templateid = input()                
            print("\nEnter the mac [xx:xx:xx:7A:B3:4E] : ")
            mac = input()                                                           
            payload = {
                "object-name": objectname,
                "account-id": accountid,
                "template-id": templateid,
                "mac": mac                                		
            }
            with requests.Session() as session:
                response = session.post(claim_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_claim_gateway_code = response.status_code
            print(response.json())
            if status_claim_gateway_code == 200:   
                print("\n\nThe Gateway is claimed Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def delete_template(status_code,sid):
    banner()
    print("                                DELETE TEMPLATE                                           ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the template-id : ")
            templateid = input()
            print("\nEnter the account-id : ")
            accountid = input()                            
            payload = {			
                "template-id": templateid,
                "account-id": accountid			
            }
            with requests.Session() as session:
                response = session.post(delete_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_delete_template_code = response.status_code
            print(response.json())
            if status_delete_template_code == 200:   
                print("\n\nTemplate Deleted Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def unclaim_gateway(status_code,sid):
    banner()
    print("                              UNCLAIM GATEWAY                                             ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("\nEnter the mac [xx:xx:xx:7A:B3:4E] : ")
            mac = input()                                                           
            print("\nEnter the account-id : ")
            accountid = input()                            
            payload = {
                "mac": mac,            
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(unclaim_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_unclaim_gateway_code = response.status_code
            print(response.json())
            if status_unclaim_gateway_code == 200:   
                print("\n\nThe Gateway is unclaimed Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def api_command_for_quantum_spark(status_code, sid,quantum_menu_title,quantum_menu_items,quantum_menu_back,quantum_menu,set_menu_title,set_menu_items,set_menu_back,set_menu,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu):           
    banner()
    print("                      API COMMANDS FOR QUANTUM SPARK                                      ")      
    while not quantum_menu_back:
        quantum_sel = quantum_menu.show()
        if quantum_sel == 0:
            add_template(status_code,sid)
        elif quantum_sel == 1:
            show_options_quantum_spark(status_code, sid,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu)
        elif quantum_sel == 2:
            set_options(status_code, sid,set_menu_title,set_menu_items,set_menu_back,set_menu)
        elif quantum_sel == 3:
            claim_gateway(status_code,sid)
        elif quantum_sel == 4:
            delete_template(status_code,sid)
        elif quantum_sel == 5:
            unclaim_gateway(status_code,sid)
        elif quantum_sel == 6:
            quantum_menu_back = True              
    quantum_menu_back = False


def add_gaia_template(status_code, sid):
    banner()
    print("                              ADD GAIA TEMPLATE                                           ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Press [[I]] to import a json file or Press [[M]] to type manually : ")
            option = input()
            if option == 'I':
                print("\nEnter the path with the json name [/mnt/c/Python34/name_of_file.json] ")
                filename = input()
                f = open(filename)
                payload = json.load(f)
                with requests.Session() as session:
                    response = session.post(add_gaia_template_url, json=payload,
                        headers={
                            "Content-Type": "application/json;charset=UTF-8",
                            "X-chkp-sid": sid
                        })    
                status_add_gaia_template_code = response.status_code
                print(response.json())
                if status_add_gaia_template_code == 200:   
                    print("\n\nImported Template Successfully::..STATUS 200 OK..::")
                    time.sleep(2)   
                f.close()
            elif option == 'M':
                print("Enter the name of template ...:::REQUIRED:::...: ")
                name = input()
                print("Enter the account-id...:::REQUIRED:::...: ")
                accountid = input()                                
                print("Enter the admin-password...:::REQUIRED:::...: ")
                adminpassword = input()                                
                print("Enter the ftw-sic-key...:::REQUIRED:::...: ")
                ftwsickey = input()
                print("Enter the identification-key [This is configured on the gateway as a unique identifier to be recognized unambiguously by Zero Touch]...:::REQUIRED:::...: ")
                identificationkey = input()
                print("Enter the gaia-version-id ID number of Gaia version from...:::REQUIRED:::...: ")
                gaiaversionid = input()
                print("Enter the force-reimage [If true, this forces a re-image of the machine even if the selected Gaia image version is already installed]...:::REQUIRED:::...: ")
                forcereimage = input()
                print("Enter the cluster-member [If true, the gateway is a member of a cluster]...:::REQUIRED:::...: ")
                clustermember = input()
                print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]...:::REQUIRED:::...: ")
                underconstruction = input()
                print("Enter config-ipv6 [Must be true to set ipv6 configuration]:...:::REQUIRED:::... ")
                configipv6 = input()                                
                print("Enter upload-info [If true, improves product experience by sending data to Check Point]:...:::REQUIRED:::... ")
                uploadinfo = input()
                print("Enter download-info [If true, automatically downloads Blade Contracts and other important data (highly recommended)]:...:::REQUIRED:::... ")
                downloadinfo = input() 
                print("Enter the time-zone:...:::REQUIRED:::... ")
                timezone = input()                                                               
                print("Enter template-id [integer value ::..unique identifier..::]: ")                                
                templateid = input()
                print("Enter comments: ")
                comments = input()                                   
                print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
                userscript = input()
                print("Enter the primary DNS Server:")
                dnsserver1 = input()                               
                print("Enter the secondary DNS Server:")
                dnsserver2 = input()                                                               
                print("Enter the tertiary DNS Server:")
                dnsserver3 = input()                                                               
                print("Enter the primary network time protocol NTP:")
                ntp1 = input() 
                print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
                ntp1version = input()                                                                                                            
                print("Enter the secondary network time protocol NTP:")
                ntp2 = input()    
                print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
                ntp2version = input() 
                print("Enter The user who created the template:")
                creatinguser = input() 
                print("Enter The user who last modified the template:")
                lastmodifyinguser = input() 
                print("Enter the mgmt IP address if config-ipv6 is true:")
                mgmtethipaddressipv6 = input()                                 
                print("Enter the mgmt IP address if config-ipv4 is true:")
                mgmtethipaddressipv4 = input()                                  
                print("Enter the subnet mask if config-ipv4 is true:")
                mgmtethsubnetmaskipv4 = input()                                   
                print("Enter the subnet mask if config-ipv6 is true:")
                mgmtethmasklengthipv6 = input()   
                print("Enter the default gateway if config-ipv6 is true:")
                defaultgatewayipv6 = input()  
                print("Enter the default gateway if config-ipv4 is true:")
                defaultgatewayipv4 = input()                                                                   
                print("Enter the IP address of the proxy server:")
                proxyserver = input()     
                print("Enter the Proxy port number for client connections (8080 by default):")
                proxyport = input()   
                payload = {			
                    "name": name,
                    "time-zone": timezone,
                    "proxy-port": proxyport,
                    "account-id": accountid,
                    "template-id": templateid,
                    "comments": comments,
                    "user-script": userscript,
                    "upload-info": uploadinfo,
                    "ftw-sic-key": ftwsickey,
                    "dns-server1": dnsserver1,
                    "dns-server2": dnsserver2,
                    "dns-server3": dnsserver3,
                    "config-ipv6": configipv6,
                    "ntp1": ntp1,
                    "ntp2": ntp2,
                    "identification-key": identificationkey,
                    "creating-user": creatinguser,
                    "last-modifying-user": lastmodifyinguser,
                    "admin-password": adminpassword,
                    "mgmt-eth-ip-address-ipv6": mgmtethipaddressipv6,
                    "mgmt-eth-ip-address-ipv4": mgmtethipaddressipv4,
                    "gaia-version-id": gaiaversionid,
                    "download-info": downloadinfo,
                    "cluster-member": clustermember,
                    "mgmt-eth-subnet-mask-ipv4": mgmtethsubnetmaskipv4,
                    "mgmt-eth-mask-length-ipv6": mgmtethmasklengthipv6,
                    "default-gateway-ipv6": defaultgatewayipv6,
                    "under-construction": underconstruction,
                    "ntp1-version": ntp1version,
                    "ntp2-version": ntp2version,
                    "default-gateway-ipv4": defaultgatewayipv4,
                    "proxy-server": proxyserver,
                    "force-reimage": forcereimage                                                                 
                }
                with requests.Session() as session:
                    response = session.post(add_gaia_template_url, json=payload,
                        headers={
                            "Content-Type": "application/json;charset=UTF-8",
                            "X-chkp-sid": sid
                        })    
                status_add_gaia_template_code = response.status_code
                print(response.json())
                if status_add_gaia_template_code == 200:   
                    print("\n\nManually Template Added Successfully::..STATUS 200 OK..::")
                    time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)
    time.sleep(2)


def show_gaia_template(status_code,sid):
    banner()
    print("                              SHOW GAIA TEMPLATE                                          ")
    #print(status_code)
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter Template id: ")
            templateid = input()        
            print("Enter Account id: ")
            accountid = input()                                                                                                          
            payload = {			
                "account-id": accountid,
                "template-id": templateid
            }
            with requests.Session() as session:
                response = session.post(show_gaia_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_gaia_template_code = response.status_code
            response_show_gaia_template_json = response.json()
            print(json.dumps(response_show_gaia_template_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_gaia_template_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_gaia_template = "show_gaia_template.json"
                f = open(show_gaia_template, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_gaia_template + " from path \n")
                time.sleep(2)
            if status_show_gaia_template_code == 200:   
                print("\n\nShow GAIA Template Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def show_all_gaia_templates(status_code,sid):
    banner()
    print("                           SHOW ALL GAIA TEMPLATES                                        ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter Account ids: 'Example [8044839, 8044339, 8043339]': ")
            accountids = input()                                                                                                          
            payload = {			
                "account-id": [accountids]
            }
            with requests.Session() as session:
                response = session.post(show_all_gaia_templates_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_all_gaia_templates_code = response.status_code
            response_show_all_gaia_templates_json = response.json()
            print(json.dumps(response_show_all_gaia_templates_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_all_gaia_templates_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_all_template = "show_all_template.json"
                f = open(show_all_template, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_all_gaia_templates + " from path \n")
                time.sleep(2)
            if status_show_all_gaia_templates_code == 200:   
                print("\n\nShow All Templates Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def show_gaia_claimed_gateway(status_code,sid):
    banner()
    print("                             SHOW GAIA CLAIMED GATEWAY                                    ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_gaia_claimed_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_gaia_claimed_gateway_code = response.status_code
            response_show_gaia_claimed_gateway_json = response.json()
            print(json.dumps(response_show_gaia_claimed_gateway_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_gaia_claimed_gateway_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_gaia_claimed_gateway = "show_gaia_claimed_gateway.json"
                f = open(show_gaia_claimed_gateway, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_gaia_claimed_gateway + " from path \n")
                time.sleep(2)
            if status_show_gaia_claimed_gateway_code == 200:   
                print("\n\nShow Claimed Gateway Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)                            

def show_gaia_claimed_gateway_configuration(status_code,sid):
    banner()
    print("                    SHOW GAIA CLAIMED GATEWAY CONFIGURATION                               ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_gaia_claimed_gateway_configuration_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_gaia_claimed_gateway_configuration_code = response.status_code
            response_show_gaia_claimed_gateway_configuration_json = response.json()
            print(json.dumps(response_show_gaia_claimed_gateway_configuration_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_gaia_claimed_gateway_configuration_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_gaia_claimed_gateway_configuration = "show_gaia_claimed_gateway_configuration.json"
                f = open(show_gaia_claimed_gateway_configuration, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_gaia_claimed_gateway_configuration + " from path \n")
                time.sleep(2)
            if status_show_gaia_claimed_gateway_configuration_code == 200:   
                print("\n\nShow Claimed Gateway Configuration Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)  

def show_all_gaia_claimed_gateways(status_code,sid):
    banner()
    print("                          SHOW ALL GAIA CLAIMED GATEWAYS                                  ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:     
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_all_gaia_claimed_gateways_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_all_gaia_claimed_gateways_code = response.status_code
            response_show_all_gaia_claimed_gateways_json = response.json()
            print(json.dumps(response_show_all_gaia_claimed_gateways_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_all_gaia_claimed_gateways_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_all_gaia_claimed_gateways = "show_all_gaia_claimed_gateways.json"
                f = open(show_all_gaia_claimed_gateways, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_all_gaia_claimed_gateways + " from path \n")
                time.sleep(2)
            if status_show_all_gaia_claimed_gateways_code == 200:   
                print("\n\nShow All Claimed Gateways Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)  

def show_gaia_claimed_gateway_status(status_code,sid):
    banner()
    print("                       SHOW GAIA CLAIMED GATEWAY STATUS                                   ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter MAC: ")
            mac = input()       
            print("Enter Account id: ")
            accountid = input()                                                                                                                                                                                                                                                 
            payload = {			
                "mac": mac,
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(show_gaia_claimed_gateway_status_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_show_gaia_claimed_gateway_status_code = response.status_code
            response_show_gaia_claimed_gateway_status_json = response.json()
            print(json.dumps(response_show_gaia_claimed_gateway_status_json, indent=4, sort_keys=True))
            template = json.dumps(response_show_gaia_claimed_gateway_status_json, indent=4, sort_keys=True)
            time.sleep(2)
            print("Press [[C]] if you want to copy a file or [[Enter]] to continue : ")
            option = input()
            if option == 'C':
                show_gaia_claimed_gateway_status = "show_gaia_claimed_gateway_status.json"
                f = open(show_gaia_claimed_gateway_status, 'w' )
                f.write(str(template))
                f.close()
                print ("Congratulations you can take the file " + show_gaia_claimed_gateway_status + " from path \n")
                time.sleep(2)
            if status_show_gaia_claimed_gateway_status_code == 200:   
                print("\n\nShow Claimed Gateway Status Successfully::..STATUS 200 OK..::")
                time.sleep(2)                                            
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)  

def show_options_quantum(status_code, sid,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu):  
    banner()
    print("                               SHOW OPTIONS                                               ")
    #["Show Template", "Show All Templates", "Show Claimed Gateway", "Show Claimed Gateway Configuration", "Show All Claimed Gateways", "Show Claimed Gateway Status", "Back to Main Menu"]  
    while not show_options_quamtum_spark_menu_back:
        show_options_quamtum_spark_sel = show_options_quamtum_spark_menu.show()
        if show_options_quamtum_spark_sel == 0:
            show_gaia_template(status_code,sid)
        elif show_options_quamtum_spark_sel == 1:
            show_all_gaia_templates(status_code,sid)            
        elif show_options_quamtum_spark_sel == 2:
            show_gaia_claimed_gateway(status_code,sid)
        elif show_options_quamtum_spark_sel == 3:
            show_gaia_claimed_gateway_configuration(status_code,sid)
        elif show_options_quamtum_spark_sel == 4:
            show_all_gaia_claimed_gateways(status_code,sid)
        elif show_options_quamtum_spark_sel == 5:
            show_gaia_claimed_gateway_status(status_code,sid)
        elif show_options_quamtum_spark_sel == 6:
            show_options_quamtum_spark_menu_back = True
    show_options_quamtum_spark_menu_back = False
    time.sleep(5)

def set_gaia_template(status_code,sid):          
    banner()
    print("                              SET GAIA TEMPLATE                                           ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the name of template ...:::REQUIRED:::...: ")
            name = input()
            print("Enter the account-id...:::REQUIRED:::...: ")
            accountid = input()                                
            print("Enter the admin-password: ")
            adminpassword = input()                                
            print("Enter the ftw-sic-key.: ")
            ftwsickey = input()
            print("Enter the identification-key [This is configured on the gateway as a unique identifier to be recognized unambiguously by Zero Touch]: ")
            identificationkey = input()
            print("Enter the gaia-version-id ID number of Gaia version from: ")
            gaiaversionid = input()
            print("Enter the force-reimage [If true, this forces a re-image of the machine even if the selected Gaia image version is already installed]: ")
            forcereimage = input()
            print("Enter the cluster-member [If true, the gateway is a member of a cluster]: ")
            clustermember = input()
            print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]: ")
            underconstruction = input()
            print("Enter config-ipv6 [Must be true to set ipv6 configuration]: ")
            configipv6 = input()                                
            print("Enter upload-info [If true, improves product experience by sending data to Check Point]: ")
            uploadinfo = input()
            print("Enter download-info [If true, automatically downloads Blade Contracts and other important data (highly recommended)]: ")
            downloadinfo = input() 
            print("Enter the time-zone:")
            timezone = input()                                                               
            print("Enter template-id [integer value ::..unique identifier..::]: ")                                
            templateid = input()
            print("Enter comments: ")
            comments = input()                                   
            print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
            userscript = input()
            print("Enter the primary DNS Server:")
            dnsserver1 = input()                               
            print("Enter the secondary DNS Server:")
            dnsserver2 = input()                                                               
            print("Enter the tertiary DNS Server:")
            dnsserver3 = input()                                                               
            print("Enter the primary network time protocol NTP:")
            ntp1 = input() 
            print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
            ntp1version = input()                                                                                                            
            print("Enter the secondary network time protocol NTP:")
            ntp2 = input()    
            print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
            ntp2version = input() 
            print("Enter The user who created the template:")
            creatinguser = input() 
            print("Enter The user who last modified the template:")
            lastmodifyinguser = input() 
            print("Enter the mgmt IP address if config-ipv6 is true:")
            mgmtethipaddressipv6 = input()                                 
            print("Enter the mgmt IP address if config-ipv4 is true:")
            mgmtethipaddressipv4 = input()                                  
            print("Enter the subnet mask if config-ipv4 is true:")
            mgmtethsubnetmaskipv4 = input()                                   
            print("Enter the subnet mask if config-ipv6 is true:")
            mgmtethmasklengthipv6 = input()   
            print("Enter the default gateway if config-ipv6 is true:")
            defaultgatewayipv6 = input()  
            print("Enter the default gateway if config-ipv4 is true:")
            defaultgatewayipv4 = input()                                                                   
            print("Enter the IP address of the proxy server:")
            proxyserver = input()     
            print("Enter the Proxy port number for client connections (8080 by default):")
            proxyport = input()   
            payload = {			
                "name": name,
                "time-zone": timezone,
                "proxy-port": proxyport,
                "account-id": accountid,
                "template-id": templateid,
                "comments": comments,
                "user-script": userscript,
                "upload-info": uploadinfo,
                "ftw-sic-key": ftwsickey,
                "dns-server1": dnsserver1,
                "dns-server2": dnsserver2,
                "dns-server3": dnsserver3,
                "config-ipv6": configipv6,
                "ntp1": ntp1,
                "ntp2": ntp2,
                "identification-key": identificationkey,
                "creating-user": creatinguser,
                "last-modifying-user": lastmodifyinguser,
                "admin-password": adminpassword,
                "mgmt-eth-ip-address-ipv6": mgmtethipaddressipv6,
                "mgmt-eth-ip-address-ipv4": mgmtethipaddressipv4,
                "gaia-version-id": gaiaversionid,
                "download-info": downloadinfo,
                "cluster-member": clustermember,
                "mgmt-eth-subnet-mask-ipv4": mgmtethsubnetmaskipv4,
                "mgmt-eth-mask-length-ipv6": mgmtethmasklengthipv6,
                "default-gateway-ipv6": defaultgatewayipv6,
                "under-construction": underconstruction,
                "ntp1-version": ntp1version,
                "ntp2-version": ntp2version,
                "default-gateway-ipv4": defaultgatewayipv4,
                "proxy-server": proxyserver,
                "force-reimage": forcereimage                                                                 
            }
            with requests.Session() as session:
                response = session.post(set_gaia_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_set_gaia_template_code = response.status_code
            print(response.json())
            if status_set_gaia_template_code == 200:   
                print("\n\nManually Template Added Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                    
    time.sleep(2)

def set_gaia_claimed_gateway_configuration(status_code,sid):
    banner()
    print("                     SET GAIA CLAIMED GATEWAY CONFIGURATION                               ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the MAC ...:::REQUIRED:::...: ")
            mac = input()     
            print("Enter the account-id...:::REQUIRED:::...:")
            accountid = input()  
            print("Enter the gateway's name: ")
            objectname = input()                                                                                                        
            print("Enter template name [The name of the template used to claim this gateway]:")                                
            templatename = input() 
            print("Enter template-id [integer value ::..unique identifier..::]:")                                
            templateid = input()                                        
            print("Enter The IP address from which the Zero Touch server receives status reports sent by the gateway:")                                
            ipaddress = input()  
            print("Enter The IP address configured on the external interface of the gateway:")                                
            extinterfaceip = input()  
            print("Enter the SKU:")                                
            sku = input()                                      
            print("Enter the parameter is-locked[If true, the gateway is locked because of repeated invalid entries of identification-key]:")                                
            islocked = input() 
            print("Enter the Timestamp when the gateway last reported its status The value is the number of milliseconds:")                                
            reportedstatustime = input()     
            print("Enter the time-zone: ")
            timezone = input()  
            print("Enter comments: ")
            comments = input()      
            print(repr("Enter user-script [Example \"set static-route 192.0.2.100 nexthop gateway address 192.0.2.155 on\nset static-route 192.0.3.0/24 nexthop blackhole\n\" ]: "))
            userscript = input()                                                                      
            print("Enter upload-info [If true, improves product experience by sending data to Check Point]:")
            uploadinfo = input()
            print("Enter the ftw-sic-key:")
            ftwsickey = input()
            print("Enter the primary DNS Server:")
            dnsserver1 = input()                               
            print("Enter the secondary DNS Server:")
            dnsserver2 = input()                                                               
            print("Enter the tertiary DNS Server:")
            dnsserver3 = input() 
            print("Enter the primary network time protocol NTP:")
            ntp1 = input() 
            print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
            ntp1version = input()                                                                                                            
            print("Enter the secondary network time protocol NTP:")
            ntp2 = input()    
            print("Enter the NTP version [Most recent version of Check Point's NTP servers is the string value '4']:")
            ntp2version = input()    
            print("Enter the identification-key [This is configured on the gateway as a unique identifier to be recognized unambiguously by Zero Touch]: ")
            identificationkey = input()
            print("Enter The user who created the template:")
            creatinguser = input() 
            print("Enter The user who last modified the template:")
            lastmodifyinguser = input() 
            print("Enter the admin-password: ")
            adminpassword = input()  
            print("Enter config-ipv6 [Must be true to set ipv6 configuration]: ")
            configipv6 = input()                                      
            print("Enter the mgmt IP address if config-ipv6 is true:")
            mgmtethipaddressipv6 = input()  
            print("Enter the default gateway if config-ipv6 is true:")
            defaultgatewayipv6 = input()                                                                     
            print("Enter the subnet mask if config-ipv6 is true:")
            mgmtethmasklengthipv6 = input()                                     
            print("Enter the mgmt IP address if config-ipv4 is true:")
            mgmtethipaddressipv4 = input()                                  
            print("Enter the subnet mask if config-ipv4 is true:")
            mgmtethsubnetmaskipv4 = input()    
            print("Enter the default gateway if config-ipv4 is true:")
            defaultgatewayipv4 = input()
            print("Enter download-info [If true, automatically downloads Blade Contracts and other important data (highly recommended)]: ")
            downloadinfo = input() 
            print("Enter the cluster-member [If true, the gateway is a member of a cluster]: ")
            clustermember = input()
            print("Enter under-construction [A true value prevents downloads to the gateway until the final configuration and deployment decisions are complete::..Default value: false..::]: ")
            underconstruction = input()  
            print("Enter the IP address of the proxy server:")
            proxyserver = input()     
            print("Enter the Proxy port number for client connections (8080 by default):")
            proxyport = input()    
            print("Enter the gaia-version-id ID number of Gaia version from: ")
            gaiaversionid = input()
            print("Enter the force-reimage [If true, this forces a re-image of the machine even if the selected Gaia image version is already installed]: ")
            forcereimage = input()                                                                    
            payload = {			
                "object-name": objectname,
                "template-name": templatename,
                "mac": mac,
                "ip-address": ipaddress,
                "sku": sku,
                "is-locked": islocked,
                "reported-status-time": reportedstatustime,
                "ext-interface-ip": extinterfaceip,
                "time-zone": timezone,
                "proxy-port": proxyport,
                "account-id": accountid,
                "template-id": templateid,
                "comments": comments,
                "user-script": userscript,
                "upload-info": uploadinfo,
                "ftw-sic-key": ftwsickey,
                "dns-server1": dnsserver1,
                "dns-server2": dnsserver2,
                "dns-server3": dnsserver3,
                "config-ipv6": configipv6,
                "ntp1": ntp1,
                "ntp2": ntp2,
                "identification-key": identificationkey,
                "creating-user": creatinguser,
                "last-modifying-user": lastmodifyinguser,
                "admin-password": adminpassword,
                "mgmt-eth-ip-address-ipv6": mgmtethipaddressipv6,
                "mgmt-eth-ip-address-ipv4": mgmtethipaddressipv4,
                "gaia-version-id": gaiaversionid,
                "download-info": downloadinfo,
                "cluster-member": clustermember,
                "mgmt-eth-subnet-mask-ipv4": mgmtethsubnetmaskipv4,
                "mgmt-eth-mask-length-ipv6": mgmtethmasklengthipv6,
                "default-gateway-ipv6": defaultgatewayipv6,
                "under-construction": underconstruction,
                "ntp1-version": ntp1version,
                "ntp2-version": ntp2version,
                "default-gateway-ipv4": defaultgatewayipv4,
                "proxy-server": proxyserver,
                "force-reimage": forcereimage                                                               
            }
            with requests.Session() as session:
                response = session.post(set_gaia_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })    
            status_set_gaia_template_code = response.status_code
            print(response.json())
            if status_set_gaia_template_code == 200:   
                print("\n\nSetting Gaia Claimed Gateway Configuration Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)
    time.sleep(2)

def set_gaia_options(status_code, sid,set_menu_title,set_menu_items,set_menu_back,set_menu):
    banner()
    print("                                SET OPTIONS                                               ")
    #set_menu_items = ["Set Template", "Set Claimed Gateway Configuration", "Back to Main Menu"]    
    while not set_menu_back:
        set_sel = set_menu.show()
        if set_sel == 0:
            set_gaia_template(status_code,sid)
        elif set_sel == 1:
            set_gaia_claimed_gateway_configuration(status_code,sid)
        elif set_sel == 2:
            set_menu_back = True
    set_menu_back = False
    time.sleep(2)

def claim_gaia_gateway(status_code,sid):
    banner()
    print("                              CLAIM GAIA GATEWAY                                          ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the gateway's sname : ")
            objectname = input()
            print("\nEnter the account-id : ")
            accountid = input()               
            print("\nEnter the template-id : ")
            templateid = input()                
            print("\nEnter the mac [xx:xx:xx:7A:B3:4E] : ")
            mac = input()                                                           
            payload = {
                "object-name": objectname,
                "account-id": accountid,
                "template-id": templateid,
                "mac": mac                                		
            }
            with requests.Session() as session:
                response = session.post(claim_gaia_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_claim_gaia_gateway_code = response.status_code
            print(response.json())
            if status_claim_gaia_gateway_code == 200:   
                print("\n\nThe Gateway is claimed Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def delete_gaia_template(status_code,sid):    
    banner()
    print("                           DELETE GAIA TEMPLATE                                           ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("Enter the template-id : ")
            templateid = input()
            print("\nEnter the account-id : ")
            accountid = input()                            
            payload = {			
                "template-id": templateid,
                "account-id": accountid			
            }
            with requests.Session() as session:
                response = session.post(delete_gaia_template_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_delete_gaia_template_code = response.status_code
            print(response.json())
            if status_delete_gaia_template_code == 200:   
                print("\n\nTemplate Deleted Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def unclaim_gaia_gateway(status_code,sid):
    banner()
    print("                             UNCLAIM GAIA GATEWAY                                         ")
    try:
        status_code
    except NameError:
        print("\n\nYou need to do Login First")
        time.sleep(2)
    else:   
        if status_code == 200:
            print("\nEnter the mac [xx:xx:xx:7A:B3:4E] : ")
            mac = input()                                                           
            print("\nEnter the account-id : ")
            accountid = input()                            
            payload = {
                "mac": mac,            
                "account-id": accountid
            }
            with requests.Session() as session:
                response = session.post(unclaim_gaia_gateway_url, json=payload,
                    headers={
                        "Content-Type": "application/json;charset=UTF-8",
                        "X-chkp-sid": sid
                    })
            status_unclaim_gaia_gateway_code = response.status_code
            print(response.json())
            if status_unclaim_gaia_gateway_code == 200:   
                print("\n\nThe Gateway is unclaimed Successfully::..STATUS 200 OK..::")
                time.sleep(2)   
        elif status_code == 500:
            print("\n\nLogin Fail::..STATUS 500 Internal Server Error..::")
            time.sleep(2)
        elif status_code == 400:
            print("\n\nLogin Fail::..STATUS 400 Bad Request..::")
            time.sleep(2)
        elif status_code == 401:
            print("\n\nLogin Fail::..STATUS 401 Unauthorized..::")
            time.sleep(2)
        elif status_code is None:
            print("\n\nYou need to do Login First")
            time.sleep(2)                       
    time.sleep(2)

def api_command_for_quantum(status_code, sid,quantum_menu_title,quantum_menu_items,quantum_menu_back,quantum_menu,set_menu_title,set_menu_items,set_menu_back,set_menu,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu):           
    banner()
    print("                           API COMMANDS FOR QUANTUM                                       ")
    #quantum_menu_items = ["Add Template", "Show Options", "Set Options", "Claim Gateway", "Delete Template", "Unclaim Gateway", "Back to Main Menu"]            
    while not quantum_menu_back:
        quantum_sel = quantum_menu.show()
        if quantum_sel == 0:
            add_gaia_template(status_code, sid)
        elif quantum_sel == 1:
            show_options_quantum(status_code, sid,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu)
        elif quantum_sel == 2:
            set_gaia_options(status_code, sid,set_menu_title,set_menu_items,set_menu_back,set_menu)
        elif quantum_sel == 3:
            claim_gaia_gateway(status_code,sid)
        elif quantum_sel == 4:
            delete_gaia_template(status_code,sid)            
        elif quantum_sel == 5:
            unclaim_gaia_gateway(status_code,sid)
        elif quantum_sel == 6:
            quantum_menu_back = True              
    quantum_menu_back = False

def main():
    banner()
    print("                                   LOGIN                                                  ")
    main_menu_title = "##########################################################################################\n##########################################################################################\n               d8888888P                                                                  \n                    .d8'                                                                  \n                   .d8'   .d8888b. 88d888b. .d8888b.                                      \n                 .d8'     88ooood8 88'  `88 88'  `88                                      \n                d8'       88.  ... 88       88.  .88                                      \n                Y8888888P `88888P' dP       `88888P'                                      \n\n               d888888P                            dP                                     \n                  88                               88                                     \n                  88    .d8888b. dP    dP .d8888b. 88d888b.                               \n                  88    88'  `88 88    88 88'      88'  `88                               \n                  88    88.  .88 88.  .88 88.      88    88                               \n                  dP    `88888P' `88888P' `88888P' dP    dP   V1.0alpha                   \n\n                      Develop by Diego Escobar Arevalillo                                 \n                       Channel & Telco Security Engineer                                  \n                             diegoe@checkpoint.com                                        \n##########################################################################################\n##########################################################################################"
    main_menu_items = ["Login", "Show All Accounts", "API Commands for Quantum Spark", "API Commands for Quantum", "Logout", "Exit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_purple", "bold")
    main_menu_style = ("bg_purple", "fg_black")
    main_menu_exit = False
    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    quantum_menu_title = "##########################################################################################\n##########################################################################################\n               d8888888P                                                                  \n                    .d8'                                                                  \n                   .d8'   .d8888b. 88d888b. .d8888b.                                      \n                 .d8'     88ooood8 88'  `88 88'  `88                                      \n                d8'       88.  ... 88       88.  .88                                      \n                Y8888888P `88888P' dP       `88888P'                                      \n\n               d888888P                            dP                                     \n                  88                               88                                     \n                  88    .d8888b. dP    dP .d8888b. 88d888b.                               \n                  88    88'  `88 88    88 88'      88'  `88                               \n                  88    88.  .88 88.  .88 88.      88    88                               \n                  dP    `88888P' `88888P' `88888P' dP    dP   V1.0alpha                   \n\n                      Develop by Diego Escobar Arevalillo                                 \n                       Channel & Telco Security Engineer                                  \n                             diegoe@checkpoint.com                                        \n##########################################################################################\n##########################################################################################\n                      API COMMANDS FOR QUANTUM                                       "
    quantum_menu_items = ["Add Template", "Show Options", "Set Options", "Claim Gateway", "Delete Template", "Unclaim Gateway", "Back to Main Menu"]
    quantum_menu_back = False
    quantum_menu = TerminalMenu(
        quantum_menu_items,
        title=quantum_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )      
    set_menu_title = "##########################################################################################\n##########################################################################################\n               d8888888P                                                                  \n                    .d8'                                                                  \n                   .d8'   .d8888b. 88d888b. .d8888b.                                      \n                 .d8'     88ooood8 88'  `88 88'  `88                                      \n                d8'       88.  ... 88       88.  .88                                      \n                Y8888888P `88888P' dP       `88888P'                                      \n\n               d888888P                            dP                                     \n                  88                               88                                     \n                  88    .d8888b. dP    dP .d8888b. 88d888b.                               \n                  88    88'  `88 88    88 88'      88'  `88                               \n                  88    88.  .88 88.  .88 88.      88    88                               \n                  dP    `88888P' `88888P' `88888P' dP    dP   V1.0alpha                   \n\n                      Develop by Diego Escobar Arevalillo                                 \n                       Channel & Telco Security Engineer                                  \n                             diegoe@checkpoint.com                                        \n##########################################################################################\n##########################################################################################\n                                SET OPTIONS                                               "
    set_menu_items = ["Set Template", "Set Claimed Gateway Configuration", "Back to Main Menu"]
    set_menu_back = False
    set_menu = TerminalMenu(
        set_menu_items,
        title=set_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )   
    show_options_quamtum_spark_menu_title = "##########################################################################################\n##########################################################################################\n               d8888888P                                                                  \n                    .d8'                                                                  \n                   .d8'   .d8888b. 88d888b. .d8888b.                                      \n                 .d8'     88ooood8 88'  `88 88'  `88                                      \n                d8'       88.  ... 88       88.  .88                                      \n                Y8888888P `88888P' dP       `88888P'                                      \n\n               d888888P                            dP                                     \n                  88                               88                                     \n                  88    .d8888b. dP    dP .d8888b. 88d888b.                               \n                  88    88'  `88 88    88 88'      88'  `88                               \n                  88    88.  .88 88.  .88 88.      88    88                               \n                  dP    `88888P' `88888P' `88888P' dP    dP   V1.0alpha                   \n\n                      Develop by Diego Escobar Arevalillo                                 \n                       Channel & Telco Security Engineer                                  \n                             diegoe@checkpoint.com                                        \n##########################################################################################\n##########################################################################################\n                               SHOW OPTIONS                                               "
    show_options_quamtum_spark_menu_items = ["Show Template", "Show All Templates", "Show Claimed Gateway", "Show Claimed Gateway Configuration", "Show All Claimed Gateways", "Show Claimed Gateway Status", "Back to Main Menu"]
    show_options_quamtum_spark_menu_back = False
    show_options_quamtum_spark_menu = TerminalMenu(
        show_options_quamtum_spark_menu_items,
        title=show_options_quamtum_spark_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )          
    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:
            sid, status_code = login()      
        elif main_sel == 1:
            try:
                status_code
            except NameError:
                print("\n\nYou need to do Login First")
                time.sleep(2)
            else:             
                show_all_accounts(status_code,sid)
        elif main_sel == 2:
            try:
                status_code
            except NameError:
                print("\n\nYou need to do Login First")
                time.sleep(2)
            else:              
                api_command_for_quantum_spark(status_code, sid,quantum_menu_title,quantum_menu_items,quantum_menu_back,quantum_menu,set_menu_title,set_menu_items,set_menu_back,set_menu,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu)
        elif main_sel == 3:
            try:
                status_code
            except NameError:
                print("\n\nYou need to do Login First")
                time.sleep(2)
            else:              
                api_command_for_quantum(status_code, sid,quantum_menu_title,quantum_menu_items,quantum_menu_back,quantum_menu,set_menu_title,set_menu_items,set_menu_back,set_menu,show_options_quamtum_spark_menu_title,show_options_quamtum_spark_menu_items,show_options_quamtum_spark_menu_back,show_options_quamtum_spark_menu)
        elif main_sel == 4:
            try:
                status_code
            except NameError:
                print("\n\nYou need to do Login First")
                time.sleep(2)
            else:              
                sid, status_code = logout(status_code,sid)
        elif main_sel == 5:
            main_menu_exit = True
            print("Exit Selected")
if (__name__ == "__main__"):
    sys.exit(main())