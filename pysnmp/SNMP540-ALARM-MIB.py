#
# PySNMP MIB module SNMP540-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP540-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
snmp540, = mibBuilder.importSymbols("SNMP540-MGMT-MIB", "snmp540")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, iso, TimeTicks, Unsigned32, Counter64, NotificationType, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "iso", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmp540Alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 4, 10))
snmp540AlarmMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmp540AlarmMIBversion.setStatus('mandatory')
snmp540AlarmStructure = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gdcProprietarySCMStandard", 1), ("generalAlarmStructure", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmp540AlarmStructure.setStatus('mandatory')
snmp540AlarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmp540AlarmNumber.setStatus('mandatory')
snmp540GeneralIntegrationTime = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmp540GeneralIntegrationTime.setStatus('mandatory')
snmp540AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5), )
if mibBuilder.loadTexts: snmp540AlarmTable.setStatus('mandatory')
snmp540AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1), ).setIndexNames((0, "SNMP540-ALARM-MIB", "alarmNumber"))
if mibBuilder.loadTexts: snmp540AlarmEntry.setStatus('mandatory')
alarmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNumber.setStatus('mandatory')
description = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: description.setStatus('mandatory')
severityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severityLevel.setStatus('mandatory')
pysmi_class = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("general", 1), ("threshold", 2), ("countWindow", 3), ("thresholdInterval", 4)))).setLabel("class").setMaxAccess("readonly")
if mibBuilder.loadTexts: pysmi_class.setStatus('mandatory')
mask = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mask", 1), ("unmask", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mask.setStatus('mandatory')
threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshold.setStatus('mandatory')
status = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('mandatory')
snmp540AlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 498, 8, 4) + (0,1)).setObjects(("SNMP540-ALARM-MIB", "description"), ("SNMP540-ALARM-MIB", "severityLevel"), ("SNMP540-ALARM-MIB", "status"))
mibBuilder.exportSymbols("SNMP540-ALARM-MIB", mask=mask, severityLevel=severityLevel, snmp540AlarmTrap=snmp540AlarmTrap, alarmNumber=alarmNumber, pysmi_class=pysmi_class, snmp540AlarmMIBversion=snmp540AlarmMIBversion, snmp540AlarmTable=snmp540AlarmTable, description=description, status=status, threshold=threshold, snmp540Alarm=snmp540Alarm, snmp540AlarmStructure=snmp540AlarmStructure, snmp540GeneralIntegrationTime=snmp540GeneralIntegrationTime, snmp540AlarmNumber=snmp540AlarmNumber, snmp540AlarmEntry=snmp540AlarmEntry)
