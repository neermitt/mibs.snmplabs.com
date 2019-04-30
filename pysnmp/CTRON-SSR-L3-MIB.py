#
# PySNMP MIB module CTRON-SSR-L3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SSR-L3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:15:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Counter64, IpAddress, MibIdentifier, ObjectIdentity, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "ObjectIdentity", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
l3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600))
l3MIB.setRevisions(('1999-09-22 00:00',))
if mibBuilder.loadTexts: l3MIB.setLastUpdated('199909220000Z')
if mibBuilder.loadTexts: l3MIB.setOrganization('Cabletron Systems, Inc.')
class SSRProtocols(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 255))
    namedValues = NamedValues(("hopopt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ipip", 4), ("stream", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnrccmon", 10), ("nvpii", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcn", 19), ("hmp", 20), ("prm", 21), ("xnsidp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irtp", 28), ("isotp4", 29), ("netblt", 30), ("mfe", 31), ("meritInp", 32), ("sep", 33), ("tpc", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tppp", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6r", 43), ("ipv6f", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("mhrp", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("inlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6Nonxt", 59), ("ipv6Opts", 60), ("hostInternal", 61), ("cftp", 62), ("any", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("adfs", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmtp", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eigrp", 88), ("ospfigp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipipep", 94), ("micp", 95), ("sccSp", 96), ("etherip", 97), ("encap", 98), ("anyEncrpyt", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("an", 107), ("ippcp", 108), ("snp", 109), ("cpqP", 110), ("ipxIp", 111), ("vrrp", 112), ("reserved", 255))

l3Group = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3))
l3FlowTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1), )
if mibBuilder.loadTexts: l3FlowTable.setStatus('obsolete')
l3FlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-SSR-L3-MIB", "l3FlowIndex"), (0, "CTRON-SSR-L3-MIB", "l3FlowFilterId"), (0, "CTRON-SSR-L3-MIB", "l3FlowPortOfEntry"), (0, "CTRON-SSR-L3-MIB", "l3FlowSrcIpAddress"), (0, "CTRON-SSR-L3-MIB", "l3FlowDstIpAddress"), (0, "CTRON-SSR-L3-MIB", "l3FlowTOS"), (0, "CTRON-SSR-L3-MIB", "l3FlowProtocol"), (0, "CTRON-SSR-L3-MIB", "l3FlowSrcPort"), (0, "CTRON-SSR-L3-MIB", "l3FlowDstPort"))
if mibBuilder.loadTexts: l3FlowEntry.setStatus('obsolete')
l3FlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowIndex.setStatus('obsolete')
l3FlowFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowFilterId.setStatus('obsolete')
l3FlowPortOfEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowPortOfEntry.setStatus('obsolete')
l3FlowSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowSrcIpAddress.setStatus('obsolete')
l3FlowDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowDstIpAddress.setStatus('obsolete')
l3FlowTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowTOS.setStatus('obsolete')
l3FlowProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 7), SSRProtocols()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowProtocol.setStatus('obsolete')
l3FlowSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowSrcPort.setStatus('obsolete')
l3FlowDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowDstPort.setStatus('obsolete')
l3FlowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowPkts.setStatus('obsolete')
l3FlowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3FlowOctets.setStatus('obsolete')
l3FlowPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2), )
if mibBuilder.loadTexts: l3FlowPriorityTable.setStatus('obsolete')
l3FlowPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1), ).setIndexNames((0, "CTRON-SSR-L3-MIB", "l3FlowPriorityIndex"))
if mibBuilder.loadTexts: l3FlowPriorityEntry.setStatus('obsolete')
l3FlowPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityIndex.setStatus('obsolete')
l3FlowPriorityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityName.setStatus('obsolete')
l3FlowPrioritySrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPrioritySrcIpAddress.setStatus('obsolete')
l3FlowPrioritySrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPrioritySrcPort.setStatus('obsolete')
l3FlowPriorityDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityDstIpAddress.setStatus('obsolete')
l3FlowPriorityDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityDstPort.setStatus('obsolete')
l3FlowPriorityTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityTOS.setStatus('obsolete')
l3FlowPriorityProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 8), SSRProtocols()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityProtocol.setStatus('obsolete')
l3FlowPriorityInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriorityInterface.setStatus('obsolete')
l3FlowPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3), ("control", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l3FlowPriority.setStatus('obsolete')
l3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2))
l3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 1))
l3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2))
l3ComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2, 1, 1)).setObjects(("CTRON-SSR-L3-MIB", "l3ConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l3ComplianceV10 = l3ComplianceV10.setStatus('obsolete')
l3ConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 600, 2, 2, 1)).setObjects(("CTRON-SSR-L3-MIB", "l3FlowIndex"), ("CTRON-SSR-L3-MIB", "l3FlowFilterId"), ("CTRON-SSR-L3-MIB", "l3FlowPortOfEntry"), ("CTRON-SSR-L3-MIB", "l3FlowSrcIpAddress"), ("CTRON-SSR-L3-MIB", "l3FlowDstIpAddress"), ("CTRON-SSR-L3-MIB", "l3FlowTOS"), ("CTRON-SSR-L3-MIB", "l3FlowProtocol"), ("CTRON-SSR-L3-MIB", "l3FlowSrcPort"), ("CTRON-SSR-L3-MIB", "l3FlowDstPort"), ("CTRON-SSR-L3-MIB", "l3FlowPkts"), ("CTRON-SSR-L3-MIB", "l3FlowOctets"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityIndex"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityName"), ("CTRON-SSR-L3-MIB", "l3FlowPrioritySrcIpAddress"), ("CTRON-SSR-L3-MIB", "l3FlowPrioritySrcPort"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityDstIpAddress"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityDstPort"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityTOS"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityProtocol"), ("CTRON-SSR-L3-MIB", "l3FlowPriorityInterface"), ("CTRON-SSR-L3-MIB", "l3FlowPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l3ConfGroupV10 = l3ConfGroupV10.setStatus('obsolete')
mibBuilder.exportSymbols("CTRON-SSR-L3-MIB", l3FlowDstPort=l3FlowDstPort, l3FlowPriorityProtocol=l3FlowPriorityProtocol, l3FlowPriorityInterface=l3FlowPriorityInterface, l3MIB=l3MIB, l3FlowPriorityDstIpAddress=l3FlowPriorityDstIpAddress, l3FlowTable=l3FlowTable, l3FlowPriority=l3FlowPriority, l3FlowTOS=l3FlowTOS, l3FlowPriorityName=l3FlowPriorityName, l3ComplianceV10=l3ComplianceV10, l3FlowFilterId=l3FlowFilterId, l3FlowSrcIpAddress=l3FlowSrcIpAddress, l3FlowProtocol=l3FlowProtocol, l3Compliances=l3Compliances, l3FlowOctets=l3FlowOctets, l3FlowIndex=l3FlowIndex, l3FlowPriorityTOS=l3FlowPriorityTOS, l3FlowPriorityDstPort=l3FlowPriorityDstPort, l3ConfGroupV10=l3ConfGroupV10, l3FlowPortOfEntry=l3FlowPortOfEntry, l3Conformance=l3Conformance, l3FlowPrioritySrcIpAddress=l3FlowPrioritySrcIpAddress, l3FlowSrcPort=l3FlowSrcPort, l3FlowDstIpAddress=l3FlowDstIpAddress, l3FlowPriorityEntry=l3FlowPriorityEntry, PYSNMP_MODULE_ID=l3MIB, l3FlowPriorityIndex=l3FlowPriorityIndex, SSRProtocols=SSRProtocols, l3Group=l3Group, l3FlowPkts=l3FlowPkts, l3Groups=l3Groups, l3FlowPriorityTable=l3FlowPriorityTable, l3FlowPrioritySrcPort=l3FlowPrioritySrcPort, l3FlowEntry=l3FlowEntry)