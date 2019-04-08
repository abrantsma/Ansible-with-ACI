import acitoolkit.acitoolkit as aci
import acitoolkit.aciphysobject as aciphys
import csv
import getpass
import sys



def main():
    """
    Main execution routine
    :return: None
    """

    # Login to APIC
    session = aci.Session("http://apic-amslab.cisco.com", "admin", "C1sco123")
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    if resp.ok:
        print("\nApic login successful")

    intDown = []
    intNames = []
    interfaces = aci.Interface.get(session)
    for interface in interfaces:
        if interface.attributes['operSt'] == 'down':
            intDown.append(interface.attributes['operSt'])
            intNames.append(interface.attributes['if_name'])


    l3outNames = []
    l3outs = aci.L3ExtDomain.get(robvand)

    print('\nThere are {} ports available'.format(intDown.count('down')))

    template = "{0:25}"
    print(template.format("\nAVAILABLE INTERFACES"))
    print(template.format("---------"))
    for intName in intNames:
        print(template.format(intName))


if __name__ == '__main__':
    main()

