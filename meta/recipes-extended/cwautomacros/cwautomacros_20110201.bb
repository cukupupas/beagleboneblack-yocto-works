DESCRIPTION = "cwautomacros: a collection of autoconf m4 macros"
SECTION = "base"
HOMEPAGE = "http://cwautomacros.berlios.de/"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://LICENSE;md5=eb723b61539feef013de476e68b5c50a"

SRC_URI = "http://download.berlios.de/cwautomacros/cwautomacros-${PV}.tar.bz2"

PR = "r0"

SRC_URI[md5sum] = "074afcb50d0a8bff10786a2954b2b02d"
SRC_URI[sha256sum] = "3115603b891f3a163c0bbb5fea2f3742113a183fa6745ee5e89e5f6d0e9f6121"

do_install() {
	oe_runmake CWAUTOMACROSPREFIX=${D}${prefix} install
}

BBCLASSEXTEND = "native"
