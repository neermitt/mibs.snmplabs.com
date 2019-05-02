#
# PySNMP MIB module APPIAN-TIMESLOTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-TIMESLOTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AcAdminStatus, acOsap = mibBuilder.importSymbols("APPIAN-SMI-MIB", "AcAdminStatus", "acOsap")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Bits, Counter64, ModuleIdentity, iso, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Bits", "Counter64", "ModuleIdentity", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acTimeSlots = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 5))
acTimeSlots.setRevisions(('1900-08-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acTimeSlots.setRevisionsDescriptions(('MIB definitons for the timeslots',))
if mibBuilder.loadTexts: acTimeSlots.setLastUpdated('0008210000Z')
if mibBuilder.loadTexts: acTimeSlots.setOrganization('Appian Communications, Inc.')
if mibBuilder.loadTexts: acTimeSlots.setContactInfo('Douglas Theriault')
if mibBuilder.loadTexts: acTimeSlots.setDescription('Appian Communications Network provisioning MIB definition.')
acTimeSlotTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1), )
if mibBuilder.loadTexts: acTimeSlotTable.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotTable.setDescription('The timeslot table defines how the SONET ring timeslots are provisioned (carved). The timeslot table is SHARED between all OSAPs in a ring. It indicates the width and payload type of each timeslot, type of SONET protection scheme used as well as other timeslot related information. It also contain the SHARED logical port data such as payload Type, LineType, and MgmtDLType.')
acTimeSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1), ).setIndexNames((0, "APPIAN-TIMESLOTS-MIB", "acTimeSlotIndex"))
if mibBuilder.loadTexts: acTimeSlotEntry.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotEntry.setDescription('A row in the timeslot table.')
acTimeSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acTimeSlotIndex.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotIndex.setDescription('The value identifies a timeslot on either the ring or the interconnect SONET interfaces. This index is a 32 bit number comprised of bit fields. The algorithm used to determine this index is set so both AppianVista (EMS) and the Command Line Interface (CLI) can configure this table. This index is also used to index rows in trunk shared table for the trunk table agent (TTA). The following bit assignments define the format for the timeslot index: Bits Description ------- ----------------------------------------- 0..2 Virtual Tributary (VT) 3..5 Virtual Tributary Group (VTG) 6..15 STS number 16..22 Reserved - Wavelength 23..26 Physical Port number 27..31 Physical Slot number Note: for additional information refer to trunk shared.mib file.')
acTimeSlotAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 2), AcAdminStatus().clone('inactivate')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotAdminStatus.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotAdminStatus.setDescription('Appian Administrative Status attribute used to set the provisioning state as either activate(1), inactivate(2) or delete(3). Refer to the Appian-SMI.mib file for additional information.')
acTimeSlotWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("vt1dot5", 1), ("vtgroup", 2), ("sts1", 3), ("sts3", 4), ("sts12", 5), ("sts48", 6))).clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotWidth.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotWidth.setDescription('The type and size of the timeslot described in this row of the timeslot table.')
acTimeSlotOuterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotOuterIndex.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotOuterIndex.setDescription("This value is either zero(0) or the index of another row in this table. If it is not zero(0), it is the index of another row in this table which describes the parent timeslot to the timeslot associated with this row. A parent timeslot is another timeslot which is carved into smaller timeslots, one of which is this current timeslot. For example, a row in this table describing a VT1.5 always has an outerIndex which identifies a row in this table which describes a VT group. A VT group always has an outerIndex that describes a STS-1. The row describing the STS-1 has an outerIndex which identifies a row describing an OC3 SONET interface or perhaps, in the future, an STS12 within an STS48. Thus this object describes a nesting of timeslots. To continue the previous example: an STS-1 with 28 VT1.5's within it is represented by 36 rows in this table; 28 of which identify and describe each VT1.5. Every 4 VT rows have a corresponding VT group (vtgroup) for a total of 7 more rows. Each of the 4 VT1.5 rows that make up the VT group have an indentical value for outerIndex (index of the VT group row that the VT1.5's are associated). Each of the 7 VT group rows have an identical value in outerIndex (index of the STS-1 row that the VT groups are associated).")
acTimeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotNumber.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotNumber.setDescription('This identifies the timeslot within a SONET payload or within an outer timeslot within the payload. In the later case, the acTimeSlotOuterIndex object identifies the outer timeslot within the SONET payload. OC-3 + For an STS-1 carved out of an OC3, acTimeSlotNumber is a number 1, 2 or 3. + For a VT group carved out of an STS-1 in an OC3, acTimeSlotNumber is a number from 1 to 7. + For a VT1.5 carved out of an VT group, acTimeSlotNumber is a number from 1 to 4. OC-48 + For an STS-1 carved out of an OC48, acTimeSlotNumber is a number from 1 to 48. + For an STS-3 carved out of an OC48, acTimeSlotNumber is a number 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, or 46. + For an STS-12 carved out of an OC48, acTimeSlotNumber is a number 1, 13, 25, or 37 + For an STS-48 carved out of an OC48, acTimeSlotNumber can only be 1. ')
acTimeSlotPathProtectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("not-used", 0), ("unprotected", 1), ("odp", 2), ("upsr", 3))).clone('not-used')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPathProtectionMode.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPathProtectionMode.setDescription("The type of protection switching to be used if independent path level protection switching is enabled on this timeslot. This object is only relevant for the ring side. Note that ODP is used on shared trunks that are either FR or TLS trunks. In either case, these shared trunks can be either STS-1, a VT1.5 or a bundle of VT1.5's. not-used: Timeslot is provisioned only over a linear interconnet. Timeslot is not protected at this level in the Timeslot hierarchy. Example: A VT1.5 row when protection switching is done at the STS-1 level unprotected: Timeslot is unprotected. One significance of this is that if this timeslot becomes unavailable, it will not remain in service by bumping another peer timeslot using the same timeslot on another fiber. odp: Appian's Optical Data Protection. ODP is used on shared trunks that are either FR or TLS trunks. uspr: Traditional UPSR can be used on non-shared timeslots such as PPP trunks and TDM service trunks. ")
acTimeSlotChassisSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("not-applicable", 0), ("slot1", 1), ("slot2", 2))).clone('not-applicable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotChassisSlot.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotChassisSlot.setDescription('For most timeslots, this object is an element of the specification of exactly which timeslot this table row identifies. In some cases, it is ignored. The ChassisSlot has the following significance for the various scenarios: ring: ChassisSlot 1 indicates the timeslot on the westward transmitting fiber. ChassisSlot 2 indicates the timeslot on the eastward facing fiber. ring/interconnect: ChassisSlot 1 indicates the timeslot on the westward transmitting fiber and on the linear interconnect fiber on slot 1. ChassisSlot 2 indicates the timeslot on the eastward transmitting fiber and the linear interconnect fiber on slot 2. linear: ChassisSlot, along with Port, identifies the fiber out of which this timeslot is extracted. ')
acTimeSlotPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("not-applicable", 0), ("port1", 1), ("port2", 2))).clone('not-applicable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPort.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPort.setDescription('For timeslots in configurations with no ring fibers, this object is an element of the specification of which exactly which timeslot this table row identifies. This object is ignored unless there are two linear interconnects on a single SONET board. When there are two linear interconnects, this object dictates out of which linear interconnect this timeslot is to be extracted. ')
acTimeSlotPayloadConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unprovisioned", 0), ("ring-only", 1), ("ring-interconnect", 2))).clone('unprovisioned')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPayloadConfiguration.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPayloadConfiguration.setDescription("The payload configuration defines the connection topology over which the payload's path is provisioned. More description needed here... This object is ignored if this row describes a timeslot that is broken down further into lower bandwidth timeslots.")
acTimeSlotPayloadLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("not-applicable", 0), ("ds1ESF", 1), ("ds1D4", 2), ("ds3M23", 3), ("ds3CbitParity", 4), ("ds1tdm", 5))).clone('not-applicable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPayloadLineType.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPayloadLineType.setDescription('This variable indicates the variety of DS1 Line or DS3 C-bit application implementing this circuit. The type of circuit affects the number of bits per second that the circuit can reasonable carry, as well as the interpretation of the usage and error statistics. The payload line type must correspond correctly to the payload type that was configured in acTimeSlotPayloadType. For example, if ds1 was choosen, the line type must either be ds1ESF or ds1D4. These values are only valid when acTimeSlotPayloadType is ds1 or ds3. For ds1tdm, these values are obtained from the acDs1ConfigTable and are not shared. The value ds1tdm is used to distinguish when a vt1.5 is used for voice. The values, in sequence describe: TITLE: SPECIFICATION not-applicable ds1ESF Extended SuperFrame DS1 (T1.107) ds1D4 AT&T D4 format DS1 (T1.107) ds3M23 ANSI T1.107-1988 [9] ds3CbitParity ANSI T1.107a-1990 [9a] This object is not applicable in rows associated with timeslots that are carved into lower bandwidth inner timeslots.')
acTimeSlotPayloadMgmtDLType = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 11), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPayloadMgmtDLType.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPayloadMgmtDLType.setDescription("This bitmap describes the use of the management data link, and is the sum of the capabilities. These values are only valid when acTimeSlotPayloadType is ds1 or ds3. For ds1tdm, these values are obtained from the acDs1ConfigTable and are not shared. Set any bits that are appropriate: none(1), ds1AnsiT1403(2), ds1Att54016(4), ds3PMDL(8), 'none' indicates that this device does not use FDL or PMDL. 'ds1AnsiT1403' refers to the DS1 FDL exchange recommended by ANSI. 'ds1Att54016' refers to DS1 ESF FDL exchanges. 'ds3PMDL' refers to DS3 Path Maintainance Data Link. PMDL will not be supported but is here for future use. Possible combinations are: (1) none (2) ANSI FDL when running in ds1 mode. (4) AT&T FDL when running in ds1 mode. (6) ANSI and AT&T FDL when running in ds1 mode. (8) PMDL when running in ds3 mode. All other combinations will result in the non-applicable bits being ignored. This object is not applicable in rows associated with timeslots that are carved into lower bandwidth inner timeslots. They are valid only when the timeslot width is vt1.5 and when payload line type is ds1ESF, ds1D4, ds3M23, or ds3CbitParity")
acTimeSlotChannelConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unprovisioned", 0), ("data-and-tdm", 1), ("tdm-only", 2))).clone('unprovisioned')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotChannelConfiguration.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotChannelConfiguration.setDescription('The channel configuration describes the payload contents of all channels making up this channelized path. These two enumerations describe the lower bandwidth component timeslots. These values also serve as a validation when creating, for example, a vt1.5 whose outerIndex corresponds to this row. It should be noted that when changing these values (tdm-ony and data-and-tdm), brief service interruptsion can result on all timeslots that are lower bandwidth components of this timeslot. This object is ignored if this row describes a timeslot that is NOT broken down further into lower bandwidth timeslots.')
acTimeSlotPayloadContent = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unprovisioned", 0), ("data", 1), ("tdm", 2), ("unequipped", 3))).clone('unprovisioned')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTimeSlotPayloadContent.setStatus('current')
if mibBuilder.loadTexts: acTimeSlotPayloadContent.setDescription('The payload content defines the content of the payload and indirectly the source fo the transmission stream within the OSAP. Payloads carrying data(1) are process by the packet switch. Payloads carrying tdm(2) traffic are not processed by the packet switch and are instead connected directly to the TDM access ports. Unequipped(3) dictates that the payloads are not sourced from either the packet switch or the TDM access ports. Instead, the timeslot is filled with unequipped payload. This object is ignored if this row describes a timeslot that is broken down further into lower bandwidth timeslots.')
mibBuilder.exportSymbols("APPIAN-TIMESLOTS-MIB", acTimeSlotPayloadContent=acTimeSlotPayloadContent, acTimeSlotOuterIndex=acTimeSlotOuterIndex, acTimeSlotEntry=acTimeSlotEntry, acTimeSlotWidth=acTimeSlotWidth, acTimeSlotPayloadLineType=acTimeSlotPayloadLineType, acTimeSlotPathProtectionMode=acTimeSlotPathProtectionMode, acTimeSlotChassisSlot=acTimeSlotChassisSlot, acTimeSlotPayloadMgmtDLType=acTimeSlotPayloadMgmtDLType, acTimeSlots=acTimeSlots, acTimeSlotAdminStatus=acTimeSlotAdminStatus, acTimeSlotPort=acTimeSlotPort, PYSNMP_MODULE_ID=acTimeSlots, acTimeSlotIndex=acTimeSlotIndex, acTimeSlotNumber=acTimeSlotNumber, acTimeSlotPayloadConfiguration=acTimeSlotPayloadConfiguration, acTimeSlotTable=acTimeSlotTable, acTimeSlotChannelConfiguration=acTimeSlotChannelConfiguration)