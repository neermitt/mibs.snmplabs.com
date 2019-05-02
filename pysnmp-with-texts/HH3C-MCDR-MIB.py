#
# PySNMP MIB module HH3C-MCDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MCDR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Gauge32, ModuleIdentity, Bits, TimeTicks, Integer32, Counter64, IpAddress, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "Integer32", "Counter64", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
hh3cMultCDR = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 86))
hh3cMultCDR.setRevisions(('2007-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cMultCDR.setRevisionsDescriptions(('The multicast call detail record MIB.',))
if mibBuilder.loadTexts: hh3cMultCDR.setLastUpdated('200712150000Z')
if mibBuilder.loadTexts: hh3cMultCDR.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cMultCDR.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cMultCDR.setDescription('The initial version of this MIB file.')
hh3cMultCDRCfgObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1))
hh3cMultCDRStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMultCDRStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cMultCDRStatus.setDescription('Configure to enable or disable multicast CDR function.')
hh3cMultCDRReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMultCDRReportInterval.setStatus('current')
if mibBuilder.loadTexts: hh3cMultCDRReportInterval.setDescription('Configure the multicast CDR report-interval. Unit: second.')
hh3cMultCDRCacheLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMultCDRCacheLimit.setStatus('current')
if mibBuilder.loadTexts: hh3cMultCDRCacheLimit.setDescription('Configure the multicast CDR cache-limit.')
hh3cMultCDRRecordDelay = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMultCDRRecordDelay.setStatus('current')
if mibBuilder.loadTexts: hh3cMultCDRRecordDelay.setDescription('Configure the multicast CDR record-delay. Unit: second')
hh3cMultCDRRecordSend = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send", 1), ("caching", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMultCDRRecordSend.setStatus('current')
if mibBuilder.loadTexts: hh3cMultCDRRecordSend.setDescription('Send record at once.')
hh3cMultUserOnlineInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2), )
if mibBuilder.loadTexts: hh3cMultUserOnlineInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserOnlineInfoTable.setDescription('Multicast user online information table.')
hh3cMultUserOnlineInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-MCDR-MIB", "hh3cMultUserRecordID"))
if mibBuilder.loadTexts: hh3cMultUserOnlineInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserOnlineInfoEntry.setDescription('The entry of multicast user online information table.')
hh3cMultUserRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cMultUserRecordID.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserRecordID.setDescription('The index of online record.')
hh3cMultUserSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserSubIfIndex.setDescription('The index of sub-interface which is active. If the value is zero, hh3cMultUserSubIfIndex should be ignored.')
hh3cMultUserVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserVlanID.setDescription('The ID of VLAN in which the user joined the multicast group.')
hh3cMultUserJoinGAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserJoinGAddrType.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserJoinGAddrType.setDescription('Type of the multicast group IP address.')
hh3cMultUserJoinGAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserJoinGAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserJoinGAddr.setDescription('The multicast group address which the user joined.')
hh3cMultUserJoinSAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserJoinSAddrType.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserJoinSAddrType.setDescription('Type of the multicast source IP address.')
hh3cMultUserJoinSAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserJoinSAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserJoinSAddr.setDescription("The multicast source address which the user joined. If the value is '0.0.0.0'(IPv4) or '::'(IPv6), hh3cMultUserJoinSAddr should be ignored.")
hh3cMultUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("preview", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserStatus.setDescription('The current status of user. permit - user in permit status. preview - user in preview status.')
hh3cMultUserJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserJoinTime.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserJoinTime.setDescription('The time when the user joined the multicast group.')
hh3cMultUserPreviewTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserPreviewTimes.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserPreviewTimes.setDescription('The times of multicast preview which the user joined. If hh3cMultUserStatus is not preview, hh3cMultUserPreviewTimes should be ignored.')
hh3cMultUserPreviewRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMultUserPreviewRemain.setStatus('current')
if mibBuilder.loadTexts: hh3cMultUserPreviewRemain.setDescription('The remanent time slice of multicast preview which the user joined. If hh3cMultUserStatus is not preview, hh3cMultUserPreviewRemain should be ignored.')
mibBuilder.exportSymbols("HH3C-MCDR-MIB", hh3cMultCDRStatus=hh3cMultCDRStatus, PYSNMP_MODULE_ID=hh3cMultCDR, hh3cMultUserPreviewTimes=hh3cMultUserPreviewTimes, hh3cMultUserJoinGAddr=hh3cMultUserJoinGAddr, hh3cMultCDRCacheLimit=hh3cMultCDRCacheLimit, hh3cMultUserOnlineInfoTable=hh3cMultUserOnlineInfoTable, hh3cMultCDRRecordSend=hh3cMultCDRRecordSend, hh3cMultUserOnlineInfoEntry=hh3cMultUserOnlineInfoEntry, hh3cMultCDRRecordDelay=hh3cMultCDRRecordDelay, hh3cMultUserJoinSAddr=hh3cMultUserJoinSAddr, hh3cMultCDRCfgObject=hh3cMultCDRCfgObject, hh3cMultUserJoinTime=hh3cMultUserJoinTime, hh3cMultUserJoinGAddrType=hh3cMultUserJoinGAddrType, hh3cMultUserRecordID=hh3cMultUserRecordID, hh3cMultUserSubIfIndex=hh3cMultUserSubIfIndex, hh3cMultCDR=hh3cMultCDR, hh3cMultCDRReportInterval=hh3cMultCDRReportInterval, hh3cMultUserStatus=hh3cMultUserStatus, hh3cMultUserJoinSAddrType=hh3cMultUserJoinSAddrType, hh3cMultUserVlanID=hh3cMultUserVlanID, hh3cMultUserPreviewRemain=hh3cMultUserPreviewRemain)