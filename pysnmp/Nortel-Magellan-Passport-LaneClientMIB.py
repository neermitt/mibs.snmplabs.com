#
# PySNMP MIB module Nortel-Magellan-Passport-LaneClientMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-LaneClientMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:18:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
StorageType, Integer32, MacAddress, InterfaceIndex, RowPointer, RowStatus, Unsigned32, Counter32, DisplayString = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "StorageType", "Integer32", "MacAddress", "InterfaceIndex", "RowPointer", "RowStatus", "Unsigned32", "Counter32", "DisplayString")
Link, DashedHexString, HexString, NonReplicated, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "DashedHexString", "HexString", "NonReplicated", "AsciiString")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, iso, Gauge32, IpAddress, Bits, ObjectIdentity, Unsigned32, Counter64, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "Gauge32", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
laneClientMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71))
lec = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124))
lecRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1), )
if mibBuilder.loadTexts: lecRowStatusTable.setStatus('mandatory')
lecRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecRowStatusEntry.setStatus('mandatory')
lecRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecRowStatus.setStatus('mandatory')
lecComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecComponentName.setStatus('mandatory')
lecStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecStorageType.setStatus('mandatory')
lecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: lecIndex.setStatus('mandatory')
lecCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10), )
if mibBuilder.loadTexts: lecCidDataTable.setStatus('mandatory')
lecCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecCidDataEntry.setStatus('mandatory')
lecCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecCustomerIdentifier.setStatus('mandatory')
lecIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11), )
if mibBuilder.loadTexts: lecIfEntryTable.setStatus('mandatory')
lecIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecIfEntryEntry.setStatus('mandatory')
lecIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecIfAdminStatus.setStatus('mandatory')
lecIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecIfIndex.setStatus('mandatory')
lecMpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12), )
if mibBuilder.loadTexts: lecMpTable.setStatus('mandatory')
lecMpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecMpEntry.setStatus('mandatory')
lecLinkToProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecLinkToProtocolPort.setStatus('mandatory')
lecProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13), )
if mibBuilder.loadTexts: lecProvTable.setStatus('mandatory')
lecProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecProvEntry.setStatus('mandatory')
lecLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unspecified", 1), ("ethernet", 2))).clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecLanType.setStatus('mandatory')
lecMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1516, 1580, 4544, 9234, 18190))).clone(namedValues=NamedValues(("unspecified", 0), ("n1516", 1516), ("n1580", 1580), ("n4544", 4544), ("n9234", 9234), ("n18190", 18190))).clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecMaxFrameSize.setStatus('mandatory')
lecLanName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 3), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecLanName.setStatus('mandatory')
lecV2Capable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecV2Capable.setStatus('mandatory')
lecLecsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 5), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecLecsAddress.setStatus('mandatory')
lecLesAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 6), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecLesAddress.setStatus('mandatory')
lecMaxDataSvcs = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1018)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecMaxDataSvcs.setStatus('mandatory')
lecMaxArpEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32, 10240)).clone(5120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecMaxArpEntries.setStatus('mandatory')
lecIlsForwarder = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 9), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecIlsForwarder.setStatus('mandatory')
lecStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15), )
if mibBuilder.loadTexts: lecStateTable.setStatus('mandatory')
lecStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecStateEntry.setStatus('mandatory')
lecAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecAdminState.setStatus('mandatory')
lecOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecOperationalState.setStatus('mandatory')
lecUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecUsageState.setStatus('mandatory')
lecOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16), )
if mibBuilder.loadTexts: lecOperStatusTable.setStatus('mandatory')
lecOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecOperStatusEntry.setStatus('mandatory')
lecSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecSnmpOperStatus.setStatus('mandatory')
lecOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17), )
if mibBuilder.loadTexts: lecOperTable.setStatus('mandatory')
lecOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecOperEntry.setStatus('mandatory')
lecActualLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unspecified", 1), ("ethernet", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualLanType.setStatus('mandatory')
lecActualMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1516, 1580, 4544, 9234, 18190))).clone(namedValues=NamedValues(("unspecified", 0), ("n1516", 1516), ("n1580", 1580), ("n4544", 4544), ("n9234", 9234), ("n18190", 18190)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualMaxFrameSize.setStatus('mandatory')
lecActualLanName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 3), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualLanName.setStatus('mandatory')
lecElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecElanId.setStatus('mandatory')
lecActualV2Capable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualV2Capable.setStatus('mandatory')
lecConfigurationSource = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("usedProvisionedLecsAddress", 1), ("gotLecsAddressViaIlmi", 2), ("usedWellKnownLecsAddress", 3), ("usedLecsPvc", 4), ("didNotUseLecs", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConfigurationSource.setStatus('mandatory')
lecActualLecsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 7), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualLecsAddress.setStatus('mandatory')
lecActualLesAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 8), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecActualLesAddress.setStatus('mandatory')
lecAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 9), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecAtmAddress.setStatus('mandatory')
lecMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 10), MacAddress().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecMacAddress.setStatus('mandatory')
lecLecId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65279))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLecId.setStatus('mandatory')
lecInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("initialState", 1), ("lecsConnect", 2), ("configure", 3), ("join", 4), ("initialRegistration", 5), ("busConnect", 6), ("operational", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecInterfaceState.setStatus('mandatory')
lecLastFailureResponseCode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("none", 1), ("timeout", 2), ("undefinedError", 3), ("versionNotSupported", 4), ("invalidRequestParameters", 5), ("duplicateLanDestination", 6), ("duplicateAtmAddress", 7), ("insufficientResources", 8), ("accessDenied", 9), ("invalidRequesterId", 10), ("invalidLanDestination", 11), ("invalidAtmAddress", 12), ("noConfiguration", 13), ("leConfigureError", 14), ("insufficientInformation", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLastFailureResponseCode.setStatus('mandatory')
lecLastFailureState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("initialState", 1), ("lecsConnect", 2), ("configure", 3), ("join", 4), ("initialRegistration", 5), ("busConnect", 6), ("operational", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLastFailureState.setStatus('mandatory')
lecStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18), )
if mibBuilder.loadTexts: lecStatsTable.setStatus('mandatory')
lecStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"))
if mibBuilder.loadTexts: lecStatsEntry.setStatus('mandatory')
lecArpRequestsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpRequestsOut.setStatus('mandatory')
lecArpRepliesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpRepliesIn.setStatus('mandatory')
lecArpRequestsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpRequestsIn.setStatus('mandatory')
lecArpRepliesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpRepliesOut.setStatus('mandatory')
lecControlFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecControlFramesOut.setStatus('mandatory')
lecControlFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecControlFramesIn.setStatus('mandatory')
lecSvcFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecSvcFailures.setStatus('mandatory')
lecCurrDataSvcs = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecCurrDataSvcs.setStatus('mandatory')
lecPeakDataSvcs = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecPeakDataSvcs.setStatus('mandatory')
lecCurrArpEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecCurrArpEntries.setStatus('mandatory')
lecPeakArpEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecPeakArpEntries.setStatus('mandatory')
lecBadControlFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecBadControlFrames.setStatus('mandatory')
lecProtocolViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecProtocolViolations.setStatus('mandatory')
lecUnsupportedTlvs = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecUnsupportedTlvs.setStatus('mandatory')
lecLeArp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2))
lecLeArpRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1), )
if mibBuilder.loadTexts: lecLeArpRowStatusTable.setStatus('mandatory')
lecLeArpRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecLeArpIndex"))
if mibBuilder.loadTexts: lecLeArpRowStatusEntry.setStatus('mandatory')
lecLeArpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpRowStatus.setStatus('mandatory')
lecLeArpComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpComponentName.setStatus('mandatory')
lecLeArpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpStorageType.setStatus('mandatory')
lecLeArpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 10), DashedHexString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6))
if mibBuilder.loadTexts: lecLeArpIndex.setStatus('mandatory')
lecLeArpOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10), )
if mibBuilder.loadTexts: lecLeArpOperTable.setStatus('mandatory')
lecLeArpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecLeArpIndex"))
if mibBuilder.loadTexts: lecLeArpOperEntry.setStatus('mandatory')
lecLeArpAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 1), HexString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpAtmAddress.setStatus('mandatory')
lecLeArpIsRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpIsRemoteAddress.setStatus('mandatory')
lecLeArpConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecLeArpConnectionId.setStatus('mandatory')
lecConn = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3))
lecConnRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1), )
if mibBuilder.loadTexts: lecConnRowStatusTable.setStatus('mandatory')
lecConnRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"))
if mibBuilder.loadTexts: lecConnRowStatusEntry.setStatus('mandatory')
lecConnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnRowStatus.setStatus('mandatory')
lecConnComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnComponentName.setStatus('mandatory')
lecConnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnStorageType.setStatus('mandatory')
lecConnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1022)))
if mibBuilder.loadTexts: lecConnIndex.setStatus('mandatory')
lecConnOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10), )
if mibBuilder.loadTexts: lecConnOperTable.setStatus('mandatory')
lecConnOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"))
if mibBuilder.loadTexts: lecConnOperEntry.setStatus('mandatory')
lecConnRemoteAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 1), HexString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnRemoteAtmAddress.setStatus('mandatory')
lecConnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4292967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnAge.setStatus('mandatory')
lecConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("configurationDirectVcc", 1), ("controlDirectVcc", 2), ("controlDistributeVcc", 3), ("dataDirectVcc", 4), ("defaultMulticastSendVcc", 5), ("multicastForward", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnType.setStatus('mandatory')
lecConnStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11), )
if mibBuilder.loadTexts: lecConnStatsTable.setStatus('mandatory')
lecConnStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"))
if mibBuilder.loadTexts: lecConnStatsEntry.setStatus('mandatory')
lecConnOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnOutFrames.setStatus('mandatory')
lecConnInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnInFrames.setStatus('mandatory')
lecConnAtmCon = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2))
lecConnAtmConRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1), )
if mibBuilder.loadTexts: lecConnAtmConRowStatusTable.setStatus('mandatory')
lecConnAtmConRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnAtmConIndex"))
if mibBuilder.loadTexts: lecConnAtmConRowStatusEntry.setStatus('mandatory')
lecConnAtmConRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnAtmConRowStatus.setStatus('mandatory')
lecConnAtmConComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnAtmConComponentName.setStatus('mandatory')
lecConnAtmConStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnAtmConStorageType.setStatus('mandatory')
lecConnAtmConIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: lecConnAtmConIndex.setStatus('mandatory')
lecConnAtmConOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10), )
if mibBuilder.loadTexts: lecConnAtmConOperTable.setStatus('mandatory')
lecConnAtmConOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"), (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnAtmConIndex"))
if mibBuilder.loadTexts: lecConnAtmConOperEntry.setStatus('mandatory')
lecConnAtmConNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConnAtmConNextHop.setStatus('mandatory')
laneClientGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1))
laneClientGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5))
laneClientGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5, 1))
laneClientGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5, 1, 2))
laneClientCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3))
laneClientCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5))
laneClientCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5, 1))
laneClientCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-LaneClientMIB", lecLesAddress=lecLesAddress, lecProvTable=lecProvTable, lecConnRowStatusTable=lecConnRowStatusTable, lecLeArpOperEntry=lecLeArpOperEntry, lecSnmpOperStatus=lecSnmpOperStatus, lecBadControlFrames=lecBadControlFrames, lecStatsTable=lecStatsTable, lecMaxArpEntries=lecMaxArpEntries, lecMpEntry=lecMpEntry, lecLeArpOperTable=lecLeArpOperTable, lecInterfaceState=lecInterfaceState, lecActualV2Capable=lecActualV2Capable, lecConnAtmConOperEntry=lecConnAtmConOperEntry, lecOperationalState=lecOperationalState, lecCidDataTable=lecCidDataTable, lecV2Capable=lecV2Capable, lecOperStatusEntry=lecOperStatusEntry, lecConnRowStatus=lecConnRowStatus, lecConnAtmCon=lecConnAtmCon, lecStatsEntry=lecStatsEntry, lec=lec, lecConnOutFrames=lecConnOutFrames, lecConnAtmConRowStatusTable=lecConnAtmConRowStatusTable, lecConnAge=lecConnAge, lecLeArpConnectionId=lecLeArpConnectionId, lecLeArpIsRemoteAddress=lecLeArpIsRemoteAddress, lecSvcFailures=lecSvcFailures, lecCurrDataSvcs=lecCurrDataSvcs, lecActualLecsAddress=lecActualLecsAddress, lecActualMaxFrameSize=lecActualMaxFrameSize, lecRowStatusTable=lecRowStatusTable, lecControlFramesIn=lecControlFramesIn, lecArpRepliesOut=lecArpRepliesOut, lecCidDataEntry=lecCidDataEntry, laneClientCapabilitiesBE00=laneClientCapabilitiesBE00, lecRowStatus=lecRowStatus, lecOperTable=lecOperTable, laneClientCapabilitiesBE00A=laneClientCapabilitiesBE00A, lecControlFramesOut=lecControlFramesOut, lecCustomerIdentifier=lecCustomerIdentifier, lecIndex=lecIndex, lecArpRequestsOut=lecArpRequestsOut, lecConnIndex=lecConnIndex, lecConnOperTable=lecConnOperTable, lecProtocolViolations=lecProtocolViolations, lecAdminState=lecAdminState, lecConnAtmConStorageType=lecConnAtmConStorageType, lecConnStatsEntry=lecConnStatsEntry, lecLeArpRowStatusTable=lecLeArpRowStatusTable, lecActualLesAddress=lecActualLesAddress, lecOperStatusTable=lecOperStatusTable, lecCurrArpEntries=lecCurrArpEntries, lecStateEntry=lecStateEntry, lecConfigurationSource=lecConfigurationSource, lecLastFailureResponseCode=lecLastFailureResponseCode, lecLecId=lecLecId, lecOperEntry=lecOperEntry, lecMpTable=lecMpTable, laneClientCapabilities=laneClientCapabilities, lecLanType=lecLanType, lecArpRepliesIn=lecArpRepliesIn, lecArpRequestsIn=lecArpRequestsIn, lecConnStorageType=lecConnStorageType, lecAtmAddress=lecAtmAddress, lecConnOperEntry=lecConnOperEntry, lecPeakDataSvcs=lecPeakDataSvcs, lecLeArpIndex=lecLeArpIndex, lecUnsupportedTlvs=lecUnsupportedTlvs, lecIfEntryTable=lecIfEntryTable, lecConnStatsTable=lecConnStatsTable, lecActualLanType=lecActualLanType, lecConnAtmConIndex=lecConnAtmConIndex, lecLeArpStorageType=lecLeArpStorageType, lecMaxFrameSize=lecMaxFrameSize, lecLeArpRowStatusEntry=lecLeArpRowStatusEntry, laneClientMIB=laneClientMIB, laneClientCapabilitiesBE=laneClientCapabilitiesBE, lecLeArp=lecLeArp, lecConnAtmConNextHop=lecConnAtmConNextHop, lecConnComponentName=lecConnComponentName, lecUsageState=lecUsageState, lecActualLanName=lecActualLanName, lecConnRemoteAtmAddress=lecConnRemoteAtmAddress, lecElanId=lecElanId, lecProvEntry=lecProvEntry, lecConnAtmConComponentName=lecConnAtmConComponentName, laneClientGroup=laneClientGroup, lecIfEntryEntry=lecIfEntryEntry, laneClientGroupBE=laneClientGroupBE, lecLeArpRowStatus=lecLeArpRowStatus, lecConnRowStatusEntry=lecConnRowStatusEntry, lecLinkToProtocolPort=lecLinkToProtocolPort, lecConnInFrames=lecConnInFrames, lecComponentName=lecComponentName, lecLeArpAtmAddress=lecLeArpAtmAddress, lecLanName=lecLanName, laneClientGroupBE00=laneClientGroupBE00, lecConnAtmConOperTable=lecConnAtmConOperTable, lecIlsForwarder=lecIlsForwarder, laneClientGroupBE00A=laneClientGroupBE00A, lecLecsAddress=lecLecsAddress, lecStateTable=lecStateTable, lecIfAdminStatus=lecIfAdminStatus, lecConn=lecConn, lecLastFailureState=lecLastFailureState, lecPeakArpEntries=lecPeakArpEntries, lecRowStatusEntry=lecRowStatusEntry, lecIfIndex=lecIfIndex, lecConnAtmConRowStatus=lecConnAtmConRowStatus, lecStorageType=lecStorageType, lecMacAddress=lecMacAddress, lecConnType=lecConnType, lecMaxDataSvcs=lecMaxDataSvcs, lecLeArpComponentName=lecLeArpComponentName, lecConnAtmConRowStatusEntry=lecConnAtmConRowStatusEntry)