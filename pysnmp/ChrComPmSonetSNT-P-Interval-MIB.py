#
# PySNMP MIB module ChrComPmSonetSNT-P-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-P-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, iso, ModuleIdentity, Counter64, ObjectIdentity, IpAddress, Unsigned32, Bits, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "iso", "ModuleIdentity", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "Bits", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmSonetSNT_P_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11), ).setLabel("chrComPmSonetSNT-P-IntervalTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalTable.setStatus('current')
chrComPmSonetSNT_P_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1), ).setLabel("chrComPmSonetSNT-P-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmSonetSNT-P-Interval-MIB", "chrComPmSonetIntervalNumber"))
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalEntry.setStatus('current')
chrComPmSonetIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setStatus('current')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
chrComPmSonetUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetUAS.setStatus('current')
chrComPmSonetPS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetPS.setStatus('current')
mibBuilder.exportSymbols("ChrComPmSonetSNT-P-Interval-MIB", chrComPmSonetES=chrComPmSonetES, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetPS=chrComPmSonetPS, chrComPmSonetSNT_P_IntervalTable=chrComPmSonetSNT_P_IntervalTable, chrComPmSonetIntervalNumber=chrComPmSonetIntervalNumber, chrComPmSonetSNT_P_IntervalEntry=chrComPmSonetSNT_P_IntervalEntry, chrComPmSonetElapsedTime=chrComPmSonetElapsedTime, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetUAS=chrComPmSonetUAS, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls, chrComPmSonetCV=chrComPmSonetCV)
