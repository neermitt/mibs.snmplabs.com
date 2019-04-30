#
# PySNMP MIB module COM21-HCXVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COM21-HCXVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
com21, com21Hcx = mibBuilder.importSymbols("COM21-HCX-MIB", "com21", "com21Hcx")
hcxAlmSeverity, hcxEventLogTime = mibBuilder.importSymbols("COM21-HCXALM-MIB", "hcxAlmSeverity", "hcxEventLogTime")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, iso, MibIdentifier, Counter32, ObjectIdentity, Bits, ModuleIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "MibIdentifier", "Counter32", "ObjectIdentity", "Bits", "ModuleIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
com21HcxVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 1141, 2, 80))
if mibBuilder.loadTexts: com21HcxVlan.setLastUpdated('9701080000Z')
if mibBuilder.loadTexts: com21HcxVlan.setOrganization('Com21, Inc.')
com21HcxVlanCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 81))
com21HcxVlanStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 82))
com21HcxOc3VlanStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 83))
class PrimServiceState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class Com21RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("create", 2), ("destroy", 3), ("deactive", 4))

com21HcxVlanCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1), )
if mibBuilder.loadTexts: com21HcxVlanCtrlTable.setStatus('current')
com21HcxVlanCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1), ).setIndexNames((0, "COM21-HCXVLAN-MIB", "hcxVlanCtrlId"))
if mibBuilder.loadTexts: com21HcxVlanCtrlEntry.setStatus('current')
hcxVlanCtrlId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanCtrlId.setStatus('current')
hcxVlanCtrlName = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanCtrlName.setStatus('current')
hcxVlanShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanShelf.setStatus('current')
hcxVlanSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanSlot.setStatus('current')
hcxVlanCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tenBaseT", 1), ("onehundredBaseT", 2), ("oc3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanCardType.setStatus('current')
hcxVlanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanPort.setStatus('current')
hcxVlanPriStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 7), Com21RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcxVlanPriStatus.setStatus('current')
hcxVlanSecStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanSecStatus.setStatus('current')
hcxVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("external", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanType.setStatus('current')
hcxVlanPeerToPeerFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanPeerToPeerFlag.setStatus('current')
hcxVlanMcastDnstrmRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanMcastDnstrmRate.setStatus('current')
hcxVlanIpArpFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpArpFiltEnbl.setStatus('current')
hcxVlanIpSrcFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpSrcFiltEnbl.setStatus('current')
hcxVlanIpDstFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpDstFiltEnbl.setStatus('current')
hcxVlanIpBootpReqFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpBootpReqFiltEnbl.setStatus('current')
hcxVlanIpBootpReplyFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpBootpReplyFiltEnbl.setStatus('current')
hcxVlanIpDhcpSnoopFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpDhcpSnoopFiltEnbl.setStatus('current')
hcxVlanL2SnapFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2SnapFiltEnbl.setStatus('current')
hcxVlanL2NonSnapFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2NonSnapFiltEnbl.setStatus('current')
hcxVlanL2EnetFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2EnetFiltEnbl.setStatus('deprecated')
hcxVlanL2ArpIpv4FiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2ArpIpv4FiltEnbl.setStatus('deprecated')
hcxVlanL2Ipv4FiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2Ipv4FiltEnbl.setStatus('deprecated')
hcxVlanL2Ipv6FiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2Ipv6FiltEnbl.setStatus('deprecated')
hcxVlanL2IpxFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2IpxFiltEnbl.setStatus('deprecated')
hcxVlanL2AppletalkFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2AppletalkFiltEnbl.setStatus('deprecated')
hcxVlanL2OthersFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanL2OthersFiltEnbl.setStatus('deprecated')
hcxVlanIpNetbiosFiltEnbl = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanIpNetbiosFiltEnbl.setStatus('current')
hcxVPNNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVPNNum.setStatus('current')
hcxVlanVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanVpi.setStatus('current')
hcxVlanVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanVci.setStatus('current')
hcxVlanRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanRate.setStatus('current')
com21HcxVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1), )
if mibBuilder.loadTexts: com21HcxVlanStatsTable.setStatus('current')
com21HcxVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1), ).setIndexNames((0, "COM21-HCXVLAN-MIB", "hcxVlanStatsId"))
if mibBuilder.loadTexts: com21HcxVlanStatsEntry.setStatus('current')
hcxVlanStatsId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanStatsId.setStatus('current')
hcxVlanCurrMcastTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanCurrMcastTxPkts.setStatus('current')
hcxVlanCurrMcastDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanCurrMcastDroppedPkts.setStatus('current')
hcxVlanIpCurrArpFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrArpFiltStat.setStatus('current')
hcxVlanIpCurrSrcFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrSrcFiltStat.setStatus('current')
hcxVlanIpCurrDstFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrDstFiltStat.setStatus('current')
hcxVlanIpCurrBootpReqFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrBootpReqFiltStat.setStatus('current')
hcxVlanIpCurrBootpReplyFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrBootpReplyFiltStat.setStatus('current')
hcxVlanIpCurrDhcpSnoopFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrDhcpSnoopFiltStat.setStatus('current')
hcxVlanPrevMcastTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanPrevMcastTxPkts.setStatus('current')
hcxVlanPrevMcastDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanPrevMcastDroppedPkts.setStatus('current')
hcxVlanIpPrevArpFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevArpFiltStat.setStatus('current')
hcxVlanIpPrevSrcFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevSrcFiltStat.setStatus('current')
hcxVlanIpPrevDstFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevDstFiltStat.setStatus('current')
hcxVlanIpPrevBootpReqFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevBootpReqFiltStat.setStatus('current')
hcxVlanIpPrevBootpReplyFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevBootpReplyFiltStat.setStatus('current')
hcxVlanIpPrevDhcpSnoopFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevDhcpSnoopFiltStat.setStatus('current')
hcxVlanClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nil", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxVlanClearStats.setStatus('current')
hcxVlanL2CurrSnapFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrSnapFiltStat.setStatus('current')
hcxVlanL2CurrNonSnapFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrNonSnapFiltStat.setStatus('current')
hcxVlanL2CurrEnetFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrEnetFiltStat.setStatus('deprecated')
hcxVlanL2CurrArpIpv4FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrArpIpv4FiltStat.setStatus('deprecated')
hcxVlanL2CurrIpv4FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrIpv4FiltStat.setStatus('deprecated')
hcxVlanL2CurrIpv6FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrIpv6FiltStat.setStatus('deprecated')
hcxVlanL2CurrIpxFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrIpxFiltStat.setStatus('deprecated')
hcxVlanL2CurrAppletalkFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrAppletalkFiltStat.setStatus('deprecated')
hcxVlanL2CurrOthersFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 27), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2CurrOthersFiltStat.setStatus('deprecated')
hcxVlanIpCurrNetbiosFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpCurrNetbiosFiltStat.setStatus('current')
hcxVlanL2PrevSnapFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 29), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevSnapFiltStat.setStatus('current')
hcxVlanL2PrevNonSnapFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 30), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevNonSnapFiltStat.setStatus('current')
hcxVlanL2PrevEnetFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 31), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevEnetFiltStat.setStatus('deprecated')
hcxVlanL2PrevArpIpv4FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 32), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevArpIpv4FiltStat.setStatus('deprecated')
hcxVlanL2PrevIpv4FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 33), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevIpv4FiltStat.setStatus('deprecated')
hcxVlanL2PrevIpv6FiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 34), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevIpv6FiltStat.setStatus('deprecated')
hcxVlanL2PrevIpxFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 35), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevIpxFiltStat.setStatus('deprecated')
hcxVlanL2PrevAppletalkFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 36), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevAppletalkFiltStat.setStatus('deprecated')
hcxVlanL2PrevOthersFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 37), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanL2PrevOthersFiltStat.setStatus('deprecated')
hcxVlanIpPrevNetbiosFiltStat = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 38), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxVlanIpPrevNetbiosFiltStat.setStatus('current')
com21HcxOc3VlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1), )
if mibBuilder.loadTexts: com21HcxOc3VlanStatsTable.setStatus('current')
com21HcxOc3VlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1), ).setIndexNames((0, "COM21-HCXVLAN-MIB", "hcxOc3VlanStatsVlanId"))
if mibBuilder.loadTexts: com21HcxOc3VlanStatsEntry.setStatus('current')
hcxOc3VlanStatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsVlanId.setStatus('current')
hcxOc3VlanStatsCurrTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsCurrTxPkts.setStatus('current')
hcxOc3VlanStatsCurrRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsCurrRxPkts.setStatus('current')
hcxOc3VlanStatsCurrCrcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsCurrCrcPkts.setStatus('current')
hcxOc3VlanStatsPrevTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsPrevTxPkts.setStatus('current')
hcxOc3VlanStatsPrevRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsPrevRxPkts.setStatus('current')
hcxOc3VlanStatsPrevCrcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxOc3VlanStatsPrevCrcPkts.setStatus('current')
hcxOc3VlanStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nil", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxOc3VlanStatsClear.setStatus('current')
mibBuilder.exportSymbols("COM21-HCXVLAN-MIB", hcxVlanL2PrevIpv6FiltStat=hcxVlanL2PrevIpv6FiltStat, hcxVlanIpPrevArpFiltStat=hcxVlanIpPrevArpFiltStat, hcxVlanCtrlId=hcxVlanCtrlId, com21HcxVlanCtrlTable=com21HcxVlanCtrlTable, hcxOc3VlanStatsPrevCrcPkts=hcxOc3VlanStatsPrevCrcPkts, hcxVlanL2PrevAppletalkFiltStat=hcxVlanL2PrevAppletalkFiltStat, hcxVlanIpPrevBootpReplyFiltStat=hcxVlanIpPrevBootpReplyFiltStat, hcxVlanL2CurrNonSnapFiltStat=hcxVlanL2CurrNonSnapFiltStat, hcxVlanMcastDnstrmRate=hcxVlanMcastDnstrmRate, com21HcxVlanCtrlEntry=com21HcxVlanCtrlEntry, hcxVlanIpDstFiltEnbl=hcxVlanIpDstFiltEnbl, hcxVlanPeerToPeerFlag=hcxVlanPeerToPeerFlag, hcxOc3VlanStatsCurrRxPkts=hcxOc3VlanStatsCurrRxPkts, hcxVlanIpCurrBootpReplyFiltStat=hcxVlanIpCurrBootpReplyFiltStat, hcxVlanVci=hcxVlanVci, hcxVlanL2CurrArpIpv4FiltStat=hcxVlanL2CurrArpIpv4FiltStat, hcxVlanL2CurrIpv6FiltStat=hcxVlanL2CurrIpv6FiltStat, com21HcxOc3VlanStatsEntry=com21HcxOc3VlanStatsEntry, hcxVlanClearStats=hcxVlanClearStats, hcxVlanIpSrcFiltEnbl=hcxVlanIpSrcFiltEnbl, hcxVlanL2IpxFiltEnbl=hcxVlanL2IpxFiltEnbl, hcxOc3VlanStatsPrevRxPkts=hcxOc3VlanStatsPrevRxPkts, com21HcxVlanStatsTable=com21HcxVlanStatsTable, hcxVlanL2Ipv4FiltEnbl=hcxVlanL2Ipv4FiltEnbl, hcxVlanIpPrevDstFiltStat=hcxVlanIpPrevDstFiltStat, hcxVlanL2AppletalkFiltEnbl=hcxVlanL2AppletalkFiltEnbl, hcxOc3VlanStatsClear=hcxOc3VlanStatsClear, com21HcxVlanStatsEntry=com21HcxVlanStatsEntry, hcxVlanL2PrevEnetFiltStat=hcxVlanL2PrevEnetFiltStat, hcxVlanIpPrevNetbiosFiltStat=hcxVlanIpPrevNetbiosFiltStat, hcxVlanL2EnetFiltEnbl=hcxVlanL2EnetFiltEnbl, hcxVlanIpBootpReplyFiltEnbl=hcxVlanIpBootpReplyFiltEnbl, hcxVlanCurrMcastDroppedPkts=hcxVlanCurrMcastDroppedPkts, hcxOc3VlanStatsVlanId=hcxOc3VlanStatsVlanId, hcxVlanL2PrevArpIpv4FiltStat=hcxVlanL2PrevArpIpv4FiltStat, hcxVlanIpPrevBootpReqFiltStat=hcxVlanIpPrevBootpReqFiltStat, hcxVlanIpArpFiltEnbl=hcxVlanIpArpFiltEnbl, com21HcxOc3VlanStatsGroup=com21HcxOc3VlanStatsGroup, hcxVlanSecStatus=hcxVlanSecStatus, hcxVlanIpDhcpSnoopFiltEnbl=hcxVlanIpDhcpSnoopFiltEnbl, PYSNMP_MODULE_ID=com21HcxVlan, hcxVlanL2NonSnapFiltEnbl=hcxVlanL2NonSnapFiltEnbl, hcxVlanSlot=hcxVlanSlot, hcxVlanL2PrevIpxFiltStat=hcxVlanL2PrevIpxFiltStat, hcxOc3VlanStatsPrevTxPkts=hcxOc3VlanStatsPrevTxPkts, Com21RowStatus=Com21RowStatus, hcxVlanPort=hcxVlanPort, hcxVlanL2CurrIpv4FiltStat=hcxVlanL2CurrIpv4FiltStat, hcxVlanCardType=hcxVlanCardType, hcxVlanL2ArpIpv4FiltEnbl=hcxVlanL2ArpIpv4FiltEnbl, hcxVlanIpBootpReqFiltEnbl=hcxVlanIpBootpReqFiltEnbl, hcxVlanL2OthersFiltEnbl=hcxVlanL2OthersFiltEnbl, hcxVlanCurrMcastTxPkts=hcxVlanCurrMcastTxPkts, hcxVlanIpCurrArpFiltStat=hcxVlanIpCurrArpFiltStat, com21HcxOc3VlanStatsTable=com21HcxOc3VlanStatsTable, hcxVlanL2Ipv6FiltEnbl=hcxVlanL2Ipv6FiltEnbl, hcxVlanIpCurrDhcpSnoopFiltStat=hcxVlanIpCurrDhcpSnoopFiltStat, hcxVlanRate=hcxVlanRate, hcxVlanIpNetbiosFiltEnbl=hcxVlanIpNetbiosFiltEnbl, hcxVlanL2SnapFiltEnbl=hcxVlanL2SnapFiltEnbl, hcxVlanL2PrevSnapFiltStat=hcxVlanL2PrevSnapFiltStat, hcxVlanIpCurrSrcFiltStat=hcxVlanIpCurrSrcFiltStat, hcxOc3VlanStatsCurrTxPkts=hcxOc3VlanStatsCurrTxPkts, hcxVlanType=hcxVlanType, hcxOc3VlanStatsCurrCrcPkts=hcxOc3VlanStatsCurrCrcPkts, hcxVlanL2CurrOthersFiltStat=hcxVlanL2CurrOthersFiltStat, hcxVlanIpCurrBootpReqFiltStat=hcxVlanIpCurrBootpReqFiltStat, hcxVlanPrevMcastTxPkts=hcxVlanPrevMcastTxPkts, com21HcxVlanStatsGroup=com21HcxVlanStatsGroup, hcxVlanIpCurrDstFiltStat=hcxVlanIpCurrDstFiltStat, hcxVlanL2CurrSnapFiltStat=hcxVlanL2CurrSnapFiltStat, hcxVlanL2PrevNonSnapFiltStat=hcxVlanL2PrevNonSnapFiltStat, com21HcxVlan=com21HcxVlan, hcxVlanL2CurrIpxFiltStat=hcxVlanL2CurrIpxFiltStat, hcxVlanIpPrevDhcpSnoopFiltStat=hcxVlanIpPrevDhcpSnoopFiltStat, hcxVlanShelf=hcxVlanShelf, hcxVlanIpPrevSrcFiltStat=hcxVlanIpPrevSrcFiltStat, com21HcxVlanCtrlGroup=com21HcxVlanCtrlGroup, hcxVlanCtrlName=hcxVlanCtrlName, PrimServiceState=PrimServiceState, hcxVlanVpi=hcxVlanVpi, hcxVlanIpCurrNetbiosFiltStat=hcxVlanIpCurrNetbiosFiltStat, hcxVlanL2CurrEnetFiltStat=hcxVlanL2CurrEnetFiltStat, hcxVlanL2PrevOthersFiltStat=hcxVlanL2PrevOthersFiltStat, hcxVlanStatsId=hcxVlanStatsId, hcxVlanPriStatus=hcxVlanPriStatus, hcxVlanPrevMcastDroppedPkts=hcxVlanPrevMcastDroppedPkts, hcxVPNNum=hcxVPNNum, hcxVlanL2CurrAppletalkFiltStat=hcxVlanL2CurrAppletalkFiltStat, hcxVlanL2PrevIpv4FiltStat=hcxVlanL2PrevIpv4FiltStat)