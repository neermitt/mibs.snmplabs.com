#
# PySNMP MIB module Nortel-Magellan-Passport-ApsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-ApsMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
Integer32, PassportCounter64, RowStatus, Unsigned32, DisplayString, StorageType, Counter32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Integer32", "PassportCounter64", "RowStatus", "Unsigned32", "DisplayString", "StorageType", "Counter32")
Link, NonReplicated, FixedPoint1, Hex, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "NonReplicated", "FixedPoint1", "Hex", "AsciiString")
components, passportMIBs = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "components", "passportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Integer32, IpAddress, Gauge32, MibIdentifier, Unsigned32, NotificationType, Bits, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Integer32", "IpAddress", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Bits", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136))
aps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134))
apsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1), )
if mibBuilder.loadTexts: apsRowStatusTable.setStatus('mandatory')
apsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"))
if mibBuilder.loadTexts: apsRowStatusEntry.setStatus('mandatory')
apsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsRowStatus.setStatus('mandatory')
apsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsComponentName.setStatus('mandatory')
apsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStorageType.setStatus('mandatory')
apsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15999)))
if mibBuilder.loadTexts: apsIndex.setStatus('mandatory')
apsCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10), )
if mibBuilder.loadTexts: apsCidDataTable.setStatus('mandatory')
apsCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"))
if mibBuilder.loadTexts: apsCidDataEntry.setStatus('mandatory')
apsCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCustomerIdentifier.setStatus('mandatory')
apsProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11), )
if mibBuilder.loadTexts: apsProvTable.setStatus('mandatory')
apsProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"))
if mibBuilder.loadTexts: apsProvEntry.setStatus('mandatory')
apsApplicationFramerName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsApplicationFramerName.setStatus('mandatory')
apsWorkingLine = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 2), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsWorkingLine.setStatus('mandatory')
apsProtectionLine = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 3), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsProtectionLine.setStatus('mandatory')
apsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 5))).clone(namedValues=NamedValues(("unidirectional", 4), ("bidirectional", 5))).clone('unidirectional')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsMode.setStatus('mandatory')
apsRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsRevertive.setStatus('mandatory')
apsHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 6), FixedPoint1().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsHoldOffTime.setStatus('mandatory')
apsWaitToRestorePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 12)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsWaitToRestorePeriod.setStatus('mandatory')
apsSignalDegradeRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-9, -5)).clone(-5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsSignalDegradeRatio.setStatus('mandatory')
apsStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12), )
if mibBuilder.loadTexts: apsStateTable.setStatus('mandatory')
apsStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"))
if mibBuilder.loadTexts: apsStateEntry.setStatus('mandatory')
apsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsAdminState.setStatus('mandatory')
apsOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsOperationalState.setStatus('mandatory')
apsUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsUsageState.setStatus('mandatory')
apsAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsAvailabilityStatus.setStatus('mandatory')
apsProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsProceduralStatus.setStatus('mandatory')
apsControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsControlStatus.setStatus('mandatory')
apsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsAlarmStatus.setStatus('mandatory')
apsStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStandbyStatus.setStatus('mandatory')
apsUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsUnknownStatus.setStatus('mandatory')
apsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13), )
if mibBuilder.loadTexts: apsOperTable.setStatus('mandatory')
apsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"))
if mibBuilder.loadTexts: apsOperEntry.setStatus('mandatory')
apsNearEndRxActiveLine = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("protection", 0), ("working", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsNearEndRxActiveLine.setStatus('mandatory')
apsNearEndRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 6, 8, 10, 12, 14, 15))).clone(namedValues=NamedValues(("noRequest", 0), ("doNotRevert", 1), ("reverseRequest", 2), ("waitToRestore", 6), ("manualSwitch", 8), ("signalDegrade", 10), ("signalFail", 12), ("forcedSwitch", 14), ("lockoutOfProtection", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsNearEndRequest.setStatus('mandatory')
apsNearEndRequestChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("protection", 0), ("working", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsNearEndRequestChannel.setStatus('mandatory')
apsFarEndRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 6, 8, 10, 12, 14, 15))).clone(namedValues=NamedValues(("noRequest", 0), ("doNotRevert", 1), ("reverseRequest", 2), ("waitToRestore", 6), ("manualSwitch", 8), ("signalDegrade", 10), ("signalFail", 12), ("forcedSwitch", 14), ("lockoutOfProtection", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsFarEndRequest.setStatus('mandatory')
apsFarEndRequestChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("protection", 0), ("working", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsFarEndRequestChannel.setStatus('mandatory')
apsSdOnLines = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSdOnLines.setStatus('mandatory')
apsSwitchovers = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSwitchovers.setStatus('mandatory')
apsTimeUntilRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTimeUntilRestore.setStatus('mandatory')
apsProtocolFailureAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsProtocolFailureAlarm.setStatus('mandatory')
apsModeMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsModeMismatchAlarm.setStatus('mandatory')
apsTest = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2))
apsTestRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1), )
if mibBuilder.loadTexts: apsTestRowStatusTable.setStatus('mandatory')
apsTestRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"), (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"))
if mibBuilder.loadTexts: apsTestRowStatusEntry.setStatus('mandatory')
apsTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestRowStatus.setStatus('mandatory')
apsTestComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestComponentName.setStatus('mandatory')
apsTestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestStorageType.setStatus('mandatory')
apsTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: apsTestIndex.setStatus('mandatory')
apsTestStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10), )
if mibBuilder.loadTexts: apsTestStateTable.setStatus('mandatory')
apsTestStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"), (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"))
if mibBuilder.loadTexts: apsTestStateEntry.setStatus('mandatory')
apsTestAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestAdminState.setStatus('mandatory')
apsTestOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestOperationalState.setStatus('mandatory')
apsTestUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestUsageState.setStatus('mandatory')
apsTestSetupTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11), )
if mibBuilder.loadTexts: apsTestSetupTable.setStatus('mandatory')
apsTestSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"), (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"))
if mibBuilder.loadTexts: apsTestSetupEntry.setStatus('mandatory')
apsTestPurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestPurpose.setStatus('mandatory')
apsTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("card", 0), ("manual", 1), ("localLoop", 2), ("remoteLoop", 3), ("externalLoop", 4), ("payloadLoop", 5), ("remoteLoopThisTrib", 6), ("v54RemoteLoop", 7), ("pn127RemoteLoop", 8))).clone('card')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestType.setStatus('mandatory')
apsTestFrmSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 4096)).clone(1024)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestFrmSize.setStatus('mandatory')
apsTestFrmPatternType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ccitt32kBitPattern", 0), ("ccitt8MBitPattern", 1), ("customizedPattern", 2))).clone('ccitt32kBitPattern')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestFrmPatternType.setStatus('mandatory')
apsTestCustomizedPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 5), Hex().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1431655765)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestCustomizedPattern.setStatus('mandatory')
apsTestDataStartDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1814400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestDataStartDelay.setStatus('mandatory')
apsTestDisplayInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 30240)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestDisplayInterval.setStatus('mandatory')
apsTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30240)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsTestDuration.setStatus('mandatory')
apsTestResultsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12), )
if mibBuilder.loadTexts: apsTestResultsTable.setStatus('mandatory')
apsTestResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"), (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"))
if mibBuilder.loadTexts: apsTestResultsEntry.setStatus('mandatory')
apsTestElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestElapsedTime.setStatus('mandatory')
apsTestTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestTimeRemaining.setStatus('mandatory')
apsTestCauseOfTermination = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("testTimeExpired", 0), ("stoppedByOperator", 1), ("unknown", 2), ("neverStarted", 3), ("testRunning", 4), ("hardwareReconfigured", 5))).clone('neverStarted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestCauseOfTermination.setStatus('mandatory')
apsTestBitsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 4), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestBitsTx.setStatus('mandatory')
apsTestBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 5), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestBytesTx.setStatus('mandatory')
apsTestFrmTx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 6), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestFrmTx.setStatus('mandatory')
apsTestBitsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 7), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestBitsRx.setStatus('mandatory')
apsTestBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 8), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestBytesRx.setStatus('mandatory')
apsTestFrmRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 9), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestFrmRx.setStatus('mandatory')
apsTestErroredFrmRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 10), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestErroredFrmRx.setStatus('mandatory')
apsTestBitErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 11), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTestBitErrorRate.setStatus('mandatory')
apsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1))
apsGroupBF = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6))
apsGroupBF00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6, 1))
apsGroupBF00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6, 1, 2))
apsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3))
apsCapabilitiesBF = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6))
apsCapabilitiesBF00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6, 1))
apsCapabilitiesBF00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-ApsMIB", apsSignalDegradeRatio=apsSignalDegradeRatio, apsNearEndRequestChannel=apsNearEndRequestChannel, apsFarEndRequestChannel=apsFarEndRequestChannel, apsTestElapsedTime=apsTestElapsedTime, apsControlStatus=apsControlStatus, apsUnknownStatus=apsUnknownStatus, apsCidDataTable=apsCidDataTable, apsAvailabilityStatus=apsAvailabilityStatus, apsGroupBF=apsGroupBF, apsTestStateTable=apsTestStateTable, apsOperTable=apsOperTable, apsRowStatusTable=apsRowStatusTable, apsSwitchovers=apsSwitchovers, apsTestBitErrorRate=apsTestBitErrorRate, apsTestFrmSize=apsTestFrmSize, apsTestAdminState=apsTestAdminState, apsRowStatusEntry=apsRowStatusEntry, apsTestPurpose=apsTestPurpose, apsProtectionLine=apsProtectionLine, apsTestSetupTable=apsTestSetupTable, apsMIB=apsMIB, apsProtocolFailureAlarm=apsProtocolFailureAlarm, apsTestRowStatus=apsTestRowStatus, apsStateEntry=apsStateEntry, apsWorkingLine=apsWorkingLine, apsTestRowStatusEntry=apsTestRowStatusEntry, apsStandbyStatus=apsStandbyStatus, apsGroup=apsGroup, apsTestBytesTx=apsTestBytesTx, apsTestOperationalState=apsTestOperationalState, apsProceduralStatus=apsProceduralStatus, apsTestDataStartDelay=apsTestDataStartDelay, apsCustomerIdentifier=apsCustomerIdentifier, apsTestDisplayInterval=apsTestDisplayInterval, apsTestCauseOfTermination=apsTestCauseOfTermination, apsTestBitsRx=apsTestBitsRx, apsGroupBF00A=apsGroupBF00A, apsMode=apsMode, apsStorageType=apsStorageType, apsNearEndRequest=apsNearEndRequest, apsTestBitsTx=apsTestBitsTx, apsWaitToRestorePeriod=apsWaitToRestorePeriod, apsTestStateEntry=apsTestStateEntry, apsComponentName=apsComponentName, apsAdminState=apsAdminState, apsAlarmStatus=apsAlarmStatus, apsApplicationFramerName=apsApplicationFramerName, apsOperationalState=apsOperationalState, apsTestFrmRx=apsTestFrmRx, apsTestFrmTx=apsTestFrmTx, apsUsageState=apsUsageState, apsRevertive=apsRevertive, apsCidDataEntry=apsCidDataEntry, apsCapabilitiesBF00A=apsCapabilitiesBF00A, apsTestResultsTable=apsTestResultsTable, apsRowStatus=apsRowStatus, apsIndex=apsIndex, apsProvEntry=apsProvEntry, apsTestCustomizedPattern=apsTestCustomizedPattern, apsTestFrmPatternType=apsTestFrmPatternType, apsTestSetupEntry=apsTestSetupEntry, apsProvTable=apsProvTable, apsTestUsageState=apsTestUsageState, apsStateTable=apsStateTable, apsTestComponentName=apsTestComponentName, apsNearEndRxActiveLine=apsNearEndRxActiveLine, apsFarEndRequest=apsFarEndRequest, apsTestTimeRemaining=apsTestTimeRemaining, apsModeMismatchAlarm=apsModeMismatchAlarm, apsCapabilitiesBF=apsCapabilitiesBF, apsSdOnLines=apsSdOnLines, apsTestErroredFrmRx=apsTestErroredFrmRx, apsTimeUntilRestore=apsTimeUntilRestore, apsHoldOffTime=apsHoldOffTime, apsTestBytesRx=apsTestBytesRx, apsTestRowStatusTable=apsTestRowStatusTable, apsTestResultsEntry=apsTestResultsEntry, apsTest=apsTest, apsTestIndex=apsTestIndex, apsCapabilitiesBF00=apsCapabilitiesBF00, aps=aps, apsTestType=apsTestType, apsTestDuration=apsTestDuration, apsGroupBF00=apsGroupBF00, apsTestStorageType=apsTestStorageType, apsCapabilities=apsCapabilities, apsOperEntry=apsOperEntry)