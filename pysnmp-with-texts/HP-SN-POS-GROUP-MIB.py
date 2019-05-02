#
# PySNMP MIB module HP-SN-POS-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Wed May  1 13:36:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
snPOS, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snPOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, TimeTicks, Integer32, NotificationType, Unsigned32, iso, Gauge32, Counter64, ObjectIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "iso", "Gauge32", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class POSStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class DisplayString(OctetString):
    pass

snPOSInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1))
snPOSInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1), )
if mibBuilder.loadTexts: snPOSInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoTable.setDescription('A specific snPOSInfo group consists of a number of switch ports. ')
snPOSInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1), ).setIndexNames((0, "HP-SN-POS-GROUP-MIB", "snPOSInfoPortNum"))
if mibBuilder.loadTexts: snPOSInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoEntry.setDescription('An entry in the snPOSInfo table indicates the configuration on a specified port. A SNMP SET PDU for a row of the snPOSInfoTable requires the entired sequence of the MIB Objects in each snPOSInfoEntry stored in one PDU. Otherwise, GENERR return-value will be returned.')
snPOSInfoPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSInfoPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoPortNum.setDescription('The port index. The bit 0 to bit 7: port number. The bit 8 to bit 11: slot number (slot for chassis only).')
snPOSIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSIfIndex.setDescription('In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 1213 and RFC 1573.')
snPOSDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSDescr.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSDescr.setDescription('A textual string containing the slot/port information about the interface.')
snPOSName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSName.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSName.setDescription('Port Name string.')
snPOSInfoSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("s155000", 1), ("s622000", 2), ("other", 3), ("s2488000", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoSpeed.setDescription('The speed configuration for a port. The values are: 155000 622000 2488000 ')
snPOSInfoAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoAdminStatus.setDescription('The desired state of all ports. The testing(3) state indicates that no operational packets can be passed. (same as ifAdminStatus in MIB-II)')
snPOSInfoLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSInfoLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoLinkStatus.setDescription('The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed. (same as ifOperStatus in MIB-II)')
snPOSInfoClock = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("line", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoClock.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoClock.setDescription('Clock default internal')
snPOSInfoLoopBack = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("line", 1), ("internal", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoLoopBack.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoLoopBack.setDescription('Loop back default none')
snPOSInfoScrambleATM = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 10), POSStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoScrambleATM.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoScrambleATM.setDescription('ATM style scrambling default off')
snPOSInfoFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoFraming.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoFraming.setDescription('Framing default SONET')
snPOSInfoCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc32bits", 1), ("crc16bits", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoCRC.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoCRC.setDescription('CRC default 32 bit')
snPOSInfoKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoKeepAlive.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoKeepAlive.setDescription('Keep-alive default 10')
snPOSInfoFlagC2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoFlagC2.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoFlagC2.setDescription('C2 flag')
snPOSInfoFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoFlagJ0.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoFlagJ0.setDescription('J0 flag')
snPOSInfoFlagH1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snPOSInfoFlagH1.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInfoFlagH1.setDescription('H1 flag')
snPOSStatsInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsInFrames.setDescription('The total number of packets received on the interface.')
snPOSStatsOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsOutFrames.setDescription('The total number of packets transmitted out of the interface.')
snPOSStatsAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsAlignErrors.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsAlignErrors.setDescription('dot3StatsAlignmentErrors : A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check. The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
snPOSStatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsFCSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsFCSErrors.setDescription('dot3StatsFCSErrors : A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check. The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
snPOSStatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsFrameTooLongs.setDescription('dot3StatsFrameTooLongs : A count of frames received on a particular interface that exceed the maximum permitted frame size. The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
snPOSStatsFrameTooShorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsFrameTooShorts.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsFrameTooShorts.setDescription(' A count of frames received on a particular interface that below the minimum permitted frame size.')
snPOSStatsInDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsInDiscard.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsInDiscard.setDescription('The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space.')
snPOSStatsOutDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsOutDiscard.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsOutDiscard.setDescription('The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.')
snPOSInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSInOctets.setDescription('The total number of octets received on the interface, including framing characters. This object is a 64-bit counter of the ifInOctets object, defined in RFC 1213. The octet string is in big-endian byte order.')
snPOSOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSOutOctets.setDescription('The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit counter of the ifOutOctets object, defined in RFC 1213. The octet string is in big-endian byte order.')
snPOSStatsInBitsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 27), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsInBitsPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsInBitsPerSec.setDescription('The number of bits per second received on the interface over a 5 minutes interval.')
snPOSStatsOutBitsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsOutBitsPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsOutBitsPerSec.setDescription('The number of bits per second transmitted out of the interface over a 5 minutes interval.')
snPOSStatsInPktsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 29), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsInPktsPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsInPktsPerSec.setDescription('The number of packets per second received on the interface over a 5 minutes interval.')
snPOSStatsOutPktsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 30), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsOutPktsPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsOutPktsPerSec.setDescription('The number of packets per second transmitted out of the interface over a 5 minutes interval.')
snPOSStatsInUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsInUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsInUtilization.setDescription('The input network utilization in hundredths of a percent over a 5 minutes interval.')
snPOSStatsOutUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsOutUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsOutUtilization.setDescription('The output network utilization in hundredths of a percent over a 5 minutes interval.')
snPOSTagType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tagged", 1), ("untagged", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSTagType.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSTagType.setDescription('For tagged port, we could have multiple VLANs per port.')
snPOSStatsB1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsB1.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsB1.setDescription('Section error monitoring.')
snPOSStatsB2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsB2.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsB2.setDescription('Line error monitoring.')
snPOSStatsB3 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsB3.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsB3.setDescription('Path error monitoring.')
snPOSStatsAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsAIS.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsAIS.setDescription('Alarm indication signal.')
snPOSStatsRDI = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsRDI.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsRDI.setDescription('Remote defect indication.')
snPOSStatsLOP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsLOP.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsLOP.setDescription('Loss of pointer.')
snPOSStatsLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsLOF.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsLOF.setDescription('Loss of frame.')
snPOSStatsLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPOSStatsLOS.setStatus('mandatory')
if mibBuilder.loadTexts: snPOSStatsLOS.setDescription('Loss of signal.')
mibBuilder.exportSymbols("HP-SN-POS-GROUP-MIB", snPOSStatsOutFrames=snPOSStatsOutFrames, snPOSStatsB1=snPOSStatsB1, snPOSStatsRDI=snPOSStatsRDI, snPOSInfoEntry=snPOSInfoEntry, snPOSInfoFlagC2=snPOSInfoFlagC2, snPOSStatsLOS=snPOSStatsLOS, snPOSInfoPortNum=snPOSInfoPortNum, snPOSInfoKeepAlive=snPOSInfoKeepAlive, snPOSStatsInBitsPerSec=snPOSStatsInBitsPerSec, snPOSStatsInUtilization=snPOSStatsInUtilization, snPOSStatsB2=snPOSStatsB2, snPOSStatsAlignErrors=snPOSStatsAlignErrors, snPOSStatsOutDiscard=snPOSStatsOutDiscard, snPOSIfIndex=snPOSIfIndex, snPOSInfoAdminStatus=snPOSInfoAdminStatus, snPOSInfoFlagJ0=snPOSInfoFlagJ0, snPOSStatsAIS=snPOSStatsAIS, snPOSInfoLoopBack=snPOSInfoLoopBack, snPOSInfoCRC=snPOSInfoCRC, snPOSStatsB3=snPOSStatsB3, snPOSInfoClock=snPOSInfoClock, snPOSStatsFCSErrors=snPOSStatsFCSErrors, snPOSStatsOutPktsPerSec=snPOSStatsOutPktsPerSec, snPOSOutOctets=snPOSOutOctets, snPOSStatsInFrames=snPOSStatsInFrames, snPOSInOctets=snPOSInOctets, snPOSInfoScrambleATM=snPOSInfoScrambleATM, snPOSInfo=snPOSInfo, snPOSInfoTable=snPOSInfoTable, snPOSInfoLinkStatus=snPOSInfoLinkStatus, snPOSStatsLOP=snPOSStatsLOP, snPOSName=snPOSName, snPOSDescr=snPOSDescr, snPOSStatsFrameTooShorts=snPOSStatsFrameTooShorts, snPOSInfoSpeed=snPOSInfoSpeed, snPOSStatsOutBitsPerSec=snPOSStatsOutBitsPerSec, snPOSStatsInPktsPerSec=snPOSStatsInPktsPerSec, snPOSStatsOutUtilization=snPOSStatsOutUtilization, snPOSStatsLOF=snPOSStatsLOF, snPOSInfoFraming=snPOSInfoFraming, snPOSStatsFrameTooLongs=snPOSStatsFrameTooLongs, POSStatus=POSStatus, snPOSStatsInDiscard=snPOSStatsInDiscard, snPOSInfoFlagH1=snPOSInfoFlagH1, snPOSTagType=snPOSTagType, DisplayString=DisplayString)