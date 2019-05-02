#
# PySNMP MIB module MLD-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MLD-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Integer32, IpAddress, Gauge32, MibIdentifier, Bits, TimeTicks, Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32")
DisplayString, RowStatus, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TextualConvention")
swMldSnpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 34))
if mibBuilder.loadTexts: swMldSnpMIB.setLastUpdated('0802020000Z')
if mibBuilder.loadTexts: swMldSnpMIB.setOrganization('D-Link Crop.')
if mibBuilder.loadTexts: swMldSnpMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swMldSnpMIB.setDescription('The Structure of MLD snooping management for the proprietary enterprise.')
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swMldSnpCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 34, 1))
swMldSnpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 34, 2))
swMldSnpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 34, 3))
swMldSnoopingGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 34, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingGlobalState.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGlobalState.setDescription('This object indicates if the MLD snooping capture function is enabled or disabled.')
swMldSnoopingMcstRTOnly = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 34, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingMcstRTOnly.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingMcstRTOnly.setDescription('Specifies that the switch should forward all multicast traffic to a multicast-enabled IPv6 router only.')
swMldSnoopingMaxSupportedVlans = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingMaxSupportedVlans.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingMaxSupportedVlans.setDescription('Maximum number of VLANs in the MLD snooping table (swMldSnoopingCtrlTable).')
swMldSnoopingCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2), )
if mibBuilder.loadTexts: swMldSnoopingCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingCtrlTable.setDescription("The table controls the VLAN's MLD function. Its scale depends on the current VLAN state (swL2VlanInfoStatus). If the VLAN is in disabled mode, there is only one entry in the table, with index 1. If the VLAN is in Port-Base or 802.1q mode, the number of entries can be up to 12, with an index range from 1 to 12.")
swMldSnoopingCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1), ).setIndexNames((0, "MLD-SNOOPING-MIB", "swMldSnoopingCtrlVid"))
if mibBuilder.loadTexts: swMldSnoopingCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingCtrlEntry.setDescription('The entry in MLD control table (swMldSnoopingCtrlTable). The entry is effective only when MLD capture switch (swMldSnoopingGlobalState) is enabled.')
swMldSnoopingCtrlVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingCtrlVid.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingCtrlVid.setDescription("This object indicates the MLD control entry's VLAN ID. If the VLAN is disabled, the VID is always 0 and cannot be changed by management users. If VLAN is in Port-Base mode, the VID is arranged from 1 to 12, fixed form. If VLAN is in 802.1q mode, the VID setting can vary from 1 to 4094 by the management user, and the VID in each entry must be unique in the MLD Control Table.")
swMldSnoopingQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(125)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingQueryInterval.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingQueryInterval.setDescription('The frequency at which MLD Host-Query packets are transmitted on this switch.')
swMldSnoopingMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingMaxResponseTime.setDescription('The maximum query response time on this switch.')
swMldSnoopingRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingRobustness.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingRobustness.setDescription('The Robustness Variable allows tuning for the expected packet loss on a subnet. If a subnet is expected to have a high loss, the Robustness Variable may be increased. MLD is robust to (Robustness Variable-1) packet losses.')
swMldSnoopingLastMemberQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingLastMemberQueryInterval.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingLastMemberQueryInterval.setDescription('The Last Member Query Interval is the Max Response Time inserted into Group-Specific Queries sent in response to Leave Group messages and is also the amount of time between Group-Specific Query messages.')
swMldSnoopingHostTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16711450)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingHostTimeout.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingHostTimeout.setDescription('The timer value for sending a MLD query packet when none were sent by the host in the LAN. The timer works on a per-VLAN basis. Our device will be activated to send a query message if the timer has expired.')
swMldSnoopingRouteTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16711450)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingRouteTimeout.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingRouteTimeout.setDescription('The Router Timeout is how long a host must wait after hearing a Query before it sends any MLD messages.')
swMldSnoopingDoneTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16711450)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingDoneTimer.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingDoneTimer.setDescription('When a querier receives a Leave Group message for a group that has group members on the reception interface, it sends Group-Specific Queries swMldSnoopingDoneTimer to the group that is left.')
swMldSnoopingQueryState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingQueryState.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingQueryState.setDescription('This object decides if the MLD query is enabled or disabled.')
swMldSnoopingCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("querier", 2), ("non-querier", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingCurrentState.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingCurrentState.setDescription('This object indicates the current MLD query state.')
swMldSnoopingCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingCtrlState.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingCtrlState.setDescription('This object indicates the status of this entry. other(1) - this entry is currently in use but the conditions under which it will remain so are different for each of the following values. disable(2) - MLD function is disabled for this entry. enable(3) - MLD function is enabled for this entry.')
swMldSnoopingFastDoneState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingFastDoneState.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingFastDoneState.setDescription('This object indicates the fast_leave status of this entry. other(1) - this entry is currently in use but the conditions under which it will remain so are different for each of the following values. disable(2) - MLD fast-done function is disabled for this entry. enable(3) - MLD fast-done function is enabled for this entry.')
swMldSnoopingVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version-1", 1), ("version-2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnoopingVersion.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingVersion.setDescription("This object indicates the MLD version of this entry. If the MLD version is configured with a lower version, the higher version's MLD Report/Leave messages will be ignored. ")
swMldSnoopingGroupInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3), )
if mibBuilder.loadTexts: swMldSnoopingGroupInfoTable.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoTable.setDescription('The table contains the current MLD snooping information captured by this device, provided that swMldSnoopingGlobalState and swMldSnoopingCtrlState of associated VLAN entries are all enabled. Note that the priority of MLD table entries is lower than the Filtering Table, i.e. if there is a table hash collision between the entries of the MLD Table and the Filtering Table inside the switch H/W address table, then the Filtering Table entry overwrites the colliding entry of the MLD snooping Table. ')
swMldSnoopingGroupInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1), ).setIndexNames((0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupInfoVid"), (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupInfoIpAddr"))
if mibBuilder.loadTexts: swMldSnoopingGroupInfoEntry.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoEntry.setDescription('Information about current MLD information which has been captured by this device, provided that swMldSnoopingGlobalState and swMldSnoopingCtrlState of the associated VLAN entries are all enabled.')
swMldSnoopingGroupInfoVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupInfoVid.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoVid.setDescription('This object indicates the VID of an individual MLD table entry. It shows the VID of MLD report information that has been captured on the network.')
swMldSnoopingGroupInfoIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupInfoIpAddr.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoIpAddr.setDescription('This object identifies the group IP address which is captured from the MLD packet, on a per-VLAN basis.')
swMldSnoopingGroupInfoMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupInfoMacAddr.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoMacAddr.setDescription('This object identifies the MAC addresses that correspond to swMldSnoopingGroupInfoIpAddr, on a per-VLAN basis.')
swMldSnoopingGroupInfoPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupInfoPortMap.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoPortMap.setDescription("This object indicates which ports belong to the same multicast group, on a per-VLAN basis. Each multicast group has an octet string to indicate the port map. The most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the switch is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'(Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant). The 4 octets represent one unit port according to its logical port. If the unit has less than 32 ports, other ports will be set to 0.")
swMldSnoopingGroupInfoReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupInfoReportCount.setStatus('obsolete')
if mibBuilder.loadTexts: swMldSnoopingGroupInfoReportCount.setDescription('This object indicates how many report packets were received by our device corresponding with the entry when the MLD function is enabled, on a per-VLAN basis.')
swMldSnpRouterPortsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4), )
if mibBuilder.loadTexts: swMldSnpRouterPortsTable.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterPortsTable.setDescription("This table controls the VLAN's MLD router ports function.")
swMldSnpRouterPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1), ).setIndexNames((0, "MLD-SNOOPING-MIB", "swMldSnpRouterPortsVid"))
if mibBuilder.loadTexts: swMldSnpRouterPortsEntry.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterPortsEntry.setDescription('This entry shows the MLD router ports table (swMldSnoopingCtrlTable). ')
swMldSnpRouterPortsVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpRouterPortsVid.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterPortsVid.setDescription('This object indicates the MLD router ports entry VLAN ID. If a VLAN is disabled, the VID is always 0 and cannot be changed by management users. If a VLAN is in Port-Base mode, the VID is arranged from 1 to 12, fixed form. If a VLAN is in 802.1q mode, the VID setting can vary from 1 to 4094 by a management user, and the VID in each entry must be unique in the MLD ports Table.')
swMldSnpRouterStaticPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnpRouterStaticPortList.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterStaticPortList.setDescription('Displays router ports that have been statically configured.')
swMldSnpRouterDynamicPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpRouterDynamicPortList.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterDynamicPortList.setDescription('Displays router ports that have been dynamically configured.')
swMldSnpRouterForbiddenPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMldSnpRouterForbiddenPortList.setStatus('current')
if mibBuilder.loadTexts: swMldSnpRouterForbiddenPortList.setDescription('Displays router ports that have been configured to be forbidden.')
swMldSnoopingGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5), )
if mibBuilder.loadTexts: swMldSnoopingGroupTable.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupTable.setDescription('The table contains the current MLD snooping information captured by the device, provided that the swMldSnoopingGlobalState and swMldSnoopingCtrlState of the associated VLAN entries are all enabled. Note that the priority of the MLD table entries is lower than the Filtering Table, i.e. if there is a table hash collision between the entries of the MLD Table and the Filtering Table inside the switch H/W address table, then the Filtering Table entry overwrites the colliding entry of the MLD snooping Table. ')
swMldSnoopingGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1), ).setIndexNames((0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupVid"), (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupGroupAddr"), (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupSourceAddr"))
if mibBuilder.loadTexts: swMldSnoopingGroupEntry.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupEntry.setDescription('Information about the current MLD information which has been captured by the device, provided that swMldSnoopingGlobalState and swMldSnoopingCtrlState of the associated VLAN entries are all enabled.')
swMldSnoopingGroupVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupVid.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupVid.setDescription('This object indicates the VID of the individual MLD table entry. It shows the VID of the MLD report information captured on the network.')
swMldSnoopingGroupGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupGroupAddr.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupGroupAddr.setDescription('This object identifies the group IP address which has been captured from the MLD packet, on a per-VLAN basis.')
swMldSnoopingGroupSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 3), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupSourceAddr.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupSourceAddr.setDescription('This object identifies the source addresses which correspond to swMldSnoopingGroupInfoGroupAddr, on a per-VLAN basis.')
swMldSnoopingGroupIncludePortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupIncludePortMap.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupIncludePortMap.setDescription('This object indicates the port list under INCLUDE mode.')
swMldSnoopingGroupExcludePortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnoopingGroupExcludePortMap.setStatus('current')
if mibBuilder.loadTexts: swMldSnoopingGroupExcludePortMap.setDescription('This object indicates the port list under EXCLUDE mode.')
swMldSnpForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6), )
if mibBuilder.loadTexts: swMldSnpForwardingTable.setStatus('current')
if mibBuilder.loadTexts: swMldSnpForwardingTable.setDescription('This table contains the MLD Snooping forwarding information.')
swMldSnpForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1), ).setIndexNames((0, "MLD-SNOOPING-MIB", "swMldSnpVid"), (0, "MLD-SNOOPING-MIB", "swMldSnpSourceIpAddr"), (0, "MLD-SNOOPING-MIB", "swMldSnpMutiGroupIpAddr"))
if mibBuilder.loadTexts: swMldSnpForwardingEntry.setStatus('current')
if mibBuilder.loadTexts: swMldSnpForwardingEntry.setDescription('A list of information about MLD Snooping forwarding.')
swMldSnpVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpVid.setStatus('current')
if mibBuilder.loadTexts: swMldSnpVid.setDescription("This object indicates the MLD Forwarding entry's VLAN ID.")
swMldSnpSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpSourceIpAddr.setStatus('current')
if mibBuilder.loadTexts: swMldSnpSourceIpAddr.setDescription('This object identifies the forwarding IP address, which is captured from the MLD packet.')
swMldSnpMutiGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 3), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpMutiGroupIpAddr.setStatus('current')
if mibBuilder.loadTexts: swMldSnpMutiGroupIpAddr.setDescription('This object identifies the Multicast Group IP address, which is captured from MLD packet.')
swMldSnpForwardingListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMldSnpForwardingListenPort.setStatus('current')
if mibBuilder.loadTexts: swMldSnpForwardingListenPort.setDescription('Indicates the MLD Snooping forwarding listen port.')
mibBuilder.exportSymbols("MLD-SNOOPING-MIB", swMldSnoopingCurrentState=swMldSnoopingCurrentState, swMldSnoopingQueryInterval=swMldSnoopingQueryInterval, swMldSnoopingGroupGroupAddr=swMldSnoopingGroupGroupAddr, swMldSnoopingGlobalState=swMldSnoopingGlobalState, swMldSnpMIB=swMldSnpMIB, swMldSnoopingRouteTimeout=swMldSnoopingRouteTimeout, swMldSnpRouterStaticPortList=swMldSnpRouterStaticPortList, swMldSnoopingGroupSourceAddr=swMldSnoopingGroupSourceAddr, swMldSnpInfo=swMldSnpInfo, swMldSnoopingCtrlState=swMldSnoopingCtrlState, swMldSnoopingGroupInfoReportCount=swMldSnoopingGroupInfoReportCount, swMldSnpForwardingTable=swMldSnpForwardingTable, swMldSnoopingGroupEntry=swMldSnoopingGroupEntry, swMldSnoopingCtrlVid=swMldSnoopingCtrlVid, swMldSnpVid=swMldSnpVid, swMldSnoopingFastDoneState=swMldSnoopingFastDoneState, swMldSnoopingGroupInfoMacAddr=swMldSnoopingGroupInfoMacAddr, swMldSnoopingGroupInfoEntry=swMldSnoopingGroupInfoEntry, swMldSnoopingRobustness=swMldSnoopingRobustness, swMldSnpForwardingListenPort=swMldSnpForwardingListenPort, PortList=PortList, swMldSnoopingHostTimeout=swMldSnoopingHostTimeout, swMldSnoopingDoneTimer=swMldSnoopingDoneTimer, swMldSnpRouterPortsVid=swMldSnpRouterPortsVid, swMldSnoopingGroupIncludePortMap=swMldSnoopingGroupIncludePortMap, swMldSnoopingCtrlTable=swMldSnoopingCtrlTable, swMldSnpMgmt=swMldSnpMgmt, swMldSnpRouterDynamicPortList=swMldSnpRouterDynamicPortList, swMldSnpRouterPortsTable=swMldSnpRouterPortsTable, swMldSnoopingMaxResponseTime=swMldSnoopingMaxResponseTime, swMldSnpRouterPortsEntry=swMldSnpRouterPortsEntry, swMldSnoopingMaxSupportedVlans=swMldSnoopingMaxSupportedVlans, swMldSnpRouterForbiddenPortList=swMldSnpRouterForbiddenPortList, swMldSnoopingGroupVid=swMldSnoopingGroupVid, swMldSnoopingVersion=swMldSnoopingVersion, Ipv6Address=Ipv6Address, swMldSnoopingGroupExcludePortMap=swMldSnoopingGroupExcludePortMap, swMldSnoopingQueryState=swMldSnoopingQueryState, swMldSnpSourceIpAddr=swMldSnpSourceIpAddr, swMldSnoopingCtrlEntry=swMldSnoopingCtrlEntry, swMldSnoopingGroupInfoVid=swMldSnoopingGroupInfoVid, swMldSnoopingGroupInfoTable=swMldSnoopingGroupInfoTable, swMldSnpCtrl=swMldSnpCtrl, swMldSnoopingGroupInfoIpAddr=swMldSnoopingGroupInfoIpAddr, swMldSnoopingMcstRTOnly=swMldSnoopingMcstRTOnly, swMldSnpMutiGroupIpAddr=swMldSnpMutiGroupIpAddr, swMldSnpForwardingEntry=swMldSnpForwardingEntry, swMldSnoopingGroupInfoPortMap=swMldSnoopingGroupInfoPortMap, PYSNMP_MODULE_ID=swMldSnpMIB, swMldSnoopingGroupTable=swMldSnoopingGroupTable, swMldSnoopingLastMemberQueryInterval=swMldSnoopingLastMemberQueryInterval)