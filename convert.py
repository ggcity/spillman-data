# -*- coding: utf-8 -*-

import arcpy


class ProcessTables():
    def __init__(self, toolbox_path, staging_path, flex_path, field_map_path):
        arcpy.ImportToolbox(toolbox_path)

        self.staging = staging_path 
        self.flex = flex_path
        self.field_maps = field_map_path

    def create_spillman_tables(self):
        # helper method runs class ProcessTables

        self.create_street()
        self.create_block()
        self.create_address()
        self.create_commonplace()
        self.create_pointofinterest()

    def create_street(self):
        # process StreetCenterline feature class

        input_street = self.staging + 'StreetCenterline'
        output_street = self.flex + 'StreetCenterline_RG'
        output_streetalt = self.flex + 'StreetCenterline_Alt'
        
        with open(self.field_maps + 'street_fields.txt', 'r') as sf:
            #reads text file of field mapping in for easier readability when altering field mapping
            street_fields = ''.join(line.rstrip() for line in sf)
            arcpy.StreetFeatureClassExporter_SpillmanToolbox(input_street, street_fields, '', 'true', self.flex, output_street)
            print(arcpy.GetMessages())

        with open(self.field_maps + 'streetalt_fields.txt', 'r') as saf:
            streetalt_fields = ''.join(line.rstrip() for line in saf)
            arcpy.AltNamesStreet_SpillmanToolbox(input_street, streetalt_fields, '', output_streetalt)
            print(arcpy.GetMessages())

    def create_block(self):
        # process Block feature class

        input_street = self.flex + 'StreetCenterline_RG'
        output_block = self.flex + 'Block'

        arcpy.BlockFeatureClassTool_SpillmanToolbox(input_street, 'BLK', '10', output_block)
        print(arcpy.GetMessages())

    def create_address(self):
        # process AddressPoint feature class

        input_address = self.staging + 'AddressPoint'
        output_address = self.flex + 'AddressPoint_RG'
        output_addressalt = self.flex + 'AddressPoint_Alt'

        with open(self.field_maps + 'address_fields.txt', 'r') as af:
            address_fields = ''.join(line.rstrip() for line in af)
            arcpy.AddressPointFeatureClassExporter_SpillmanToolbox(input_address, address_fields, '', 'true', '', output_address)
            print(arcpy.GetMessages())

        with open(self.field_maps + 'addressalt_fields.txt', 'r') as aaf:
            addressalt_fields = ''.join(line.rstrip() for line in aaf)
            arcpy.AltNamesStreet_SpillmanToolbox(input_address, addressalt_fields, '', output_addressalt)
            print(arcpy.GetMessages())

    def create_commonplace(self):
        # process CommonPlace feature class

        input_commonplace = self.staging + 'CommonPlace'
        output_commonplace = self.flex + 'CommonPlace_RG'
        output_commonplacealt = self.flex + 'CommonPlace_Alt'

        with open(self.field_maps + 'commonplace_fields.txt', 'r') as cpf:
            commonplace_fields = ''.join(line.rstrip() for line in cpf)
            arcpy.AddressPointFeatureClassExporter_SpillmanToolbox(input_commonplace, commonplace_fields, '', 'true', '', output_commonplace)
            print(arcpy.GetMessages())

        with open(self.field_maps + 'commonplacealt_fields.txt', 'r') as cpaf:
            commonplacealt_fields = ''.join(line.rstrip() for line in cpaf)
            arcpy.AltNamesPOI_SpillmanToolbox(input_commonplace, commonplacealt_fields, '', output_commonplacealt)
            print(arcpy.GetMessages())

    def create_pointofinterest(self):
        # process PointOfInterest feature class

        input_poi = self.staging + 'PointOfInterest'
        output_poi = self.flex + 'PointOfInterest_RG'
        output_poialt = self.flex + 'PointOfInterest_Alt'

        with open(self.field_maps + 'pointofinterest_fields.txt', 'r') as poif:
            poi_fields = ''.join(line.rstrip() for line in poif)
            arcpy.AddressPointFeatureClassExporter_SpillmanToolbox(input_poi, poi_fields, '', 'true', '', output_poi)
            print(arcpy.GetMessages())

        with open(self.field_maps + 'pointofinterestalt_fields.txt', 'r') as poiaf:
            poialt_fields = ''.join(line.rstrip() for line in poiaf)
            arcpy.AltNamesPOI_SpillmanToolbox(input_poi, poialt_fields, '', output_poialt)
            print(arcpy.GetMessages())
