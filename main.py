# -*- coding: utf-8 -*-
# created: 2017-05-08 by josephs@ci.garden-grove.ca.us

# make sure to update target_production variable below and
# stop services for target production in ArcCatalog

import datetime
import arcpy

import staging
import convert
import zones
import locators
import handler


def run():

    # update target production service here
    target_production = 'A'

    # Spillman toolbox location toolbox_path based on Esri version and installation directories
    toolbox_path = 'C:/Python27/ArcGIS10.4/lib/site-packages/SpillmanArcGIS/esri/toolboxes/SpillmanToolbox.pyt'

    # remote directory containing pre-processed input data
    input_data_path = 'G:/pd/geovalidation/locator_data/'

    # local path for field mapping txt files included with package
    field_map_path = 'field_maps/'

    # paths based on default Spillman file structure
    working_path = 'C:/GeoValidation/Working/'
    staging_path = 'C:/GeoValidation/Working/Staging.gdb/'
    flex_path = 'C:/GeoValidation/Working/Flex.gdb/'
    locator_path = 'C:/GeoValidation/Working/Locators/'
    production_path = 'C:/GeoValidation/Production%s/' % target_production
    archive_path = 'C:/GeoValidation/Archive/'

    # initialize classes from tools
    cs = staging.CreateStaging(working_path, staging_path, input_data_path)
    pt = convert.ProcessTables(toolbox_path, staging_path, flex_path, field_map_path)
    cz = zones.CreateZones(toolbox_path, staging_path, flex_path)
    rl = locators.RebuildLocators(locator_path)
    fh = handler.FileHandler(target_production, production_path, archive_path, working_path)

    # helper code will run entire set of tools
    cs.create_staging_gdb()
    pt.create_spillman_tables()
    cz.create_zone_table()
    rl.rebuild_locators()
    fh.backup_production()

    try:
        fh.overwrite_production()
    except:
        print('Overwrite of production failed. Trying alternate production directory.')
        if target_production == 'A':
            fh = handler.FileHandler('B', production_path, archive_path, working_path)
            
        if target_production == 'B':
            fh = handler.FileHandler('A', production_path, archive_path, working_path)

        try:
            fh.overwrite_production()
        except:
            print('WARNING: Cannot replace production data while services are running.\
                Shutdown services on Production%s and try again.' % target_production)
        

if __name__ == '__main__':
    print('starting...')
    start_time = datetime.datetime.now()

    run()

    print('runtime: %s' % str(datetime.datetime.now() - start_time))
