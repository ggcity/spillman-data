# -*- coding: utf-8 -*-

import glob
import shutil
import datetime

import arcpy


class CreateStaging():
    def __init__(self, working_path, staging_path, input_data_path):
        self.working = working_path
        self.staging = staging_path
        self.input_dir = input_data_path

    def create_staging_gdb(self):
        # delete and recreate staging gdb environment

        if glob.glob(self.staging):
            shutil.rmtree(self.staging)
            print('removed existing Staging.gdb')
        arcpy.CreateFileGDB_management(self.working, 'Staging', 'CURRENT')
        print(arcpy.GetMessages())

        self.copy_to_staging()
     
    def copy_to_staging(self):
        # copy data into staging environment with batch projection

        address = self.input_dir + 'AddressPoint.shp'
        street = self.input_dir + 'StreetCenterline.shp'
        cp = self.input_dir + 'CommonPlace.shp'
        poi = self.input_dir + 'PointOfInterest.shp'
        ld = self.input_dir + 'LawDispatch.shp'
        la = self.input_dir + 'LawArea.shp'
        city = self.input_dir + 'City.shp'
        cd = self.input_dir + 'CouncilDistrict.shp'
        input_shps = '%s;%s;%s;%s;%s;%s;%s;%s' % (address, street, cp, poi, ld, la, city, cd)
        projection = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"

        arcpy.BatchProject_management(input_shps, self.staging, projection, '', '')
        print(arcpy.GetMessages())
