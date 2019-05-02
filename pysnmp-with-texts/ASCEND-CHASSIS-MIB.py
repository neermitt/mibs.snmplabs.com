#
# PySNMP MIB module ASCEND-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
slots, = mibBuilder.importSymbols("ASCEND-MIB", "slots")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, IpAddress, Unsigned32, NotificationType, iso, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "IpAddress", "Unsigned32", "NotificationType", "iso", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class AscendSlotType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 91, 92, 93, 94, 96, 97))
    namedValues = NamedValues(("other", 1), ("empty", 2), ("sysT1", 3), ("slotT1", 4), ("sysE1", 5), ("slotE1", 6), ("bri", 7), ("s56-2", 8), ("s56-4", 9), ("dualHost", 10), ("quadHost", 11), ("aim2", 12), ("aim6", 13), ("ethernet", 14), ("ethernetData", 15), ("slotBriTE", 16), ("slotBriNT", 17), ("lanModem", 18), ("serialWan", 19), ("v110", 20), ("slotBriLT", 21), ("lanModemP", 22), ("lanModemP12", 23), ("pots", 24), ("analogModem", 25), ("lanModemP48", 26), ("router", 27), ("unchanT1", 28), ("t3", 29), ("hssi", 30), ("primaryNailedT1", 31), ("primaryNailed56", 32), ("dig-8modem", 33), ("dig-12modem", 34), ("dig-16modem", 35), ("dig-48modem", 36), ("phs-8v32modem", 37), ("phs-12v32modem", 38), ("phs-16v32modem", 39), ("sdsl", 40), ("cap-adsl", 41), ("dmt-adsl", 42), ("idsl", 43), ("unchanE1", 44), ("analogModem2", 45), ("voip-8dsp", 46), ("voip-12dsp", 47), ("voip-16dsp", 48), ("csmx", 49), ("uds3", 50), ("ethernet10-100", 51), ("ds3-atm", 52), ("ethernet2", 53), ("ethernetData2", 54), ("sdsl-data", 55), ("madd", 56), ("sdsl-voice", 57), ("slotBriTeU", 58), ("slotOc3Daughter", 59), ("oc3-atm", 60), ("ethernet3", 61), ("srs-ether", 62), ("sdsl-atm", 63), ("alcatel-dadsl-atm", 64), ("csm3v", 65), ("st100-ds3-atm", 66), ("st100-uds3", 67), ("st100-sdsl16", 68), ("ethernetData2ec", 69), ("slotDs3Daughter", 70), ("st100-sdsl8", 71), ("ether-dual", 72), ("st100-oc3-atm", 73), ("ethernet4", 74), ("stm0", 75), ("st100-cc3-atm", 76), ("lanModem-csmx", 77), ("maxpotsFxs", 78), ("ds3-atm2", 79), ("occupied", 80), ("stinger-control-module", 81), ("tnt-control-module", 82), ("dadsl-atm-16ports", 83), ("alcatel-dadsl-atm-v2", 84), ("sdsl-atm-v2", 85), ("dadsl-atm-16ports-v2", 86), ("dadsl-atm-24ports", 87), ("glite-atm-48ports", 91), ("e3-atm", 92), ("madd2", 93), ("hdsl2", 94), ("annexb-dadsl-atm", 96), ("apx-control-module", 97))

chassisInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 2, 6))
chassisDesc = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisDesc.setStatus('mandatory')
if mibBuilder.loadTexts: chassisDesc.setDescription('The chassis type description.')
chassisSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNo.setStatus('mandatory')
if mibBuilder.loadTexts: chassisSerialNo.setDescription('The chassis serial number.')
chassisHWRev = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisHWRev.setStatus('mandatory')
if mibBuilder.loadTexts: chassisHWRev.setDescription('The chassis hardware revision. For non-TNT platforms it is always reported as empty string.')
chassisRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noRedundancy", 1), ("redundancy", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisRedundancy.setStatus('mandatory')
if mibBuilder.loadTexts: chassisRedundancy.setDescription('Value to indicate if this platform is running with redundant controller.')
chassisMemTotal = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMemTotal.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMemTotal.setDescription('The total RAM (bytes) on the shelf controller.')
chassisMemAvail = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMemAvail.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMemAvail.setDescription('The RAM (bytes) currently available on the shelf controller.')
chassisMemThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMemThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMemThreshold.setDescription('The low water mark for RAM (bytes) on the shelf controller.')
cntrReduGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 2, 6, 8))
cntrReduSwitchLastTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduSwitchLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduSwitchLastTime.setDescription('The value of sysUpTime at the time the controller switched over, 0 if none after last system reboot.')
cntrReduSwitchReason = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("failure", 2), ("manual", 3), ("scheduled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduSwitchReason.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduSwitchReason.setDescription('Reason for last controller switchover, unknown if no switchover has occurred.')
cntrReduSwitchIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduSwitchIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduSwitchIndex.setDescription('Controller Index into slot-table for last controller that was switched from.')
cntrReduCurrentIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 8, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduCurrentIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduCurrentIndex.setDescription('Current Controller Index into slot-table.')
cntrReduAvailGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 2, 6, 9))
cntrReduAvailLastTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduAvailLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduAvailLastTime.setDescription('The last time the redundacy availabilty state changed. This object reports 0 if the system did not yet transition from the boot stage.')
class CntrReduAvailState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("boot", 2), ("fullRedundancy", 3), ("partialRedundancy", 4), ("noRedundancy", 5))

