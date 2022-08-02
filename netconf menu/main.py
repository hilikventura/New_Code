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


@web.route("/get")
def get_interfaces():
    netconf_filter = """
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
    </filter>"""

    netconf_reply = connect().get_config(source='running', filter=netconf_filter)

    netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    interfaces = netconf_data["interfaces"]["interface"]

    show = "<h1>The interface status of the device is: </h1> <ul>"
    for interface in interfaces:
        show += f'<li>Interface {interface["name"]} enabled status is {interface["enabled"]}</li>'
    show += "</ul>"
    return show


@web.route("/del/<num>")
def delInterface(num):
    new_loopback = {}
    new_loopback["name"] = "Loopback" + num

    netconf_data = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>{new_loopback["name"]}</name>
            </interface>
        </interfaces>
    </config>"""
    netconf_reply = connect().edit_config(netconf_data, target='running')

    show = f"<h1>The interface{num} was deleted</h1>" + get_interfaces()
    return show

@web.route('/add/<int:num>/<string:desc>/<string:ip>/<string:mask>')
def addInterface(num, desc="default", ip="10.10.10.10", mask="255.255.255.0"):
    IETF_INTERFACE_TYPES = {
        "loopback": "ianaift:softwareLoopback",
        "ethernet": "ianaift:ethernetCsmacd"
    }
    new_loopback = {}
    new_loopback["name"] = "Loopback" + str(num)
    new_loopback["desc"] = desc
    new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
    new_loopback["status"] = "true"
    new_loopback["ip_address"] = ip
    new_loopback["mask"] = mask
    # print(new_loopback)

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
    data=f"<h1>Interface Number {num} was created:</h1>"+get_interfaces()
    return data



@web.route("/")
def show_options():
    options = [(1, "Show Interface=get", get_interfaces), (2, "Add Interface=add", addInterface),
               (3, "Delete interface", delInterface)]
    show = "<h1>What would you like to do:</h1>"
    for option in options:
        show += f"<h2>({option[0]}) go to ---> {option[1]}</h2>"
    return show


if __name__ == "__main__":
    web.run(host="0.0.0.0", port=8080)
