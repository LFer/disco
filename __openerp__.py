
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2014 Datamatic (http://www.datamatic.com.uy). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Administrador de Discos",
    'author': 'Datamatic',
    'website': 'http://www.datamatic.com.uy',    
    "version": "1.0",
    "depends": ["base"],
    "category": "Curso",
    "description": """
    Este módulo administra Discos
    """,
    "init_xml": [],
    'update_xml': ['disc_management_view.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,

}
