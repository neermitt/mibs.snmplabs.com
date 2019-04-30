#
# PySNMP MIB module ChrComPmAtmATM-VC-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-VC-Current-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, iso, Counter64, NotificationType, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter32, Integer32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "iso", "Counter64", "NotificationType", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter32", "Integer32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmAtmATM_VC_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7), ).setLabel("chrComPmAtmATM-VC-CurrentTable")
if mibBuilder.loadTexts: chrComPmAtmATM_VC_CurrentTable.setStatus('current')
chrComPmAtmATM_VC_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1), ).setLabel("chrComPmAtmATM-VC-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: chrComPmAtmATM_VC_CurrentEntry.setStatus('current')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
chrComPmAtmThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmThresholdProfIndex.setStatus('current')
chrComPmAtmResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmAtmATM-VC-Current-MIB", chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells, chrComPmAtmThresholdProfIndex=chrComPmAtmThresholdProfIndex, chrComPmAtmATM_VC_CurrentTable=chrComPmAtmATM_VC_CurrentTable, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval, chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmATM_VC_CurrentEntry=chrComPmAtmATM_VC_CurrentEntry, chrComPmAtmResetPmCountersAction=chrComPmAtmResetPmCountersAction)