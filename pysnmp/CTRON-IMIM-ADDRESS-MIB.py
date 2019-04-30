#
# PySNMP MIB module CTRON-IMIM-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-IMIM-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, IpAddress, Integer32, enterprises, TimeTicks, ModuleIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "IpAddress", "Integer32", "enterprises", "TimeTicks", "ModuleIdentity", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
subsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6))
backplaneProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5))
imimAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1))
imimAddressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1), )
if mibBuilder.loadTexts: imimAddressTable.setStatus('mandatory')
imimAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1), ).setIndexNames((0, "CTRON-IMIM-ADDRESS-MIB", "imimAddressChassisSlot"))
if mibBuilder.loadTexts: imimAddressEntry.setStatus('mandatory')
imimAddressChassisSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressChassisSlot.setStatus('mandatory')
imimAddressMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressMAC.setStatus('mandatory')
imimAddressIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressIP.setStatus('mandatory')
backplaneHeartbeat = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("heartBeatPresent", 1), ("heartBeatAbsent", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backplaneHeartbeat.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-IMIM-ADDRESS-MIB", imimAddressTable=imimAddressTable, imimAddressEntry=imimAddressEntry, imimAddress=imimAddress, backplaneHeartbeat=backplaneHeartbeat, cabletron=cabletron, imimAddressMAC=imimAddressMAC, backplaneProtocol=backplaneProtocol, imimAddressIP=imimAddressIP, imimAddressChassisSlot=imimAddressChassisSlot, subsystem=subsystem, commsDevice=commsDevice)