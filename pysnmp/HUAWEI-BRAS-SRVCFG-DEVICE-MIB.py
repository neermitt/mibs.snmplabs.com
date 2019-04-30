#
# PySNMP MIB module HUAWEI-BRAS-SRVCFG-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-SRVCFG-DEVICE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
mplsVpnVrfName, = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, IpAddress, NotificationType, TimeTicks, ModuleIdentity, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "IpAddress", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity")
RowStatus, TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
hwBRASSrvcfgDevice = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6))
if mibBuilder.loadTexts: hwBRASSrvcfgDevice.setLastUpdated('200403041608Z')
if mibBuilder.loadTexts: hwBRASSrvcfgDevice.setOrganization('Huawei Technologies Co., Ltd. ')
hwSrvcfgDeviceMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1))
hwDeviceUserTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1), )
if mibBuilder.loadTexts: hwDeviceUserTable.setStatus('current')
hwDeviceUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddr"))
if mibBuilder.loadTexts: hwDeviceUserEntry.setStatus('current')
hwDeviceUserStartIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserStartIpAddr.setStatus('current')
hwDeviceUserEndIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserEndIpAddr.setStatus('current')
hwDeviceUserIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserIfIndex.setStatus('current')
hwDeviceUserIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserIfName.setStatus('current')
hwDeviceUserVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVlan.setStatus('current')
hwDeviceUserVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVpi.setStatus('current')
hwDeviceUserVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVci.setStatus('current')
hwDeviceUserMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 8), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserMac.setStatus('current')
hwDeviceUserDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserDomain.setStatus('current')
hwDeviceUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ready", 0), ("detecting", 1), ("deleting", 2), ("online", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserStatus.setStatus('current')
hwDeviceUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDeviceUserRowStatus.setStatus('current')
hwDeviceQinQUserVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceQinQUserVlan.setStatus('current')
hwDeviceUserTableV2 = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2), )
if mibBuilder.loadTexts: hwDeviceUserTableV2.setStatus('current')
hwDeviceUserEntryV2 = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVrfNameV2"), (0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddrV2"))
if mibBuilder.loadTexts: hwDeviceUserEntryV2.setStatus('current')
hwDeviceUserStartIpAddrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserStartIpAddrV2.setStatus('current')
hwDeviceUserEndIpAddrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserEndIpAddrV2.setStatus('current')
hwDeviceUserIfIndexV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserIfIndexV2.setStatus('current')
hwDeviceUserIfNameV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserIfNameV2.setStatus('current')
hwDeviceUserVlanV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVlanV2.setStatus('current')
hwDeviceUserVpiV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVpiV2.setStatus('current')
hwDeviceUserVciV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserVciV2.setStatus('current')
hwDeviceUserMacV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 8), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserMacV2.setStatus('current')
hwDeviceUserDomainV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceUserDomainV2.setStatus('current')
hwDeviceUserStatusV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ready", 0), ("detecting", 1), ("deleting", 2), ("online", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserStatusV2.setStatus('current')
hwDeviceUserRowStatusV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDeviceUserRowStatusV2.setStatus('current')
hwDeviceQinQUserVlanV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDeviceQinQUserVlanV2.setStatus('current')
hwDeviceUserVrfNameV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceUserVrfNameV2.setStatus('current')
hwSrvcfgDeviceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2))
hwSrvcfgDeviceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 1))
hwSrvcfgDeviceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 1, 1)).setObjects(("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserGroup"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserV2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvcfgDeviceCompliance = hwSrvcfgDeviceCompliance.setStatus('current')
hwDeviceUserGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2))
hwDeviceUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2, 1)).setObjects(("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddr"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserEndIpAddr"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfIndex"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfName"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVlan"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVpi"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVci"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserMac"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserDomain"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStatus"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserRowStatus"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceQinQUserVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceUserGroup = hwDeviceUserGroup.setStatus('current')
hwDeviceUserV2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2, 2)).setObjects(("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddrV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserEndIpAddrV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfIndexV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfNameV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVlanV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVpiV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVciV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserMacV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserDomainV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStatusV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserRowStatusV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceQinQUserVlanV2"), ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVrfNameV2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceUserV2Group = hwDeviceUserV2Group.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", hwDeviceUserRowStatus=hwDeviceUserRowStatus, hwDeviceUserVci=hwDeviceUserVci, hwDeviceUserMacV2=hwDeviceUserMacV2, hwDeviceUserStartIpAddr=hwDeviceUserStartIpAddr, hwSrvcfgDeviceConformance=hwSrvcfgDeviceConformance, hwDeviceUserRowStatusV2=hwDeviceUserRowStatusV2, hwDeviceUserEntryV2=hwDeviceUserEntryV2, hwSrvcfgDeviceMibObjects=hwSrvcfgDeviceMibObjects, hwDeviceUserMac=hwDeviceUserMac, hwDeviceUserIfNameV2=hwDeviceUserIfNameV2, hwDeviceUserVlanV2=hwDeviceUserVlanV2, hwDeviceUserVrfNameV2=hwDeviceUserVrfNameV2, hwDeviceUserVpiV2=hwDeviceUserVpiV2, hwDeviceUserVlan=hwDeviceUserVlan, hwDeviceUserTableV2=hwDeviceUserTableV2, hwDeviceUserEntry=hwDeviceUserEntry, hwDeviceUserEndIpAddr=hwDeviceUserEndIpAddr, hwDeviceUserIfIndex=hwDeviceUserIfIndex, hwDeviceQinQUserVlanV2=hwDeviceQinQUserVlanV2, hwDeviceQinQUserVlan=hwDeviceQinQUserVlan, hwDeviceUserIfName=hwDeviceUserIfName, hwDeviceUserIfIndexV2=hwDeviceUserIfIndexV2, hwSrvcfgDeviceCompliance=hwSrvcfgDeviceCompliance, hwDeviceUserV2Group=hwDeviceUserV2Group, hwDeviceUserTable=hwDeviceUserTable, hwSrvcfgDeviceCompliances=hwSrvcfgDeviceCompliances, hwDeviceUserEndIpAddrV2=hwDeviceUserEndIpAddrV2, hwDeviceUserDomain=hwDeviceUserDomain, hwBRASSrvcfgDevice=hwBRASSrvcfgDevice, hwDeviceUserGroup=hwDeviceUserGroup, hwDeviceUserStartIpAddrV2=hwDeviceUserStartIpAddrV2, hwDeviceUserStatus=hwDeviceUserStatus, hwDeviceUserVciV2=hwDeviceUserVciV2, hwDeviceUserGroups=hwDeviceUserGroups, hwDeviceUserVpi=hwDeviceUserVpi, hwDeviceUserStatusV2=hwDeviceUserStatusV2, hwDeviceUserDomainV2=hwDeviceUserDomainV2, PYSNMP_MODULE_ID=hwBRASSrvcfgDevice)