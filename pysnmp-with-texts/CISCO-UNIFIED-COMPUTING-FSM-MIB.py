#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-FSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-FSM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:16:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, TimeIntervalSec, CiscoInetAddressMask, CiscoAlarmSeverity, CiscoNetworkAddress = mibBuilder.importSymbols("CISCO-TC", "Unsigned64", "TimeIntervalSec", "CiscoInetAddressMask", "CiscoAlarmSeverity", "CiscoNetworkAddress")
CucsManagedObjectDn, ciscoUnifiedComputingMIBObjects, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId")
CucsFsmFsmStageStatus, = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsFsmFsmStageStatus")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, NotificationType, Bits, TimeTicks, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Counter64, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "NotificationType", "Bits", "TimeTicks", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "Counter32", "IpAddress")
DisplayString, RowPointer, DateAndTime, TruthValue, MacAddress, TextualConvention, TimeInterval, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "DateAndTime", "TruthValue", "MacAddress", "TextualConvention", "TimeInterval", "TimeStamp")
cucsFsmObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63))
if mibBuilder.loadTexts: cucsFsmObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsFsmObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsFsmObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsFsmObjects.setDescription('MIB representation of the Cisco Unified Computing System FSM management information model package')
cucsFsmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1), )
if mibBuilder.loadTexts: cucsFsmStatusTable.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusTable.setDescription('Cisco UCS fsm:Status managed object table')
cucsFsmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FSM-MIB", "cucsFsmStatusInstanceId"))
if mibBuilder.loadTexts: cucsFsmStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusEntry.setDescription('Entry for the cucsFsmStatusTable table.')
cucsFsmStatusInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFsmStatusInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusInstanceId.setDescription('Instance identifier of the managed object.')
cucsFsmStatusDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusDn.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusDn.setDescription('Cisco UCS fsm:Status:dn managed object property')
cucsFsmStatusRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusRn.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusRn.setDescription('Cisco UCS fsm:Status:rn managed object property')
cucsFsmStatusConvertedEpRef = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusConvertedEpRef.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusConvertedEpRef.setDescription('Cisco UCS fsm:Status:convertedEpRef managed object property')
cucsFsmStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusDescr.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusDescr.setDescription('Cisco UCS fsm:Status:descr managed object property')
cucsFsmStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusName.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusName.setDescription('Cisco UCS fsm:Status:name managed object property')
cucsFsmStatusObjectClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusObjectClassName.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusObjectClassName.setDescription('Cisco UCS fsm:Status:objectClassName managed object property')
cucsFsmStatusRemoteEpRef = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusRemoteEpRef.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusRemoteEpRef.setDescription('Cisco UCS fsm:Status:remoteEpRef managed object property')
cucsFsmStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFsmStatusState.setStatus('current')
if mibBuilder.loadTexts: cucsFsmStatusState.setDescription('Cisco UCS fsm:Status:state managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-FSM-MIB", cucsFsmStatusInstanceId=cucsFsmStatusInstanceId, cucsFsmStatusTable=cucsFsmStatusTable, cucsFsmStatusObjectClassName=cucsFsmStatusObjectClassName, cucsFsmStatusConvertedEpRef=cucsFsmStatusConvertedEpRef, cucsFsmStatusDescr=cucsFsmStatusDescr, cucsFsmStatusRn=cucsFsmStatusRn, cucsFsmStatusState=cucsFsmStatusState, cucsFsmStatusEntry=cucsFsmStatusEntry, cucsFsmStatusDn=cucsFsmStatusDn, PYSNMP_MODULE_ID=cucsFsmObjects, cucsFsmObjects=cucsFsmObjects, cucsFsmStatusName=cucsFsmStatusName, cucsFsmStatusRemoteEpRef=cucsFsmStatusRemoteEpRef)