#
# PySNMP MIB module HPN-ICF-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FCOE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, Gauge32, ObjectIdentity, Integer32, IpAddress, Unsigned32, MibIdentifier, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "Bits", "Counter64")
RowStatus, MacAddress, TruthValue, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TruthValue", "TextualConvention", "DisplayString", "TimeStamp")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
hpnicfFCoE = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120))
hpnicfFCoE.setRevisions(('2012-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfFCoE.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfFCoE.setLastUpdated('201203280000Z')
if mibBuilder.loadTexts: hpnicfFCoE.setOrganization('')
if mibBuilder.loadTexts: hpnicfFCoE.setContactInfo('')
if mibBuilder.loadTexts: hpnicfFCoE.setDescription('This MIB module is for configuring and monitoring Fibre Channel over Ethernet (FCoE) related entities. This MIB defines a Virtual FC (VFC) Interface as an object that represents either a VF_Port or a VE_Port on a FCoE Forwarder (FCF). VFC interfaces can be created either statically (by management request) or dynamically (at the time of FIP based FLOGI or ELP request). Other terminologies used in this MIB are defined by the Hpnicf FCoE standard, as defined in the FC-BB-5 specification. This MIB also supports configuration of the following objects: - Mapping of FCoE VLAN-ID used to carry traffic for a Fabric - FC-MAP value used by the FCF operating in FPMA mode - FIP snooping related objects')
hpnicfFCoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1))
hpnicfFCoEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1))
class HpnicfFCoEVfcBindType(TextualConvention, Integer32):
    description = "Defines the different methods to identify (or bind to) - the ENode associated with a particular VF_Port VFC - the remote-FCF associated with a particular VE_Port VFC interfaceIndex(1) - This type is used only when an ENode or remote-FCF is directly connected to the local FCF via one of the local Ethernet interfaces, in which case the value contains the ifIndex of said Ethernet interface. macAddress(2) - This type is used when an ENode or remote-FCF is reachable from the local FCF over a (Layer-2) Ethernet network. A FIP frame from an ENode or remote-FCF is associated to a VFC only if the frame's source MAC address is the same as the MAC Address bound on that VFC."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

hpnicfFCoECfgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfFCoECfgTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgTable.setDescription('This table facilitates configuration of FCoE parameters on a per Fibre Channel management instance.')
hpnicfFCoECfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"))
if mibBuilder.loadTexts: hpnicfFCoECfgEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgEntry.setDescription('There is one entry in this table for each Fibre Channel management instance.')
hpnicfFCoECfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgFcmap.setReference('Fibre Channel - Backbone - 5 (FC-BB-5), section 7.6 and table 47')
if mibBuilder.loadTexts: hpnicfFCoECfgFcmap.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgFcmap.setDescription('This object configures the FC-MAP value used by the FCF when operating in FPMA mode. The default value is 0EFC00h, as written in the standard.')
hpnicfFCoECfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDynamicVfcCreation.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgDynamicVfcCreation.setDescription("This object is set to 'true' to enable, or 'false' to disable, the dynamic creation of VFC interfaces on this FCF. When set to 'true', VFC interfaces are dynamically created as and when a FIP-based FLOGI or ELP request is received.")
hpnicfFCoECfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDefaultFCFPriority.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgDefaultFCFPriority.setDescription('The FIP priority value advertised by the FCF to ENodes by default. hpnicfFCoEStaticVfcFCFPriority configured for a VFC interface overrides this setting for the ENode associated with the VFC.')
hpnicfFCoECfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgDATov.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgDATov.setDescription('The Discovery_Advertisement_Timeout value configured for the FCF. This is used as the timeout value in seconds by the FCF to send periodic Discovery Advertisements.')
hpnicfFCoECfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("fpmaAndSpma", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoECfgAddressingMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoECfgAddressingMode.setDescription('Addressing mode(s) supported by the FCF. Implementations should fail SetRequests for unsupported modes.')
hpnicfFCoEVLANTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfFCoEVLANTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEVLANTable.setDescription('In fabrics in which VLANs are deployed, this table facilitates configuration of VLAN and Virtual Fabric associations in an FCoE network. In such fabrics, FCoE forwarding for a fabric is over a VLAN in a (Layer-2) Ethernet network. That is, reachability between the ENode/remote-FCF and an FCF for a given fabric is determined by the reachability provided by the Ethernet network on the corresponding VLAN. An active entry in this table indicates which VLAN is used to transport FCoE traffic for a particular Virtual Fabric. If VLANs are not deployed or not enabled, entries in this table are ignored by the bridge. Some implmentations may allow traffic from only one Virtual Fabric to be transported over a given VLAN. Such implementations should prevent multiple entries with the same VLAN-ID from being created in this table. Modifying existing VLAN-Virtual Fabric associations is not possible. The specific row must first be deleted and then a new one created.')
hpnicfFCoEVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEVLANIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFabricIndex"))
if mibBuilder.loadTexts: hpnicfFCoEVLANEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEVLANEntry.setDescription('There is one entry in this table for each VLAN that is designated to transport FCoE traffic for a given Virtual Fabric.')
hpnicfFCoEVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hpnicfFCoEVLANIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEVLANIndex.setDescription('This object identifies the VLAN-ID that the FCoE FCF function is being enabled for.')
hpnicfFCoEFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: hpnicfFCoEFabricIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFabricIndex.setDescription('This object identifies the Fabric Index of the Virtual Fabric traffic which is to be transported over the VLAN identified by hpnicfFCoEVLANIndex.')
hpnicfFCoEVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEVLANOperState.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEVLANOperState.setDescription("Operational state of this VLAN-Virtual Fabric association entry. The 'up' state is achieved when both the Virtual Fabric and VLAN are valid.")
hpnicfFCoEVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEVLANRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEVLANRowStatus.setDescription('The status of this conceptual row. The RowStatus becomes active on successful creation of an entry.')
hpnicfFCoEStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcTable.setDescription('This table facilitates the creation and deletion of static VFC interfaces. While VFCs can be dynamically created based on FIP FLOGI/ELP requests, operators may want to associate certain pre-configured policy for a particular ENode or a remote-FCF. In such cases static VFC creation becomes necessary. In addition to being creating, a static VFC also needs to be associated to an ENode or remote-FCF. The VFC binding provides such an associaton. The binding does not need to be specified when the row for a VFC is created, but may be specified later.')
hpnicfFCoEStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEStaticVfcIndex"))
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcEntry.setDescription('There is one entry in this table for each statically created VFC Interface.')
hpnicfFCoEStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIndex.setDescription('This index uniquely identifies a static VFC entry in this table.')
hpnicfFCoEStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFCFPriority.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFCFPriority.setDescription('If this VFC is for a VF_Port this object is used to configure FCF priority to be advertised to the ENode associated with the VFC.')
hpnicfFCoEStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 3), HpnicfFCoEVfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindType.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindType.setDescription('The mechanism to identify the ENode associated with this VFC if it is of type VF_Port or to identify the remote-FCF associated with this VFC if it is of type VE_Port.')
hpnicfFCoEStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindIfIndex.setDescription('This object is applicable only when the local FCF is directly connected to an ENode or remote-FCF over a specific Ethernet interface, in which case this object contains the ifIndex of said Ethernet interface. If the ENode or remote-FCF is not directly connected to the FCF, this value of this object is zero.')
hpnicfFCoEStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindMACAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcBindMACAddress.setDescription('This object is applicable when the ENode or remote-FCF to which the local FCF is connected is identified by a MAC address. A FIP frame from a ENode or remote-FCF is associated with this VFC only if the source MAC address in the frame is the same as the value of this object.')
hpnicfFCoEStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcIfIndex.setDescription('The ifIndex of this Virtual FC interface.')
hpnicfFCoEStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcCreationTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcCreationTime.setDescription("The timestamp of this entry's creation time.")
hpnicfFCoEStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFailureCause.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcFailureCause.setDescription('The cause of failure for the last bind operation. This object will be zero length if and only if the bind is successful.')
hpnicfFCoEStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEStaticVfcRowStatus.setDescription('The status of this conceptual row. The RowStatus becomes active on successful creation of a VFC. The VFC does not need to be bound for the row to be active, but the VFC must be bound before becoming operational.')
hpnicfFCoEFIPSnoopingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4), )
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingTable.setDescription('FCoE provides increased flexibility, but with this flexibility new challenges arise in assuring highly robust Fabrics. The FCF does not have the complete control that a Fibre Channel switch has. Ethernet bridges commonly provide a feature called Access Control Lists (ACLs). Properly configured ACLs may emulate a point-to-point link by providing the traffic enforcement previously discussed. Furthermore, the FIP protocol has been designed to enable Ethernet bridges to efficiently monitor FIP frames passing through them. This data facilitates the automatic configuration of these ACLs. In addition, the automatic configuration is possible independent of any other ACLs that may be in use in the network for other applications. And FIP Snooping is to maintain these ACLs.')
hpnicfFCoEFIPSnoopingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFIPSnoopingVLANIndex"))
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEntry.setDescription('There is one entry in this table for each VLAN that is designated to ensures that only valid FCoE traffic is allowed.')
hpnicfFCoEFIPSnoopingVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingVLANIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingVLANIndex.setDescription('This object identifies the VLAN-ID that the FIP Snooping function is being enabled for.')
hpnicfFCoEFIPSnoopingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingEnable.setDescription('This object is used to enable or disable FIP Snooping on an Ethernet Bridge.')
hpnicfFCoEFIPSnoopingFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingFcmap.setStatus('current')
if mibBuilder.loadTexts: hpnicfFCoEFIPSnoopingFcmap.setDescription('This object configures the FC-MAP value associated with the FIP snooping Ethernet Bridge.')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MIB", hpnicfFCoEVLANOperState=hpnicfFCoEVLANOperState, hpnicfFCoECfgFcmap=hpnicfFCoECfgFcmap, hpnicfFCoECfgDefaultFCFPriority=hpnicfFCoECfgDefaultFCFPriority, hpnicfFCoEObjects=hpnicfFCoEObjects, hpnicfFCoEStaticVfcEntry=hpnicfFCoEStaticVfcEntry, hpnicfFCoECfgTable=hpnicfFCoECfgTable, hpnicfFCoEFIPSnoopingEntry=hpnicfFCoEFIPSnoopingEntry, hpnicfFCoEVLANIndex=hpnicfFCoEVLANIndex, hpnicfFCoEFIPSnoopingVLANIndex=hpnicfFCoEFIPSnoopingVLANIndex, hpnicfFCoEStaticVfcFCFPriority=hpnicfFCoEStaticVfcFCFPriority, HpnicfFCoEVfcBindType=HpnicfFCoEVfcBindType, hpnicfFCoEStaticVfcIfIndex=hpnicfFCoEStaticVfcIfIndex, hpnicfFCoEStaticVfcFailureCause=hpnicfFCoEStaticVfcFailureCause, hpnicfFCoEFIPSnoopingFcmap=hpnicfFCoEFIPSnoopingFcmap, hpnicfFCoEVLANTable=hpnicfFCoEVLANTable, hpnicfFCoEVLANEntry=hpnicfFCoEVLANEntry, hpnicfFCoEFIPSnoopingEnable=hpnicfFCoEFIPSnoopingEnable, hpnicfFCoEStaticVfcIndex=hpnicfFCoEStaticVfcIndex, hpnicfFCoEStaticVfcBindMACAddress=hpnicfFCoEStaticVfcBindMACAddress, hpnicfFCoECfgDynamicVfcCreation=hpnicfFCoECfgDynamicVfcCreation, hpnicfFCoEFIPSnoopingTable=hpnicfFCoEFIPSnoopingTable, hpnicfFCoE=hpnicfFCoE, hpnicfFCoEConfig=hpnicfFCoEConfig, hpnicfFCoEStaticVfcBindType=hpnicfFCoEStaticVfcBindType, hpnicfFCoECfgAddressingMode=hpnicfFCoECfgAddressingMode, PYSNMP_MODULE_ID=hpnicfFCoE, hpnicfFCoEStaticVfcCreationTime=hpnicfFCoEStaticVfcCreationTime, hpnicfFCoECfgDATov=hpnicfFCoECfgDATov, hpnicfFCoECfgEntry=hpnicfFCoECfgEntry, hpnicfFCoEStaticVfcRowStatus=hpnicfFCoEStaticVfcRowStatus, hpnicfFCoEStaticVfcTable=hpnicfFCoEStaticVfcTable, hpnicfFCoEFabricIndex=hpnicfFCoEFabricIndex, hpnicfFCoEStaticVfcBindIfIndex=hpnicfFCoEStaticVfcBindIfIndex, hpnicfFCoEVLANRowStatus=hpnicfFCoEVLANRowStatus)