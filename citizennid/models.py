from django.db import models

# Create your models here.

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


POST_CODE = [
    ('3070', '3070'),

]


WORD_NO = [
    ('1', '1 (Nurpur)'),
    ('2', '2 (Vujna)'),
    ('3', '3 (Sharifpur)'),
    ('4', '4 (Girishnagor)'),
    ('5', '5 (Tengratila)'),
    ('6', '6 (Tilagaon)'),
    ('7', '7 (Alipur)'),
    ('8', '8 (Mahobbatpur)'),
    ('9', '9 (Borkatnagor)'),

]

class Village(models.Model):
    village_name = models.CharField(max_length=60, null=False, blank=False)
    village_id = models.CharField(help_text="Village code", max_length=17, null=True, blank=True, unique=True)
    village_code_old = models.CharField(max_length=15, null=True, blank=True)
    word_no = models.CharField(max_length=2, choices=WORD_NO, null=True, blank=True)
    # mouja = models.ForeignKey(Mouja, null=True, blank=True, on_delete=models.CASCADE)
    # union = models.ForeignKey(Union, null=True, blank=True, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=20, null=True, blank=True)
    post_code = models.CharField(max_length=10, choices=POST_CODE, null=True, blank=True, default='3070')

    def __unicode__(self):
        return self.village_name

    def __str__(self):
        return self.village_name


class CitizenNid(models.Model):
    nid_no = models.CharField(max_length=17, null=False, blank=False, unique=True)
    name_bn = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=False, blank=False)

    father_name_bn = models.CharField(max_length=100, null=True, blank=True)
    # father_name_en = models.CharField(max_length=100, null=True, blank=True)

    mother_name_bn = models.CharField(max_length=100, null=True, blank=True)
    # mother_name_en = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=200, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)

    village = models.ForeignKey(Village, null=True, blank=True, on_delete=models.DO_NOTHING)
    road_no = models.CharField(max_length=26,  null=True, blank=True)




    def __unicode__(self):
        return self.nid_no
