#
# PySNMP MIB module FOUNDRY-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-POE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
snAgentSys, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snAgentSys")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, Bits, NotificationType, ObjectIdentity, iso, ModuleIdentity, IpAddress, TimeTicks, MibIdentifier, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snAgentPoe = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14))
snAgentPoe.setRevisions(('2010-06-02 00:00', '2009-09-30 00:00', '2009-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snAgentPoe.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Changed INTEGER to Integer32', 'Initial version, snAgentPoePortTable which was in SNMPv1 written in SNMPv2-SMI.',))
if mibBuilder.loadTexts: snAgentPoe.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snAgentPoe.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snAgentPoe.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snAgentPoe.setDescription("The Brocade proprietary MIB module for Power Over Ethernet(PoE) It has PoE port and module configuring information. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snAgentPoeGbl = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1))
snAgentPoePort = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2))
snAgentPoeModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3))
snAgentPoeUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4))
snAgentPoeGblPowerCapacityTotal = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeGblPowerCapacityTotal.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeGblPowerCapacityTotal.setDescription('This object shows the total inline power capacity available in the device, measured in mWatts. ')
snAgentPoeGblPowerCapacityFree = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeGblPowerCapacityFree.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeGblPowerCapacityFree.setDescription('This object shows the inline power capacity currently available in the device which is unallocated, measured in mWatts.')
snAgentPoeGblPowerAllocationsRequestsHonored = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeGblPowerAllocationsRequestsHonored.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeGblPowerAllocationsRequestsHonored.setDescription('This object shows number of times the inline power allocations requests honored.')
snAgentPoePortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2), )
if mibBuilder.loadTexts: snAgentPoePortTable.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortTable.setDescription('A table of POE port information.')
snAgentPoePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-POE-MIB", "snAgentPoePortNumber"))
if mibBuilder.loadTexts: snAgentPoePortEntry.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortEntry.setDescription('A row in the POE port table.')
snAgentPoePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoePortNumber.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortNumber.setDescription('The port number in ifIndex value.')
snAgentPoePortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("enableLegacyDevice", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgentPoePortControl.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortControl.setDescription("Control inline power on/off to a port. If a port does not have inline power capability, reading this object returns 'other(1)'.")
snAgentPoePortWattage = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgentPoePortWattage.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortWattage.setDescription("Adjust the inline power wattage. Valid value between 1000 to 15400(IEEE802_3AF)/30000(IEEE802_3AT). Each unit is milliwatts. This object can only be set after snSwIfInLinePowerControl has been set to 'enable(3)' or 'enableLegacyDevice(4)'. If a port does not have inline power capability, reading this object returns undefined value.")
snAgentPoePortClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgentPoePortClass.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortClass.setDescription("Adjust the inline power class. Valid value between 0 to 3(IEEE802_3AF)/4(IEEE802_3AT). This object can only be set after snSwIfInLinePowerControl has been set to 'enable(3)' or 'enableLegacyDevice(4)'. If a port does not have inline power capability, reading this object returns undefined value.")
snAgentPoePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 0), ("critical", 1), ("high", 2), ("low", 3), ("medium", 4), ("other", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgentPoePortPriority.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortPriority.setDescription('Inline power allocation priority for the power device 0- Not a POE port, 1- Critical, 2- High, 3- Low, 4- Medium, 5- other.')
snAgentPoePortConsumed = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoePortConsumed.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortConsumed.setDescription('Inline power consumed by the port. Each unit is milliwatts.')
snAgentPoePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoePortType.setStatus('current')
if mibBuilder.loadTexts: snAgentPoePortType.setDescription('Inline Power device type 802.3af, 802.3at or Legacy device.')
snAgentPoeModuleTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1), )
if mibBuilder.loadTexts: snAgentPoeModuleTable.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeModuleTable.setDescription('A table of POE Module configuration.')
snAgentPoeModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1), ).setIndexNames((0, "FOUNDRY-POE-MIB", "snAgentPoeModuleNumber"))
if mibBuilder.loadTexts: snAgentPoeModuleEntry.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeModuleEntry.setDescription('A row in the POE Module table.')
snAgentPoeModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeModuleNumber.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeModuleNumber.setDescription('This objects talks about POE module number.')
snAgentPoeModuleBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snAgentPoeModuleBudget.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeModuleBudget.setDescription('This objects talks about module power budget in watts.')
snAgentPoeModuleMaxPDTypeSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ieee802dot3af", 0), ("ieee802dot3at", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeModuleMaxPDTypeSupport.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeModuleMaxPDTypeSupport.setDescription('This object talks about the POE module type which is capable to support Power Device (PD) type ieee802.3af or ieee802.3at(also called POE plus)type. Module which support ieee802.3at can also support ieee802.3af but reverse is not true.')
snAgentPoeUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1), )
if mibBuilder.loadTexts: snAgentPoeUnitTable.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitTable.setDescription('A table of POE informaion for each unit. Only the unit that has POE capability appears in a table row')
snAgentPoeUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1), ).setIndexNames((0, "FOUNDRY-POE-MIB", "snAgentPoeUnitIndex"))
if mibBuilder.loadTexts: snAgentPoeUnitEntry.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitEntry.setDescription('A row in the POE Unit table.')
snAgentPoeUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeUnitIndex.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitIndex.setDescription('The Index to POE unit Table.')
snAgentPoeUnitPowerCapacityTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeUnitPowerCapacityTotal.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitPowerCapacityTotal.setDescription('This object shows the total inline power capacity available on that unit (device), measured in mWatts. ')
snAgentPoeUnitPowerCapacityFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeUnitPowerCapacityFree.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitPowerCapacityFree.setDescription('This object shows the inline power capacity currently available on that unit (device) which is unallocated, measured in mWatts.')
snAgentPoeUnitPowerAllocationsRequestsHonored = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentPoeUnitPowerAllocationsRequestsHonored.setStatus('current')
if mibBuilder.loadTexts: snAgentPoeUnitPowerAllocationsRequestsHonored.setDescription('This object shows number of times the inline power allocations requests honored on that unit (device).')
mibBuilder.exportSymbols("FOUNDRY-POE-MIB", snAgentPoeModuleNumber=snAgentPoeModuleNumber, snAgentPoeModuleMaxPDTypeSupport=snAgentPoeModuleMaxPDTypeSupport, snAgentPoePortNumber=snAgentPoePortNumber, snAgentPoePortPriority=snAgentPoePortPriority, snAgentPoeModuleBudget=snAgentPoeModuleBudget, snAgentPoePortClass=snAgentPoePortClass, snAgentPoeUnitPowerAllocationsRequestsHonored=snAgentPoeUnitPowerAllocationsRequestsHonored, snAgentPoePortEntry=snAgentPoePortEntry, snAgentPoePortConsumed=snAgentPoePortConsumed, snAgentPoeUnitTable=snAgentPoeUnitTable, snAgentPoeGblPowerCapacityTotal=snAgentPoeGblPowerCapacityTotal, snAgentPoeGblPowerAllocationsRequestsHonored=snAgentPoeGblPowerAllocationsRequestsHonored, snAgentPoeModuleEntry=snAgentPoeModuleEntry, snAgentPoeGbl=snAgentPoeGbl, snAgentPoePort=snAgentPoePort, snAgentPoeGblPowerCapacityFree=snAgentPoeGblPowerCapacityFree, snAgentPoeModule=snAgentPoeModule, snAgentPoe=snAgentPoe, snAgentPoePortWattage=snAgentPoePortWattage, snAgentPoeUnitIndex=snAgentPoeUnitIndex, snAgentPoeUnitPowerCapacityTotal=snAgentPoeUnitPowerCapacityTotal, snAgentPoeUnit=snAgentPoeUnit, snAgentPoePortControl=snAgentPoePortControl, snAgentPoePortTable=snAgentPoePortTable, snAgentPoeModuleTable=snAgentPoeModuleTable, snAgentPoeUnitPowerCapacityFree=snAgentPoeUnitPowerCapacityFree, PYSNMP_MODULE_ID=snAgentPoe, snAgentPoePortType=snAgentPoePortType, snAgentPoeUnitEntry=snAgentPoeUnitEntry)