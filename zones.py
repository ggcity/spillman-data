# -*- coding: utf-8 -*-

import arcpy


class CreateZones():
    def __init__(self, toolbox_path, staging_path, flex_path):
        arcpy.ImportToolbox(toolbox_path)
        
        self.staging = staging_path
        self.flex = flex_path
        
    def create_zone_table(self):
        # helper method runs class CreateZones

        self.create_lawzone()
        self.create_lawarea()
        self.create_misczone()
        self.create_city()
        self.merge_zones()

    def create_lawzone(self):
        # process LawDispatch feature class

        input_lawzone = self.staging + 'LawDispatch'
        output_lawzone = self.flex + 'LawDispatch'
        lawzone_fields = 'ZoneCode ZONECODE;ZoneDescription ZONEDESCRI;AgencyCode AGENCYCODE'
        
        arcpy.ZoneFeatureClassExporter_SpillmanToolbox(input_lawzone, lawzone_fields, output_lawzone)
        print(arcpy.GetMessages())

    def create_lawarea(self):
        # process LawArea feature class

        input_lawarea = self.staging + 'LawArea'
        output_lawarea = self.flex + 'LawArea'
        lawarea_fields = 'ZoneCode ZONECODE;ZoneDescription ZONEDESCRI;AgencyCode AGENCYCODE'
        
        arcpy.ZoneFeatureClassExporter_SpillmanToolbox(input_lawarea, lawarea_fields, output_lawarea)
        print(arcpy.GetMessages()) 

    def create_misczone(self):
        # process MiscZone feature class

        input_misczone = self.staging + 'CouncilDistrict'
        output_misczone = self.flex + 'CouncilDistrict'
        misczone_fields = 'ZoneCode ZONECODE;ZoneDescription ZONEDESC;AgencyCode AGENCYCODE'
        
        arcpy.ZoneFeatureClassExporter_SpillmanToolbox(input_misczone, misczone_fields, output_misczone)
        print(arcpy.GetMessages())

    def create_city(self):
        # process City feature class

        input_city = self.staging + 'City'
        output_city = self.flex + 'City'
        city_fields = 'CityCode CITYCODE;CityName CITYNAME;StateCode STATECODE'

        arcpy.CityFeatureClassExporter_SpillmanToolbox(input_city, city_fields, output_city)
        print(arcpy.GetMessages())

    def merge_zones(self):
        # merge all zone feature classes

        input_lawzone = self.flex + 'LawDispatch'
        input_lawarea = self.flex + 'LawArea'
        input_misczone = self.flex + 'CouncilDistrict'
        input_city = self.flex + 'City'
        input_zones = "%s 'Law Dispatch Zones';%s 'Law Reporting Areas';%s 'Misc Dispatch Zones';" % (input_lawarea, input_lawzone, input_misczone)
        output_zones = self.flex + 'AllZones'

        arcpy.UnionZones_SpillmanToolbox(input_city, input_zones, '', self.flex, output_zones)
        print(arcpy.GetMessages())
