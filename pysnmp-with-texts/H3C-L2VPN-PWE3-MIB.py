#
# PySNMP MIB module H3C-L2VPN-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-L2VPN-PWE3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, Counter32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, iso, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
h3cL2VpnPwe3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78))
if mibBuilder.loadTexts: h3cL2VpnPwe3.setLastUpdated('200703310000Z')
if mibBuilder.loadTexts: h3cL2VpnPwe3.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cL2VpnPwe3.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cL2VpnPwe3.setDescription('This MIB contains objects to manage PWE3.')
class H3cL2VpnVcEncapsType(TextualConvention, Integer32):
    description = "An indication of the L2Vpn's VC encapsulation type: Frame Relay DLCI ( Martini Mode ) (1) ATM AAL5 SDU VCC transport (2) ATM transparent cell transport (3) Ethernet Tagged Mode (4) Ethernet (5) HDLC (6) PPP (7) SONET/SDH Circuit Emulation Service Over MPLS (CEM) (8) ATM n-to-one VCC cell transport (9) ATM n-to-one VPC cell transport (10) IP Layer2 Transport (11) ATM one-to-one VCC Cell Mode (12) ATM one-to-one VPC Cell Mode (13) ATM AAL5 PDU VCC transport (14) Frame-Relay Port mode (15) SONET/SDH Circuit Emulation over Packet (CEP) (16) Structure-agnostic E1 over Packet (SAE1oP) (17) Structure-agnostic T1 (DS1) over Packet (SAT1oP) (18) Structure-agnostic E3 over Packet (SAE3oP) (19) Structure-agnostic T3 (DS3) over Packet (SAT3oP) (20) CESoPSN basic mode (21) TDMoIP basic mode (22) CESoPSN TDM with CAS (23) TDMoIP TDM with CAS (24) Frame Relay DLCI (25) IP-interworking (64) unknown (255) "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 255))
    namedValues = NamedValues(("frameRelayDlciMartini", 1), ("atmAal5SduVccTransport", 2), ("atmTransparentCellTransport", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmN2OneVccCellTransport", 9), ("atmN2OneVpcCellTransport", 10), ("ipLayer2Transport", 11), ("atmOne2OneVccCellMode", 12), ("atmOne2OneVpcCellMode", 13), ("atmAal5PduVccTransport", 14), ("frameRelayPortMode", 15), ("cep", 16), ("saE1oP", 17), ("saT1oP", 18), ("saE3oP", 19), ("saT3oP", 20), ("cESoPsnBasicMode", 21), ("tDMoIPbasicMode", 22), ("l2VpnCESoPSNTDMwithCAS", 23), ("l2VpnTDMoIPTDMwithCAS", 24), ("frameRelayDlci", 25), ("ipInterworking", 64), ("unknown", 255))

h3cL2VpnPwe3ScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 1))
h3cPwVcTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPwVcTrapOpen.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcTrapOpen.setDescription('Whether pwe3 trap is globally enabled. false: disable; true: enable.')
h3cL2VpnPwe3Table = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2))
h3cPwVcTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1), )
if mibBuilder.loadTexts: h3cPwVcTable.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcTable.setDescription('This table is the VC configuration table. Users can create or delete a VC by it.')
h3cPwVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1), ).setIndexNames((0, "H3C-L2VPN-PWE3-MIB", "h3cPwVcIndex"))
if mibBuilder.loadTexts: h3cPwVcEntry.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcEntry.setDescription('Provides the information of a VC entry.')
h3cPwVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cPwVcIndex.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcIndex.setDescription('Index for the conceptual row identifying a PW within this PW Emulation table.')
h3cPwVcID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcID.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcID.setDescription("Used in the outgoing PW ID field within the 'Virtual Circuit FEC Element'.")
h3cPwVcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 3), H3cL2VpnVcEncapsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcType.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcType.setDescription("Indication of the L2Vpn's VC encapsulation type.")
h3cPwVcPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcPeerAddr.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcPeerAddr.setDescription('This object contain the value of the peer ip address of the Martini VLL PW.')
h3cPwVcMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcMtu.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcMtu.setDescription('If not equal zero, the optional Mtu object in the signaling protocol will be sent with this value, representing the locally supported MTU size over the interface (or the virtual interface) associated with the PW. The default value is 1500.')
hwPwVcCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("multiPort", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPwVcCfgType.setStatus('current')
if mibBuilder.loadTexts: hwPwVcCfgType.setDescription('Indicates the type of the pw: 1: primary; 2: backup; 3: multiPort.')
h3cPwVcInboundLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPwVcInboundLabel.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcInboundLabel.setDescription('For Martini VLL, the value will be created by system automatically.')
h3cPwVcOutboundLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPwVcOutboundLabel.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcOutboundLabel.setDescription('For Martini VLL, the value will be created by the peer automatically.')
h3cPwVcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcIfIndex.setDescription('Index of the interface (or the virtual interface) associated with the PW.')
h3cPwVcAcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPwVcAcStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcAcStatus.setDescription('Local AC(Attachment Circuit) status: 1: down; 2: up.')
h3cPwVcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPwVcStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcStatus.setDescription('Indicates the status of the PW in the local node. 1: down; 2: up.')
h3cPwVcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPwVcRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, h3cPwVcID, h3cPwVcType, h3cPwVcPeerAddr h3cPwVcMtu, hwPwVcCfgType and h3cPwVcIfIndex must be specified.')
h3cL2VpnPwe3Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3))
h3cPwVcSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3, 1)).setObjects(("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
if mibBuilder.loadTexts: h3cPwVcSwitchWtoP.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcSwitchWtoP.setDescription('This notification is generated when switch from working pw to protect pw happens. The first group of h3cPwVcID/h3cPwVcTypeh3cPwVcPeerAddr is parameter of the work PW , and the second group of h3cPwVcID/h3cPwVcTypeh3cPwVcPeerAddr is parameter of the protect PW.')
h3cPwVcSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3, 2)).setObjects(("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
if mibBuilder.loadTexts: h3cPwVcSwitchPtoW.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcSwitchPtoW.setDescription('This notification is generated when switch from protect pw to working pw happens. The first group of h3cPwVcID/h3cPwVcTypeh3cPwVcPeerAddr is parameter of the protect PW , and the second group of h3cPwVcID/h3cPwVcTypeh3cPwVcPeerAddr is parameter of the work PW.')
h3cPwVcDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3, 3)).setObjects(("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
if mibBuilder.loadTexts: h3cPwVcDown.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcDown.setDescription("This notification indicates the VC's state changes to down.")
h3cPwVcUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3, 4)).setObjects(("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
if mibBuilder.loadTexts: h3cPwVcUp.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcUp.setDescription("This notification indicates the VC's state changes to up.")
h3cPwVcDeleted = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 78, 3, 5)).setObjects(("H3C-L2VPN-PWE3-MIB", "h3cPwVcID"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcType"), ("H3C-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
if mibBuilder.loadTexts: h3cPwVcDeleted.setStatus('current')
if mibBuilder.loadTexts: h3cPwVcDeleted.setDescription('This notification indicates the VC is deleted.')
mibBuilder.exportSymbols("H3C-L2VPN-PWE3-MIB", h3cL2VpnPwe3ScalarGroup=h3cL2VpnPwe3ScalarGroup, h3cPwVcRowStatus=h3cPwVcRowStatus, h3cPwVcSwitchPtoW=h3cPwVcSwitchPtoW, h3cPwVcID=h3cPwVcID, h3cPwVcSwitchWtoP=h3cPwVcSwitchWtoP, h3cPwVcDown=h3cPwVcDown, h3cPwVcDeleted=h3cPwVcDeleted, h3cPwVcTable=h3cPwVcTable, h3cPwVcIndex=h3cPwVcIndex, h3cPwVcMtu=h3cPwVcMtu, H3cL2VpnVcEncapsType=H3cL2VpnVcEncapsType, hwPwVcCfgType=hwPwVcCfgType, h3cPwVcEntry=h3cPwVcEntry, h3cPwVcUp=h3cPwVcUp, h3cPwVcIfIndex=h3cPwVcIfIndex, h3cPwVcStatus=h3cPwVcStatus, h3cPwVcTrapOpen=h3cPwVcTrapOpen, h3cPwVcPeerAddr=h3cPwVcPeerAddr, h3cPwVcType=h3cPwVcType, h3cPwVcOutboundLabel=h3cPwVcOutboundLabel, h3cL2VpnPwe3Notifications=h3cL2VpnPwe3Notifications, h3cL2VpnPwe3Table=h3cL2VpnPwe3Table, PYSNMP_MODULE_ID=h3cL2VpnPwe3, h3cPwVcInboundLabel=h3cPwVcInboundLabel, h3cPwVcAcStatus=h3cPwVcAcStatus, h3cL2VpnPwe3=h3cL2VpnPwe3)
