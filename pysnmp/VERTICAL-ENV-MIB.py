#
# PySNMP MIB module VERTICAL-ENV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERTICAL-ENV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, TimeTicks, ModuleIdentity, Gauge32, Bits, Counter32, IpAddress, NotificationType, Integer32, Unsigned32, Counter64, NotificationType, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "Counter64", "NotificationType", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vertical = MibIdentifier((1, 3, 6, 1, 4, 1, 2338))
environment = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 11))
iOFanTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 11, 1), )
if mibBuilder.loadTexts: iOFanTable.setStatus('current')
iOFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 11, 1, 1), ).setIndexNames((0, "VERTICAL-ENV-MIB", "fanIndex"))
if mibBuilder.loadTexts: iOFanEntry.setStatus('mandatory')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
fanOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanOperStatus.setStatus('mandatory')
iOPSTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 11, 2), )
if mibBuilder.loadTexts: iOPSTable.setStatus('current')
iOPSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 11, 2, 1), ).setIndexNames((0, "VERTICAL-ENV-MIB", "psIndex"))
if mibBuilder.loadTexts: iOPSEntry.setStatus('mandatory')
psIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psIndex.setStatus('mandatory')
psOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 11, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOperStatus.setStatus('mandatory')
iOFaultMonitorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 11, 3))
iOFaultMonitorStatus = MibScalar((1, 3, 6, 1, 4, 1, 2338, 11, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rAMFull", 1), ("notResponding", 2), ("ok", 3), ("modemFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iOFaultMonitorStatus.setStatus('mandatory')
iOTrapInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 11, 4))
iOLastFanTrap = MibScalar((1, 3, 6, 1, 4, 1, 2338, 11, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iOLastFanTrap.setStatus('mandatory')
iOLastPowerSupplyTrap = MibScalar((1, 3, 6, 1, 4, 1, 2338, 11, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iOLastPowerSupplyTrap.setStatus('mandatory')
iOLastFaultMonitorTrap = MibScalar((1, 3, 6, 1, 4, 1, 2338, 11, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iOLastFaultMonitorTrap.setStatus('mandatory')
iOFanStatus = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,47)).setObjects(("VERTICAL-ENV-MIB", "iOLastFanTrap"))
iOPowerSupplyStatus = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,48)).setObjects(("VERTICAL-ENV-MIB", "iOLastPowerSupplyTrap"))
iOFaultMonitorStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,49)).setObjects(("VERTICAL-ENV-MIB", "iOLastFaultMonitorTrap"))
mibBuilder.exportSymbols("VERTICAL-ENV-MIB", iOLastFaultMonitorTrap=iOLastFaultMonitorTrap, iOFanStatus=iOFanStatus, psIndex=psIndex, iOLastFanTrap=iOLastFanTrap, iOFanEntry=iOFanEntry, iOFaultMonitorGroup=iOFaultMonitorGroup, iOTrapInfoGroup=iOTrapInfoGroup, iOPSEntry=iOPSEntry, fanOperStatus=fanOperStatus, psOperStatus=psOperStatus, fanIndex=fanIndex, vertical=vertical, iOLastPowerSupplyTrap=iOLastPowerSupplyTrap, iOFaultMonitorStatus=iOFaultMonitorStatus, iOPSTable=iOPSTable, environment=environment, iOPowerSupplyStatus=iOPowerSupplyStatus, iOFaultMonitorStatusTrap=iOFaultMonitorStatusTrap, iOFanTable=iOFanTable)