<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:ogr="http://osgeo.org/gdal" xmlns:gpx="http://www.topografix.com/GPX/1/1"
    xmlns="http://www.topografix.com/GPX/1/1"
    exclude-result-prefixes="ogr gpx">
<!--
Note the namespaces
    * ogr - because that's in the original GPX file
    * gpx - because I couldn't select the "extension" element without it
    * xmlns="http://www.topografix.com/GPX/1/1" - because otherwise an empty namespace is added to new elements
Frankly I don't understand why this is the case.
 -->
<xsl:strip-space elements="*"/>
<xsl:output method="xml" omit-xml-declaration="no" indent="yes"/>

<!--
Copy everything that has no other pattern defined
-->
<xsl:template match="*">
<xsl:copy copy-namespaces="no">
    <xsl:copy-of select="@*"/>
    <xsl:apply-templates />
</xsl:copy>
</xsl:template>

<xsl:template match="gpx:extensions">
    <name>Sample Site <xsl:value-of select="ogr:id"/></name>
    <description>Sample Site <xsl:value-of select="ogr:id"/></description>
</xsl:template>

</xsl:stylesheet>
