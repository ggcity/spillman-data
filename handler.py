# -*- coding: utf-8 -*-

import glob
import shutil
import datetime

import arcpy


class FileHandler():
    def __init__(self, target_production, production_path, archive_path, working_path):
        self.target = target_production
        self.production = production_path 
        self.archive = archive_path
        self.production_locators = production_path + 'Locators/'
        self.production_flex = production_path + 'Flex.gdb/'
        self.working = working_path

    def backup_production(self):
        # creates backup of current dataset

        backup_dir = self.archive + str(datetime.date.today()) + '%s/' % self.target
        backup_locators = backup_dir + 'Locators/'
        backup_flex = backup_dir + 'Flex.gdb/'
        
        if glob.glob(backup_dir):
            shutil.rmtree(backup_dir)
            print('removed duplicate backup from today')

        shutil.copytree(self.production_locators, backup_locators)
        shutil.copytree(self.production_flex, backup_flex)
        print('created backup: %s' % backup_dir)

    def overwrite_production(self):
        # delete and replace target production environment

        working_locators = self.working + 'Locators/'
        working_flex = self.working + 'Flex.gdb'

        shutil.rmtree(self.production_locators)
        shutil.copytree(working_locators, self.production_locators)
        print('replaced %s' % self.production_locators)

        shutil.rmtree(self.production_flex)
        shutil.copytree(working_flex, self.production_flex)
        print('replaced %s' % self.production_flex)
