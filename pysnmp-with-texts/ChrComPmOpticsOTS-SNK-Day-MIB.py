#
# PySNMP MIB module ChrComPmOpticsOTS-SNK-Day-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOTS-SNK-Day-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, iso, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, MibIdentifier, Counter64, Gauge32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmOpticsOTS_SNK_DayTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3), ).setLabel("chrComPmOpticsOTS-SNK-DayTable")
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_DayTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_DayTable.setDescription('')
chrComPmOpticsOTS_SNK_DayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1), ).setLabel("chrComPmOpticsOTS-SNK-DayEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmOpticsOTS-SNK-Day-MIB", "chrComPmOpticsDayNumber"))
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_DayEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOTS_SNK_DayEntry.setDescription('')
chrComPmOpticsDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsDayNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsDayNumber.setDescription('')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setDescription('a flag marking the validity of the entry data')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setDescription('measurment duration, in 0.01 seconds')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setDescription('invalid for first version. indicates how many all-zero periods have passed.')
chrComPmOpticsORS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsORS.setDescription('')
chrComPmOpticsSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSES.setDescription('')
chrComPmOpticsUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsUAS.setDescription('')
chrComPmOpticsMean = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMean.setDescription('')
chrComPmOpticsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMax.setDescription('')
chrComPmOpticsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMin.setDescription('')
chrComPmOpticsSD = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSD.setDescription('')
chrComPmOpticsThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsThresholdProfIndex.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsThresholdProfIndex.setDescription('')
chrComPmOpticsResetCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 3, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsResetCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsResetCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmOpticsOTS-SNK-Day-MIB", chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl, chrComPmOpticsSD=chrComPmOpticsSD, chrComPmOpticsMax=chrComPmOpticsMax, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsThresholdProfIndex=chrComPmOpticsThresholdProfIndex, chrComPmOpticsORS=chrComPmOpticsORS, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsResetCountersAction=chrComPmOpticsResetCountersAction, chrComPmOpticsDayNumber=chrComPmOpticsDayNumber, chrComPmOpticsOTS_SNK_DayEntry=chrComPmOpticsOTS_SNK_DayEntry, chrComPmOpticsMin=chrComPmOpticsMin, chrComPmOpticsSES=chrComPmOpticsSES, chrComPmOpticsMean=chrComPmOpticsMean, chrComPmOpticsUAS=chrComPmOpticsUAS, chrComPmOpticsOTS_SNK_DayTable=chrComPmOpticsOTS_SNK_DayTable)