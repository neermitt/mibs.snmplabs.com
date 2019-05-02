#
# PySNMP MIB module ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Gauge32, TimeTicks, IpAddress, iso, ObjectIdentity, Integer32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "iso", "ObjectIdentity", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysMgmtAuthNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60))
etsysMgmtAuthNotificationMIB.setRevisions(('2011-03-08 20:40', '2005-11-14 16:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setRevisionsDescriptions(('Added the following notifications (and associated configuration controls): etsysMgmtAuthInactiveNotification, etsysMgmtAuthMaxAuthAttemptNotification, and etsysmgmtAuthMaxFailNotification.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setLastUpdated('201103082040Z')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setDescription("This MIB module defines a portion of the SNMP enterprise MIBs under Enterasys Networks' enterprise OID pertaining to Network management authentication notifications. This MIB was designed to be used for monitoring authentication events on the network management system by various remote monitoring mechanisms.")
class EtsysMgmtAuthNotificationTypes(TextualConvention, Bits):
    description = 'The list of authentication notification types that could be supported and enabled on the managed entity. cliConsole(0) CLI console connection authentication cliSsh(1) CLI SSH connection authentication cliTelnet(2) CLI TELNET connection authentication webview(3) Webview connection authentication inactiveUser(4) Username unused for specified interval maxUserAttempt(5) Exceeded maximum simultaneous authentications maxUserFail(6) Exceeded maximum failed authentications'
    status = 'current'
    namedValues = NamedValues(("cliConsole", 0), ("cliSsh", 1), ("cliTelnet", 2), ("webview", 3), ("inactiveUser", 4), ("maxUserAttempt", 5), ("maxUserFail", 6))

etsysMgmtAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1))
etsysMgmtAuthNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0))
etsysMgmtAuthConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1))
etsysMgmtAuthAuthenticationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2))
etsysMgmtAuthNotificationsSupported = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationsSupported.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationsSupported.setDescription('Specifies the management notification types supported on this management entity.')
etsysMgmtAuthNotificationEnabledStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 2), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationEnabledStatus.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationEnabledStatus.setDescription('The authentication types the management entity is configured to send notifications for.')
etsysMgmtAuthType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthType.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthType.setDescription('The authentication type that was attempted by the user. Only 1 bit MAY be set in any given notification.')
etsysMgmtAuthUserName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthUserName.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthUserName.setDescription('The username supplied by the user in the in the authentication attempt.')
etsysMgmtAuthInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddressType.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthInetAddressType.setDescription('A value that represents a type of Internet address specified by etsysMgmtAuthInetAddress.')
etsysMgmtAuthInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddress.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthInetAddress.setDescription('The Internet Address of the remote user being authenticated. The format of this object is defined by the etsysMgmtAuthInetAddressType object.')
etsysMgmtAuthInIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 5), InterfaceIndexOrZero()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInIfIndex.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthInIfIndex.setDescription('The MIB2 interface on the managed entity that the authentication request was received on. This object must return a value of zero if the interface is unknown.')
etsysMgmtAuthSuccessNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthSuccessNotificiation.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthSuccessNotificiation.setDescription('Authentication passed notification. The managed entity will send this notification when the remote user is successfully authenticated')
etsysMgmtAuthFailNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthFailNotificiation.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthFailNotificiation.setDescription('Authentication failed notification. The managed entity will send this notification when the remote user fails authentication')
etsysMgmtAuthInactiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthInactiveNotification.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthInactiveNotification.setDescription('Disable unused user(name) notification. The managed entity will send this notification to alert the appropriate administrator that the username has not been used during a specified time interval, so that the administrator may disable or delete that username.')
etsysMgmtAuthMaxAuthAttemptNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxAuthAttemptNotification.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthMaxAuthAttemptNotification.setDescription('Max user authentication attempt notification. The managed entity will send this notification to alert the appropriate administrator that a particular user has attempted to authenticate on the device a specified number of times.')
etsysMgmtAuthMaxFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 5)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxFailNotification.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthMaxFailNotification.setDescription('Failed authentication threshold notification. The managed entity will send this notification to alert the appropriate administrator when the threshold for failed authentications for a particular user has been exceeded.')
etsysMgmtAuthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2))
etsysMgmtAuthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1))
etsysMgmtAuthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2))
etsysMgmtAuthConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationsSupported"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationEnabledStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthConfigGroup = etsysMgmtAuthConfigGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthConfigGroup.setDescription('A collection of objects providing basic instrumentation of network management authentication notifications.')
etsysMgmtAuthHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthHistoryGroup = etsysMgmtAuthHistoryGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthHistoryGroup.setDescription('A collection of objects providing authentication history information.')
etsysMgmtAuthNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthSuccessNotificiation"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthFailNotificiation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationGroup = etsysMgmtAuthNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationGroup.setDescription('The management authentication notifications.')
etsysMgmtAuthNotificationUserGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInactiveNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxAuthAttemptNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxFailNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationUserGroup = etsysMgmtAuthNotificationUserGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationUserGroup.setDescription("The management authentication notifications relating to a particular user's attributes.")
etsysMgmtAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthConfigGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthHistoryGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthCompliance = etsysMgmtAuthCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthCompliance.setDescription('The compliance statement for devices that support Enterasys management authentication notification.')
etsysMgmtAuthUserCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthUserCompliance = etsysMgmtAuthUserCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysMgmtAuthUserCompliance.setDescription('The compliance statement for devices that support Enterasys management authentication notifications based on user attributes.')
mibBuilder.exportSymbols("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", etsysMgmtAuthAuthenticationBranch=etsysMgmtAuthAuthenticationBranch, PYSNMP_MODULE_ID=etsysMgmtAuthNotificationMIB, etsysMgmtAuthNotificationEnabledStatus=etsysMgmtAuthNotificationEnabledStatus, etsysMgmtAuthInactiveNotification=etsysMgmtAuthInactiveNotification, etsysMgmtAuthNotificationGroup=etsysMgmtAuthNotificationGroup, etsysMgmtAuthNotificationMIB=etsysMgmtAuthNotificationMIB, etsysMgmtAuthInetAddressType=etsysMgmtAuthInetAddressType, etsysMgmtAuthInetAddress=etsysMgmtAuthInetAddress, etsysMgmtAuthUserCompliance=etsysMgmtAuthUserCompliance, etsysMgmtAuthInIfIndex=etsysMgmtAuthInIfIndex, etsysMgmtAuthHistoryGroup=etsysMgmtAuthHistoryGroup, etsysMgmtAuthNotificationUserGroup=etsysMgmtAuthNotificationUserGroup, EtsysMgmtAuthNotificationTypes=EtsysMgmtAuthNotificationTypes, etsysMgmtAuthGroups=etsysMgmtAuthGroups, etsysMgmtAuthObjects=etsysMgmtAuthObjects, etsysMgmtAuthFailNotificiation=etsysMgmtAuthFailNotificiation, etsysMgmtAuthType=etsysMgmtAuthType, etsysMgmtAuthMaxAuthAttemptNotification=etsysMgmtAuthMaxAuthAttemptNotification, etsysMgmtAuthNotificationsSupported=etsysMgmtAuthNotificationsSupported, etsysMgmtAuthSuccessNotificiation=etsysMgmtAuthSuccessNotificiation, etsysMgmtAuthConfigBranch=etsysMgmtAuthConfigBranch, etsysMgmtAuthCompliance=etsysMgmtAuthCompliance, etsysMgmtAuthCompliances=etsysMgmtAuthCompliances, etsysMgmtAuthNotificationBranch=etsysMgmtAuthNotificationBranch, etsysMgmtAuthConformance=etsysMgmtAuthConformance, etsysMgmtAuthUserName=etsysMgmtAuthUserName, etsysMgmtAuthMaxFailNotification=etsysMgmtAuthMaxFailNotification, etsysMgmtAuthConfigGroup=etsysMgmtAuthConfigGroup)