#
# PySNMP MIB module PDN-MPE-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpe_bridge, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-bridge")
VnidRange, = mibBuilder.importSymbols("PDN-TC", "VnidRange")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, Counter64, Bits, ModuleIdentity, Unsigned32, TimeTicks, Gauge32, NotificationType, Counter32, ObjectIdentity, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Counter64", "Bits", "ModuleIdentity", "Unsigned32", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
mpePdnBridgeGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1))
mpePdnBridgeMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 2))
mpePdnDot1dGenericBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1))
mpePdnDot1dTpFdb = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2))
mpePdnDot1dBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnDot1dBridgeTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dBridgeTable.setDescription('A table that contains generic information about the bridge.')
mpePdnDot1dBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnDot1dBridgeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dBridgeEntry.setDescription('A list of information for the bridge.')
mpePdnDot1dBaseBridgeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseBridgeAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dBaseBridgeAddress.setDescription('The MAC address used by this bridge when it must be referred to in a unique fashion. It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge. However it is only required to be unique.')
mpePdnDot1dBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseNumPorts.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dBaseNumPorts.setDescription('The number of ports controlled by this bridging entity.')
mpePdnDot1dBaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseType.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dBaseType.setDescription('Indicates what type of bridging this bridge can perform.')
mpePdnDot1dTpLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpLearnedEntryDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpLearnedEntryDiscards.setDescription('The total number of Forwarding Database entries, which have been or would have been learned, but have been discarded due to a lack of space to store them in the Forwarding Database. If this counter is increasing, it indicates that the Forwarding Database is regularly becoming full (a condition which has unpleasant performance effects on the subnetwork). If this counter has a significant value but is not presently increasing, it indicates that the problem has been occurring but is not persistent.')
mpePdnDot1dTpAgeingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingTime.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingTime.setDescription('The timeout period in seconds for aging out dynamically learned forwarding information. 802.1D-1990 recommends a default of 300 seconds.')
mpePdnDot1dTpAgeingCleanupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 500000)).clone(150)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingCleanupTime.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingCleanupTime.setDescription(' mpePdnDot1dTpEntryAgeingCleanupupTime is the length of time before an entry is removed from the bridge . This parameter is typically set to one-half of the bridge Ageing time.')
mpePdnDot1dTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1), )
if mibBuilder.loadTexts: mpePdnDot1dTpFdbTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbTable.setDescription('A table that contains information about unicast entries for which the bridge has forwarding and/or filtering information. This information is used by the transparent bridging function in determining how to propagate a received frame.')
mpePdnDot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbAddress"), (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbVnidId"))
if mibBuilder.loadTexts: mpePdnDot1dTpFdbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbEntry.setDescription('Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information.')
mpePdnDot1dTpFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAddress.setDescription('A unicast MAC address for which the bridge has forwarding and/or filtering information.')
mpePdnDot1dTpFdbVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 2), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbVnidId.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbVnidId.setDescription('The VNID Id number of the virtual network for which the bridge has forwarding and/or filtering information.')
mpePdnDot1dTpFdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbIfIndex.setDescription('The ifIndex of the interface associated with the mac address and vlan-id.')
mpePdnDot1dTpFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbStatus.setDescription("The status of this entry. The meanings of the values are: other(1) : none of the following. This would include the case where some other MIB object (not the corresponding instance of mpePdnDot1dTpFdbPort, nor an entry in the mpePdnDot1dStaticTable) in being used to determine if and how frames addressed to the value of the corresponding instance of mpePdnDot1dTpFdbAddress are being forwarded. invalid(2) : this entry is not longer valid (e.g., it was learned but has since aged-out), but has not yet been flushed from the table. learned(3) : the value of the corresponding instance of mpePdnDot1dTpFdbPort was learned, and is being used. self(4) : the value of the corresponding instance of mpePdnDot1dTpFdbAddress represents one of the bridge's addresses. The corresponding instance of mpePdnDot1dTpFdbPort indicates which of the bridge's ports has this address. mgmt(5) : the value of the corresponding instance of mpePdnDot1dTpFdbAddress is also the value of an existing instance of mpePdnDot1dStaticAddress.")
mpePdnDot1dTpFdbAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAgeTime.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAgeTime.setDescription('The amount of time in seconds that this entry is in the Bridge table')
mpePdnDot1dTpFdbFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("permanentDHCP", 2), ("permanentCONFIGURED", 3), ("dynamic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbFlags.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnDot1dTpFdbFlags.setDescription('This object indicates the type of entry in the Bridge table. permanentDHCP -- Entry added due to DHCP client permanentCONFIGURED -- Entry added by User dynamic -- Dynamic Entry ')
mibBuilder.exportSymbols("PDN-MPE-BRIDGE-MIB", mpePdnDot1dTpLearnedEntryDiscards=mpePdnDot1dTpLearnedEntryDiscards, mpePdnDot1dTpFdbEntry=mpePdnDot1dTpFdbEntry, mpePdnDot1dBaseType=mpePdnDot1dBaseType, mpePdnDot1dTpFdbIfIndex=mpePdnDot1dTpFdbIfIndex, mpePdnDot1dTpFdbAgeTime=mpePdnDot1dTpFdbAgeTime, mpePdnBridgeGenericMIBObjects=mpePdnBridgeGenericMIBObjects, mpePdnDot1dTpAgeingCleanupTime=mpePdnDot1dTpAgeingCleanupTime, mpePdnDot1dTpFdbVnidId=mpePdnDot1dTpFdbVnidId, mpePdnDot1dTpFdbStatus=mpePdnDot1dTpFdbStatus, mpePdnDot1dBridgeTable=mpePdnDot1dBridgeTable, mpePdnDot1dTpFdbAddress=mpePdnDot1dTpFdbAddress, mpePdnDot1dTpAgeingTime=mpePdnDot1dTpAgeingTime, mpePdnDot1dBaseBridgeAddress=mpePdnDot1dBaseBridgeAddress, mpePdnBridgeMIBTraps=mpePdnBridgeMIBTraps, mpePdnDot1dTpFdbFlags=mpePdnDot1dTpFdbFlags, mpePdnDot1dBaseNumPorts=mpePdnDot1dBaseNumPorts, mpePdnDot1dTpFdb=mpePdnDot1dTpFdb, mpePdnDot1dTpFdbTable=mpePdnDot1dTpFdbTable, mpePdnDot1dBridgeEntry=mpePdnDot1dBridgeEntry, mpePdnDot1dGenericBridge=mpePdnDot1dGenericBridge)
