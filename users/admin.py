from django.contrib import admin

from users.models import EmailVerification, User

admin.site.register(User)


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("code", "user", "created", "expiration")
    list_display_links = ("code", "user")


admin.site.register(EmailVerification, EmailVerificationAdmin)
