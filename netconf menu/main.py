import env_lab  # noqa
from ncclient import manager
import xmltodict
import xml.dom.minidom
from flask import Flask
web = Flask(__name__)



def connect():
    return manager.connect(
            host=env_lab.IOS_XE_1["host"],
            port=env_lab.IOS_XE_1["netconf_port"],
            username=env_lab.IOS_XE_1["username"],
            password=env_lab.IOS_XE_1["password"],
            hostkey_verify=False
            )

def get_interfaces():
    netconf_filter = """
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
    </filter>"""

    netconf_reply = connect().get_config(source = 'running', filter = netconf_filter)

    netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    interfaces = netconf_data["interfaces"]["interface"]
    print()
    print("The interface status of the device is: ")
    for interface in interfaces:
        print(f'Interface {interface["name"]} enabled status is {interface["enabled"]}')

def delInterface():
    new_loopback = {}
    new_loopback["name"] = "Loopback" + input("What loopback number to delete? ")

    netconf_data = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>{new_loopback["name"]}</name>
            </interface>
        </interfaces>
    </config>"""
    netconf_reply = connect().edit_config(netconf_data, target = 'running')
    print("Here is the raw XML data returned from the device.\n")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    get_interfaces()

def addInterface():
    IETF_INTERFACE_TYPES = {
    "loopback": "ianaift:softwareLoopback",
    "ethernet": "ianaift:ethernetCsmacd"
    }
    new_loopback = {}
    new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
    new_loopback["desc"] = input("What description to use? ")
    new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
    new_loopback["status"] = "true"
    new_loopback["ip_address"] = input("What IP address? ")
    new_loopback["mask"] = input("What network mask? ")

    netconf_data = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{new_loopback["name"]}</name>
                <description>{new_loopback["desc"]}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    {new_loopback["type"]}
                </type>
                <enabled>{new_loopback["status"]}</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{new_loopback["ip_address"]}</ip>
                        <netmask>{new_loopback["mask"]}</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>"""

    netconf_reply = connect().edit_config(netconf_data, target = 'running')
    print("Here is the raw XML data returned from the device.\n")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    get_interfaces()
    
@web.route("/")
def show_options():
    options=[(1,"Show Interface=get",get_interfaces),(2,"Add Interface=add",addInterface),(3,"Delete interface",delInterface)]
    show="<h1>What would you like to do:</h1>"
    for option in options:
        show+=f"<h2>({option[0]}) go to ---> {option[1]}</h2>"
    return show

if __name__ == "__main__":

    web.run(host="0.0.0.0", port=8000)
