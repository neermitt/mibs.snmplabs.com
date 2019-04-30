#
# PySNMP MIB module DNOS-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-PFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter32, iso, IpAddress, MibIdentifier, ObjectIdentity, TimeTicks, NotificationType, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter32", "iso", "IpAddress", "MibIdentifier", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter64", "Unsigned32")
MacAddress, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString")
fastPathPFC = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47))
fastPathPFC.setRevisions(('2011-01-26 00:00', '2009-05-22 00:00',))
if mibBuilder.loadTexts: fastPathPFC.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathPFC.setOrganization('Dell, Inc.')
agentPfcCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1))
agentPfcTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1), )
if mibBuilder.loadTexts: agentPfcTable.setStatus('current')
agentPfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1), ).setIndexNames((0, "DNOS-PFC-MIB", "agentPfcIntfIndex"))
if mibBuilder.loadTexts: agentPfcEntry.setStatus('current')
agentPfcIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentPfcIntfIndex.setStatus('current')
agentPfcIntfAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcIntfAdminMode.setStatus('current')
agentPfcIntfPfcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcStatus.setStatus('current')
agentPfcTotalIntfPfcFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesRx.setStatus('current')
agentPfcTotalIntfPfcFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesTx.setStatus('current')
agentPfcIntfLinkDelayAllowance = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfLinkDelayAllowance.setStatus('current')
agentPfcIntfAdvWilling = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("willing", 1), ("unwilling", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfAdvWilling.setStatus('current')
agentPfcIntfPeerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("absent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerDetected.setStatus('current')
agentPfcIntfPeerMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerMacAddr.setStatus('current')
agentPfcIntfPeerWilling = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absent", 1), ("willing", 2), ("unwilling", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerWilling.setStatus('current')
agentPfcIntfPeerMBCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absent", 1), ("true", 2), ("false", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerMBCStatus.setStatus('current')
agentPfcIntfPeerCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerCapability.setStatus('current')
agentPfcIntfPeerCfgCompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absent", 1), ("true", 2), ("false", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerCfgCompatible.setStatus('current')
agentPfcIntfPeerCompatibleCfgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerCompatibleCfgCount.setStatus('current')
agentPfcIntfPeerIncompatibleCfgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPeerIncompatibleCfgCount.setStatus('current')
agentPfcActionTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2), )
if mibBuilder.loadTexts: agentPfcActionTable.setStatus('current')
agentPfcActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1), ).setIndexNames((0, "DNOS-PFC-MIB", "agentPfcIntfIndex"), (0, "DNOS-PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcActionEntry.setStatus('current')
agentPfcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: agentPfcPriority.setStatus('current')
agentPfcAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("nodrop", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcAction.setStatus('current')
agentPfcOperAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("nodrop", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcOperAction.setStatus('current')
agentPfcAdvAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("nodrop", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcAdvAction.setStatus('current')
agentPfcPeerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absent", 1), ("drop", 2), ("nodrop", 3))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcPeerAction.setStatus('current')
agentPfcIntfStatsPerPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3), )
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityTable.setStatus('current')
agentPfcIntfStatsPerPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1), ).setIndexNames((0, "DNOS-PFC-MIB", "agentPfcIntfIndex"), (0, "DNOS-PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityEntry.setStatus('current')
agentPfcIntfPfcPriorityFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcPriorityFramesRx.setStatus('current')
agentPfcIntfPfcPriorityFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 47, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcPriorityFramesTx.setStatus('current')
mibBuilder.exportSymbols("DNOS-PFC-MIB", agentPfcIntfPeerIncompatibleCfgCount=agentPfcIntfPeerIncompatibleCfgCount, agentPfcEntry=agentPfcEntry, agentPfcIntfPeerMBCStatus=agentPfcIntfPeerMBCStatus, agentPfcIntfPeerDetected=agentPfcIntfPeerDetected, agentPfcAction=agentPfcAction, agentPfcIntfLinkDelayAllowance=agentPfcIntfLinkDelayAllowance, agentPfcTotalIntfPfcFramesRx=agentPfcTotalIntfPfcFramesRx, fastPathPFC=fastPathPFC, agentPfcCfgGroup=agentPfcCfgGroup, agentPfcIntfPfcPriorityFramesTx=agentPfcIntfPfcPriorityFramesTx, agentPfcIntfPeerCompatibleCfgCount=agentPfcIntfPeerCompatibleCfgCount, agentPfcOperAction=agentPfcOperAction, agentPfcIntfStatsPerPriorityTable=agentPfcIntfStatsPerPriorityTable, agentPfcPriority=agentPfcPriority, agentPfcActionTable=agentPfcActionTable, agentPfcIntfAdvWilling=agentPfcIntfAdvWilling, agentPfcAdvAction=agentPfcAdvAction, agentPfcIntfStatsPerPriorityEntry=agentPfcIntfStatsPerPriorityEntry, PYSNMP_MODULE_ID=fastPathPFC, agentPfcActionEntry=agentPfcActionEntry, agentPfcTotalIntfPfcFramesTx=agentPfcTotalIntfPfcFramesTx, agentPfcIntfPeerWilling=agentPfcIntfPeerWilling, agentPfcIntfPfcPriorityFramesRx=agentPfcIntfPfcPriorityFramesRx, agentPfcIntfPeerCapability=agentPfcIntfPeerCapability, agentPfcIntfPeerMacAddr=agentPfcIntfPeerMacAddr, agentPfcPeerAction=agentPfcPeerAction, agentPfcIntfPeerCfgCompatible=agentPfcIntfPeerCfgCompatible, agentPfcIntfIndex=agentPfcIntfIndex, agentPfcIntfAdminMode=agentPfcIntfAdminMode, agentPfcIntfPfcStatus=agentPfcIntfPfcStatus, agentPfcTable=agentPfcTable)