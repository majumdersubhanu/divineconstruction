from django.contrib import admin

from app.models import Project, UpcomingProjects, Testimonial, Quote, Enquiry, TeamMember


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type', 'image_tag')
    list_filter = ('location', 'type')
    # fields = ('name', 'description', 'image_tag', 'location', 'type')
    # readonly_fields = ('image_tag',)
    search_fields = ('name', 'description', 'location')
    ordering = ('name', 'location')


@admin.register(UpcomingProjects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_tag')
    # fields = ('name', 'description', 'image_tag')
    # readonly_fields = ('image_tag',)
    search_fields = ('name', 'description')
    ordering = ('name',)


admin.site.register(Testimonial)
admin.site.register(Quote)
admin.site.register(Enquiry)


@admin.register(TeamMember)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image_tag')
    search_fields = ('name', 'bio')
    ordering = ('name',)
