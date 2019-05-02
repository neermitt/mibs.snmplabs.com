#
# PySNMP MIB module Wellfleet-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibIdentifier, ModuleIdentity, iso, ObjectIdentity, Counter64, NotificationType, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "NotificationType", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfServicePkgGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfServicePkgGroup")
wfQosServPkgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1), )
if mibBuilder.loadTexts: wfQosServPkgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgTable.setDescription('This file describes the MIBS for managing Qos Templates')
wfQosServPkgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1), ).setIndexNames((0, "Wellfleet-QOS-MIB", "wfQosServPkgIndex"))
if mibBuilder.loadTexts: wfQosServPkgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgEntry.setDescription('An entry in the Qos Base table')
wfQosServPkgDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgDelete.setDescription('Create/Delete parameter')
wfQosServPkgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgIndex.setDescription('Instance ID, filled in by driver')
wfQosServPkgServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgServiceName.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgServiceName.setDescription('Service Name given to this template')
wfQosServPkgScheduling = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("round-robin", 1), ("strict-priority", 2))).clone('round-robin')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgScheduling.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgScheduling.setDescription('Selects the scheduling method, Round Robbin or Strict Priority, to service the Tx Queues. In Round Robbin, each Queue is serviced according to the weights applied in the Queue Mib. In Strict Priority, the highest priority Queue with data is serviced.')
wfQosServPkgNumQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgNumQueues.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgNumQueues.setDescription('Number of queues configured for this queue package')
wfQosServPkgNumLines = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgNumLines.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgNumLines.setDescription('Number of lines using this queue package')
wfQosServPkgQueCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2), )
if mibBuilder.loadTexts: wfQosServPkgQueCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgTable.setDescription('This file describes the MIBS for managing Qos Templates')
wfQosServPkgQueCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1), ).setIndexNames((0, "Wellfleet-QOS-MIB", "wfQosServPkgQueCfgServiceIndex"), (0, "Wellfleet-QOS-MIB", "wfQosServPkgQueCfgQueueIndex"))
if mibBuilder.loadTexts: wfQosServPkgQueCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgEntry.setDescription('An entry in the Qos Base table')
wfQosServPkgQueCfgDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgDelete.setDescription('Create/Delete parameter')
wfQosServPkgQueCfgServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgQueCfgServiceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgServiceIndex.setDescription('Instance Service ID, filled in by driver')
wfQosServPkgQueCfgQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgQueCfgQueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgQueueIndex.setDescription('Instance Queue ID, filled in by driver')
wfQosServPkgQueCfgQueueName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgQueueName.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgQueueName.setDescription('Queue Name given to this template')
wfQosServPkgQueCfgState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("waitPkg", 2), ("misCfg", 3))).clone('waitPkg')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgQueCfgState.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgState.setDescription('State of this Queue, either Up, Waiting for a Service Package, or Misconfigured.')
wfQosServPkgQueCfgClass = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgClass.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgClass.setDescription('Class level for this queue, 0=highest, 7=lowest')
wfQosServPkgQueCfgAcctRule = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgAcctRule.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgAcctRule.setDescription('Accounting Rule Template Index.')
wfQosServPkgQueCfgRxCommitInfoRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxCommitInfoRate.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxCommitInfoRate.setDescription('Commit Info Rate (CIR), in Kbits per second, configured for this template')
wfQosServPkgQueCfgRxBurstRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstRate.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstRate.setDescription('Burst Rate (BR), in Kbits per second, configured for this template')
wfQosServPkgQueCfgRxBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 10), Integer32().clone(8000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstSize.setDescription('Burst Size, in bytes, configured for this template')
wfQosServPkgQueCfgRxBurstAction = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("downgrade", 2), ("mark", 3), ("mark-downgrade", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstAction.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgRxBurstAction.setDescription('Action when Burst Rate is exceeded')
wfQosServPkgQueCfgTxDropThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("percent-83", 2), ("percent-66", 3), ("percent-50", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxDropThresh.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxDropThresh.setDescription('Hardware Threshold in percent to start dropping Output Packets for this queue. When set to none, all packets are accepted until the Queue Fills 100 percent.')
wfQosServPkgQueCfgTxWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 13), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxWeight.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxWeight.setDescription('Weight in percentage for the Tx Queue when set to Round Robbin Priority Type.')
wfQosServPkgQueCfgTxActualWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxActualWeight.setStatus('mandatory')
if mibBuilder.loadTexts: wfQosServPkgQueCfgTxActualWeight.setDescription('Actual Weight, in percentage, given to this Tx Queue within its Service Package when set to Round Robbin Scheduling.')
wfQueueStatTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3), )
if mibBuilder.loadTexts: wfQueueStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatTable.setDescription('This file describes the MIBS for getting Queues Stats')
wfQueueStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1), ).setIndexNames((0, "Wellfleet-QOS-MIB", "wfQueueStatPortLineNumber"), (0, "Wellfleet-QOS-MIB", "wfQueueStatLineIndex"), (0, "Wellfleet-QOS-MIB", "wfQueueStatQueueIndex"))
if mibBuilder.loadTexts: wfQueueStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatEntry.setDescription('An entry in the Queue Base table')
wfQueueStatPortLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatPortLineNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatPortLineNumber.setDescription('Instance ID PortLineNumber')
wfQueueStatLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatLineIndex.setDescription('Instance Line Number')
wfQueueStatQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatQueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatQueueIndex.setDescription('Queue Index, matches that of wfQosServPkgQueCfgQueueIndex')
wfQueueStatTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatTxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatTxOctets.setDescription('Number of Transmit Octets received without error')
wfQueueStatTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatTxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatTxPackets.setDescription('Number of Transmit Packets received without error')
wfQueueStatTxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatTxDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatTxDrops.setDescription('Number of Transmit Packets Dropped')
wfQueueStatRxBelowCirOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxBelowCirOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxBelowCirOctets.setDescription('The number of octets received which were below the committed information rate (CIR).')
wfQueueStatRxBelowCirPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxBelowCirPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxBelowCirPackets.setDescription('The number of packets received which were below the committed information rate (CIR).')
wfQueueStatRxAboveCirOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxAboveCirOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxAboveCirOctets.setDescription('The number of octets received which exceeded the committed information rate, but which were within the allocated burst rate (BR).')
wfQueueStatRxAboveCirPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxAboveCirPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxAboveCirPackets.setDescription('The number of packets received which exceeded the committed information rate, but which were within the allocated burst rate (BR).')
wfQueueStatRxAboveBrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxAboveBrOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxAboveBrOctets.setDescription('The number of octets received which exceeded the allocated burst rate (BR).')
wfQueueStatRxAboveBrPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfQueueStatRxAboveBrPackets.setStatus('mandatory')
if mibBuilder.loadTexts: wfQueueStatRxAboveBrPackets.setDescription('The number of packets received which exceeded the allocated burst rate (BR).')
mibBuilder.exportSymbols("Wellfleet-QOS-MIB", wfQosServPkgNumLines=wfQosServPkgNumLines, wfQosServPkgQueCfgTxActualWeight=wfQosServPkgQueCfgTxActualWeight, wfQueueStatTxDrops=wfQueueStatTxDrops, wfQueueStatTxOctets=wfQueueStatTxOctets, wfQosServPkgQueCfgRxBurstRate=wfQosServPkgQueCfgRxBurstRate, wfQosServPkgServiceName=wfQosServPkgServiceName, wfQosServPkgQueCfgQueueName=wfQosServPkgQueCfgQueueName, wfQosServPkgTable=wfQosServPkgTable, wfQosServPkgQueCfgTable=wfQosServPkgQueCfgTable, wfQosServPkgQueCfgTxDropThresh=wfQosServPkgQueCfgTxDropThresh, wfQosServPkgQueCfgAcctRule=wfQosServPkgQueCfgAcctRule, wfQosServPkgQueCfgRxBurstAction=wfQosServPkgQueCfgRxBurstAction, wfQueueStatEntry=wfQueueStatEntry, wfQueueStatRxBelowCirOctets=wfQueueStatRxBelowCirOctets, wfQueueStatRxBelowCirPackets=wfQueueStatRxBelowCirPackets, wfQueueStatRxAboveBrOctets=wfQueueStatRxAboveBrOctets, wfQueueStatTxPackets=wfQueueStatTxPackets, wfQosServPkgEntry=wfQosServPkgEntry, wfQosServPkgQueCfgRxBurstSize=wfQosServPkgQueCfgRxBurstSize, wfQosServPkgQueCfgState=wfQosServPkgQueCfgState, wfQosServPkgQueCfgTxWeight=wfQosServPkgQueCfgTxWeight, wfQosServPkgQueCfgServiceIndex=wfQosServPkgQueCfgServiceIndex, wfQosServPkgScheduling=wfQosServPkgScheduling, wfQosServPkgIndex=wfQosServPkgIndex, wfQueueStatRxAboveCirOctets=wfQueueStatRxAboveCirOctets, wfQosServPkgQueCfgClass=wfQosServPkgQueCfgClass, wfQueueStatLineIndex=wfQueueStatLineIndex, wfQueueStatRxAboveBrPackets=wfQueueStatRxAboveBrPackets, wfQueueStatQueueIndex=wfQueueStatQueueIndex, wfQosServPkgQueCfgDelete=wfQosServPkgQueCfgDelete, wfQosServPkgQueCfgQueueIndex=wfQosServPkgQueCfgQueueIndex, wfQueueStatPortLineNumber=wfQueueStatPortLineNumber, wfQosServPkgQueCfgEntry=wfQosServPkgQueCfgEntry, wfQosServPkgQueCfgRxCommitInfoRate=wfQosServPkgQueCfgRxCommitInfoRate, wfQosServPkgNumQueues=wfQosServPkgNumQueues, wfQueueStatRxAboveCirPackets=wfQueueStatRxAboveCirPackets, wfQueueStatTable=wfQueueStatTable, wfQosServPkgDelete=wfQosServPkgDelete)