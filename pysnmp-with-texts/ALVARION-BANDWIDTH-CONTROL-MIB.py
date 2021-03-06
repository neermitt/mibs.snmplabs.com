#
# PySNMP MIB module ALVARION-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-BANDWIDTH-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionPriorityQueue, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionPriorityQueue")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Unsigned32, Counter32, Integer32, Gauge32, ObjectIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter32", "Integer32", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "IpAddress")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
alvarionBandwidthControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14))
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionBandwidthControlMIB.setDescription('Alvarion Bandwidth Control MIB.')
alvarionBandwidthControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1))
coBandwidthControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1))
coBandwidthControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlEnable.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlEnable.setDescription('Indicates if bandwidth control is enabled or disabled on the Internet port.')
coBandwidthControlMaxTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setDescription('Indicates the maximum rate at which data can be transmitted on the Internet port. If traffic exceeds this rate for short bursts, it is buffered. Long overages will result in data being dropped.')
coBandwidthControlMaxReceiveRate = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setDescription('Indicates the maximum rate at which data can be received on the Internet port. If traffic exceeds this rate for short bursts it is buffered. Long overages will result in data being dropped.')
coBandwidthControlLevelTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4), )
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setDescription('A table defining the current bandwidth level settings that are active on the device.')
coBandwidthControlLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1), ).setIndexNames((0, "ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelIndex"))
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setDescription('An entry in the coBandwidthControlLevelTable. coBandwidthControlLevelIndex - Uniquely access a definition for this particular bandwidth control level.')
coBandwidthControlLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 1), AlvarionPriorityQueue())
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setDescription('Specifies the level index. Each index defines a bandwidth level that traffic can be assigned to. Four indexes are defined (1 to 4) with the following meanings: 1-Low, 2-Normal, 3- High, 4-Very High.')
coBandwidthControlLevelMinTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setDescription('Specify the minimum transmit rate for the level as a percentage of coBandwidthControlMaxTransmitRate. This is the minimum amount of bandwidth that will be assigned to a level as soon as outgoing traffic is present on the level.')
coBandwidthControlLevelMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setDescription('Specify the maximum transmit rate for the specified level as a percentage of coBandwidthControlMaxTransmitRate. This is the maximum amount of outgoing bandwidth that can be consumed by the level. Traffic in excess will be buffered for short bursts, and dropped for sustained overages')
coBandwidthControlLevelMinReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setDescription('Specify the minimum receive rate for the specified level as a percentage of coBandwidthControlMaxReceiveRateRate. This is the minimum amount of bandwidth that will be assigned to a level as soon as incoming traffic is present on the level.')
coBandwidthControlLevelMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setDescription('Specify the maximum receive rate for the specified level as a percentage of coBandwidthControlMaxReceiveRateRate. This is the maximum amount of incoming bandwidth that can be consumed by the level. Traffic in excess will be buffered for short bursts, and dropped for sustained overages.')
alvarionBandwidthControlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2))
alvarionBandwidthControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 1))
alvarionBandwidthControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2))
alvarionBandwidthControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 1, 1)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "alvarionBandwidthControlMIBGroup"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "alvarionBandwidthControlLevelMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlMIBCompliance = alvarionBandwidthControlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionBandwidthControlMIBCompliance.setDescription('The compliance statement for the Bandwidth Control MIB.')
alvarionBandwidthControlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2, 1)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlEnable"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlMIBGroup = alvarionBandwidthControlMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionBandwidthControlMIBGroup.setDescription('A collection of objects for use with Bandwidth Controls.')
alvarionBandwidthControlLevelMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 14, 2, 2, 2)).setObjects(("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxTransmitRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinReceiveRate"), ("ALVARION-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionBandwidthControlLevelMIBGroup = alvarionBandwidthControlLevelMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionBandwidthControlLevelMIBGroup.setDescription('A collection of objects for use with Bandwidth Controls.')
mibBuilder.exportSymbols("ALVARION-BANDWIDTH-CONTROL-MIB", coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, alvarionBandwidthControlMIBGroups=alvarionBandwidthControlMIBGroups, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate, alvarionBandwidthControlMIBGroup=alvarionBandwidthControlMIBGroup, alvarionBandwidthControlMIBCompliance=alvarionBandwidthControlMIBCompliance, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate, alvarionBandwidthControlMIBConformance=alvarionBandwidthControlMIBConformance, coBandwidthControlConfig=coBandwidthControlConfig, alvarionBandwidthControlMIB=alvarionBandwidthControlMIB, alvarionBandwidthControlMIBObjects=alvarionBandwidthControlMIBObjects, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, PYSNMP_MODULE_ID=alvarionBandwidthControlMIB, coBandwidthControlEnable=coBandwidthControlEnable, coBandwidthControlLevelTable=coBandwidthControlLevelTable, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, alvarionBandwidthControlLevelMIBGroup=alvarionBandwidthControlLevelMIBGroup, alvarionBandwidthControlMIBCompliances=alvarionBandwidthControlMIBCompliances)
