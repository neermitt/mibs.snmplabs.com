#
# PySNMP MIB module H3C-DHCPRELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DHCPRELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Bits, ModuleIdentity, TimeTicks, Counter64, Gauge32, iso, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Bits", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "iso", "Unsigned32", "ObjectIdentity")
MacAddress, DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
h3cDhcpRelay = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58))
h3cDhcpRelay.setRevisions(('2005-06-08 00:00',))
if mibBuilder.loadTexts: h3cDhcpRelay.setLastUpdated('200506080000Z')
if mibBuilder.loadTexts: h3cDhcpRelay.setOrganization('Huawei 3Com Technologies Co.,Ltd. ')
h3cDHCPRMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1))
h3cDHCPRIfSelectTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 1), )
if mibBuilder.loadTexts: h3cDHCPRIfSelectTable.setStatus('current')
h3cDHCPRIfSelectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDHCPRIfSelectEntry.setStatus('current')
h3cDHCPRIfSelectRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRIfSelectRelayMode.setStatus('current')
h3cDHCPRIpToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2), )
if mibBuilder.loadTexts: h3cDHCPRIpToGroupTable.setStatus('current')
h3cDHCPRIpToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2, 1), ).setIndexNames((0, "H3C-DHCPRELAY-MIB", "h3cDHCPRIpToGroupGroupId"), (0, "H3C-DHCPRELAY-MIB", "h3cDHCPRIpToGroupServerIpType"), (0, "H3C-DHCPRELAY-MIB", "h3cDHCPRIpToGroupServerIp"))
if mibBuilder.loadTexts: h3cDHCPRIpToGroupEntry.setStatus('current')
h3cDHCPRIpToGroupGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19)))
if mibBuilder.loadTexts: h3cDHCPRIpToGroupGroupId.setStatus('current')
h3cDHCPRIpToGroupServerIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cDHCPRIpToGroupServerIpType.setStatus('current')
h3cDHCPRIpToGroupServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cDHCPRIpToGroupServerIp.setStatus('current')
h3cDHCPRIpToGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPRIpToGroupRowStatus.setStatus('current')
h3cDHCPRIfToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 3), )
if mibBuilder.loadTexts: h3cDHCPRIfToGroupTable.setStatus('current')
h3cDHCPRIfToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDHCPRIfToGroupEntry.setStatus('current')
h3cDHCPRIfToGroupGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRIfToGroupGroupId.setStatus('current')
h3cDHCPRIfToGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPRIfToGroupRowStatus.setStatus('current')
h3cDHCPRAddrCheckTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 4), )
if mibBuilder.loadTexts: h3cDHCPRAddrCheckTable.setStatus('current')
h3cDHCPRAddrCheckEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDHCPRAddrCheckEntry.setStatus('current')
h3cDHCPRAddrCheckSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRAddrCheckSwitch.setStatus('current')
h3cDHCPRSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5), )
if mibBuilder.loadTexts: h3cDHCPRSecurityTable.setStatus('current')
h3cDHCPRSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1), ).setIndexNames((0, "H3C-DHCPRELAY-MIB", "h3cDHCPRSecurityClientIpAddrType"), (0, "H3C-DHCPRELAY-MIB", "h3cDHCPRSecurityClientIpAddr"))
if mibBuilder.loadTexts: h3cDHCPRSecurityEntry.setStatus('current')
h3cDHCPRSecurityClientIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cDHCPRSecurityClientIpAddrType.setStatus('current')
h3cDHCPRSecurityClientIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cDHCPRSecurityClientIpAddr.setStatus('current')
h3cDHCPRSecurityClientMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRSecurityClientMacAddr.setStatus('current')
h3cDHCPRSecurityClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRSecurityClientProperty.setStatus('current')
h3cDHCPRSecurityClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPRSecurityClientRowStatus.setStatus('current')
h3cDHCPRStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6))
h3cDHCPRRxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRRxClientPktNum.setStatus('current')
h3cDHCPRTxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRTxClientPktNum.setStatus('current')
h3cDHCPRRxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRRxServerPktNum.setStatus('current')
h3cDHCPRTxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRTxServerPktNum.setStatus('current')
h3cDHCPRDiscoverPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRDiscoverPktNum.setStatus('current')
h3cDHCPRRequestPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRRequestPktNum.setStatus('current')
h3cDHCPRDeclinePktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRDeclinePktNum.setStatus('current')
h3cDHCPRReleasePktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRReleasePktNum.setStatus('current')
h3cDHCPRInformPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRInformPktNum.setStatus('current')
h3cDHCPROfferPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPROfferPktNum.setStatus('current')
h3cDHCPRAckPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRAckPktNum.setStatus('current')
h3cDHCPRNakPktNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPRNakPktNum.setStatus('current')
h3cDHCPRStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 6, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRStatisticsReset.setStatus('current')
h3cDHCPRCycleGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 7))
h3cDHCPRCycleStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPRCycleStatus.setStatus('current')
h3cDHCPRConfigOption82Group = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8))
h3cDHCPROption82Switch = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82Switch.setStatus('current')
h3cDHCPROption82HandleStrategy = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("keep", 2), ("replace", 3))).clone('replace')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82HandleStrategy.setStatus('current')
h3cDHCPRConfigOption82IfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3), )
if mibBuilder.loadTexts: h3cDHCPRConfigOption82IfTable.setStatus('current')
h3cDHCPRConfigOption82IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDHCPRConfigOption82IfEntry.setStatus('current')
h3cDHCPROption82IfSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82IfSwitch.setStatus('current')
h3cDHCPROption82IfStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("keep", 2), ("replace", 3))).clone('replace')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82IfStrategy.setStatus('current')
h3cDHCPROption82IfFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("verbose", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82IfFormat.setStatus('current')
h3cDHCPROption82IfNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("mac", 2), ("sysname", 3), ("userdefine", 4))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82IfNodeType.setStatus('current')
h3cDHCPROption82IfUsrDefString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 58, 1, 8, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPROption82IfUsrDefString.setStatus('current')
mibBuilder.exportSymbols("H3C-DHCPRELAY-MIB", h3cDHCPROfferPktNum=h3cDHCPROfferPktNum, h3cDHCPRSecurityTable=h3cDHCPRSecurityTable, h3cDHCPRDeclinePktNum=h3cDHCPRDeclinePktNum, h3cDHCPRIpToGroupRowStatus=h3cDHCPRIpToGroupRowStatus, h3cDHCPRAddrCheckEntry=h3cDHCPRAddrCheckEntry, h3cDHCPRNakPktNum=h3cDHCPRNakPktNum, h3cDHCPRIpToGroupGroupId=h3cDHCPRIpToGroupGroupId, h3cDHCPROption82IfSwitch=h3cDHCPROption82IfSwitch, h3cDHCPRIfToGroupTable=h3cDHCPRIfToGroupTable, h3cDHCPRIpToGroupServerIp=h3cDHCPRIpToGroupServerIp, h3cDHCPRIpToGroupServerIpType=h3cDHCPRIpToGroupServerIpType, h3cDHCPRDiscoverPktNum=h3cDHCPRDiscoverPktNum, h3cDHCPRSecurityClientProperty=h3cDHCPRSecurityClientProperty, h3cDHCPRIfSelectTable=h3cDHCPRIfSelectTable, h3cDHCPRCycleStatus=h3cDHCPRCycleStatus, h3cDHCPRSecurityClientRowStatus=h3cDHCPRSecurityClientRowStatus, h3cDHCPRTxServerPktNum=h3cDHCPRTxServerPktNum, h3cDhcpRelay=h3cDhcpRelay, h3cDHCPROption82IfStrategy=h3cDHCPROption82IfStrategy, h3cDHCPRConfigOption82Group=h3cDHCPRConfigOption82Group, h3cDHCPRMibObject=h3cDHCPRMibObject, h3cDHCPRSecurityClientIpAddr=h3cDHCPRSecurityClientIpAddr, h3cDHCPRRxClientPktNum=h3cDHCPRRxClientPktNum, h3cDHCPRConfigOption82IfTable=h3cDHCPRConfigOption82IfTable, h3cDHCPRIfSelectRelayMode=h3cDHCPRIfSelectRelayMode, PYSNMP_MODULE_ID=h3cDhcpRelay, h3cDHCPRCycleGroup=h3cDHCPRCycleGroup, h3cDHCPRTxClientPktNum=h3cDHCPRTxClientPktNum, h3cDHCPRAddrCheckTable=h3cDHCPRAddrCheckTable, h3cDHCPRIfToGroupRowStatus=h3cDHCPRIfToGroupRowStatus, h3cDHCPRAckPktNum=h3cDHCPRAckPktNum, h3cDHCPRRxServerPktNum=h3cDHCPRRxServerPktNum, h3cDHCPRIfToGroupEntry=h3cDHCPRIfToGroupEntry, h3cDHCPRSecurityClientMacAddr=h3cDHCPRSecurityClientMacAddr, h3cDHCPRIfSelectEntry=h3cDHCPRIfSelectEntry, h3cDHCPRRequestPktNum=h3cDHCPRRequestPktNum, h3cDHCPRIpToGroupEntry=h3cDHCPRIpToGroupEntry, h3cDHCPROption82IfFormat=h3cDHCPROption82IfFormat, h3cDHCPRStatisticsReset=h3cDHCPRStatisticsReset, h3cDHCPRIfToGroupGroupId=h3cDHCPRIfToGroupGroupId, h3cDHCPROption82HandleStrategy=h3cDHCPROption82HandleStrategy, h3cDHCPRSecurityEntry=h3cDHCPRSecurityEntry, h3cDHCPRReleasePktNum=h3cDHCPRReleasePktNum, h3cDHCPROption82Switch=h3cDHCPROption82Switch, h3cDHCPRAddrCheckSwitch=h3cDHCPRAddrCheckSwitch, h3cDHCPRInformPktNum=h3cDHCPRInformPktNum, h3cDHCPROption82IfNodeType=h3cDHCPROption82IfNodeType, h3cDHCPRIpToGroupTable=h3cDHCPRIpToGroupTable, h3cDHCPROption82IfUsrDefString=h3cDHCPROption82IfUsrDefString, h3cDHCPRConfigOption82IfEntry=h3cDHCPRConfigOption82IfEntry, h3cDHCPRStatisticsGroup=h3cDHCPRStatisticsGroup, h3cDHCPRSecurityClientIpAddrType=h3cDHCPRSecurityClientIpAddrType)