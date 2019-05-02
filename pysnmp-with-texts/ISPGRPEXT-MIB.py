#
# PySNMP MIB module ISPGRPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ISPGRPEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ispgrpExt, = mibBuilder.importSymbols("APENT-MIB", "ispgrpExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, NotificationType, Gauge32, iso, Counter64, Bits, ModuleIdentity, ObjectIdentity, Counter32, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "iso", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "Unsigned32", "TimeTicks", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
apIspgrpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 27, 1))
if mibBuilder.loadTexts: apIspgrpExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apIspgrpExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIspgrpExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIspgrpExtMib.setDescription('The MIB module used to describe the ArrowPoint Communications ISP interface information')
apIspgrpTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2), )
if mibBuilder.loadTexts: apIspgrpTable.setStatus('current')
if mibBuilder.loadTexts: apIspgrpTable.setDescription('A list of Interfaces configured as uplinks to the specified ISP.')
apIspgrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1), ).setIndexNames((0, "ISPGRPEXT-MIB", "apIspgrpName"))
if mibBuilder.loadTexts: apIspgrpEntry.setStatus('current')
if mibBuilder.loadTexts: apIspgrpEntry.setDescription('A group of information to uniquely identify the uplinks to one or more ISPs.')
apIspgrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspgrpName.setStatus('current')
if mibBuilder.loadTexts: apIspgrpName.setDescription('The name of the ISP connected to this composer.')
apIspgrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspgrpIndex.setStatus('current')
if mibBuilder.loadTexts: apIspgrpIndex.setDescription('The unique index for each ISP defined.')
apIspgrpTotalBwdth = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspgrpTotalBwdth.setStatus('current')
if mibBuilder.loadTexts: apIspgrpTotalBwdth.setDescription('The Total Bandwidth connected to the specified ISP.')
apIspgrpWebHostPipeBwdth = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspgrpWebHostPipeBwdth.setStatus('current')
if mibBuilder.loadTexts: apIspgrpWebHostPipeBwdth.setDescription('The amount of Bandwidth reserved for flow pipes to configured web hosts.')
apIspgrpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 5), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspgrpMode.setStatus('current')
if mibBuilder.loadTexts: apIspgrpMode.setDescription('This field signifies whether this ISP is considered the primary connection to the Internet or is a backup used only if the primary fails.')
apIspgrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspgrpStatus.setStatus('current')
if mibBuilder.loadTexts: apIspgrpStatus.setDescription('Status entry for this row ')
apIspLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3), )
if mibBuilder.loadTexts: apIspLinkTable.setStatus('current')
if mibBuilder.loadTexts: apIspLinkTable.setDescription('A list of uplinks connected to a specified ISP.')
apIspLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1), ).setIndexNames((0, "ISPGRPEXT-MIB", "apIspName"), (0, "ISPGRPEXT-MIB", "apIspLinkifIndex"))
if mibBuilder.loadTexts: apIspLinkEntry.setStatus('current')
if mibBuilder.loadTexts: apIspLinkEntry.setDescription('A record to describe each uplink to a specified ISP.')
apIspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspName.setStatus('current')
if mibBuilder.loadTexts: apIspName.setDescription('The name of the ISP which this uplink connects to.')
apIspLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspLinkIndex.setStatus('current')
if mibBuilder.loadTexts: apIspLinkIndex.setDescription('The unique index for each ISP link configured on this box.')
apIspLinkifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspLinkifIndex.setStatus('current')
if mibBuilder.loadTexts: apIspLinkifIndex.setDescription('The If Index of the link being specified as an uplink.')
apIspLinkBwdthAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspLinkBwdthAlloc.setStatus('current')
if mibBuilder.loadTexts: apIspLinkBwdthAlloc.setDescription('The statistics of allocated Bandwidth for this link.')
apIspLinkBEBwdthAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIspLinkBEBwdthAlloc.setStatus('current')
if mibBuilder.loadTexts: apIspLinkBEBwdthAlloc.setDescription('The amount of best effort traffic allocated on this link.')
apIspLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIspLinkStatus.setStatus('current')
if mibBuilder.loadTexts: apIspLinkStatus.setDescription('Status entry for this row ')
mibBuilder.exportSymbols("ISPGRPEXT-MIB", apIspgrpWebHostPipeBwdth=apIspgrpWebHostPipeBwdth, apIspLinkStatus=apIspLinkStatus, apIspLinkifIndex=apIspLinkifIndex, apIspgrpTotalBwdth=apIspgrpTotalBwdth, apIspgrpName=apIspgrpName, apIspLinkBEBwdthAlloc=apIspLinkBEBwdthAlloc, PYSNMP_MODULE_ID=apIspgrpExtMib, apIspgrpEntry=apIspgrpEntry, apIspgrpMode=apIspgrpMode, apIspLinkIndex=apIspLinkIndex, apIspLinkEntry=apIspLinkEntry, apIspName=apIspName, apIspgrpIndex=apIspgrpIndex, apIspLinkBwdthAlloc=apIspLinkBwdthAlloc, apIspgrpExtMib=apIspgrpExtMib, apIspgrpStatus=apIspgrpStatus, apIspgrpTable=apIspgrpTable, apIspLinkTable=apIspLinkTable)