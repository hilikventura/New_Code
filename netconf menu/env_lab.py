# User Input

# Please select the lab environment that you will be using today
#     sandbox - Cisco DevNet Always-On / Reserved Sandboxes
#     express - Cisco DevNet Express Lab Backend
#     custom  - Your Own "Custom" Lab Backend
ENVIRONMENT_IN_USE = "sandbox"

# Custom Lab Backend
DNA_CENTER = {
    "host": "",
    "username": "",
    "password": ""
}

# End User Input


# Set the 'Environment Variables' based on the lab environment in use
if ENVIRONMENT_IN_USE == "sandbox":
    DNA_CENTER = {
        "host": "sandboxdnac.cisco.com",
        "username": "devnetuser",
        "password": "Cisco123!"
    }

    # Values for the Always On IOS XE Sandbox
    IOS_XE_1 = {
        "host": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

    # Values for the Reservable IOS XE Sandbox
    IOS_XE_2 = {
        "host": "10.10.20.48",
        "username": "developer",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

    # Values for the Always On NX-OS Sandbox
    NXOS_1 = {
        "host": "sbx-nxos-mgmt.cisco.com",
        "username": "admin",
        "password": "Admin_1234!",
        "netconf_port": 10000,
        "restconf_port": 443,
        "nxapi_port": 80,
        "ssh_port": 8181
    }

elif ENVIRONMENT_IN_USE == "express":
    DNA_CENTER = {
        "host": "sandboxdnac2.cisco.com",
        "port": 443,
        "username": "dnacdev",
        "password": "D3v93T@wK!"
    }

    NFVIS_SERVER = {
        "host": "198.18.134.46",
        "port": 443,
        "username": "admin",
        "password": "C1sco12345_"
    }

    # Values for the CSR1 from the dCloud Pod
    IOS_XE_1 = {
        "host": "198.18.134.11",
        "username": "admin",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

    # Values for the CSR2 from the dCloud Pod
    IOS_XE_2 = {
        "host": "198.18.134.12",
        "username": "admin",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

    # Values for the Always On NX-OS Sandbox
    NXOS_1 = {
        "host": "sbx-nxos-mgmt.cisco.com",
        "username": "admin",
        "password": "Admin_1234!",
        "netconf_port": 10000,
        "restconf_port": 443,
        "nxapi_port": 80,
        "ssh_port": 8181
    }
