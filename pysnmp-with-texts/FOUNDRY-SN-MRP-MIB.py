#
# PySNMP MIB module FOUNDRY-SN-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-MRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Bits, Counter64, NotificationType, ModuleIdentity, Unsigned32, IpAddress, ObjectIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Bits", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snMetroRing = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29))
snMetroRing.setRevisions(('2010-06-02 00:00', '2007-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snMetroRing.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', '',))
if mibBuilder.loadTexts: snMetroRing.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snMetroRing.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snMetroRing.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snMetroRing.setDescription("Management Information Base module for metro ring configuration and statistics. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snMetroRingGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 1))
snMetroRingTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2))
snMetroRingTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1), )
if mibBuilder.loadTexts: snMetroRingTable.setStatus('current')
if mibBuilder.loadTexts: snMetroRingTable.setDescription('Metro ring table.')
snMetroRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-MRP-MIB", "snMetroRingVLanId"), (0, "FOUNDRY-SN-MRP-MIB", "snMetroRingId"))
if mibBuilder.loadTexts: snMetroRingEntry.setStatus('current')
if mibBuilder.loadTexts: snMetroRingEntry.setDescription('An entry of the metro ring table.')
snMetroRingVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: snMetroRingVLanId.setStatus('current')
if mibBuilder.loadTexts: snMetroRingVLanId.setDescription('Identifier of a VLAN that controls the metro ring.')
snMetroRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: snMetroRingId.setStatus('current')
if mibBuilder.loadTexts: snMetroRingId.setDescription('Metro ring identifier.')
snMetroRingConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingConfigState.setStatus('current')
if mibBuilder.loadTexts: snMetroRingConfigState.setDescription('Metro ring state.')
snMetroRingRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("master", 2), ("member", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingRole.setStatus('current')
if mibBuilder.loadTexts: snMetroRingRole.setDescription('Metro ring role. other(1).........none of the cases in below. master(2)........device which originates RHP packets. member(3)........device which forwards RHP packets.')
snMetroRingHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingHelloTime.setStatus('current')
if mibBuilder.loadTexts: snMetroRingHelloTime.setDescription('The time interval to periodically transmit ring health protocol (RHP). Each unit is millisecond.')
snMetroRingPreforwardingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPreforwardingTime.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPreforwardingTime.setDescription('The time interval of which a metro ring port is staying in preforwarding state before changing to forwarding state. Each unit is millisecond.')
snMetroRingPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 7), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPort1.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPort1.setDescription('The ifIndex value of port 1 to configure into the metro ring.')
snMetroRingPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 8), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPort2.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPort2.setDescription('The ifIndex value of port 2 to configure into the metro ring.')
snMetroRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingName.setStatus('current')
if mibBuilder.loadTexts: snMetroRingName.setDescription('The metro ring description.')
snMetroRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingRowStatus.setStatus('current')
if mibBuilder.loadTexts: snMetroRingRowStatus.setDescription("This object is used to create and delete row in the table and control if they are used. The values that can be written are: delete(3)...deletes the row create(4)...creates a new row If the row exists, then a SET with value of create(4) returns error 'badValue'. Deleted rows go away immediately. The following values can be returned on reads: noSuchName...no such row other(1).....some other cases valid(2)....the row exists and is valid")
snMetroRingOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingOperState.setStatus('current')
if mibBuilder.loadTexts: snMetroRingOperState.setDescription('Metro ring operational state.')
snMetroRingTopoGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingTopoGroupId.setStatus('current')
if mibBuilder.loadTexts: snMetroRingTopoGroupId.setDescription('Topology group ID that controls the metro ring.')
snMetroRingRHPTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingRHPTransmitted.setStatus('current')
if mibBuilder.loadTexts: snMetroRingRHPTransmitted.setDescription('Ring health protocol (RHP) transmitted counter.')
snMetroRingRHPReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingRHPReceived.setStatus('current')
if mibBuilder.loadTexts: snMetroRingRHPReceived.setDescription('Ring health protocol (RHP) received counter.')
snMetroRingStateChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingStateChanged.setStatus('current')
if mibBuilder.loadTexts: snMetroRingStateChanged.setDescription('Ring state changed counter.')
snMetroRingTCRBPDUReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingTCRBPDUReceived.setStatus('current')
if mibBuilder.loadTexts: snMetroRingTCRBPDUReceived.setDescription('Topology change protocol received counter.')
snMetroRingPriPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 17), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPort.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPriPort.setDescription('The ifIndex value of primary port.')
snMetroRingSecPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 18), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPort.setStatus('current')
if mibBuilder.loadTexts: snMetroRingSecPort.setDescription('The ifIndex value of secondary port.')
snMetroRingPriPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("preforwarding", 2), ("forwarding", 3), ("blocking", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortState.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPriPortState.setDescription('Metro ring primary port state. other(1)...........none of the cases in below. preforwarding(2)...port transmits RHP packets, port does not transmit data packets. forwarding(3)......port transmits RHP and data packets. blocking(4)........port receives RHP packets, port does not receive data packets. disabled(5)........port is disabled from metro ring.')
snMetroRingSecPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("preforwarding", 2), ("forwarding", 3), ("blocking", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortState.setStatus('current')
if mibBuilder.loadTexts: snMetroRingSecPortState.setDescription('Metro ring secondary port state. other(1)...........none of the cases in below. preforwarding(2)...port transmits RHP packets, port does not transmit data packets. forwarding(3)......port transmits RHP and data packets. blocking(4)........port receives RHP packets, port does not receive data packets. disabled(5)........port is disabled from metro ring.')
snMetroRingPriPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("regular", 2), ("tunnel", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortType.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPriPortType.setDescription('Metro ring primary port type. other(1).....none of the cases in below. regular(2)...port is configured to operate on a single ring. tunnel(3)....port is configured to operate on multiple rings.')
snMetroRingSecPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("regular", 2), ("tunnel", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortType.setStatus('current')
if mibBuilder.loadTexts: snMetroRingSecPortType.setDescription('Metro ring secondary port type. other(1).....none of the cases in below. regular(2)...port is configured to operate on a single ring. tunnel(3)....port is configured to operate on multiple rings.')
snMetroRingPriPortActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 23), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortActivePort.setStatus('current')
if mibBuilder.loadTexts: snMetroRingPriPortActivePort.setDescription('The ifIndex value of active primary port.')
snMetroRingSecPortActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 24), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortActivePort.setStatus('current')
if mibBuilder.loadTexts: snMetroRingSecPortActivePort.setDescription('The ifIndex value of active secondary port.')
mibBuilder.exportSymbols("FOUNDRY-SN-MRP-MIB", snMetroRingTableObjects=snMetroRingTableObjects, snMetroRingRHPReceived=snMetroRingRHPReceived, snMetroRingPriPortActivePort=snMetroRingPriPortActivePort, snMetroRingHelloTime=snMetroRingHelloTime, snMetroRingStateChanged=snMetroRingStateChanged, snMetroRingSecPort=snMetroRingSecPort, snMetroRingEntry=snMetroRingEntry, snMetroRingPort1=snMetroRingPort1, snMetroRingGlobalObjects=snMetroRingGlobalObjects, snMetroRingPort2=snMetroRingPort2, snMetroRingTCRBPDUReceived=snMetroRingTCRBPDUReceived, snMetroRingOperState=snMetroRingOperState, snMetroRingSecPortType=snMetroRingSecPortType, snMetroRingSecPortActivePort=snMetroRingSecPortActivePort, snMetroRingPreforwardingTime=snMetroRingPreforwardingTime, snMetroRingName=snMetroRingName, snMetroRingPriPortType=snMetroRingPriPortType, snMetroRingTable=snMetroRingTable, snMetroRingTopoGroupId=snMetroRingTopoGroupId, snMetroRingVLanId=snMetroRingVLanId, snMetroRingId=snMetroRingId, snMetroRingRowStatus=snMetroRingRowStatus, snMetroRingPriPortState=snMetroRingPriPortState, PYSNMP_MODULE_ID=snMetroRing, snMetroRingRole=snMetroRingRole, snMetroRingSecPortState=snMetroRingSecPortState, snMetroRingRHPTransmitted=snMetroRingRHPTransmitted, snMetroRingConfigState=snMetroRingConfigState, snMetroRing=snMetroRing, snMetroRingPriPort=snMetroRingPriPort)
