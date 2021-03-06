################################################################################
#   (c) 2010, The Honeynet Project
#   Author: Patrik Lantz  patrik@pjlantz.com
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
################################################################################

from piston.models import Consumer
from webdb.hale.models import Module, Proxy
from django.contrib import admin

class ConsumerAdmin(admin.ModelAdmin):
    """
    Handle consumer (oauth) administration
    """

class ModuleAdmin(admin.ModelAdmin):
    """
    Handle module administration
    """
    
    list_display = ('modulename', 'filename')
    
class ProxyAdmin(admin.ModelAdmin):
    """
    Handle proxy administration
    """
    
    list_display = ('host', 'port')
    
admin.site.register(Module, ModuleAdmin)
admin.site.register(Proxy, ProxyAdmin)
admin.site.register(Consumer, ConsumerAdmin)