cntrReduAvailPrevState = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 2), CntrReduAvailState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduAvailPrevState.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduAvailPrevState.setDescription("The previous redundancy state. It's value is other before the first transition.")
cntrReduAvailCurrState = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 3), CntrReduAvailState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduAvailCurrState.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduAvailCurrState.setDescription("The current redundancy state. It's value is boot before the first transition.")
cntrReduAvailSlotIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 6, 9, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntrReduAvailSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cntrReduAvailSlotIndex.setDescription('The slotIndex as used in the slot table for the slot that observed the transition.')
slotNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: slotNumber.setDescription('The number of slots, fixed or removable, supported by this device.')
slotTable = MibTable((1, 3, 6, 1, 4, 1, 529, 2, 2), )
if mibBuilder.loadTexts: slotTable.setStatus('mandatory')
if mibBuilder.loadTexts: slotTable.setDescription('A list of slot entries. The number of entries is given by the value slotNumber.')
slotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 2, 2, 1), ).setIndexNames((0, "ASCEND-CHASSIS-MIB", "slotIndex"))
if mibBuilder.loadTexts: slotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: slotEntry.setDescription('A slot entry containing objects to describe the slot.')
slotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotIndex.setDescription('A unique value for each slot card. Its value ranges between 1 and the value slotNumber.')
slotName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotName.setStatus('mandatory')
if mibBuilder.loadTexts: slotName.setDescription("The ASCII representation of the name of the card in the indexed slot. The name is the same name displayed on the Main Edit Menu less the menu number. The empty string is returned when there is no slot card present. The value 'Not Avail' is used when the card in the slot has failed POST. The value 'Occupied' is used for cards occupying more than one slot space.")
slotType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 3), AscendSlotType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotType.setStatus('mandatory')
if mibBuilder.loadTexts: slotType.setDescription('The type of card in the indexed slot.')
slotFixed = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotFixed.setStatus('mandatory')
if mibBuilder.loadTexts: slotFixed.setDescription('The value fixed( 1 ) returned if the slot card is not removable and removable( 2 ) if the slot card is removable.')
slotItems = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItems.setStatus('mandatory')
if mibBuilder.loadTexts: slotItems.setDescription("A count of the number of 'items' contained by this slot card. An 'item' is a 'port' for host and a 'line' for network slot cards.")
slotSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotSpecific.setStatus('mandatory')
if mibBuilder.loadTexts: slotSpecific.setDescription('A reference to MIB definitions specific to the hardware in this slot card. Contains the object identifier { 0 0 } if there is no slot specific information for the current slot card type.')
slotSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: slotSerialNumber.setDescription("The TNT slot card's serial number. The serial number is reported as 0 if the slot card does not have a serial number, if the card did not boot, or if the slot is empty. The serial number is reported as 7777777 if the slot card does not support serialization. The serial number is reported as 0 for platforms other than TNT.")
slotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("operStateDown", 1), ("operStateUp", 2), ("operStateDiag", 3), ("operStateCoreDump", 4), ("operStateLoading", 5), ("operStatePost", 6), ("operStateNone", 7), ("operStateOccupied", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotStatus.setStatus('mandatory')
if mibBuilder.loadTexts: slotStatus.setDescription('The current status of the TNT slot card For non-TNT systems operStateNone is always reported.')
slotLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: slotLastChange.setDescription('The value of sysUpTime at the time the TNT slot card entered its current state. For non-TNT systems 0 is always reported.')
slotHWRev = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotHWRev.setStatus('mandatory')
if mibBuilder.loadTexts: slotHWRev.setDescription('Hardware revision of the slot card. On systems that do not support this object, an empty string is returned.')
slotSWRev = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotSWRev.setStatus('mandatory')
if mibBuilder.loadTexts: slotSWRev.setDescription('Software revision of the slot card. On systems that do not support this object, an empty string is returned.')
slotAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: slotAdminStatus.setDescription('This attribute changes the state of the slot card or deletes the slot card. When read, returns the last admin. state set. For non-TNT systems slotAdminStatusUp(1) always returned. For non-TNT system this attribute can not be SET and GENERAL_ERROR(5) is returned, if a SET-REQUEST is received.')
slotUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: slotUpTime.setDescription('Time the slot card has been up. If the slot card is not UP, returns 0.')
slotMemoryTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMemoryTotal.setStatus('mandatory')
if mibBuilder.loadTexts: slotMemoryTotal.setDescription('Total RAM(bytes) present on the slot card.')
slotMemoryAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMemoryAvail.setStatus('mandatory')
if mibBuilder.loadTexts: slotMemoryAvail.setDescription('The amount of RAM(bytes) currently available.')
slotMemoryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMemoryThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: slotMemoryThreshold.setDescription('The RAM low water mark (bytes) for the slot card.')
slotItemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 2, 3), )
if mibBuilder.loadTexts: slotItemTable.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemTable.setDescription('A list of slot item entries. Each slot contains slotItems entries, indexed by slotItemSlotIndex and by slotItemIndex')
slotItemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 2, 3, 1), ).setIndexNames((0, "ASCEND-CHASSIS-MIB", "slotItemSlotIndex"), (0, "ASCEND-CHASSIS-MIB", "slotItemIndex"))
if mibBuilder.loadTexts: slotItemEntry.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemEntry.setDescription('A slot entry containing the starting interface and number of interfaces used by the indexed slot/item.')
slotItemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemSlotIndex.setDescription('A unique value for each slot card. The slot card identified by a particular value of this index is the same slot card as identified by the same value of slotIndex.')
slotItemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemIndex.setDescription('A unique value for each item in each slot card. Its value ranges between 1 and the value of slotItems in the slot indexed by the same value as slotItemSlotIndex.')
slotItemFirstIf = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemFirstIf.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemFirstIf.setDescription('The interface number associated with the indexed item on the indexed slot. May be set to 0 if the slot/item is not associated with any interface.')
slotItemIfCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemIfCount.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemIfCount.setDescription('The number of interfaces associated with the indexed item on the indexed slot. Typically set to 1 for host slots and the number of channels on network (WAN) slots. May be set to 0 when the item is not associated with an interface.')
slotItemSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemSpecific.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemSpecific.setDescription('A reference to MIB definitions specific to the indexed item on the indexed slot. Contains the object identifier { 0 0 } if there is no item specific information for the indexed item.')
slotItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("statusOther", 1), ("slotItemNotRunning", 2), ("briLinkNotStuffed", 3), ("briLinkDisabled", 4), ("briDown", 5), ("briNotInit", 6), ("briNotInitWithL2", 7), ("briPInit", 8), ("briMInit", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotItemStatus.setStatus('mandatory')
if mibBuilder.loadTexts: slotItemStatus.setDescription('The current status of this item in this slot card.')
slotIfTable = MibTable((1, 3, 6, 1, 4, 1, 529, 2, 4), )
if mibBuilder.loadTexts: slotIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: slotIfTable.setDescription('A list of interfaces and the slot/item entry that the interface is associated with.')
slotIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 2, 4, 1), ).setIndexNames((0, "ASCEND-CHASSIS-MIB", "slotIfIndex"))
if mibBuilder.loadTexts: slotIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: slotIfEntry.setDescription('A slot interface entry containing the slot and item that the interface is associated with.')
slotIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotIfIndex.setDescription('The interface index, ranging from 1 to the number of interfaces specified in the MIB-II variable ifNumber. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
slotIfSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIfSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotIfSlotIndex.setDescription('The slot index, ranging from 0 to the number of slots specified in slotNumber. When zero the interface references an item in the console group of this MIB. Otherwise the slot identified by a particular value of this index is the same slot as identified by the same value of slotIndex.')
slotIfItemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIfItemIndex.setStatus('mandatory')
if mibBuilder.loadTexts: slotIfItemIndex.setDescription('The item index, ranging from 1 to the number of items supported on the slot indicated by slotIfSlotIndex. When slotIfSlotIndex is non-zero the number of items supported is specified in slotItems for the slot entry index by slotIfSlotIndex. The item identified by a particular value of this index is the same item as identified by the same value of slotItemIndex.')
mibBuilder.exportSymbols("ASCEND-CHASSIS-MIB", slotTable=slotTable, cntrReduGroup=cntrReduGroup, cntrReduAvailSlotIndex=cntrReduAvailSlotIndex, slotUpTime=slotUpTime, CntrReduAvailState=CntrReduAvailState, slotItemStatus=slotItemStatus, slotItemFirstIf=slotItemFirstIf, chassisSerialNo=chassisSerialNo, cntrReduCurrentIndex=cntrReduCurrentIndex, chassisMemTotal=chassisMemTotal, slotMemoryTotal=slotMemoryTotal, slotItemEntry=slotItemEntry, AscendSlotType=AscendSlotType, slotType=slotType, cntrReduAvailCurrState=cntrReduAvailCurrState, slotItemTable=slotItemTable, chassisInfo=chassisInfo, slotIfSlotIndex=slotIfSlotIndex, slotAdminStatus=slotAdminStatus, cntrReduAvailPrevState=cntrReduAvailPrevState, slotMemoryAvail=slotMemoryAvail, slotIndex=slotIndex, slotSerialNumber=slotSerialNumber, cntrReduAvailLastTime=cntrReduAvailLastTime, chassisMemThreshold=chassisMemThreshold, slotStatus=slotStatus, chassisHWRev=chassisHWRev, slotItems=slotItems, slotSpecific=slotSpecific, cntrReduSwitchReason=cntrReduSwitchReason, slotItemSpecific=slotItemSpecific, slotHWRev=slotHWRev, cntrReduAvailGroup=cntrReduAvailGroup, cntrReduSwitchIndex=cntrReduSwitchIndex, slotIfItemIndex=slotIfItemIndex, slotItemIfCount=slotItemIfCount, slotLastChange=slotLastChange, slotItemSlotIndex=slotItemSlotIndex, chassisDesc=chassisDesc, slotEntry=slotEntry, slotMemoryThreshold=slotMemoryThreshold, slotNumber=slotNumber, slotItemIndex=slotItemIndex, slotIfEntry=slotIfEntry, slotName=slotName, cntrReduSwitchLastTime=cntrReduSwitchLastTime, chassisRedundancy=chassisRedundancy, chassisMemAvail=chassisMemAvail, slotIfTable=slotIfTable, slotIfIndex=slotIfIndex, slotFixed=slotFixed, slotSWRev=slotSWRev)