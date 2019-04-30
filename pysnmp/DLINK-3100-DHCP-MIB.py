#
# PySNMP MIB module DLINK-3100-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Counter32, Gauge32, MibIdentifier, ModuleIdentity, iso, Integer32, NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
rsDHCP = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38))
rsDHCP.setRevisions(('2003-10-18 00:00',))
if mibBuilder.loadTexts: rsDHCP.setLastUpdated('200310180000Z')
if mibBuilder.loadTexts: rsDHCP.setOrganization('Dlink, Inc.')
rsDhcpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDhcpMibVersion.setStatus('current')
rlDhcpRelayEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayEnable.setStatus('current')
rlDhcpRelayExists = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 26), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayExists.setStatus('current')
rlDhcpRelayNextServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 27), )
if mibBuilder.loadTexts: rlDhcpRelayNextServerTable.setStatus('current')
rlDhcpRelayNextServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 27, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpRelayNextServerIpAddr"))
if mibBuilder.loadTexts: rlDhcpRelayNextServerEntry.setStatus('current')
rlDhcpRelayNextServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 27, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayNextServerIpAddr.setStatus('current')
rlDhcpRelayNextServerSecThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 27, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayNextServerSecThreshold.setStatus('current')
rlDhcpRelayNextServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 27, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayNextServerRowStatus.setStatus('current')
rlDhcpRelayInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 28), )
if mibBuilder.loadTexts: rlDhcpRelayInterfaceTable.setStatus('current')
rlDhcpRelayInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 28, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpRelayInterfaceIfindex"))
if mibBuilder.loadTexts: rlDhcpRelayInterfaceEntry.setStatus('current')
rlDhcpRelayInterfaceIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 28, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceIfindex.setStatus('current')
rlDhcpRelayInterfaceUseGiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 28, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceUseGiaddr.setStatus('current')
rlDhcpRelayInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 28, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceRowStatus.setStatus('current')
rlDhcpRelayInterfaceListTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29), )
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListTable.setStatus('current')
rlDhcpRelayInterfaceListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpRelayInterfaceListIndex"))
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListEntry.setStatus('current')
rlDhcpRelayInterfaceListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListIndex.setStatus('current')
rlDhcpRelayInterfaceListPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListPortList.setStatus('current')
rlDhcpRelayInterfaceListVlanId1To1024 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId1To1024.setStatus('current')
rlDhcpRelayInterfaceListVlanId1025To2048 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId1025To2048.setStatus('current')
rlDhcpRelayInterfaceListVlanId2049To3072 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId2049To3072.setStatus('current')
rlDhcpRelayInterfaceListVlanId3073To4094 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 29, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpRelayInterfaceListVlanId3073To4094.setStatus('current')
rlDhcpSrvEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 30), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvEnable.setStatus('current')
rlDhcpSrvExists = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 31), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvExists.setStatus('current')
rlDhcpSrvDbLocation = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nvram", 1), ("flash", 2))).clone('flash')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDbLocation.setStatus('current')
rlDhcpSrvMaxNumOfClients = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvMaxNumOfClients.setStatus('current')
rlDhcpSrvDbNumOfActiveEntries = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 34), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDbNumOfActiveEntries.setStatus('current')
rlDhcpSrvDbErase = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 35), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDbErase.setStatus('current')
rlDhcpSrvProbeEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 36), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeEnable.setStatus('current')
rlDhcpSrvProbeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 37), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 10000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeTimeout.setStatus('current')
rlDhcpSrvProbeRetries = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 38), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvProbeRetries.setStatus('current')
rlDhcpSrvDefaultNetworkPoolName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 39), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDefaultNetworkPoolName.setStatus('current')
rlDhcpSrvIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45), )
if mibBuilder.loadTexts: rlDhcpSrvIpAddrTable.setStatus('current')
rlDhcpSrvIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpSrvIpAddrIpAddr"))
if mibBuilder.loadTexts: rlDhcpSrvIpAddrEntry.setStatus('current')
rlDhcpSrvIpAddrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIpAddr.setStatus('current')
rlDhcpSrvIpAddrIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIpNetMask.setStatus('current')
rlDhcpSrvIpAddrIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIdentifier.setStatus('current')
rlDhcpSrvIpAddrIdentifierType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physAddr", 1), ("clientId", 2))).clone('clientId')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrIdentifierType.setStatus('current')
rlDhcpSrvIpAddrClnHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrClnHostName.setStatus('current')
rlDhcpSrvIpAddrMechanism = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2), ("dynamic", 3))).clone('manual')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrMechanism.setStatus('current')
rlDhcpSrvIpAddrAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrAgeTime.setStatus('current')
rlDhcpSrvIpAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrPoolName.setStatus('current')
rlDhcpSrvIpAddrConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrConfParamsName.setStatus('current')
rlDhcpSrvIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 45, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvIpAddrRowStatus.setStatus('current')
rlDhcpSrvDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46), )
if mibBuilder.loadTexts: rlDhcpSrvDynamicTable.setStatus('current')
rlDhcpSrvDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpSrvDynamicPoolName"))
if mibBuilder.loadTexts: rlDhcpSrvDynamicEntry.setStatus('current')
rlDhcpSrvDynamicPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicPoolName.setStatus('current')
rlDhcpSrvDynamicIpAddrFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpAddrFrom.setStatus('current')
rlDhcpSrvDynamicIpAddrTo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpAddrTo.setStatus('current')
rlDhcpSrvDynamicIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicIpNetMask.setStatus('current')
rlDhcpSrvDynamicLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 5), Unsigned32().clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicLeaseTime.setStatus('current')
rlDhcpSrvDynamicProbeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicProbeEnable.setStatus('current')
rlDhcpSrvDynamicTotalNumOfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicTotalNumOfAddr.setStatus('current')
rlDhcpSrvDynamicFreeNumOfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpSrvDynamicFreeNumOfAddr.setStatus('current')
rlDhcpSrvDynamicConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicConfParamsName.setStatus('current')
rlDhcpSrvDynamicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 46, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvDynamicRowStatus.setStatus('current')
rlDhcpSrvConfParamsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47), )
if mibBuilder.loadTexts: rlDhcpSrvConfParamsTable.setStatus('current')
rlDhcpSrvConfParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1), ).setIndexNames((0, "DLINK-3100-DHCP-MIB", "rlDhcpSrvConfParamsName"))
if mibBuilder.loadTexts: rlDhcpSrvConfParamsEntry.setStatus('current')
rlDhcpSrvConfParamsName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsName.setStatus('current')
rlDhcpSrvConfParamsNextServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNextServerIp.setStatus('current')
rlDhcpSrvConfParamsNextServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNextServerName.setStatus('current')
rlDhcpSrvConfParamsBootfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsBootfileName.setStatus('current')
rlDhcpSrvConfParamsRoutersList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsRoutersList.setStatus('current')
rlDhcpSrvConfParamsTimeSrvList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsTimeSrvList.setStatus('current')
rlDhcpSrvConfParamsDnsList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsDnsList.setStatus('current')
rlDhcpSrvConfParamsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsDomainName.setStatus('current')
rlDhcpSrvConfParamsNetbiosNameList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNetbiosNameList.setStatus('current')
rlDhcpSrvConfParamsNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))).clone(namedValues=NamedValues(("b-node", 1), ("p-node", 2), ("m-node", 4), ("h-node", 8))).clone('h-node')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNetbiosNodeType.setStatus('current')
rlDhcpSrvConfParamsCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsCommunity.setStatus('obsolete')
rlDhcpSrvConfParamsNmsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsNmsIp.setStatus('obsolete')
rlDhcpSrvConfParamsOptionsList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsOptionsList.setStatus('current')
rlDhcpSrvConfParamsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 38, 47, 1, 14), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSrvConfParamsRowStatus.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-DHCP-MIB", rlDhcpSrvConfParamsNextServerName=rlDhcpSrvConfParamsNextServerName, rlDhcpRelayNextServerRowStatus=rlDhcpRelayNextServerRowStatus, rlDhcpSrvConfParamsRoutersList=rlDhcpSrvConfParamsRoutersList, rlDhcpRelayInterfaceListVlanId1To1024=rlDhcpRelayInterfaceListVlanId1To1024, rlDhcpRelayInterfaceListIndex=rlDhcpRelayInterfaceListIndex, rlDhcpSrvDefaultNetworkPoolName=rlDhcpSrvDefaultNetworkPoolName, rlDhcpSrvDynamicPoolName=rlDhcpSrvDynamicPoolName, rlDhcpSrvExists=rlDhcpSrvExists, rlDhcpSrvConfParamsName=rlDhcpSrvConfParamsName, rlDhcpSrvConfParamsRowStatus=rlDhcpSrvConfParamsRowStatus, rlDhcpSrvDynamicIpAddrFrom=rlDhcpSrvDynamicIpAddrFrom, rlDhcpSrvDynamicRowStatus=rlDhcpSrvDynamicRowStatus, rlDhcpRelayInterfaceListVlanId3073To4094=rlDhcpRelayInterfaceListVlanId3073To4094, rsDHCP=rsDHCP, rsDhcpMibVersion=rsDhcpMibVersion, rlDhcpRelayInterfaceEntry=rlDhcpRelayInterfaceEntry, rlDhcpRelayInterfaceTable=rlDhcpRelayInterfaceTable, rlDhcpSrvIpAddrTable=rlDhcpSrvIpAddrTable, rlDhcpSrvIpAddrIdentifierType=rlDhcpSrvIpAddrIdentifierType, rlDhcpRelayEnable=rlDhcpRelayEnable, rlDhcpSrvDynamicIpNetMask=rlDhcpSrvDynamicIpNetMask, rlDhcpSrvIpAddrConfParamsName=rlDhcpSrvIpAddrConfParamsName, rlDhcpSrvConfParamsCommunity=rlDhcpSrvConfParamsCommunity, rlDhcpRelayInterfaceIfindex=rlDhcpRelayInterfaceIfindex, rlDhcpRelayInterfaceListPortList=rlDhcpRelayInterfaceListPortList, rlDhcpSrvEnable=rlDhcpSrvEnable, rlDhcpRelayNextServerEntry=rlDhcpRelayNextServerEntry, rlDhcpSrvDynamicTable=rlDhcpSrvDynamicTable, rlDhcpSrvDynamicConfParamsName=rlDhcpSrvDynamicConfParamsName, rlDhcpSrvIpAddrIpAddr=rlDhcpSrvIpAddrIpAddr, rlDhcpSrvConfParamsTimeSrvList=rlDhcpSrvConfParamsTimeSrvList, rlDhcpSrvConfParamsNetbiosNodeType=rlDhcpSrvConfParamsNetbiosNodeType, rlDhcpRelayExists=rlDhcpRelayExists, rlDhcpSrvProbeTimeout=rlDhcpSrvProbeTimeout, rlDhcpSrvDbNumOfActiveEntries=rlDhcpSrvDbNumOfActiveEntries, rlDhcpSrvIpAddrEntry=rlDhcpSrvIpAddrEntry, rlDhcpSrvIpAddrAgeTime=rlDhcpSrvIpAddrAgeTime, rlDhcpSrvDynamicLeaseTime=rlDhcpSrvDynamicLeaseTime, rlDhcpSrvDbErase=rlDhcpSrvDbErase, rlDhcpSrvProbeEnable=rlDhcpSrvProbeEnable, rlDhcpSrvConfParamsNmsIp=rlDhcpSrvConfParamsNmsIp, rlDhcpSrvConfParamsEntry=rlDhcpSrvConfParamsEntry, rlDhcpSrvDynamicEntry=rlDhcpSrvDynamicEntry, rlDhcpSrvConfParamsDomainName=rlDhcpSrvConfParamsDomainName, rlDhcpRelayInterfaceListEntry=rlDhcpRelayInterfaceListEntry, rlDhcpSrvMaxNumOfClients=rlDhcpSrvMaxNumOfClients, rlDhcpRelayInterfaceListVlanId1025To2048=rlDhcpRelayInterfaceListVlanId1025To2048, rlDhcpSrvIpAddrRowStatus=rlDhcpSrvIpAddrRowStatus, rlDhcpSrvIpAddrIpNetMask=rlDhcpSrvIpAddrIpNetMask, rlDhcpRelayNextServerIpAddr=rlDhcpRelayNextServerIpAddr, rlDhcpRelayInterfaceRowStatus=rlDhcpRelayInterfaceRowStatus, rlDhcpSrvDynamicFreeNumOfAddr=rlDhcpSrvDynamicFreeNumOfAddr, rlDhcpSrvDynamicIpAddrTo=rlDhcpSrvDynamicIpAddrTo, rlDhcpSrvDbLocation=rlDhcpSrvDbLocation, rlDhcpSrvConfParamsNextServerIp=rlDhcpSrvConfParamsNextServerIp, rlDhcpSrvConfParamsNetbiosNameList=rlDhcpSrvConfParamsNetbiosNameList, rlDhcpSrvIpAddrMechanism=rlDhcpSrvIpAddrMechanism, rlDhcpRelayInterfaceListTable=rlDhcpRelayInterfaceListTable, rlDhcpRelayNextServerSecThreshold=rlDhcpRelayNextServerSecThreshold, rlDhcpSrvConfParamsOptionsList=rlDhcpSrvConfParamsOptionsList, rlDhcpRelayInterfaceUseGiaddr=rlDhcpRelayInterfaceUseGiaddr, rlDhcpSrvIpAddrClnHostName=rlDhcpSrvIpAddrClnHostName, rlDhcpRelayInterfaceListVlanId2049To3072=rlDhcpRelayInterfaceListVlanId2049To3072, rlDhcpSrvDynamicProbeEnable=rlDhcpSrvDynamicProbeEnable, rlDhcpSrvIpAddrPoolName=rlDhcpSrvIpAddrPoolName, PYSNMP_MODULE_ID=rsDHCP, rlDhcpSrvProbeRetries=rlDhcpSrvProbeRetries, rlDhcpSrvIpAddrIdentifier=rlDhcpSrvIpAddrIdentifier, rlDhcpSrvConfParamsBootfileName=rlDhcpSrvConfParamsBootfileName, rlDhcpSrvDynamicTotalNumOfAddr=rlDhcpSrvDynamicTotalNumOfAddr, rlDhcpSrvConfParamsDnsList=rlDhcpSrvConfParamsDnsList, rlDhcpSrvConfParamsTable=rlDhcpSrvConfParamsTable, rlDhcpRelayNextServerTable=rlDhcpRelayNextServerTable)