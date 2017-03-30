<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<xsl:stylesheet
version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:cdf="http://checklists.nist.gov/xccdf/1.1">
	<xsl:template match="cdf:TestResult">
        <h3 align="center">Profile <xsl:value-of select="./cdf:profile"/></h3>
		<p><b>Test Result ID: </b> <xsl:value-of select="./@id"/><br/>
		<b>Start Time: </b> <xsl:value-of select="./@start-time"/><br/>
		<b>End Time: </b> <xsl:value-of select="./@end-time"/><br/>
		<b>Version: </b> <xsl:value-of select="./@version"/><br/>
		<b>Targeted Machine's hostname: </b> <xsl:value-of select="./cdf:target"/><br/>
		<b>Identity used to perform tests: </b> <xsl:value-of select="./cdf:identity"/><br/>
		<b>Addresses: </b> <xsl:for-each select="cdf:target-address">
			<xsl:value-of select="."/>
			<xsl:if test="position() != last()">, </xsl:if>
			</xsl:for-each><br/>
		<b>MAC Addresses: </b> <xsl:for-each select="cdf:target-facts/cdf:fact[@name = 'urn:fact:ethernet:MAC']">
			<xsl:value-of select="."/>
			<xsl:if test="position() != last()">, </xsl:if>
		</xsl:for-each></p>
		<h2>Summary</h2>
		<p><b><xsl:value-of select="count(./cdf:rule-result)"/> Total Results</b><br/>
		<span style="color: green">
		<xsl:value-of select="count(./cdf:rule-result[cdf:result='pass'])"/> Pass Results<br/>
		<xsl:if test="count(./cdf:rule-result[cdf:result='fixed']) != 0">
			<xsl:value-of select="count(./cdf:rule-result[cdf:result='fixed'])"/> Fixed Results<br/>
		</xsl:if>
		</span>
		<span style="color: red">
		<xsl:value-of select="count(./cdf:rule-result[cdf:result='fail'])"/> Fail Results<br/>
		</span>
		<span style="color: gray">
		<xsl:value-of select="count(./cdf:rule-result[cdf:result='notapplicable'])"/> Not Applicable Results<br/>
		</span>
		<xsl:value-of select="count(./cdf:rule-result[cdf:result='notchecked'])"/> Not Checked Results<br/>
		<xsl:if test="count(./cdf:rule-result[cdf:result='error']) != 0">
			<xsl:value-of select="count(./cdf:rule-result[cdf:result='error'])"/> Error Results<br/>
		</xsl:if>
		<xsl:if test="count(./cdf:rule-result[cdf:result='unknown']) != 0">
			<xsl:value-of select="count(./cdf:rule-result[cdf:result='unknown'])"/> Unknown Results<br/>
		</xsl:if>
		<xsl:if test="count(./cdf:rule-result[cdf:result='informational']) != 0">
			<xsl:value-of select="count(./cdf:rule-result[cdf:result='informational'])"/> Informational Results<br/>
		</xsl:if>
		<xsl:value-of select="(count(./cdf:rule-result[cdf:result='pass']) + count(./cdf:rule-result[cdf:result='fixed']) + count(./cdf:rule-result[cdf:result='notapplicable'])) div count(./cdf:rule-result) * 100"/>%
		</p>
		<h2>Results</h2>
		<xsl:apply-templates select="cdf:rule-result" />
	</xsl:template>
	<xsl:template match="cdf:rule-result">
		<p><b>ID: </b><xsl:value-of select="./@idref"/><br/>
		<b>When Checked: </b><xsl:value-of select="./@time"/><br/>
		<b>Rule Version: </b><xsl:value-of select="./@version"/><br/>
		<b>Result: </b><xsl:choose>
			<xsl:when test="./cdf:result = 'pass'">
				<span style="color: green">Pass</span>
			</xsl:when>
			<xsl:when test="./cdf:result = 'fail'">
				<span style="color: red">Fail</span>
			</xsl:when>
			<xsl:when test="./cdf:result = 'error'">
				<span style="color: red">Error</span>
			</xsl:when>
			<xsl:when test="./cdf:result = 'unknown'">
				Unknown
			</xsl:when>
			<xsl:when test="./cdf:result = 'notapplicable'">
				<span style="color: gray">Not Applicable</span>
			</xsl:when>
			<xsl:when test="./cdf:result = 'notchecked'">
				Not Checked
			</xsl:when>
			<xsl:when test="./cdf:result = 'notselected'">
				Not Selected
			</xsl:when>
			<xsl:when test="./cdf:result = 'informational'">
				Informational
			</xsl:when>
			<xsl:when test="./cdf:result = 'fixed'">
				<span style="color: green">Fixed</span>
			</xsl:when>
		</xsl:choose><br/>
		<pre><xsl:value-of select="./cdf:message"/></pre>
		</p>
	</xsl:template>
	<xsl:template match="/">
		<html>
			<head>
				<title><xsl:value-of select="cdf:Benchmark/@id"/> Test Results</title>
			</head>
			<body>
				<div style="text-align: center"><img src="http://www.mcdean.com/images/logo.gif" alt="M.C. Dean" /></div>
                <h1 align="center"><xsl:value-of select="cdf:Benchmark/@id"/> Test Results</h1>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>
	
</xsl:stylesheet>