import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Organizer(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.title)

class ConferenceSeries(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.title)

class Conference(models.Model):
    year = models.IntegerField()
    venue = models.CharField(max_length=100, null=True)
    series = models.ManyToManyField(
        ConferenceSeries,
        through='SeriesMembership',
        through_fields=("conference", "series"),
        related_name="conferences"
    )
    organizers = models.ManyToManyField(Organizer, related_name="conferences_organized")
    notes = models.TextField(null=True)

    def __str__(self):
        return f"{self.year} - {self.venue}"

class SeriesMembership(models.Model):
    series = models.ForeignKey(
        ConferenceSeries, on_delete=models.CASCADE, related_name='conference_memberships')
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE,
                                    related_name='series_memberships')
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.series.title} - {self.number} - {self.conference}"

class Work(models.Model):
    conference = models.ForeignKey(Conference, on_delete = models.CASCADE, related_name = 'works')

    def __str__(self):
        return f"{self.pk} - {self.versions.all().last().title}"

    def __eq__(self, other):
        return(self.pk == other.pk)

    @property
    def pref_title(self):
        return self.versions.all()[0].title

class Tag(models.Model):
    title = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    start_date = models.CharField(max_length=100, null=True)
    end_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Version(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='versions')
    title = models.CharField(max_length=500, null=True)
    submission_type = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, choices=(
        ("ac", "accpeted"),
        ("su", "submission"),
    ))
    full_text = models.TextField(max_length=50000, null=True)
    tags = models.ManyToManyField(Tag, related_name="versions")

    def __str__(self):
        return self.title

    def age(self):
        return datetime.date.today().year - self.year

    def __eq__(self, other):
        return(self.pk == other.pk)

class Gender(models.Model):
    gender = models.CharField(max_length = 100)

    def __str__(self):
        return self.gender

class Institution(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"

class Department(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} - {self.institution}"

class Appellation(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    versions = models.ManyToManyField(
        Version,
        through="Authorship",
        through_fields=("author", "version"),
        related_name="authors"
    )
    appellations = models.ManyToManyField(
        Appellation,
        through="AppellationAssertion",
        through_fields=("author", "appellation"),
        related_name="authors"
    )
    genders = models.ManyToManyField(
        Gender,
        through="GenderAssertion",
        through_fields=("author", "gender"),
        related_name="members"
    )
    institutions = models.ManyToManyField(
        Institution,
        through="InstitutionAssertion",
        through_fields=("author", "institution"),
        related_name="members"
    )
    departments = models.ManyToManyField(
        Department,
        through="DepartmentAssertion",
        through_fields=("author", "department"),
        related_name="members"
    )

    def __str__(self):
        return f"{self.author_id} - {self.pref_name}"

    @property
    def pref_name(self):
        return f"{self.pref_first_name} {self.pref_last_name}"

    @property
    def pref_first_name(self):
        return self.appellation_assertions.all()[0].appellation.first_name

    @property
    def pref_last_name(self):
        return self.appellation_assertions.all()[0].appellation.last_name

    class Meta:
        ordering: ["pref_last_name"]

class AppellationAssertion(models.Model):
    appellation = models.ForeignKey(Appellation, on_delete = models.CASCADE, related_name='assertions')
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='appellation_assertions')
    asserted_by = models.ForeignKey(
        Version, on_delete=models.CASCADE, related_name='appellation_assertions')

    def __str__(self):
        return f"{self.appellation}"

class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authorships')
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='authorships')
    authorship_order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.version} - {self.author} ({self.authorship_order})"

class DepartmentAssertion(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="department_memberships")
    asserted_by = models.ForeignKey(
        Version, on_delete=models.CASCADE, related_name="department_assertions")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='assertions')

    def __str__(self):
        return f"{self.department} - {self.author}"

class InstitutionAssertion(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='institution_memberships')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='assertions')
    asserted_by=models.ForeignKey(Version, on_delete = models.CASCADE, related_name = 'institution_assertions')

    def __str__(self):
        return f"{self.institution} - {self.author}"

class GenderAssertion(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='gender_memberships')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_authors')
    asserted_by=models.ForeignKey(Version, on_delete = models.CASCADE, related_name = 'gender_assertions')

    def __str__(self):
        return f"{self.gender} - {self.author}"
