#
# PySNMP MIB module DC-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DC-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:37:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, ObjectIdentity, Unsigned32, Integer32, Bits, MibIdentifier, Counter32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "Bits", "MibIdentifier", "Counter32", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500DCStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10))
cdx6500DCGenStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1))
cdx6500DCGenStatTableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1))
cdx6500DCGenStatDSPStatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("missing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatDSPStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatDSPStatus.setDescription('This parameter specifies the current status/existence of the DC SIMM/DSP on the motherboard. up - DC SIMM/DSP is installed and operational. down - DC SIMM/DSP is non-functional. missing - DC SIMM/DSP is missing.')
cdx6500DCGenStatHndlrSWRev = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatHndlrSWRev.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatHndlrSWRev.setDescription('This parameter displays the DC Handler Software Revision Number.')
cdx6500DCGenStatFnctnSWRev = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatFnctnSWRev.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatFnctnSWRev.setDescription('DC Function Revision number. For example, revision number of DSP firmware.')
cdx6500DCGenStatMaxChannels = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxChannels.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatMaxChannels.setDescription('Number of DC Channels supported.')
cdx6500DCGenStatChanInUse = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatChanInUse.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatChanInUse.setDescription('Number of DC Channels in use.')
cdx6500DCGenStatMaxSmltChanUse = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxSmltChanUse.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatMaxSmltChanUse.setDescription('Maximum number of DC Channels in use simultaneously since the last stats reset.')
cdx6500DCGenStatRejectConn = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatRejectConn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatRejectConn.setDescription('Number of call requests rejected due to the unavailability of DC channels.')
cdx6500DCGenStatAggCRatio = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatAggCRatio.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatAggCRatio.setDescription('Ratio of total number of incoming charactersfor all DC channels to total number of outgoing characters for all channels, for the past minute.')
cdx6500DCGenStatCurrEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatCurrEncQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatCurrEncQDepth.setDescription('Current number of frames in the encoder queue, waiting to be compressed.')
cdx6500DCGenStatMaxEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxEncQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatMaxEncQDepth.setDescription('Maximum number of frames that were on the encoder queue since the last stats reset.')
cdx6500DCGenStatTmOfMaxEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxEncQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxEncQDepth.setDescription('Time when the maximum Encoder Queue Depth is reached.')
cdx6500DCGenStatCurrDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatCurrDecQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatCurrDecQDepth.setDescription('Current number of frames in the decoder queue, waiting to be decompressed.')
cdx6500DCGenStatMaxDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxDecQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatMaxDecQDepth.setDescription('Maximum number of frames that were on the decoder queue waiting to be decompressed.')
cdx6500DCGenStatTmOfMaxDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxDecQDepth.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxDecQDepth.setDescription('Time when the maximum Decoder Queue Depth is reached.')
cdx6500DCChanStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2), )
if mibBuilder.loadTexts: cdx6500DCChanStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatTable.setDescription('The Data Compression Channel Statistics Table.')
cdx6500DCChanStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1), ).setIndexNames((0, "DC-OPT-MIB", "cdx6500DCChanStatChanNum"))
if mibBuilder.loadTexts: cdx6500DCChanStatTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatTableEntry.setDescription('Each entry in this table pertains to the Data Compression Channel statistics.')
cdx6500DCChanStatChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatChanNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatChanNum.setDescription('Channel number whose statistics were requested.')
cdx6500DCChanStatTmOfLastStatRst = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatTmOfLastStatRst.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatTmOfLastStatRst.setDescription('Time when the node restarted or the stats reset by CTP/SNMP Manager command.')
cdx6500DCChanStatChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("dspDown", 1), ("idle", 2), ("negotiating", 3), ("dataPassing", 4), ("flushingData", 5), ("flushingDCRing", 6), ("apClearing", 7), ("npClearing", 8), ("clearingCall", 9), ("flushingOnClr", 10), ("clearing", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatChanState.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatChanState.setDescription("Activity state of the DC channel. dspDown - DSP is down. idle - DSP is ready to be assigned to a connection. negotiating - Source has accepted the Call Request and is waiting for a Call Accept from the destination node. dataPassing - Normal data passing state. apClearing - Call Clear request arrived from access side. npClearing - Call Clear request arrived from network side. clearingCall - A call collision or a Call Clear along with a X.25 reset or a `start buffer discarding'. flushingOnClr - Call has been cleared with FLUSH, waiting packets to flush from DC Handler rings. flushingData - Waiting for x25 confirm. flushingDCRing - Waiting for the data on the DC Handler ring to be flushed after a x.25 confirm or stop discard. clearing - Call has been cleared.")
cdx6500DCChanStatSourceChan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatSourceChan.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatSourceChan.setDescription("Access Protocol's identity string.")
cdx6500DCChanStatDestChan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDestChan.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDestChan.setDescription("Network Protocol's identity string.")
cdx6500DCChanStatXmitCRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatXmitCRatio.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatXmitCRatio.setDescription('Actual compression ratio for outgoing data. This is a 60 second snapshot. Range is 1 - 9.2')
cdx6500DCChanStatNumOfEncFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfEncFrames.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfEncFrames.setDescription('Number of frames received from the Access Protocol to be compressed.')
cdx6500DCChanStatNumOfCharInToEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToEnc.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToEnc.setDescription('Number of bytes pushed into the encoder to be compressed.')
cdx6500DCChanStatNumOfCharOutOfEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfEnc.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfEnc.setDescription('Number of compressed bytes produced by the encoder.')
cdx6500DCChanStatNumOfDecFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfDecFrames.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfDecFrames.setDescription('Number of frames received from the Network Protocol to be decompressed.')
cdx6500DCChanStatNumOfCharInToDec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToDec.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToDec.setDescription('Number of bytes pushed into the decoder to be decompressed.')
cdx6500DCChanStatNumOfCharOutOfDec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfDec.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfDec.setDescription('Number of decompressed bytes produced by the decoder.')
cdx6500DCChanStatEncAETrnstnCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAETrnstnCnt.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatEncAETrnstnCnt.setDescription('Number of times the encoder switched from compressed mode to anti-expansion mode.')
cdx6500DCChanStatEncAEFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEFrameCnt.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEFrameCnt.setDescription('Number of anti-expansion frames sent by the encoder.')
cdx6500DCChanStatEncAEModeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEModeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEModeStatus.setDescription('Anti Expansion mode Status for Encoder : on - Data Compression is in the anti expansion mode. off - Data Compression is out of the anti expansion mode.')
cdx6500DCChanStatDecAETrnstnCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAETrnstnCnt.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDecAETrnstnCnt.setDescription('Number of times the decoder switched from compressed mode to anti-expansion mode.')
cdx6500DCChanStatDecAEFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEFrameCnt.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEFrameCnt.setDescription('Number of anti-expansion frames received by the decoder.')
cdx6500DCChanStatDecAEModeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEModeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEModeStatus.setDescription('Anti Expansion mode Status for Decoder : on - Data Compression is in the anti expansion mode. off - Data Compression is out of the anti expansion mode.')
cdx6500DCChanStatDSWithBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadFrames.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadFrames.setDescription('Number of decoded frames detected by the decoder to have been corrupted. This includes frames with bad headers.')
cdx6500DCChanStatDSWithBadHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadHeaders.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadHeaders.setDescription('Number of decoded frames detected by the decoder to have a bad header.')
cdx6500DCChanStatDSDueToRstOrCng = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSDueToRstOrCng.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500DCChanStatDSDueToRstOrCng.setDescription('Number of packets discarded while processing a X.25 reset or during node congestion.')
cdx6500ContDC = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9))
cdx6500ContResetAllDCStats = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetAllDCStats.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContResetAllDCStats.setDescription('Reset the DC Statistics for all channels.')
cdx6500ContDCTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2), )
if mibBuilder.loadTexts: cdx6500ContDCTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContDCTable.setDescription('These resets require the channel number as the index.')
cdx6500ContDCTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1), ).setIndexNames((0, "DC-OPT-MIB", "cdx6500ContDCChanNum"))
if mibBuilder.loadTexts: cdx6500ContDCTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContDCTableEntry.setDescription('Each entry represents a control parameter used to reset Channel Statistics or Channel Vocabulary.')
cdx6500ContDCChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500ContDCChanNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContDCChanNum.setDescription('Channel number used as the index.')
cdx6500ContResetDCChanStats = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetDCChanStats.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContResetDCChanStats.setDescription('Reset the DC Statistics for this channel.')
cdx6500ContResetDCChanVocab = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetDCChanVocab.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContResetDCChanVocab.setDescription('Reset the vocabulary/history buffer for this channel if this channel number is active.')
mibBuilder.exportSymbols("DC-OPT-MIB", cdx6500ContDCChanNum=cdx6500ContDCChanNum, cdx6500DCGenStatTmOfMaxDecQDepth=cdx6500DCGenStatTmOfMaxDecQDepth, cdx6500Controls=cdx6500Controls, cdx6500ContResetAllDCStats=cdx6500ContResetAllDCStats, cdx6500ContDCTableEntry=cdx6500ContDCTableEntry, codex=codex, cdx6500DCGenStatMaxSmltChanUse=cdx6500DCGenStatMaxSmltChanUse, cdx6500ContResetDCChanVocab=cdx6500ContResetDCChanVocab, cdx6500DCChanStatDecAEFrameCnt=cdx6500DCChanStatDecAEFrameCnt, cdx6500DCChanStatNumOfCharOutOfDec=cdx6500DCChanStatNumOfCharOutOfDec, cdx6500DCChanStatTmOfLastStatRst=cdx6500DCChanStatTmOfLastStatRst, cdx6500DCChanStatXmitCRatio=cdx6500DCChanStatXmitCRatio, cdx6500DCChanStatNumOfEncFrames=cdx6500DCChanStatNumOfEncFrames, cdx6500ContDCTable=cdx6500ContDCTable, cdxProductSpecific=cdxProductSpecific, cdx6500Statistics=cdx6500Statistics, cdx6500DCGenStatCurrDecQDepth=cdx6500DCGenStatCurrDecQDepth, cdx6500DCGenStatTableEntry=cdx6500DCGenStatTableEntry, cdx6500DCChanStatSourceChan=cdx6500DCChanStatSourceChan, cdx6500DCGenStatAggCRatio=cdx6500DCGenStatAggCRatio, cdx6500DCGenStatCurrEncQDepth=cdx6500DCGenStatCurrEncQDepth, cdx6500DCGenStatHndlrSWRev=cdx6500DCGenStatHndlrSWRev, cdx6500DCGenStatRejectConn=cdx6500DCGenStatRejectConn, cdx6500DCGenStatTable=cdx6500DCGenStatTable, cdx6500DCChanStatNumOfCharInToDec=cdx6500DCChanStatNumOfCharInToDec, cdx6500DCChanStatNumOfCharInToEnc=cdx6500DCChanStatNumOfCharInToEnc, cdx6500DCChanStatDSDueToRstOrCng=cdx6500DCChanStatDSDueToRstOrCng, cdx6500DCChanStatDestChan=cdx6500DCChanStatDestChan, cdx6500DCChanStatChanNum=cdx6500DCChanStatChanNum, cdx6500DCChanStatDSWithBadFrames=cdx6500DCChanStatDSWithBadFrames, cdx6500DCChanStatNumOfCharOutOfEnc=cdx6500DCChanStatNumOfCharOutOfEnc, cdx6500DCChanStatDSWithBadHeaders=cdx6500DCChanStatDSWithBadHeaders, cdx6500DCChanStatEncAEModeStatus=cdx6500DCChanStatEncAEModeStatus, cdx6500DCChanStatDecAETrnstnCnt=cdx6500DCChanStatDecAETrnstnCnt, cdx6500ContResetDCChanStats=cdx6500ContResetDCChanStats, cdx6500DCChanStatTableEntry=cdx6500DCChanStatTableEntry, cdx6500ContDC=cdx6500ContDC, cdx6500DCGenStatMaxEncQDepth=cdx6500DCGenStatMaxEncQDepth, cdx6500DCGenStatChanInUse=cdx6500DCGenStatChanInUse, cdx6500=cdx6500, cdx6500DCGenStatFnctnSWRev=cdx6500DCGenStatFnctnSWRev, cdx6500DCChanStatTable=cdx6500DCChanStatTable, cdx6500DCGenStatMaxChannels=cdx6500DCGenStatMaxChannels, cdx6500DCGenStatTmOfMaxEncQDepth=cdx6500DCGenStatTmOfMaxEncQDepth, DisplayString=DisplayString, cdx6500DCChanStatChanState=cdx6500DCChanStatChanState, cdx6500DCChanStatNumOfDecFrames=cdx6500DCChanStatNumOfDecFrames, cdx6500DCChanStatEncAEFrameCnt=cdx6500DCChanStatEncAEFrameCnt, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup, cdx6500DCChanStatDecAEModeStatus=cdx6500DCChanStatDecAEModeStatus, cdx6500DCGenStatMaxDecQDepth=cdx6500DCGenStatMaxDecQDepth, cdx6500DCStatTable=cdx6500DCStatTable, cdx6500DCChanStatEncAETrnstnCnt=cdx6500DCChanStatEncAETrnstnCnt, cdx6500DCGenStatDSPStatus=cdx6500DCGenStatDSPStatus)
