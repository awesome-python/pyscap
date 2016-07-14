This document briefly explains the contents of the USGCB Platform ZIP files.

USGCB Platform ZIP bundles are provided to allow consumers to download all data streams for products supported by the indicated platform.

The file naming scheme is described in the USGCB FAQ (http://usgcb.nist.gov/usgcb_faq.html), please take a look at FAQ #64 for a complete description: http://usgcb.nist.gov/usgcb_faq.html#vhdfaq_scapnumsys.

USGCB-Windows.zip includes the following data streams:
	IE7-2.1.3.1.zip              
	IE8-1.3.3.1.zip
	WinXP-3.0.3.1.zip            
	WinXP-Firewall-2.1.0.1.zip
	WinVista-3.0.5.1.zip
	WinVista-Firewall-2.1.0.1.zip
	Win7-2.0.5.1.zip             
	Win7-Firewall-1.3.0.1.zip    

USGCB-Major-Version-1.2.x.0.zip extracts to USGCB-Major-Version-1.2.x.0 folder containing:
	USGCB-Major-Version-1.2.0.0 -> SCAP 1.0, OVAL 5.4 data stream.
	USGCB-Major-Version-1.2.1.0 -> SCAP 1.0, OVAL 5.3 data stream.
	USGCB-Major-Version-1.2.7.1 -> SCAP 1.2, OVAL 5.10, digitally signed data stream.

USGCB-Major-Version-2.0.x.0.zip extracts to USGCB-Major-Version-2.0.x.0 folder containing:
	USGCB-Major-Version-2.0.0.0 -> SCAP 1.0, OVAL 5.4 data stream.
	USGCB-Major-Version-2.0.1.0 -> SCAP 1.0, OVAL 5.3 data stream.
	USGCB-Major-Version-2.0.7.1 -> SCAP 1.2, OVAL 5.10, digitally signed data stream.


The SCAP 1.0 datastreams utilize XCCDF 1.1.4, OVAL 5.3 and OVAL 5.4, and CPE 2.2 content, these datastreams should work with tools validated as USGCB scanners as described here: http://scap.nist.gov/validation/index.html. This content may also work correctly with tools validated as FDCC scanners. 

The SCAP 1.2 datastreams utilize XCCDF 1.2, OVAL 5.10, OCIL 2.0, CPE 2.3, and TMSAD 1.0. These datastreams should work with authenticated configuration scanners as described here: http://scap.nist.gov/validation/index.html. When the SCAP 1.2 content was initially published in April, 2012 there were no validated scanners for using the content. You may want to contact the firm that created the scanner your organization uses to find out what their plans are for supporting SCAP 1.2 content. 