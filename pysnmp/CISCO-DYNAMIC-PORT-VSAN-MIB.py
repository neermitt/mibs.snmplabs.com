#
# PySNMP MIB module CISCO-DYNAMIC-PORT-VSAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DYNAMIC-PORT-VSAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
CpsmDiffReason, CpsmDbActivate, CpsmActivateResult, CpsmDiffDb = mibBuilder.importSymbols("CISCO-PSM-MIB", "CpsmDiffReason", "CpsmDbActivate", "CpsmActivateResult", "CpsmDiffDb")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcNameId, FcNameIdOrZero = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcNameId", "FcNameIdOrZero")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Unsigned32, TimeTicks, MibIdentifier, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Counter32, Gauge32, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Counter32", "Gauge32", "Bits", "ModuleIdentity", "Integer32")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoDpvmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 421))
ciscoDpvmMIB.setRevisions(('2004-06-22 00:00',))
if mibBuilder.loadTexts: ciscoDpvmMIB.setLastUpdated('200406220000Z')
if mibBuilder.loadTexts: ciscoDpvmMIB.setOrganization('Cisco Systems Inc.')
ciscoDpvmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 0))
ciscoDpvmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 1))
ciscoDpvmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2))
cdpvmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1))
class CdpvmDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pwwn", 1), ("nwwn", 2))

cdpvmNextAvailIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmNextAvailIndex.setStatus('current')
cdpvmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2), )
if mibBuilder.loadTexts: cdpvmTable.setStatus('current')
cdpvmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmIndex"))
if mibBuilder.loadTexts: cdpvmEntry.setStatus('current')
cdpvmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmIndex.setStatus('current')
cdpvmLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 2), CdpvmDevType().clone('pwwn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDevType.setStatus('current')
cdpvmLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 3), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDev.setStatus('current')
cdpvmLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 4), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDevVsan.setStatus('current')
cdpvmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmRowStatus.setStatus('current')
cdpvmActivate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 3), CpsmDbActivate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmActivate.setStatus('current')
cdpvmActivateResult = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 4), CpsmActivateResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmActivateResult.setStatus('current')
cdpvmAutoLearn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmAutoLearn.setStatus('current')
cdpvmCopyEnfToConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copy", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmCopyEnfToConfig.setStatus('current')
cdpvmEnfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7), )
if mibBuilder.loadTexts: cdpvmEnfTable.setStatus('current')
cdpvmEnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIndex"))
if mibBuilder.loadTexts: cdpvmEnfEntry.setStatus('current')
cdpvmEnfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmEnfIndex.setStatus('current')
cdpvmEnfLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 2), CdpvmDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDevType.setStatus('current')
cdpvmEnfLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 3), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDev.setStatus('current')
cdpvmEnfLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 4), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDevVsan.setStatus('current')
cdpvmEnfIsLearnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfIsLearnt.setStatus('current')
cdpvmDynPortsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8), )
if mibBuilder.loadTexts: cdpvmDynPortsTable.setStatus('current')
cdpvmDynPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdpvmDynPortsEntry.setStatus('current')
cdpvmDynPortVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 1), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortVsan.setStatus('current')
cdpvmDynPortDevPwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 2), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortDevPwwn.setStatus('current')
cdpvmDynPortDevNwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 3), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortDevNwwn.setStatus('current')
cdpvmDiffConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 9), CpsmDiffDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmDiffConfig.setStatus('current')
cdpvmDiffTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10), )
if mibBuilder.loadTexts: cdpvmDiffTable.setStatus('current')
cdpvmDiffEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffIndex"))
if mibBuilder.loadTexts: cdpvmDiffEntry.setStatus('current')
cdpvmDiffIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmDiffIndex.setStatus('current')
cdpvmDiffReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 2), CpsmDiffReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffReason.setStatus('current')
cdpvmDiffLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 3), CdpvmDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDevType.setStatus('current')
cdpvmDiffLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 4), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDev.setStatus('current')
cdpvmDiffLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 5), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDevVsan.setStatus('current')
cdpvmClearAutoLearn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("clearOnWwn", 2), ("noop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmClearAutoLearn.setStatus('current')
cdpvmClearAutoLearnWwn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 12), FcNameIdOrZero().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmClearAutoLearnWwn.setStatus('current')
cdpvmActivationState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmActivationState.setStatus('current')
ciscoDpvmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1))
ciscoDpvmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2))
ciscoDpvmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1, 1)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmConfigGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmEnforcedGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmAutoLearnGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmDiffGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmMIBCompliance = ciscoDpvmMIBCompliance.setStatus('current')
ciscoDpvmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 1)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmNextAvailIndex"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmRowStatus"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivate"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivateResult"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmCopyEnfToConfig"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevPwwn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevNwwn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivationState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmConfigGroup = ciscoDpvmConfigGroup.setStatus('current')
ciscoDpvmEnforcedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 2)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIsLearnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmEnforcedGroup = ciscoDpvmEnforcedGroup.setStatus('current')
ciscoDpvmAutoLearnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 3)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmAutoLearn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearnWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmAutoLearnGroup = ciscoDpvmAutoLearnGroup.setStatus('current')
ciscoDpvmDiffGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 4)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffConfig"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffReason"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevVsan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmDiffGroup = ciscoDpvmDiffGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", ciscoDpvmMIBConform=ciscoDpvmMIBConform, cdpvmLoginDevVsan=cdpvmLoginDevVsan, ciscoDpvmMIB=ciscoDpvmMIB, cdpvmDiffReason=cdpvmDiffReason, cdpvmConfiguration=cdpvmConfiguration, cdpvmDiffLoginDevVsan=cdpvmDiffLoginDevVsan, cdpvmDiffLoginDevType=cdpvmDiffLoginDevType, cdpvmClearAutoLearn=cdpvmClearAutoLearn, ciscoDpvmEnforcedGroup=ciscoDpvmEnforcedGroup, cdpvmEnfEntry=cdpvmEnfEntry, cdpvmDynPortsEntry=cdpvmDynPortsEntry, ciscoDpvmMIBCompliances=ciscoDpvmMIBCompliances, cdpvmTable=cdpvmTable, cdpvmDiffIndex=cdpvmDiffIndex, cdpvmDiffEntry=cdpvmDiffEntry, cdpvmActivate=cdpvmActivate, cdpvmIndex=cdpvmIndex, ciscoDpvmMIBCompliance=ciscoDpvmMIBCompliance, cdpvmEnfTable=cdpvmEnfTable, cdpvmDynPortDevNwwn=cdpvmDynPortDevNwwn, cdpvmActivationState=cdpvmActivationState, ciscoDpvmConfigGroup=ciscoDpvmConfigGroup, CdpvmDevType=CdpvmDevType, cdpvmCopyEnfToConfig=cdpvmCopyEnfToConfig, cdpvmDiffConfig=cdpvmDiffConfig, ciscoDpvmAutoLearnGroup=ciscoDpvmAutoLearnGroup, cdpvmLoginDev=cdpvmLoginDev, cdpvmEntry=cdpvmEntry, cdpvmEnfLoginDev=cdpvmEnfLoginDev, cdpvmRowStatus=cdpvmRowStatus, cdpvmDiffLoginDev=cdpvmDiffLoginDev, ciscoDpvmMIBGroups=ciscoDpvmMIBGroups, cdpvmAutoLearn=cdpvmAutoLearn, ciscoDpvmMIBNotifs=ciscoDpvmMIBNotifs, cdpvmDiffTable=cdpvmDiffTable, ciscoDpvmMIBObjects=ciscoDpvmMIBObjects, ciscoDpvmDiffGroup=ciscoDpvmDiffGroup, cdpvmEnfIndex=cdpvmEnfIndex, cdpvmActivateResult=cdpvmActivateResult, cdpvmEnfIsLearnt=cdpvmEnfIsLearnt, cdpvmEnfLoginDevType=cdpvmEnfLoginDevType, cdpvmDynPortsTable=cdpvmDynPortsTable, cdpvmEnfLoginDevVsan=cdpvmEnfLoginDevVsan, cdpvmDynPortDevPwwn=cdpvmDynPortDevPwwn, PYSNMP_MODULE_ID=ciscoDpvmMIB, cdpvmClearAutoLearnWwn=cdpvmClearAutoLearnWwn, cdpvmLoginDevType=cdpvmLoginDevType, cdpvmDynPortVsan=cdpvmDynPortVsan, cdpvmNextAvailIndex=cdpvmNextAvailIndex)