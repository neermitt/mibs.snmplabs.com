#
# PySNMP MIB module CISCO-RADIUS-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Integer32, IpAddress, TimeTicks, MibIdentifier, iso, Gauge32, Bits, Counter32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Integer32", "IpAddress", "TimeTicks", "MibIdentifier", "iso", "Gauge32", "Bits", "Counter32", "Unsigned32", "NotificationType")
TimeInterval, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TextualConvention")
ciscoRadiusExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 736))
ciscoRadiusExtMIB.setRevisions(('2010-05-25 00:00', '2010-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusExtMIB.setRevisionsDescriptions(("Modified 'max-access' of creAuthClientLastUsedSourceId and creAcctClientLastUsedSourceId", 'Initial Version',))
if mibBuilder.loadTexts: ciscoRadiusExtMIB.setLastUpdated('201005250000Z')
if mibBuilder.loadTexts: ciscoRadiusExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusExtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusExtMIB.setDescription('This MIB module defines objects describing RADIUS (Remote Access Dialin User Service), serving as an extension of the following MIB modules: - - RADIUS-AUTH-CLIENT-MIB [RFC4668] - RADIUS-AUTH-SERVER-MIB [RFC4669] - RADIUS-ACC-CLIENT-MIB [RFC4670] - RADIUS-ACC-SERVER-MIB [RFC4671] - RADIUS-DYNAUTH-CLIENT-MIB [RFC4672] - RADIUS-DYNAUTH-SERVER-MIB [RFC4673] - [RFC4668] D. Nelson, RADIUS Authentication Client MIB for IPv6, RFC-4668, August 2006. - [RFC4669] D. Nelson, RADIUS Authentication Server MIB for IPv6, RFC-4669, August 2006. - [RFC4670] D. Nelson, RADIUS Accounting Client MIB for IPv6, RFC-4670, August 2006. - [RFC4671] D. Nelson, RADIUS Accounting Server MIB for IPv6, RFC-4671, August 2006. - [RFC4672] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic Authorization Client MIB, RFC-4672, September 2006. - [RFC4673] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic Authorization Server MIB, RFC-4673, September 2006.')
class RadiusSourceIdentifier(TextualConvention, Unsigned32):
    description = "This textual convention represents the range of identifers used when 'extended RADIUS source port' is configured."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

cRadiusExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1))
creClientGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1))
creClientAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2))
creClientAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3))
creClientDynAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 4))
creServerGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 5))
creServerAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 6))
creServerAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 7))
creServerDynAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 8))
creClientTotalMaxInQLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 1), Gauge32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientTotalMaxInQLength.setStatus('current')
if mibBuilder.loadTexts: creClientTotalMaxInQLength.setDescription('This object indicates the maximum length of the queue which stores the incoming RADIUS packets.')
creClientTotalMaxWaitQLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 2), Gauge32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientTotalMaxWaitQLength.setStatus('current')
if mibBuilder.loadTexts: creClientTotalMaxWaitQLength.setDescription('This object indicates the maximum length of the queue which stores the pending RADIUS packets for which the responses are outstanding.')
creClientTotalMaxDoneQLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 3), Gauge32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientTotalMaxDoneQLength.setStatus('current')
if mibBuilder.loadTexts: creClientTotalMaxDoneQLength.setDescription('This object indicates the maximum length of the queue which stores those RADIUS packets for which the responses are received.')
creClientTotalAccessRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 4), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientTotalAccessRejects.setStatus('current')
if mibBuilder.loadTexts: creClientTotalAccessRejects.setDescription('This object indicates the number of access reject packets received by the RADIUS client.')
creClientTotalAverageResponseDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientTotalAverageResponseDelay.setStatus('current')
if mibBuilder.loadTexts: creClientTotalAverageResponseDelay.setDescription('This object indicates the overall response delay experienced by RADIUS packets (both authentication and accounting).')
creClientSourcePortRangeStart = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientSourcePortRangeStart.setStatus('current')
if mibBuilder.loadTexts: creClientSourcePortRangeStart.setDescription("If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests. This MIB object indicates the port value from where this range starts.")
creClientSourcePortRangeEnd = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 7), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientSourcePortRangeEnd.setStatus('current')
if mibBuilder.loadTexts: creClientSourcePortRangeEnd.setDescription("If the 'extended RADIUS source port' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests. This MIB object indicates the port value where this range ends.")
creClientLastUsedSourcePort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 8), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientLastUsedSourcePort.setStatus('current')
if mibBuilder.loadTexts: creClientLastUsedSourcePort.setDescription("If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests. This MIB object indicates the last source port that was used to send out a RADIUS authentication or accounting request.")
creClientLastUsedSourceId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 9), RadiusSourceIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creClientLastUsedSourceId.setStatus('current')
if mibBuilder.loadTexts: creClientLastUsedSourceId.setDescription("This MIB object indicates the last source identifier that was used to send out a RADIUS packet when 'extended RADIUS source ports' is configured. The source identifier is a counter that is incremented everytime a RADIUS authentication or an accounting packet is sent.")
creAuthClientBadAuthenticators = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 1), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: creAuthClientBadAuthenticators.setDescription('This object indicates the number of RADIUS authentication response packets received which contained invalid authenticators.')
creAuthClientUnknownResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 2), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientUnknownResponses.setStatus('current')
if mibBuilder.loadTexts: creAuthClientUnknownResponses.setDescription('This object indicates the number of unknown RADIUS authentication responses received.')
creAuthClientTotalPacketsWithResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 3), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientTotalPacketsWithResponses.setStatus('current')
if mibBuilder.loadTexts: creAuthClientTotalPacketsWithResponses.setDescription('This object indicates the number of RADIUS authentication packets that received responses.')
creAuthClientBufferAllocFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 4), Counter32()).setUnits('buffer failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientBufferAllocFailures.setStatus('current')
if mibBuilder.loadTexts: creAuthClientBufferAllocFailures.setDescription('This object indicates the number of buffer allocation failures encountered during RADIUS request formation.')
creAuthClientTotalResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 5), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientTotalResponses.setStatus('current')
if mibBuilder.loadTexts: creAuthClientTotalResponses.setDescription('This object indicates the number of RADIUS authentication response packets received by the RADIUS client.')
creAuthClientTotalPacketsWithoutResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 6), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientTotalPacketsWithoutResponses.setStatus('current')
if mibBuilder.loadTexts: creAuthClientTotalPacketsWithoutResponses.setDescription('This object indicates the number of RADIUS authentication packets that never received a response.')
creAuthClientAverageResponseDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientAverageResponseDelay.setStatus('current')
if mibBuilder.loadTexts: creAuthClientAverageResponseDelay.setDescription('This object indicates the average response delay experienced for RADIUS authentication requests.')
creAuthClientMaxResponseDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 8), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientMaxResponseDelay.setStatus('current')
if mibBuilder.loadTexts: creAuthClientMaxResponseDelay.setDescription('This object indicates the maximum delay experienced for RADIUS authentication requests.')
creAuthClientMaxBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientMaxBufferSize.setStatus('current')
if mibBuilder.loadTexts: creAuthClientMaxBufferSize.setDescription('This object indicates the maximum buffer size for RADIUS authentication packet.')
creAuthClientTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 10), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientTimeouts.setStatus('current')
if mibBuilder.loadTexts: creAuthClientTimeouts.setDescription('This object indicates the number of timeouts that have occurred for RADIUS authentication. After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration.')
creAuthClientDupIDs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 11), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientDupIDs.setStatus('current')
if mibBuilder.loadTexts: creAuthClientDupIDs.setDescription('This object indicates the number of times client has received duplicate authentication responses with the same identifier. Out of these two packets, the later packet is considered as a true match.')
creAuthClientMalformedResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 12), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientMalformedResponses.setStatus('current')
if mibBuilder.loadTexts: creAuthClientMalformedResponses.setDescription('This object indicates the number of malformed RADIUS authentication responses received. Malformed packets include packets with an invalid length.')
creAuthClientLastUsedSourceId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 13), RadiusSourceIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAuthClientLastUsedSourceId.setStatus('current')
if mibBuilder.loadTexts: creAuthClientLastUsedSourceId.setDescription("This MIB object indicates the last source identifier that was used to send out a RADIUS authentication request when 'extended RADIUS source ports' is configured. The source identifier is a counter that is incremented everytime a RADIUS authentication request is sent.")
creAcctClientBadAuthenticators = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 1), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: creAcctClientBadAuthenticators.setDescription('This object indicates the number of RADIUS Accounting-Response packets received with invalid authenticators.')
creAcctClientUnknownResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 2), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientUnknownResponses.setStatus('current')
if mibBuilder.loadTexts: creAcctClientUnknownResponses.setDescription('This object indicates the number of unknown RADIUS accounting responses received.')
creAcctClientTotalPacketsWithResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 3), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientTotalPacketsWithResponses.setStatus('current')
if mibBuilder.loadTexts: creAcctClientTotalPacketsWithResponses.setDescription('This object indicates the number of RADIUS accounting packets that received responses.')
creAcctClientBufferAllocFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 4), Counter32()).setUnits('buffer failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientBufferAllocFailures.setStatus('current')
if mibBuilder.loadTexts: creAcctClientBufferAllocFailures.setDescription('This object indicates the number of buffer allocation failures encountered for RADIUS accounting request.')
creAcctClientTotalResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 5), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientTotalResponses.setStatus('current')
if mibBuilder.loadTexts: creAcctClientTotalResponses.setDescription('This object indicates the number of RADIUS accounting response packets received by the RADIUS client.')
creAcctClientTotalPacketsWithoutResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 6), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientTotalPacketsWithoutResponses.setStatus('current')
if mibBuilder.loadTexts: creAcctClientTotalPacketsWithoutResponses.setDescription('This object indicates the number of RADIUS accounting packets that never received a response.')
creAcctClientAverageResponseDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientAverageResponseDelay.setStatus('current')
if mibBuilder.loadTexts: creAcctClientAverageResponseDelay.setDescription('This object indicates the average response delay experienced for RADIUS accounting.')
creAcctClientMaxResponseDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 8), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientMaxResponseDelay.setStatus('current')
if mibBuilder.loadTexts: creAcctClientMaxResponseDelay.setDescription('This object indicates the maximum delay experienced for RADIUS accounting.')
creAcctClientMaxBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientMaxBufferSize.setStatus('current')
if mibBuilder.loadTexts: creAcctClientMaxBufferSize.setDescription('This object indicates the maximum buffer size for RADIUS accounting packets.')
creAcctClientTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 10), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientTimeouts.setStatus('current')
if mibBuilder.loadTexts: creAcctClientTimeouts.setDescription('This object indicates the number of timeouts that have occurred for RADIUS accounting. After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration.')
creAcctClientDupIDs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 11), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientDupIDs.setStatus('current')
if mibBuilder.loadTexts: creAcctClientDupIDs.setDescription('This object indicates the number of times client has received duplicate accounting responses with the same identifier. Out of these two packets, the later packet is considered as a true match.')
creAcctClientMalformedResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 12), Counter32()).setUnits('RADIUS packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientMalformedResponses.setStatus('current')
if mibBuilder.loadTexts: creAcctClientMalformedResponses.setDescription('This object indicates the number of malformed RADIUS accounting responses received. Malformed packets include packets with an invalid length.')
creAcctClientLastUsedSourceId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 13), RadiusSourceIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: creAcctClientLastUsedSourceId.setStatus('current')
if mibBuilder.loadTexts: creAcctClientLastUsedSourceId.setDescription("This MIB object indicates the last source identifier that was used to send out a RADIUS accounting request when 'extended RADIUS source ports' is configured. The source identifier is a counter that is incremented everytime a RADIUS accounting request is sent.")
cRadiusExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 2))
creMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 1))
creMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2))
creMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 1, 1)).setObjects(("CISCO-RADIUS-EXT-MIB", "creClientAuthenenticationGroup"), ("CISCO-RADIUS-EXT-MIB", "creClientGlobalGroup"), ("CISCO-RADIUS-EXT-MIB", "creClientAccountingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    creMIBCompliance = creMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: creMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO RADIUS Extention MIB')
creClientGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 1)).setObjects(("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxInQLength"), ("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxWaitQLength"), ("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxDoneQLength"), ("CISCO-RADIUS-EXT-MIB", "creClientTotalAccessRejects"), ("CISCO-RADIUS-EXT-MIB", "creClientSourcePortRangeStart"), ("CISCO-RADIUS-EXT-MIB", "creClientSourcePortRangeEnd"), ("CISCO-RADIUS-EXT-MIB", "creClientLastUsedSourcePort"), ("CISCO-RADIUS-EXT-MIB", "creClientLastUsedSourceId"), ("CISCO-RADIUS-EXT-MIB", "creClientTotalAverageResponseDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    creClientGlobalGroup = creClientGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: creClientGlobalGroup.setDescription('Objects for providing aggregated statistics of RADIUS client.')
creClientAuthenenticationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 2)).setObjects(("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalResponses"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalPacketsWithResponses"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalPacketsWithoutResponses"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientAverageResponseDelay"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientMaxResponseDelay"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientTimeouts"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientDupIDs"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientBufferAllocFailures"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientMaxBufferSize"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientMalformedResponses"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientBadAuthenticators"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientUnknownResponses"), ("CISCO-RADIUS-EXT-MIB", "creAuthClientLastUsedSourceId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    creClientAuthenenticationGroup = creClientAuthenenticationGroup.setStatus('current')
if mibBuilder.loadTexts: creClientAuthenenticationGroup.setDescription('Objects for providing statistics of RADIUS client authentication packets.')
creClientAccountingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 3)).setObjects(("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalResponses"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalPacketsWithResponses"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalPacketsWithoutResponses"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientAverageResponseDelay"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientMaxResponseDelay"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientTimeouts"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientBadAuthenticators"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientUnknownResponses"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientLastUsedSourceId"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientDupIDs"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientBufferAllocFailures"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientMaxBufferSize"), ("CISCO-RADIUS-EXT-MIB", "creAcctClientMalformedResponses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    creClientAccountingGroup = creClientAccountingGroup.setStatus('current')
if mibBuilder.loadTexts: creClientAccountingGroup.setDescription('Objects for providing statistics of RADIUS client accounting packets.')
mibBuilder.exportSymbols("CISCO-RADIUS-EXT-MIB", creAuthClientBadAuthenticators=creAuthClientBadAuthenticators, creClientDynAuth=creClientDynAuth, creAuthClientTotalPacketsWithoutResponses=creAuthClientTotalPacketsWithoutResponses, creAuthClientBufferAllocFailures=creAuthClientBufferAllocFailures, creAuthClientAverageResponseDelay=creAuthClientAverageResponseDelay, creAuthClientTimeouts=creAuthClientTimeouts, creClientTotalAccessRejects=creClientTotalAccessRejects, creAcctClientBufferAllocFailures=creAcctClientBufferAllocFailures, creAuthClientLastUsedSourceId=creAuthClientLastUsedSourceId, creClientAuthentication=creClientAuthentication, creClientTotalMaxWaitQLength=creClientTotalMaxWaitQLength, cRadiusExtMIBConformance=cRadiusExtMIBConformance, creClientTotalMaxInQLength=creClientTotalMaxInQLength, creClientGlobalGroup=creClientGlobalGroup, creClientAccounting=creClientAccounting, PYSNMP_MODULE_ID=ciscoRadiusExtMIB, creServerAuthentication=creServerAuthentication, creAcctClientMalformedResponses=creAcctClientMalformedResponses, creAcctClientTimeouts=creAcctClientTimeouts, ciscoRadiusExtMIB=ciscoRadiusExtMIB, creClientLastUsedSourcePort=creClientLastUsedSourcePort, creClientAuthenenticationGroup=creClientAuthenenticationGroup, creClientTotalMaxDoneQLength=creClientTotalMaxDoneQLength, creAcctClientAverageResponseDelay=creAcctClientAverageResponseDelay, creClientLastUsedSourceId=creClientLastUsedSourceId, creAcctClientMaxBufferSize=creAcctClientMaxBufferSize, creAcctClientBadAuthenticators=creAcctClientBadAuthenticators, RadiusSourceIdentifier=RadiusSourceIdentifier, creAcctClientLastUsedSourceId=creAcctClientLastUsedSourceId, creClientSourcePortRangeStart=creClientSourcePortRangeStart, creMIBCompliances=creMIBCompliances, creAcctClientTotalPacketsWithoutResponses=creAcctClientTotalPacketsWithoutResponses, creAcctClientMaxResponseDelay=creAcctClientMaxResponseDelay, cRadiusExtMIBObjects=cRadiusExtMIBObjects, creAuthClientTotalResponses=creAuthClientTotalResponses, creMIBGroups=creMIBGroups, creServerGlobal=creServerGlobal, creMIBCompliance=creMIBCompliance, creServerDynAuth=creServerDynAuth, creAuthClientTotalPacketsWithResponses=creAuthClientTotalPacketsWithResponses, creAuthClientMaxResponseDelay=creAuthClientMaxResponseDelay, creClientGlobal=creClientGlobal, creAcctClientTotalPacketsWithResponses=creAcctClientTotalPacketsWithResponses, creAuthClientUnknownResponses=creAuthClientUnknownResponses, creClientAccountingGroup=creClientAccountingGroup, creClientTotalAverageResponseDelay=creClientTotalAverageResponseDelay, creAcctClientUnknownResponses=creAcctClientUnknownResponses, creClientSourcePortRangeEnd=creClientSourcePortRangeEnd, creAuthClientMaxBufferSize=creAuthClientMaxBufferSize, creAuthClientDupIDs=creAuthClientDupIDs, creAcctClientDupIDs=creAcctClientDupIDs, creAuthClientMalformedResponses=creAuthClientMalformedResponses, creServerAccounting=creServerAccounting, creAcctClientTotalResponses=creAcctClientTotalResponses)