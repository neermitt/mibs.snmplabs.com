#
# PySNMP MIB module MPLS-FRR-GENERAL-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-FRR-GENERAL-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifGeneralInformationGroup, ifCounterDiscontinuityGroup, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup", "ifCounterDiscontinuityGroup", "InterfaceIndexOrZero")
MplsTunnelInstanceIndex, MplsTunnelIndex, MplsTunnelAffinity, MplsBitRate = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsTunnelInstanceIndex", "MplsTunnelIndex", "MplsTunnelAffinity", "MplsBitRate")
mplsTunnelGroup, mplsTunnelARHopIndex, mplsTunnelARHopListIndex, mplsTunnelScalarGroup = mibBuilder.importSymbols("MPLS-TE-STD-MIB", "mplsTunnelGroup", "mplsTunnelARHopIndex", "mplsTunnelARHopListIndex", "mplsTunnelScalarGroup")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Counter64, TimeTicks, Integer32, mib_2, Counter32, iso, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "Integer32", "mib-2", "Counter32", "iso", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
StorageType, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "RowStatus", "TextualConvention")
mplsFrrGeneralMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 202))
mplsFrrGeneralMIB.setRevisions(('2011-11-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsFrrGeneralMIB.setRevisionsDescriptions(('Initial version. Published as RFC 6445.',))
if mibBuilder.loadTexts: mplsFrrGeneralMIB.setLastUpdated('201111030000Z')
if mibBuilder.loadTexts: mplsFrrGeneralMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsFrrGeneralMIB.setContactInfo(' Riza Cetin Email: riza.cetin@alcatel.be Thomas D. Nadeau Email: thomas.nadeau@ca.com A S Kiran Koushik Email: kkoushik@cisco.com Stefaan De Cnodder Email: Stefaan.de_cnodder@alcatel.be Der-Hwa Gan Email: dhg@juniper.net ')
if mibBuilder.loadTexts: mplsFrrGeneralMIB.setDescription("Copyright (c) 2011 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This MIB module contains generic object definitions for MPLS Traffic Engineering Fast Reroute as defined in RFC 4090.")
mplsFrrGeneralObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 202, 1))
mplsFrrGeneralConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 202, 2))
mplsFrrGeneralProtectionMethod = MibScalar((1, 3, 6, 1, 2, 1, 202, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("oneToOneBackup", 2), ("facilityBackup", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsFrrGeneralProtectionMethod.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralProtectionMethod.setDescription('Indicates which protection method is to be used for fast reroute on this device. Some devices may require a reboot if this variable is to take effect after being modified.')
mplsFrrGeneralIngressTunnelInstances = MibScalar((1, 3, 6, 1, 2, 1, 202, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFrrGeneralIngressTunnelInstances.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralIngressTunnelInstances.setDescription('The number of tunnel instances for either detour LSPs or bypass tunnels for which this LSR is the ingress.')
mplsFrrGeneralConstraintsTable = MibTable((1, 3, 6, 1, 2, 1, 202, 1, 3), )
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTable.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTable.setDescription('This table shows detour LSP or bypass tunnel setup constraints.')
mplsFrrGeneralConstraintsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 202, 1, 3, 1), ).setIndexNames((0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsIfIndexOrZero"), (0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsTunnelIndex"), (0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsTunnelInstance"))
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsEntry.setReference('Section 4.1 of RFC 4090 and Section 6.1 of RFC 3812.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsEntry.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsEntry.setDescription('An entry in this table represents detour LSP or bypass tunnel setup constraints for an interface or link to be protected by detour LSPs or a bypass tunnel. Once the LSP or tunnel instance to be protected is identified in the mplsTunnelTable, the corresponding mplsTunnelIfIndex value of that tunnel can be used to get the ifIndex of the underlying physical interface using the ifStackTable. That ifIndex of the underlying physical interface will be used as mplsFrrGeneralConstraintsIfIndexOrZero in this table to protect the LSPs or tunnel instances determined earlier. It is recommended that ifIndex persistence be enabled across re-initializations. If persistence is not implemented, then the value of mplsFrrGeneralConstraintsIfIndexOrZero in this table cannot be guaranteed across restarts and all entries in this table MUST NOT be persistent, or the values of mplsFrrGeneralConstraintsIfIndexOrZero MUST be reconstructed on restart. SNMP engines must only allow entries in this table to be created for tunnel instances that require fast reroute as indicated by the presence of the FAST_REROUTE object in the signaling for the LSP in question. An entry in this table can be created only if a corresponding entry in mplsTunnelTable exists with the same mplsTunnelIndex as mplsFrrGeneralConstraintsTunnelIndex. Entries in this table are deleted when the corresponding entries in mplsTunnelTable are deleted. It is recommended that entries in this table be persistent across reboots. Entries indexed with mplsFrrGeneralConstraintsIfIndexOrZero and set to 0 apply to all interfaces on this device for which the FRR feature can operate. If the mplsTunnelInstance object is set to a value of 0, it indicates that the mplsTunnelEntry contains a tunnel ingress. This is typically how configuration of this feature is performed on devices where the actual protection LSP used is left up to the protecting tunnel. However, in cases where static configuration is possible, any valid tunnel instance is possible; however, it is strongly RECOMMENDED that the instance index SHOULD use the following convention to identify backup LSPs: - lower 16 bits : protected tunnel instance - higher 16 bits: must be all zeros')
mplsFrrGeneralConstraintsIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsIfIndexOrZero.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsIfIndexOrZero.setDescription('Uniquely identifies an interface that a fast-reroute protection tunnel is configured to potentially protect in the event of a fault. Entries with this index set to 0 indicate that the configured protection tunnel protects all interfaces on this device (i.e., node protection).')
mplsFrrGeneralConstraintsTunnelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 2), MplsTunnelIndex())
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTunnelIndex.setReference('mplsTunnelTable from RFC 3812.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTunnelIndex.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTunnelIndex.setDescription('Uniquely identifies a tunnel in the mplsTunnelTable that is configured to possibly protect the interface(s) specified by mplsFrrGeneralConstraintsIfIndexOrZero in the event of a fault.')
mplsFrrGeneralConstraintsTunnelInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 3), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTunnelInstance.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsTunnelInstance.setDescription('Uniquely identifies an existing instance of this tunnel for which fast reroute is requested. Note that a value of 0 indicates that the configuration points at a tunnel head (as specified in RFC 3812). This is typically how configuration of this feature is performed on devices where the actual protection LSP used is left up to the protecting tunnel. However, in cases where static configuration is possible, any valid tunnel instance is permissible. In these cases, it is recommended that the instance index follow the following convention so as to make identification of backup LSPs easier: - lower 16 bits : protected tunnel instance - higher 16 bits: must be all zeros')
mplsFrrGeneralConstraintsProtectionType = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkProtection", 1), ("nodeProtection", 2))).clone('nodeProtection')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsProtectionType.setReference('Section 3 of RFC 4090.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsProtectionType.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsProtectionType.setDescription("Indicates type of the resource protection: linkProtection(1) indicates that this tunnel is set up to protect a particular link's resources. nodeProtection(2) indicates that this tunnel is set up to protect an entire node from failure.")
mplsFrrGeneralConstraintsSetupPrio = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsSetupPrio.setReference('Section 4.7 of RFC 3209.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsSetupPrio.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsSetupPrio.setDescription('Indicates the setup priority of the detour LSP or bypass tunnel.')
mplsFrrGeneralConstraintsHoldingPrio = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHoldingPrio.setReference('Section 4.7 of RFC 3209.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHoldingPrio.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHoldingPrio.setDescription('Indicates the holding priority for the detour LSP or bypass tunnel.')
mplsFrrGeneralConstraintsInclAnyAffinity = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 7), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAnyAffinity.setReference('Section 4.7 of RFC 3209.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAnyAffinity.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAnyAffinity.setDescription('Indicates the include-any link constraint for the detour LSP or bypass tunnel. A link satisfies the include-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common.')
mplsFrrGeneralConstraintsInclAllAffinity = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 8), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAllAffinity.setReference('Section 4.7 of RFC 3209.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAllAffinity.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsInclAllAffinity.setDescription('Indicates the include-all link constraint for the detour LSP or bypass tunnel. A link satisfies the include-all constraint if and only if the link contains all of the administrative groups specified in the constraint.')
mplsFrrGeneralConstraintsExclAnyAffinity = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 9), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsExclAnyAffinity.setReference('Section 4.7 of RFC 3209.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsExclAnyAffinity.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsExclAnyAffinity.setDescription('Indicates the exclude-any link constraint for the detour LSP or bypass tunnel. A link satisfies the exclude-any constraint if and only if the link contains none of the administrative groups specified in the constraint.')
mplsFrrGeneralConstraintsHopLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHopLimit.setReference('Section 4.1 of RFC 4090.')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHopLimit.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsHopLimit.setDescription('The maximum number of hops that the detour LSP or bypass tunnel may traverse.')
mplsFrrGeneralConstraintsBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 11), MplsBitRate()).setUnits('kilobits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsBandwidth.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsBandwidth.setDescription('The maximum bandwidth specifically reserved for a detour LSP or bypass tunnel, in units of thousands of bits per second (kbps). Note that setting this value to 0 indicates best-effort treatment.')
mplsFrrGeneralConstraintsStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 12), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsStorageType.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsStorageType.setDescription("The storage type for this configuration entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row.")
mplsFrrGeneralConstraintsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsRowStatus.setDescription('This object is used to create, modify, and/or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified except mplsFrrGeneralConstraintsRowStatus and mplsFrrGeneralConstraintsStorageType.')
mplsFrrGeneralTunnelARHopTable = MibTable((1, 3, 6, 1, 2, 1, 202, 1, 4), )
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopTable.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopTable.setDescription('This table sparsely extends mplsTunnelARHopTable defined in the MPLS-TE-STD-MIB module with fast-reroute objects. These objects specify the status of local protection, including availability and active use, on a per-hop basis, of hops traversed by a protected tunnel.')
mplsFrrGeneralTunnelARHopEntry = MibTableRow((1, 3, 6, 1, 2, 1, 202, 1, 4, 1), ).setIndexNames((0, "MPLS-TE-STD-MIB", "mplsTunnelARHopListIndex"), (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopIndex"))
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopEntry.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopEntry.setDescription('This entry contains fast-reroute protection status of a single protected tunnel hop.')
mplsFrrGeneralTunnelARHopSessionAttributeFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 4, 1, 1), Bits().clone(namedValues=NamedValues(("arHopSessionAttrFlagsUnsupported", 0), ("localProtectionDesired", 1), ("labelRecordingDesired", 2), ("sestyleDesired", 3), ("bandwidthProtectionDesired", 4), ("nodeProtectionDesired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopSessionAttributeFlags.setReference('See Section 4.3 of RFC 4090 for SESSION_ATTRIBUTE flags.')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopSessionAttributeFlags.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopSessionAttributeFlags.setDescription('This object indicates the desired values for the associated SESSION_ATTRIBUTE flags. Note that since this object is a BITS type, the bits may be set to indicate various desired combinations of the SESSION_ATTRIBUTE flags. If SESSION_ATTRIBUTE flags are not supported, then this object contains the value of arHopSessionAttrFlagsUnsupported(0).')
mplsFrrGeneralTunnelARHopRROSubObjectFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 202, 1, 4, 1, 2), Bits().clone(namedValues=NamedValues(("arHopRROSubObjectFlagsUnsupported", 0), ("localProtectionAvailable", 1), ("localProtectionInUse", 2), ("bandwidthProtection", 3), ("nodeProtection", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopRROSubObjectFlags.setReference('Section 4.4 of RFC 4090.')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopRROSubObjectFlags.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopRROSubObjectFlags.setDescription('This object indicates the flags that are currently in use by the associated Record Route Object (RRO) sub-object. Note that since this object is a BITS type, the bits may be set to indicate various combinations of the flags. If the RRO sub-object is not supported, then this object contains the value of arHopRROSubObjectFlagsUnsupported(0).')
mplsFrrGeneralCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 202, 2, 1))
mplsFrrGeneralGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 202, 2, 2))
mplsFrrGeneralModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 202, 2, 1, 1)).setObjects(("IF-MIB", "ifGeneralInformationGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("MPLS-TE-STD-MIB", "mplsTunnelGroup"), ("MPLS-TE-STD-MIB", "mplsTunnelScalarGroup"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralScalarGroup"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopGroup"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsFrrGeneralModuleFullCompliance = mplsFrrGeneralModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralModuleFullCompliance.setDescription('Compliance statements for SNMP engines that support the MPLS-FRR-GENERAL-STD-MIB module.')
mplsFrrGeneralModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 202, 2, 1, 2)).setObjects(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralScalarGroup"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopGroup"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsFrrGeneralModuleReadOnlyCompliance = mplsFrrGeneralModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralModuleReadOnlyCompliance.setDescription('Compliance statements for SNMP engines that support the MPLS-FRR-GENERAL-STD-MIB module.')
mplsFrrGeneralScalarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 202, 2, 2, 1)).setObjects(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralIngressTunnelInstances"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralProtectionMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsFrrGeneralScalarGroup = mplsFrrGeneralScalarGroup.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralScalarGroup.setDescription('Objects that are required to display general fast-reroute information.')
mplsFrrGeneralConstraintsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 202, 2, 2, 2)).setObjects(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsProtectionType"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsSetupPrio"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsHoldingPrio"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsInclAnyAffinity"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsInclAllAffinity"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsExclAnyAffinity"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsHopLimit"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsBandwidth"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsStorageType"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsFrrGeneralConstraintsGroup = mplsFrrGeneralConstraintsGroup.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralConstraintsGroup.setDescription('Objects that are required to configure fast-reroute constraints at the ingress LSR of the tunnel that requires fast-reroute service.')
mplsFrrGeneralTunnelARHopGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 202, 2, 2, 3)).setObjects(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopSessionAttributeFlags"), ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopRROSubObjectFlags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsFrrGeneralTunnelARHopGroup = mplsFrrGeneralTunnelARHopGroup.setStatus('current')
if mibBuilder.loadTexts: mplsFrrGeneralTunnelARHopGroup.setDescription('Objects that are required to present per-hop fast-reroute protection status.')
mibBuilder.exportSymbols("MPLS-FRR-GENERAL-STD-MIB", mplsFrrGeneralProtectionMethod=mplsFrrGeneralProtectionMethod, mplsFrrGeneralMIB=mplsFrrGeneralMIB, mplsFrrGeneralConstraintsStorageType=mplsFrrGeneralConstraintsStorageType, mplsFrrGeneralConstraintsSetupPrio=mplsFrrGeneralConstraintsSetupPrio, mplsFrrGeneralConstraintsHopLimit=mplsFrrGeneralConstraintsHopLimit, mplsFrrGeneralConstraintsTunnelIndex=mplsFrrGeneralConstraintsTunnelIndex, mplsFrrGeneralTunnelARHopGroup=mplsFrrGeneralTunnelARHopGroup, mplsFrrGeneralTunnelARHopRROSubObjectFlags=mplsFrrGeneralTunnelARHopRROSubObjectFlags, mplsFrrGeneralConstraintsGroup=mplsFrrGeneralConstraintsGroup, mplsFrrGeneralConstraintsProtectionType=mplsFrrGeneralConstraintsProtectionType, mplsFrrGeneralConstraintsTunnelInstance=mplsFrrGeneralConstraintsTunnelInstance, mplsFrrGeneralConstraintsEntry=mplsFrrGeneralConstraintsEntry, mplsFrrGeneralConformance=mplsFrrGeneralConformance, mplsFrrGeneralGroups=mplsFrrGeneralGroups, mplsFrrGeneralConstraintsInclAllAffinity=mplsFrrGeneralConstraintsInclAllAffinity, mplsFrrGeneralConstraintsTable=mplsFrrGeneralConstraintsTable, mplsFrrGeneralConstraintsIfIndexOrZero=mplsFrrGeneralConstraintsIfIndexOrZero, mplsFrrGeneralConstraintsBandwidth=mplsFrrGeneralConstraintsBandwidth, PYSNMP_MODULE_ID=mplsFrrGeneralMIB, mplsFrrGeneralModuleFullCompliance=mplsFrrGeneralModuleFullCompliance, mplsFrrGeneralScalarGroup=mplsFrrGeneralScalarGroup, mplsFrrGeneralConstraintsRowStatus=mplsFrrGeneralConstraintsRowStatus, mplsFrrGeneralConstraintsHoldingPrio=mplsFrrGeneralConstraintsHoldingPrio, mplsFrrGeneralModuleReadOnlyCompliance=mplsFrrGeneralModuleReadOnlyCompliance, mplsFrrGeneralTunnelARHopTable=mplsFrrGeneralTunnelARHopTable, mplsFrrGeneralConstraintsInclAnyAffinity=mplsFrrGeneralConstraintsInclAnyAffinity, mplsFrrGeneralTunnelARHopEntry=mplsFrrGeneralTunnelARHopEntry, mplsFrrGeneralCompliances=mplsFrrGeneralCompliances, mplsFrrGeneralObjects=mplsFrrGeneralObjects, mplsFrrGeneralTunnelARHopSessionAttributeFlags=mplsFrrGeneralTunnelARHopSessionAttributeFlags, mplsFrrGeneralIngressTunnelInstances=mplsFrrGeneralIngressTunnelInstances, mplsFrrGeneralConstraintsExclAnyAffinity=mplsFrrGeneralConstraintsExclAnyAffinity)