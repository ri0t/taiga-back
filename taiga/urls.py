# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

from .routers import router


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    def mediafiles_urlpatterns():
        """
        Method for serve media files with runserver.
        """

        _media_url = settings.MEDIA_URL
        if _media_url.startswith('/'):
            _media_url = _media_url[1:]

        from django.views.static import serve
        return patterns('',
            (r'^%s(?P<path>.*)$' % 'media', serve,
                {'document_root': settings.MEDIA_ROOT}))

    urlpatterns += static.static(settings.STATIC_URL,
                                 view="django.contrib.staticfiles.views.serve")
    urlpatterns += mediafiles_urlpatterns()
