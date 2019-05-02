#
# PySNMP MIB module ALCATEL-IND1-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-PIM-BSR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:18:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Pim, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Pim")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Unsigned32, MibIdentifier, Counter32, TimeTicks, Bits, Integer32, iso, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks", "Bits", "Integer32", "iso", "ModuleIdentity", "IpAddress")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
alaPimBsrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3))
alaPimBsrMIB.setRevisions(('2007-07-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alaPimBsrMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alaPimBsrMIB.setLastUpdated('200707020000Z')
if mibBuilder.loadTexts: alaPimBsrMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alaPimBsrMIB.setContactInfo('Please consult with Customer Service to insure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alaPimBsrMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): This proprietary MIB contains management information for the Bootstrap Router (BSR) mechanism for PIM routers. This MIB is based on the Internet Draft <draft-ietf-pim-bsr-mib-02.txt> developed by the IETF PIM Working Group. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alaPimBsrNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0))
alaPimBsrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1))
alaPimBsrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2))
alaPimBsrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 1))
alaPimBsrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2))
alaPimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1), )
if mibBuilder.loadTexts: alaPimBsrCandidateRPTable.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPTable.setDescription('The (conceptual) table listing the IP multicast group prefixes for which the local router is to advertise itself as a Candidate-RP.')
alaPimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAddressType"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAddress"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPGroupAddress"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPGroupPrefixLength"))
if mibBuilder.loadTexts: alaPimBsrCandidateRPEntry.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPEntry.setDescription('An entry (conceptual row) in the alaBsrCandidateRPTable.')
alaPimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaPimBsrCandidateRPAddressType.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPAddressType.setDescription('The Inet address type of the Candidate-RP.')
alaPimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: alaPimBsrCandidateRPAddress.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPAddress.setDescription('The (unicast) address which will be advertised as a Candidate-RP. The InetAddressType is given by the alaPimBsrCandidateRPAddressType object.')
alaPimBsrCandidateRPGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: alaPimBsrCandidateRPGroupAddress.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPGroupAddress.setDescription('The IP multicast group address which, when combined with the corresponding value of alaPimBsrCandidateRPGroupPrefixLength, identifies a group prefix for which the local router will advertise itself as a Candidate-RP. The InetAddressType is given by the alaPimBsrCandidateRPAddressType object.')
alaPimBsrCandidateRPGroupPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 4), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: alaPimBsrCandidateRPGroupPrefixLength.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPGroupPrefixLength.setDescription('The multicast group address mask which, when combined with the corresponding value of alaPimBsrCandidateRPGroupAddress, identifies a group prefix for which the local router will advertise itself as a Candidate-RP. The InetAddressType is given by the alaPimBsrCandidateRPAddressType object.')
alaPimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateRPBidir.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPBidir.setDescription('If this object is set to TRUE, this group range is advertised with this RP as a BIDIR-PIM group range. If it is set to FALSE, it is advertised as a PIM-SM group range.')
alaPimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrCandidateRPAdvTimer.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPAdvTimer.setDescription('The time remaining before the local router next sends a Candidate-RP-Advertisement to the elected BSR for this address type.')
alaPimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateRPPriority.setReference('I-D.ietf-pim-sm-bsr section 3.2')
if mibBuilder.loadTexts: alaPimBsrCandidateRPPriority.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPPriority.setDescription('The priority for this Candidate RP advertised in Candidate-RP-Advertisements.')
alaPimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 26214)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateRPAdvInterval.setReference('I-D.ietf-pim-sm-bsr section 3.2 and section 5')
if mibBuilder.loadTexts: alaPimBsrCandidateRPAdvInterval.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPAdvInterval.setDescription('A Candidate RP generates Candidate-RP-Advertisements periodically. This object represents the time interval in seconds between two consecutive advertisements.')
alaPimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateRPHoldtime.setReference('I-D.ietf-pim-sm-bsr section 4.2')
if mibBuilder.loadTexts: alaPimBsrCandidateRPHoldtime.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPHoldtime.setDescription('Holdtime for this Candidate RP. The amount of time (in seconds) this Candidate-RP entry is valid.')
alaPimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateRPStatus.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateRPStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
alaPimBsrElectedBSRRPSetTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2), )
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetTable.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetTable.setDescription('The (conceptual) table listing BSR-specific information about PIM group mappings learned via C-RP advertisements or created locally using configurations. This table is maintained only on the Elected BSR. An Elected BSR uses this table to create Bootstrap Messages after applying a local policy to include some or all of the group mappings in this table.')
alaPimBsrElectedBSRRPSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingAddrType"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingGrpAddr"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingGrpPrefixLen"), (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingRPAddr"))
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetEntry.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetEntry.setDescription('An entry (conceptual row) in the alaPimBsrElectedBSRRPSetTable.')
alaPimBsrElectedBSRGrpMappingAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingAddrType.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingAddrType.setDescription('The Inet address type of the IP multicast group prefix.')
alaPimBsrElectedBSRGrpMappingGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingGrpAddr.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingGrpAddr.setDescription('The IP multicast group address which, when combined with alaPimBsrElectedBSRGrpMappingGrpPrefixLen, gives the group prefix for this mapping. The InetAddressType is given by the alaPimBsrElectedBSRGrpMappingAddrType object. This address object is only significant up to alaPimBsrElectedBSRGrpMappingGrpPrefixLen bits. The remainder of the address bits are zero. This is especially important for this field, which is part of the index of this entry. Any non-zero bits would signify an entirely different entry.')
alaPimBsrElectedBSRGrpMappingGrpPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 4), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setDescription("The multicast group prefix length that, when combined with alaPimBsrElectedBSRGrpMappingGrpAddr, gives the group prefix for this mapping. The InetAddressType is given by the alaPimBsrElectedBSRGrpMappingAddrType object. If alaPimBsrElectedBSRGrpMappingAddrType is 'ipv4' or 'ipv4z', this object must be in the range 4..32. If alaPimBsrElectedBSRGrpMappingAddrType is 'ipv6' or 'ipv6z', this object must be in the range 8..128.")
alaPimBsrElectedBSRGrpMappingRPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingRPAddr.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRGrpMappingRPAddr.setDescription('The IP address of the RP to be used for groups within this group prefix. The InetAddressType is given by the alaPimBsrElectedBSRGrpMappingAddrType object.')
alaPimBsrElectedBSRRPSetPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetPriority.setReference('I-D.ietf-pim-sm-bsr section 4.1')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetPriority.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetPriority.setDescription('The priority for RP. Numerically higher values for this object indicate lower priorities, with the value zero denoting the highest priority.')
alaPimBsrElectedBSRRPSetHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetHoldtime.setReference('I-D.ietf-pim-sm-bsr section 4.1')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetHoldtime.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetHoldtime.setDescription('The holdtime for RP')
alaPimBsrElectedBSRRPSetExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetExpiryTime.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetExpiryTime.setDescription('The minimum time remaining before this entry will be aged out. The value zero indicates that this entry will never be aged out.')
alaPimBsrElectedBSRRPSetGrpBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetGrpBidir.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRRPSetGrpBidir.setDescription('If this object is TRUE, this group range with this RP is a BIDIR-PIM group range. If it is set to FALSE, it is a PIM-SM group range.')
alaPimBsrCandidateBSRTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3), )
if mibBuilder.loadTexts: alaPimBsrCandidateBSRTable.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRTable.setDescription('The (conceptual) table containing Candidate-BSR configuration for the local router. The table contains one row for each address family for which the local router is to advertise itself as a Candidate-BSR.')
alaPimBsrCandidateBSREntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRAddressType"))
if mibBuilder.loadTexts: alaPimBsrCandidateBSREntry.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSREntry.setDescription('An entry (conceptual row) in the alaPimBsrCandidateBSRTable.')
alaPimBsrCandidateBSRAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaPimBsrCandidateBSRAddressType.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRAddressType.setDescription('The address type of the Candidate-BSR.')
alaPimBsrCandidateBSRAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRAddress.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRAddress.setDescription('The (unicast) address which the local router will use to advertise itself as a Candidate-BSR. The InetAddressType is given by the alaPimBsrCandidateBSRAddressType object.')
alaPimBsrCandidateBSRPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRPriority.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRPriority.setDescription('The priority value for the local router as a Candidate-BSR for this address type. Numerically higher values for this object indicate higher priorities.')
alaPimBsrCandidateBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRHashMaskLength.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRHashMaskLength.setDescription("The hash mask length (used in the RP hash function) that the local router will advertise in its Bootstrap messages for this address type. This object defaults to 30 if alaPimBsrCandidateBSRAddressType is 'ipv4' or 'ipv4z' , and defaults to 126 if alaPimBsrCandidateBSRAddressType is 'ipv6' or 'ipv6z'.")
alaPimBsrCandidateBSRElectedBSR = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRElectedBSR.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRElectedBSR.setDescription('Whether the local router is the elected BSR for this address type.')
alaPimBsrCandidateBSRBootstrapTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRBootstrapTimer.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRBootstrapTimer.setDescription("The time remaining before the local router next originates a Bootstrap message for this address type. Value of this object is zero if alaPimBsrCandidateBSRElectedBSR is 'FALSE'.")
alaPimBsrCandidateBSRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaPimBsrCandidateBSRStatus.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
alaPimBsrElectedBSRTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4), )
if mibBuilder.loadTexts: alaPimBsrElectedBSRTable.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRTable.setDescription('The (conceptual) table containing information about elected BSRs. The table contains one row for each address family for which there is an elected BSR.')
alaPimBsrElectedBSREntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRAddressType"))
if mibBuilder.loadTexts: alaPimBsrElectedBSREntry.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSREntry.setDescription('An entry (conceptual row) in the alaPimBsrElectedBSRTable.')
alaPimBsrElectedBSRAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaPimBsrElectedBSRAddressType.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRAddressType.setDescription('The address type of the elected BSR.')
alaPimBsrElectedBSRAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRAddress.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRAddress.setDescription('The (unicast) address of the elected BSR. The InetAddressType is given by the alaPimBsrElectedBSRAddressType object.')
alaPimBsrElectedBSRPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRPriority.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRPriority.setDescription('The priority value for the elected BSR for this address type. Numerically higher values for this object indicate higher priorities.')
alaPimBsrElectedBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRHashMaskLength.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRHashMaskLength.setDescription('The hash mask length (used in the RP hash function) advertised by the elected BSR for this address type.')
alaPimBsrElectedBSRExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaPimBsrElectedBSRExpiryTime.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRExpiryTime.setDescription('The minimum time remaining before the elected BSR for this address type will be declared down.')
alaPimBsrElectedBSRLostElection = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0, 1)).setObjects(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR"))
if mibBuilder.loadTexts: alaPimBsrElectedBSRLostElection.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrElectedBSRLostElection.setDescription('A alaPimBsrElectedBSRLostElection trap should be generated when current E-BSR lost election to a new Candidate BSR current E-BSR, start sending BootStrap Messages. Only an E-BSR should generate this trap. This notification is generated when alaPimBsrCandidateBSRElectedBSR becomes FALSE.')
if mibBuilder.loadTexts: alaPimBsrElectedBSRLostElection.setReference('I-D.ietf-pim-sm-bsr section 3.1')
alaPimBsrCandidateBSRWinElection = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0, 2)).setObjects(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR"))
if mibBuilder.loadTexts: alaPimBsrCandidateBSRWinElection.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRWinElection.setDescription('A alaPimBsrCandidateBSRWinElection trap should be generated when a C-BSR wins BSR Election. Only an E-BSR should generate this trap. This notification is generated when alaPimBsrCandidateBSRElectedBSR becomes TRUE')
if mibBuilder.loadTexts: alaPimBsrCandidateBSRWinElection.setReference('I-D.ietf-pim-sm-bsr section 3.1')
alaPimBsrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 1, 1)).setObjects(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrObjectGroup"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrDiagnosticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimBsrCompliance = alaPimBsrCompliance.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrCompliance.setDescription('The compliance statement for PIM routers that implement the Bootstrap Router (BSR) mechanism.')
alaPimBsrObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2, 1)).setObjects(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPBidir"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAdvTimer"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPPriority"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAdvInterval"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPHoldtime"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPStatus"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetPriority"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetHoldtime"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetExpiryTime"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetGrpBidir"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRAddress"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRPriority"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRHashMaskLength"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRBootstrapTimer"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRStatus"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRAddress"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRPriority"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRHashMaskLength"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimBsrObjectGroup = alaPimBsrObjectGroup.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrObjectGroup.setDescription('A collection of objects for managing PIM routers.')
alaPimBsrDiagnosticsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2, 2)).setObjects(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRLostElection"), ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRWinElection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaPimBsrDiagnosticsGroup = alaPimBsrDiagnosticsGroup.setStatus('current')
if mibBuilder.loadTexts: alaPimBsrDiagnosticsGroup.setDescription('Objects providing additonal diagnostics related to BSR mechanism of PIM router.')
mibBuilder.exportSymbols("ALCATEL-IND1-PIM-BSR-MIB", alaPimBsrCandidateRPAddress=alaPimBsrCandidateRPAddress, alaPimBsrCandidateRPStatus=alaPimBsrCandidateRPStatus, alaPimBsrCandidateRPAdvInterval=alaPimBsrCandidateRPAdvInterval, alaPimBsrCandidateRPAddressType=alaPimBsrCandidateRPAddressType, alaPimBsrCandidateRPHoldtime=alaPimBsrCandidateRPHoldtime, alaPimBsrCandidateBSRAddressType=alaPimBsrCandidateBSRAddressType, alaPimBsrElectedBSRAddressType=alaPimBsrElectedBSRAddressType, alaPimBsrElectedBSRExpiryTime=alaPimBsrElectedBSRExpiryTime, alaPimBsrCandidateRPEntry=alaPimBsrCandidateRPEntry, alaPimBsrElectedBSRLostElection=alaPimBsrElectedBSRLostElection, alaPimBsrNotifications=alaPimBsrNotifications, alaPimBsrGroups=alaPimBsrGroups, alaPimBsrCompliances=alaPimBsrCompliances, alaPimBsrElectedBSRRPSetGrpBidir=alaPimBsrElectedBSRRPSetGrpBidir, alaPimBsrCandidateRPPriority=alaPimBsrCandidateRPPriority, alaPimBsrCandidateBSREntry=alaPimBsrCandidateBSREntry, alaPimBsrCandidateBSRAddress=alaPimBsrCandidateBSRAddress, alaPimBsrCompliance=alaPimBsrCompliance, alaPimBsrCandidateBSRBootstrapTimer=alaPimBsrCandidateBSRBootstrapTimer, alaPimBsrElectedBSRGrpMappingGrpPrefixLen=alaPimBsrElectedBSRGrpMappingGrpPrefixLen, alaPimBsrCandidateBSRStatus=alaPimBsrCandidateBSRStatus, alaPimBsrCandidateRPBidir=alaPimBsrCandidateRPBidir, alaPimBsrElectedBSRRPSetEntry=alaPimBsrElectedBSRRPSetEntry, alaPimBsrElectedBSRAddress=alaPimBsrElectedBSRAddress, alaPimBsrElectedBSRGrpMappingAddrType=alaPimBsrElectedBSRGrpMappingAddrType, alaPimBsrCandidateBSRWinElection=alaPimBsrCandidateBSRWinElection, alaPimBsrConformance=alaPimBsrConformance, alaPimBsrElectedBSRRPSetExpiryTime=alaPimBsrElectedBSRRPSetExpiryTime, alaPimBsrDiagnosticsGroup=alaPimBsrDiagnosticsGroup, alaPimBsrElectedBSREntry=alaPimBsrElectedBSREntry, alaPimBsrElectedBSRPriority=alaPimBsrElectedBSRPriority, alaPimBsrElectedBSRRPSetTable=alaPimBsrElectedBSRRPSetTable, alaPimBsrElectedBSRRPSetPriority=alaPimBsrElectedBSRRPSetPriority, alaPimBsrObjectGroup=alaPimBsrObjectGroup, alaPimBsrCandidateRPGroupPrefixLength=alaPimBsrCandidateRPGroupPrefixLength, alaPimBsrCandidateRPTable=alaPimBsrCandidateRPTable, alaPimBsrElectedBSRGrpMappingGrpAddr=alaPimBsrElectedBSRGrpMappingGrpAddr, alaPimBsrCandidateRPAdvTimer=alaPimBsrCandidateRPAdvTimer, alaPimBsrElectedBSRTable=alaPimBsrElectedBSRTable, alaPimBsrObjects=alaPimBsrObjects, PYSNMP_MODULE_ID=alaPimBsrMIB, alaPimBsrCandidateBSRTable=alaPimBsrCandidateBSRTable, alaPimBsrMIB=alaPimBsrMIB, alaPimBsrElectedBSRGrpMappingRPAddr=alaPimBsrElectedBSRGrpMappingRPAddr, alaPimBsrCandidateBSRElectedBSR=alaPimBsrCandidateBSRElectedBSR, alaPimBsrCandidateBSRPriority=alaPimBsrCandidateBSRPriority, alaPimBsrElectedBSRRPSetHoldtime=alaPimBsrElectedBSRRPSetHoldtime, alaPimBsrElectedBSRHashMaskLength=alaPimBsrElectedBSRHashMaskLength, alaPimBsrCandidateRPGroupAddress=alaPimBsrCandidateRPGroupAddress, alaPimBsrCandidateBSRHashMaskLength=alaPimBsrCandidateBSRHashMaskLength)