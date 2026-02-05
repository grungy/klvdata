#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MISB ST 0903 - Video Moving Target Indicator (VMTI) Local Set

This module implements parsing for VMTI metadata embedded in MISB ST 0601
UAS Local Metadata Sets. VMTI data contains target tracking and motion
information for detected moving objects.

Reference: MISB ST 0903 - Video Moving Target Indicator and Track Metadata
"""

from klvdata.element import UnknownElement as _UnknownElement
from klvdata.elementparser import BytesElementParser
from klvdata.elementparser import MappedElementParser
from klvdata.elementparser import StringElementParser
from klvdata.elementparser import DateTimeElementParser
from klvdata.setparser import SetParser
from klvdata.misb0601 import UASLocalMetadataSet


class UnknownElement(_UnknownElement):
    pass


# Register VMTILocalSet as a nested SetParser under UASLocalMetadataSet (tag 74)
@UASLocalMetadataSet.add_parser
class VMTILocalSet(SetParser):
    """MISB ST0903 Video Moving Target Indicator Local Set.
    
    Contains target tracking and motion information per MISB ST 0903.
    """
    key = b'\x4A'  # Tag 74
    TAG = 74
    UDSKey = "06 0E 2B 34 02 0B 01 01 0E 01 03 03 06 00 00 00"
    LDSName = "VMTI Local Set"
    ESDName = ""
    UDSName = "Video Moving Target Indicator Local Set"
    name = "VMTI Local Set"
    
    parsers = {}
    _unknown_element = UnknownElement


# VMTI Elements per MISB ST 0903

@VMTILocalSet.add_parser
class VMTIChecksum(BytesElementParser):
    """Checksum for VMTI Local Set (Tag 1)"""
    key = b'\x01'
    TAG = 1
    LDSName = "VMTI Checksum"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class VMTIPrecisionTimeStamp(DateTimeElementParser):
    """VMTI Precision Time Stamp in microseconds since epoch (Tag 2)"""
    key = b'\x02'
    TAG = 2
    LDSName = "VMTI Precision Time Stamp"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class VMTISystemName(StringElementParser):
    """Name of VMTI system (Tag 3)"""
    key = b'\x03'
    TAG = 3
    LDSName = "VMTI System Name"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class VMTILSVersionNumber(BytesElementParser):
    """VMTI LS Version Number (Tag 4)"""
    key = b'\x04'
    TAG = 4
    LDSName = "VMTI LS Version"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class TotalTargetsDetected(BytesElementParser):
    """Total number of targets detected in frame (Tag 5)"""
    key = b'\x05'
    TAG = 5
    LDSName = "Total Targets Detected"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class NumberOfReportedTargets(BytesElementParser):
    """Number of targets reported in this packet (Tag 6)"""
    key = b'\x06'
    TAG = 6
    LDSName = "Number of Reported Targets"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class FrameNumber(BytesElementParser):
    """Frame number (Tag 7)"""
    key = b'\x07'
    TAG = 7
    LDSName = "Frame Number"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class FrameWidth(BytesElementParser):
    """Frame width in pixels (Tag 8)"""
    key = b'\x08'
    TAG = 8
    LDSName = "Frame Width"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class FrameHeight(BytesElementParser):
    """Frame height in pixels (Tag 9)"""
    key = b'\x09'
    TAG = 9
    LDSName = "Frame Height"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class VMTISourceSensor(StringElementParser):
    """Source sensor for VMTI (Tag 10)"""
    key = b'\x0A'
    TAG = 10
    LDSName = "VMTI Source Sensor"
    ESDName = ""
    UDSName = ""


@VMTILocalSet.add_parser
class VMTIHorizontalFOV(MappedElementParser):
    """VMTI Horizontal Field of View (Tag 11)"""
    key = b'\x0B'
    TAG = 11
    LDSName = "VMTI Horizontal FOV"
    ESDName = ""
    UDSName = ""
    _domain = (0, 2**16-1)
    _range = (0, 180)
    units = 'degrees'


@VMTILocalSet.add_parser
class VMTIVerticalFOV(MappedElementParser):
    """VMTI Vertical Field of View (Tag 12)"""
    key = b'\x0C'
    TAG = 12
    LDSName = "VMTI Vertical FOV"
    ESDName = ""
    UDSName = ""
    _domain = (0, 2**16-1)
    _range = (0, 180)
    units = 'degrees'


@VMTILocalSet.add_parser
class MotionImageryURL(StringElementParser):
    """URL for associated motion imagery (Tag 13)"""
    key = b'\x0D'
    TAG = 13
    LDSName = "Motion Imagery URL"
    ESDName = ""
    UDSName = ""


# VTarget Pack (Tag 101) contains per-target data
# This is a series of nested target records
@VMTILocalSet.add_parser
class VTargetPack(BytesElementParser):
    """VTarget Pack - contains per-target tracking data (Tag 101)
    
    Each VTarget Pack contains information about a single detected target
    including position, velocity, and confidence metrics.
    """
    key = b'\x65'  # Tag 101
    TAG = 101
    LDSName = "VTarget Pack"
    ESDName = ""
    UDSName = ""


# Algorithm Series (Tag 102) - describes detection/tracking algorithms
@VMTILocalSet.add_parser
class AlgorithmSeries(BytesElementParser):
    """Algorithm Series - detection/tracking algorithm info (Tag 102)"""
    key = b'\x66'  # Tag 102
    TAG = 102
    LDSName = "Algorithm Series"
    ESDName = ""
    UDSName = ""


# Ontology Series (Tag 103)
@VMTILocalSet.add_parser
class OntologySeries(BytesElementParser):
    """Ontology Series (Tag 103)"""
    key = b'\x67'  # Tag 103
    TAG = 103
    LDSName = "Ontology Series"
    ESDName = ""
    UDSName = ""
