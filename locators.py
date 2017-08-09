# -*- coding: utf-8 -*-

import arcpy


class RebuildLocators():
    def __init__(self, locator_path):              
        self.locators = locator_path 

    def rebuild_locators(self):
        # helper method runs class RebuildLocators

        self.rebuild_ap()
        self.rebuild_bk()
        self.rebuild_cp()
        self.rebuild_poi()
        self.rebuild_sc()

    def rebuild_ap(self):
        # rebuild AP_LOC with new data and existing locator parameters

        ap_loc = self.locators + 'AP_LOC'
        
        arcpy.RebuildAddressLocator_geocoding(ap_loc)
        print(arcpy.GetMessages())

    def rebuild_bk(self):
        # rebuild BK_LOC with new data and existing locator parameters

        bk_loc = self.locators + 'BK_LOC'
        
        arcpy.RebuildAddressLocator_geocoding(bk_loc)
        print(arcpy.GetMessages())

    def rebuild_cp(self):
        # rebuild CP_LOC with new data and existing locator parameters

        cp_loc = self.locators + 'CP_LOC'
        
        arcpy.RebuildAddressLocator_geocoding(cp_loc)
        print(arcpy.GetMessages())

    def rebuild_poi(self):
        # rebuild PIO_LOC with new data and existing locator parameters

        poi_loc = self.locators + 'POI_LOC'
        
        arcpy.RebuildAddressLocator_geocoding(poi_loc)
        print(arcpy.GetMessages())

    def rebuild_sc(self):
        # rebuild SC_LOC with new data and existing locator parameters

        sc_loc = self.locators + 'SC_LOC'
        
        arcpy.RebuildAddressLocator_geocoding(sc_loc)
        print(arcpy.GetMessages())

