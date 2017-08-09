CITY OF GARDEN GROVE - SPILLMAN GEOVALIDATION DATA PROCESSING SCRIPTS
=====================================================================

USAGE
----------------
All feature classes and field mappings included in this code are specific to the City of Garden Grove. Update accordingly

* Create and update directory locations throughout as necessary
* Update `target_production` variable to production environment not currently in use in main.py during each run
* Stop all services for the target production environment in ArcCatalog prior to running
* Close all local ArcGIS applications prior to running 
* Make any field mapping changes via .txt files in the `field_maps` directory
* Changes to field mappings will require a rebuild of affected Staging locators in ArcCatalog


LICENSE
----------------

    Copyright (C) 2017  City of Garden Grove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
