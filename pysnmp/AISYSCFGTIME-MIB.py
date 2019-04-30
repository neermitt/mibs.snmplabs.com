#
# PySNMP MIB module AISYSCFGTIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISYSCFGTIME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, NotificationType, Gauge32, Bits, TimeTicks, ObjectIdentity, Integer32, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Counter32", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 32))
aiSysCfgTime = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 32, 2))
aiSysCfgTime.setRevisions(('2001-04-30 17:00',))
if mibBuilder.loadTexts: aiSysCfgTime.setLastUpdated('200104301700Z')
if mibBuilder.loadTexts: aiSysCfgTime.setOrganization('Applied Innovation Inc.')
aiSCTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTimeZone.setStatus('current')
aiSCDaylightSavingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCDaylightSavingEnabled.setStatus('current')
aiSCDaylightSavingStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCDaylightSavingStatus.setStatus('current')
aiSCTimeSntpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 2, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTimeSntpEnabled.setStatus('current')
aiSCTimeSntpPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTimeSntpPollInterval.setStatus('current')
aiSCTimeNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 539, 32, 2, 6), )
if mibBuilder.loadTexts: aiSCTimeNtpServerTable.setStatus('current')
aiSCTimeNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1), ).setIndexNames((0, "AISYSCFGTIME-MIB", "aiSCTimeNtpServerIndex"))
if mibBuilder.loadTexts: aiSCTimeNtpServerEntry.setStatus('current')
aiSCTimeNtpServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTimeNtpServerIndex.setStatus('current')
aiSCTimeNtpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTimeNtpServerAddress.setStatus('current')
mibBuilder.exportSymbols("AISYSCFGTIME-MIB", aiSCDaylightSavingEnabled=aiSCDaylightSavingEnabled, PYSNMP_MODULE_ID=aiSysCfgTime, aiSCTimeNtpServerAddress=aiSCTimeNtpServerAddress, aiSysCfgTime=aiSysCfgTime, aiSCTimeNtpServerIndex=aiSCTimeNtpServerIndex, aiSCTimeZone=aiSCTimeZone, aiSCTimeSntpPollInterval=aiSCTimeSntpPollInterval, aiSCTimeNtpServerTable=aiSCTimeNtpServerTable, aiSCTimeSntpEnabled=aiSCTimeSntpEnabled, aiSCTimeNtpServerEntry=aiSCTimeNtpServerEntry, aii=aii, aiSysCfg=aiSysCfg, aiSCDaylightSavingStatus=aiSCDaylightSavingStatus)